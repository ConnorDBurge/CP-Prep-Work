import './App.css';
import React from 'react'
import ButtonComponent from './components/ButtonComponent/ButtonComponent.js'

class App extends React.Component {
  createButtons = () => {
    let buttons = []
    for (let i = 0; i < 100; i++) {
      buttons.push(<ButtonComponent key={i} />)
    }
    return buttons
  }

  render() {
    return (
      <div className="App">
        {this.createButtons()}
      </div>
    )
  }
}

export default App;
