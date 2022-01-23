import React from 'react';
// import './styles/Spinner.css';

const Spinner = (props) => {
    return (
        <div className="ui active dimmer spinner">
            <div className="ui text loader">{props.text}</div>
        </div>
    );
}

Spinner.defaultProps = {
    text: 'Loading'
}

export default Spinner;