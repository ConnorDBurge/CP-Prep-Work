// Import the React and ReactDOM libraries
import React from 'react';
import ReactDOM from 'react-dom';

// Create a React component
const App = () => {
    const buttonText = 'Submit';
    const labelText = 'Enter Name:';

    return (
        <div>
            <label className="label" htmlFor="name">{labelText}</label>
            <input type="text" id="name" />
            <button>{buttonText}</button>
        </div>
    )
}


// Take the React component and show it on the screen
ReactDOM.render(
    <App />,
    document.querySelector('#root')
);