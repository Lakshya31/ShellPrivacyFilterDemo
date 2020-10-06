import React, { Component } from 'react'

//Importing Components
import MyTextBox from './MyTextBox';

//Importing Images4
import Mail from '../Images/Mail.png';
import Maximize from '../Images/Maximize.png';
import Minimize from '../Images/Minimize.png';
import Close from '../Images/Close.png';

export default class MainApp extends Component {
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
                        <img className="WindowIcon" src={Minimize} alt="Mail Icon"/>
                        <img className="WindowIcon" src={Maximize} alt="Mail Icon"/>
                        <img className="WindowIcon" src={Close} alt="Mail Icon"/>
                    </div>
                </div>
                <div className="InputBoxes">
                    <div className="form-group row">
                        <label for="staticEmail" className="col-sm-2 col-form-label">To</label>
                        <div className="col-sm-10">
                        <input type="text" readonly className="form-control-plaintext InputBox" id="staticEmail" value="Example.Email@shell.com"/>
                        </div>
                    </div>
                    <div className="form-group row">
                        <label for="SubjectLine" className="col-sm-2 col-form-label">Subject</label>
                        <div className="col-sm-10">
                        <input type="text" className="form-control InputBox" id="SubjectLine"/>
                        </div>
                    </div>
                    <MyTextBox/>
                </div>
                <div className="BottomRow">
                    {/* <AttachFile/> */}
                </div>
            </div>
        )
    }
}
