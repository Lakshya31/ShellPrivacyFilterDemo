import React, { Component } from 'react';

import InteractOn from '../Images/on.png';
import InteractOff from '../Images/off.png';

export default class InteractSwitch extends Component {

    getImage = () => this.props.interact ? InteractOn : InteractOff

    toggleImage = () => {
        this.props.onInteractChange();
    }

    render() {
        const ImageName = this.getImage();
        return (
            <img className="InteractImage" src={ImageName} alt="InteractImage" onClick={this.toggleImage} title="Toggle to interact with highlighted text"/>
        )
    }


}
