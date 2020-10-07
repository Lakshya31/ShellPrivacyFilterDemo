import React, { Component } from 'react'

//Importing Components
import MyTextBox from './MyTextBox';
import AttachFiles from './AttachFiles';

//Importing Images4
import Mail from '../Images/Mail.png';
import Maximize from '../Images/Maximize.png';
import Minimize from '../Images/Minimize.png';
import Close from '../Images/Close.png';

export default class MainApp extends Component {

    constructor(props){
        super(props);
        this.state = {
            subject : ""
        }
    }

    subjectChange = (event) => {
        this.setState({subject: event.target.value})
    }

    render() {
        return (
            <div className="MainApp">
                <div className="TopBar">
                    <div className="LeftItems">
                        <img className="MailIcon" src={Mail} alt="Mail Icon"/>
                        <div className="BoxTitle">
                            New Email
                        </div>
                    </div>
                    <div className="WindowIcons">
                        <img className="WindowIcon" src={Minimize} alt="Min Icon"/>
                        <img className="WindowIcon" src={Maximize} alt="Max Icon"/>
                        <img className="WindowIcon" src={Close} alt="Close Icon"/>
                    </div>
                </div>
                <div className="InputBoxes">
                    <div className="form-group row">
                        <label htmlFor="staticEmail" className="col-sm-2 col-form-label">To</label>
                        <div className="col-sm-10">
                        <input type="text" readOnly className="form-control-plaintext InputBox" id="staticEmail" value="Example.Email@shell.com"/>
                        </div>
                    </div>
                    <div className="form-group row">
                        <label htmlFor="SubjectLine" className="col-sm-2 col-form-label">Subject</label>
                        <div className="col-sm-10">
                        <input type="text" className="form-control InputBox" id="SubjectLine" onChange={this.subjectChange}/>
                        </div>
                    </div>
                    <MyTextBox subject={this.state.subject}/>
                </div>
                <AttachFiles/>
            </div>
        )
    }
}
