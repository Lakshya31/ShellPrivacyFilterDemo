import React, { Component } from 'react'

import Attach from '../Images/attach.png'

export default class AttachFiles extends Component {
    constructor(props){
        super(props)
        this.state = {
            files: [],
            data: []
        }
    }

    onSend = () => {

    }

    onFileSelect = (event) => {
        var formdata = new FormData();
        var files = event.target.files;

        this.setState({files:event.target.files})

        event.target.value = null;

    }

    render() {
        return (
            <div className="BottomRow">
                <p className="roundit" onClick={this.onSend}>SEND</p>
                <label htmlFor="files">
                    <img className="AttachmentIcon" src={Attach} alt="AttachmentIcon" />
                    <input type="file" multiple="multiple" className="InputFile" id="files" onInput={this.onFileSelect} style={{visibility:"hidden"}}/>
                </label>
            </div>
        )
    }
}
