import './App.css';
import React from 'react';
import ChalkBoardText from './components/Detention/ChalkBoardText.js'
import React, { Component } from 'react';

// Functional
function App() {
  const writeDetention = (num) => {
    let phrases = []
    for (let i = 0; i < num; i++) {
      phrases.push(<ChalkBoardText key={i} />)
    }
    return phrases
  }

  return (
    <div className="App" >
      {writeDetention(15)}
    </div>
  );
}
export default App;

// Class
class App extends Component {
  writeDetention = () => {
    let phrases = []
    for (let i = 0; i < 100; i++) {
      phrases.push(<ChalkBoardText key={i} />)
    }
    return phrases
  }

  render() {
    return (
      <div>
        {this.writeDetention()}
      </div>
    )
  }
}