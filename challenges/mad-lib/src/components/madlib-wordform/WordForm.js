import React, { Component } from 'react'
import './WordForm.css'

class WordForm extends Component {

  onInputChange(key, index, event) {
    const { onInputChange } = this.props;
    onInputChange(key, event.currentTarget.value, index)
  }

  listWords = (event) => {
    const { words } = this.props;
    let inputs = []
    for (let i = 0; i < words.length; i++) {
      let word = this.props.words[i]
      inputs.push(
        <div key={i}>
          <input
            key={word.key}
            type="text"
            placeholder={word.label}
            onChange={(event) => {
              this.props.onInputChange(word.key, event.currentTarget.value, i)
            }} />
          <br />
        </div>

      )
    }
    return inputs;
  }

  render() {
    return (
      <div>
        {this.listWords()}
      </div>
    )
  }
}

export default WordForm;
