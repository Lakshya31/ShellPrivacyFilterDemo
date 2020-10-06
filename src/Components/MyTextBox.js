import React, { Component } from 'react';

import InteractSwitch from './InteractSwitch';

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
        fetch("http://localhost:3001/analyzetext", {
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

    onTextChange = (event) => {
        event.target.value = event.target.value.replace( /(<([^>]+)>)/ig, '');
        this.setState({ text: event.target.value}, this.sendRequest)
    }

    onInteractChange = () => {
        this.setState(state => ({ interact: !state.interact }), this.ChangeMode)
    }

    ChangeMode = () => {
        if (this.state.interact) {
            var Node = document.getElementsByClassName("MyTextBox")[0];
            var newdiv = document.createElement("div");
            newdiv.className = "newDiv";
            newdiv.onclick = this.onInteractChange;
            newdiv.innerHTML = document.getElementById("highlighter").innerHTML;
            Node.appendChild(newdiv);
        }
        else {
            var Node1 = document.getElementsByClassName("MyTextBox")[0];
            var newdiv1 = document.getElementsByClassName("newDiv")[0];
            Node1.removeChild(newdiv1);
        }
    }

    renderTextinBackground = () => {
        var open = '<span class="highlight">';
        var close = '';
        var add = 0
        var text = this.state.text;
        this.state.data.forEach((marker) => {
            close = '<span class="tooltiptext">'+marker.message+'</span></span>';
            text = [text.slice(0, marker.indices[0] + add), open, text.slice(marker.indices[0] + add)].join('');
            add = add + open.length
            text = [text.slice(0, marker.indices[1] + add), close, text.slice(marker.indices[1] + add)].join('');
            add = add + close.length
        })
        text = text.replace(/(?:\r\n|\r|\n)/g, "<br>");

        return { __html: text }
    }


    render() {
        return (
            <div className="MyTextBox">
                <div id="highlighter" dangerouslySetInnerHTML={this.renderTextinBackground()} />
                <textarea type="text" onChange={this.onTextChange}></textarea>
                <InteractSwitch onInteractChange={this.onInteractChange} interact={this.state.interact} />
            </div>
        )
    }

}