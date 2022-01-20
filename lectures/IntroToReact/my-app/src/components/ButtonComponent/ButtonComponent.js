import React from 'react';

class ButtonComponent extends React.Component {
    state = {
        count: 0
    };

    handleButtonClick = () => {
        this.setState({
            count: this.state.count + 1
        });
    }

    render() {
        return (
            <div className="App">
                <h1>I have been clicked {this.state.count} times</h1>
                <button onClick={this.handleButtonClick}>Click me!</button>
            </div>
        );
    }
}

export default ButtonComponent;