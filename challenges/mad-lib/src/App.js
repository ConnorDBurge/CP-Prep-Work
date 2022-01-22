import React, { Component } from 'react'
import './App.css'
import WordForm from './components/madlib-wordform/WordForm.js'
import Story from './components/madlib-story/Story.js'
import MadLibs from './madlibs/MadLibs.js'

class App extends Component {
  state = {
    madLibs: MadLibs,
    selectedMadLib: MadLibs[0]
  }

  onWordInputChange = (key, value, index) => {
    /* Creating a new object that is a copy of the current state. */
    const newState = {
      ...this.state
    }
    /* 1. We create a new state object by copying the old one.
    2. We update the selectedMadLib.words array by replacing the word at the specified index with
    the new word.
    3. We return the new state object. */
    newState.selectedMadLib.words[index] = {
      ...newState.selectedMadLib.words[index],
      value: value
    }
    this.setState(newState)
  }

  createMadLibsDropDown() {
    let output = []
    for (let i = 0; i < this.state.madLibs.length; i++) {
      output.push(
        <option value={i}>{this.state.madLibs[i].title}</option>
      )
    }
    return output;
  }

  changeMadLibSelection(event) {
    this.setState({
      selectedMadLib: MadLibs[event.target.value]
    })
  }

  render() {
    return (
      <div className="App">
        <h1>MADLIBS!</h1>
        <h2>Select a Mad Lib</h2>
        <select onChange={(event) => this.changeMadLibSelection(event)}>
          {this.createMadLibsDropDown()}
        </select>
        <WordForm words={this.state.selectedMadLib.words} onInputChange={this.onWordInputChange} />
        <Story text={this.state.selectedMadLib.getText()} />
      </div>
    )
  }
}

export default App
