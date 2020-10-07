import React, { Component } from 'react'

//Components
import Attach from '../Images/attach.png';
import Attachments from './Attachments';

export default class AttachFiles extends Component {
    constructor(props){
        super(props)
        this.state = {
            attachments: []
        }
    }

    deleteAttachment = (index) => {
        var newAttachments = this.state.attachments;
        newAttachments.splice(index,1);
        this.setState({attachments:newAttachments});
    }

    onSend = () => {
    window.location.reload();
    }

    updateAttachmentStatus = (index, resp) => {
        var updated = [];
        if(resp === "issue"){
            updated = this.state.attachments;
            updated[index].issue = true;
            this.setState({attachments:updated})
        }
        if(resp === "no issue"){
            updated = this.state.attachments;
            updated[index].issue = false;
            this.setState({attachments:updated})
        }
    }

    sendFiles = () => {
        this.state.attachments.forEach((attachment,index) => {
            var formdata = new FormData();
            formdata.append('file', attachment.file, attachment.file.name)
            fetch("http://localhost:3001/analyzeattachment", {
                method: "POST",
                body: formdata
            })
            .then(response => response.json())
            .then(resp => {
                this.updateAttachmentStatus(index, resp)
            })
        })
    }

    onFileSelect = (event) => {

        for(var i=0; i<event.target.files.length;i=i+1){
            var filename = event.target.files[i].name.split(".")
            if(filename[filename.length-1].toLowerCase() === "docx"){
                var newfiles = this.state.attachments
                newfiles.push({
                    file:event.target.files[i],
                    issue:false
                })
                this.setState({attachments:newfiles}, this.sendFiles);
            }
        }

        event.target.value = null;
    }

    render() {
        return (
            <div className="BottomRow">
                <p className="roundit" onClick={this.onSend}>SEND</p>
                <label htmlFor="files">
                    <img className="AttachmentIcon" src={Attach} alt="AttachmentIcon" />
                    <input type="file" multiple="multiple" className="InputFile" id="files" onInput={this.onFileSelect} accept="application/vnd.openxmlformats-officedocument.wordprocessingml.document" style={{display: "none"}}/>
                </label>
                <Attachments attachments={this.state.attachments} deleteAttachment={this.deleteAttachment} />
            </div>
        )
    }
}
