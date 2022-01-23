import React from 'react';
import ReactDOM from 'react-dom';
import SeasonDisplay from './SeasonDisplay/SeasonDisplay';
import Spinner from './Spinner/Spinner';

class App extends React.Component {

    state = {
        lat: null,
        errorMessage: null
    }

    componentDidMount() { // best place to data loading after mounting the component
        window.navigator.geolocation.getCurrentPosition(
            (position) => this.setState({ lat: position.coords.latitude }),
            (err) => this.setState({ errorMessage: err.message })
        );
    }

    renderContent() {
        if (this.state.errorMessage && !this.state.lat) {
            return <div>Error: {this.state.errorMessage}</div>;
        } else if (!this.state.errorMessage && this.state.lat) {
            return <SeasonDisplay latitude={this.state.lat} />
        } else {
            return <Spinner text="Please allow us to access your location" />;
        }
    }

    render() {
        return (
            <div className="border red">
                {this.renderContent()}
            </div>
        )
    }
}


ReactDOM.render(<App />, document.querySelector('#root'))