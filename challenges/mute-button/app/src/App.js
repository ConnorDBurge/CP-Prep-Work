import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import MuteButton from './components/MuteButton/MuteButton';

class App extends Component {
  state = {
    isMuted: false
  };

  toggleMute = () => {
    this.setState({
      isMuted: !this.state.isMuted
    });
  }

  render() {
    console.log(this.state)
    return (
      <div className="App">
        <MuteButton isMuted={this.state.isMuted} toggleMute={this.toggleMute} />
      </div>
    )
  }
}

export default App;
