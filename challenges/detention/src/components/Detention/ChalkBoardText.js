import React from 'react';
import React, { Component } from 'react';


// Function
const ChalkBoardText = () => {
    return (
        <div>
            <h1>I will never mutate state or props directly</h1>
        </div>
    );
}

export default ChalkBoardText;

// Class
class ChalkBoardText extends Component {
    render() {
        return (
            <div>
                <h1>I will never mutate state or props directly</h1>
            </div>
        )
    }
}