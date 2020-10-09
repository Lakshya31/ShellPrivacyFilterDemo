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
        // console.log(JSON.stringify(target.value));
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
            document.getElementById("highlighter").style.color = "white";
        }
        else {
            document.getElementById("highlighter").style.zIndex = "1";
            document.getElementById("highlighter").style.color = "black";
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
                close = '<span class="tooltiptext">Violation of Privacy Policy</span></span>';
            }
            if (marker.message === "Breach of Confidentiality") {
                open = '<span class="highlight highlight2">';
                close = '<span class="tooltiptext">Breach of Confidentiality</span></span>';
            }
            text = [text.slice(0, marker.indices[0] + add), open, text.slice(marker.indices[0] + add)].join('');
            add = add + open.length
            text = [text.slice(0, marker.indices[1] + add), close, text.slice(marker.indices[1] + add)].join('');
            add = add + close.length
        })

        text = text.replace(/(?:\r\n|\r|\n)/g, "<br>");
        text = text.replace(/ /g, "&nbsp;");
        text = text.replace(/<span&nbsp;class="highlight&nbsp;highlight1">/g, '<span class="highlight highlight1">');
        text = text.replace(/<span&nbsp;class="highlight&nbsp;highlight2">/g, '<span class="highlight highlight2">');
        text = text.replace(/<span&nbsp;class="tooltiptext">/g, '<span class="tooltiptext">');
        // console.log(JSON.stringify(text));
        return { __html: text }
    }

    pasteText = () => {
        setTimeout(this.limitLines, 1);
    }

    limitLines = () => {
        var target = document.getElementById("mytextarea");
        // const vlimit = 13;
        // const hlimit = 50;

        var elmnt = document.getElementById("highlighter");
        var vlimit = Math.floor(elmnt.offsetHeight/24)-1 ;
        var hlimit = Math.floor(elmnt.offsetWidth/10)-1 ;

        var temp = target.value.replace(/\r\n/g, "\n").replace(/\r/g, "").split(/\n/g);//split lines

        var upper = temp.length;
        for(let i=0; i<upper; i++){
            if(temp[i].length > hlimit){
                let lastspace = hlimit;
                for(let j=hlimit; j>0; j=j-1){
                    if(temp[i][j] === " "){
                        lastspace = j+1;
                        break;
                    }
                }
                temp.splice(i,1,temp[i].slice(0,lastspace), temp[i].slice(lastspace));
                upper = upper + 1;
            }
        }

        if (temp.length > vlimit) {
            target.value = temp.slice(0, vlimit).join("\n");
        }
        else{
            target.value = temp.join("\n")
        }

        this.onTextChange(target)
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
                        <textarea id="mytextarea" type="text" rows="16" onPaste={this.pasteText} onKeyUp={this.limitLines}></textarea>
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