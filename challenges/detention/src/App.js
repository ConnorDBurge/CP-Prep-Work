import './App.css';
import React from 'react';
import Detention from './components/Detention/Detention.js'

class App extends React.Component {

  writeDetention = () => {
    let phrases = []
    for (let i = 0; i < 100; i++) {
      phrases.push(<Detention />)
    }
    return phrases
  }

  render() {
    return (
      <div className="App" >
        {this.writeDetention()}
      </div>
    );
  }
}

export default App;
