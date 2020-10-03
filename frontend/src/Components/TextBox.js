import React, { Component } from 'react'

export default class TextBox extends Component {

    constructor(props){
        super(props);
        this.state = {
            text : ""
        }
    }

    sendRequest = () => {
        var open = '<span class="highlight">';
        var close = '</span>';
        var text = this.state.text
        if(text.length >= 10){
            fetch("http://localhost:3001/analyze",{
                method:"post",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({text:text})
            })
            .then(resp => resp.json())
            .then(markers => {
                var add = 0
                markers.forEach((marker)=>{
                    text = [text.slice(0, marker[0]+add), open, text.slice(marker[0]+add)].join('');
                    add = add + open.length
                    text = [text.slice(0, marker[1]+add), close, text.slice(marker[1]+add)].join('');
                    add = add + close.length
                })
                text = text.replace(/(?:\r\n|\r|\n)/g,"<br>");
                console.log(text)
                document.getElementById("highlighter").innerHTML = text;
            })
            .catch(error => {
                alert("API Bugged");
            })
        }
        else{
            document.getElementById("highlighter").innerHTML = ""
        }
    }

    onTextChange = (event) => {
        // document.getElementById("highlighter").innerHTML = event.target.value
        this.setState({text:event.target.value},this.sendRequest)
    }

    render() {
        return (
            <div className="TextBox">
                <div id="highlighter"></div>
                <textarea type="text" id="InputBox" onChange={this.onTextChange}></textarea>
            </div>
        )
    }
}
