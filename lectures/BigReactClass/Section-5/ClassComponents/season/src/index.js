import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { // state is a special name
            lat: null,
            errorMessage: null
        };
        window.navigator.geolocation.getCurrentPosition(
            (position) => {
                this.setState({ lat: position.coords.latitude });
            },
            (err) => {
                this.setState({ errorMessage: err.message });
            }
        );
    }

    render() {
        if (this.state.errorMessage && !this.state.lat) {
            return <div>Error: {this.state.errorMessage}</div>;
        } else if (!this.state.errorMessage && this.state.lat) {
            return <div>Latitude: {this.state.lat}</div>;
        } else {
            return <div>Loading...</div>;
        }
    }
}


ReactDOM.render(<App />, document.querySelector('#root'))