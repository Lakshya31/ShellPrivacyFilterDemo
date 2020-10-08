import React, { Component } from 'react';

import InteractSwitch from './InteractSwitch';
import { ScrollSync, ScrollSyncPane } from 'react-scroll-sync';
// import { ScrollSync, ScrollSyncNode } from 'scroll-sync-react';

export default class MyTextBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            text: "",
            data: [],
            interact: false,
        }
    }

    sendRequest = () => {
        fetch("https://shellprivacyfilterdemo.herokuapp.com/analyzetext", {
            method: "post",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: this.state.text, subject: this.props.subject })
        })
            .then(resp => resp.json())
            .then(markers => {
                this.setState({ data: markers })
            })
            .catch(error => {
                console.log("API Bugged");
            })
    }

    // htmlDecode = (input) => {
    //     var e = document.createElement('textarea');
    //     e.innerHTML = input;
    //     // handle case of empty input
    //     return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
    //   }

    onTextChange = (target) => {
        // var text = event.target.innerText;
        // text = text.replace(/(\n){2}/g, '\n')
        // this.setState({ text: text }, this.sendRequest);
        target.value = target.value.replace(/(<([^>]+)>)/ig, '');
        this.setState({ text: target.value }, this.sendRequest);
    }

    onInteractChange = () => {
        this.setState(state => ({ interact: !state.interact }), this.ChangeMode)
    }

    // ChangeMode = () => {
    //     if (this.state.interact) {
    //         var Node = document.getElementsByClassName("MyTextBox")[0];
    //         var newdiv = document.createElement("div");
    //         newdiv.className = "newDiv";
    //         newdiv.onclick = this.onInteractChange;
    //         newdiv.innerHTML = document.getElementById("highlighter").innerHTML;
    //         Node.appendChild(newdiv);
    //     }
    //     else {
    //         var Node1 = document.getElementsByClassName("MyTextBox")[0];
    //         var newdiv1 = document.getElementsByClassName("newDiv")[0];
    //         Node1.removeChild(newdiv1);
    //     }
    // }

    ChangeMode = () => {
        if (!this.state.interact) {
            document.getElementById("highlighter").style.zIndex = "0";
        }
        else {
            document.getElementById("highlighter").style.zIndex = "1";
        }
    }

    renderTextinBackground = () => {
        var open = '';
        var close = '';
        var add = 0;
        var text = this.state.text;
        this.state.data.forEach((marker) => {
            if (marker.message === "Violation of Privacy Policy") {
                open = '<span class="highlight highlight1">';
                close = '<span class="tooltiptext">' + marker.message + '</span></span>';
            }
            if (marker.message === "Breach of Confidentiality") {
                open = '<span class="highlight highlight2">';
                close = '<span class="tooltiptext">' + marker.message + '</span></span>';
            }
            close = '<span class="tooltiptext">' + marker.message + '</span></span>';
            text = [text.slice(0, marker.indices[0] + add), open, text.slice(marker.indices[0] + add)].join('');
            add = add + open.length
            text = [text.slice(0, marker.indices[1] + add), close, text.slice(marker.indices[1] + add)].join('');
            add = add + close.length
        })
        text = text.replace(/(?:\r\n|\r|\n)/g, "<br>");

        return { __html: text }
    }

    pasteText = (event) => {
        setTimeout(this.limitLines, 1);
    }

    limitLines = (event) => {
        const vlimit = 15;
        const hlimit = 50;

        var temp = event.target.value.replace(/\r\n/g, "\n").replace(/\r/g, "").split(/\n/g);//split lines

        let upper = temp.length
        for (let i = 0; i < upper; i = i + 1) {
            console.log("Hi")
            if (temp[i].length > hlimit) {
                temp.splice(i, 1, temp[i].slice(0, hlimit), temp[i].slice(hlimit))
            }
        }

        if (temp.length > vlimit) {
            event.target.value = temp.slice(0, vlimit).join("\n");
        }

        this.onTextChange(event.target)
    }

    render() {
        return (
            <ScrollSync>
                <div className="MyTextBox">
                    <ScrollSyncPane>
                        <div id="highlighter" onClick={this.onInteractChange} dangerouslySetInnerHTML={this.renderTextinBackground()} />
                    </ScrollSyncPane>
                    <ScrollSyncPane>
                        {/* <div contentEditable="true" id="maindiv" type="text" onInput={this.onTextChange}></div> */}
                        <textarea type="text" rows="16" cols="72" onPaste={this.pasteText} onKeyUp={this.limitLines}></textarea>
                    </ScrollSyncPane>
                    <InteractSwitch onInteractChange={this.onInteractChange} interact={this.state.interact} />
                    {/* <ScrollSyncPane>
                        <div id="newDiv" onClick={this.onInteractChange} dangerouslySetInnerHTML={this.renderTextinBackground()} />
                    </ScrollSyncPane> */}
                </div>
            </ScrollSync>
        )
    }

    componentDidMount() {
        this.ChangeMode();
    }
}