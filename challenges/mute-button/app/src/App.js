import './App.css';
import React, { Component } from 'react';
import MuteButton from './components/MuteButton/MuteButton';
import { useState } from 'react';

// Class solution
// class App extends Component {
//   state = {
//     isMuted: false
//   };

//   toggleMute = () => {
//     this.setState({
//       isMuted: !this.state.isMuted
//     });
//   }

//   render() {
//     console.log(this.state)
//     return (
//       <div className="App">
//         <MuteButton isMuted={this.state.isMuted} toggleMute={this.toggleMute} />
//       </div>
//     )
//   }
// }

// Functional solution
const App = () => {
  const [isMuted, setIsMuted] = useState(false);

  const toggleMute = () => {
    setIsMuted(!isMuted);
  }

  return (
    <div className="App">
      <MuteButton isMuted={isMuted} toggleMute={toggleMute} />
    </div>
  )

}

export default App;
