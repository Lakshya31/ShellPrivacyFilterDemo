import React, { Component } from 'react';

import DocxIcon from '../Images/docx.png';
import DelIcon from '../Images/Close.png';

export default class Attachments extends Component {

    render() {
        return (
            <div className="AttachmentsSection">
                {
                    this.props.attachments.map((attachment, index)=>{
                        if(!attachment.issue){
                            return (
                            <div key={index} className="AttachmentCard">
                                <img src={DocxIcon} alt="DocxIcon" className="DocxIcon" />
                                <div className="AttachmentName">{attachment.file.name}</div>
                                <img src={DelIcon} alt="DelIcon" className="DelIcon" onClick={()=>{this.props.deleteAttachment(index)}} />
                            </div>
                            )
                        }

                        else{
                            return (
                            <div key={index} className="AttachmentCardIssue">
                                <img src={DocxIcon} alt="DocxIcon" className="DocxIcon" />
                                <div className="AttachmentName">{attachment.file.name}</div>
                                <img src={DelIcon} alt="DelIcon" className="DelIcon" onClick={()=>{this.props.deleteAttachment(index)}} />
                            </div>
                            )
                        }
                    })
                }
            </div>
        )
    }
}
