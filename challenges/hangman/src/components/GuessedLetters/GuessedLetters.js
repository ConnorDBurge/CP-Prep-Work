import React from 'react';
import '../Puzzle/styles/styles.css';

const GuessedLetters = ({ guessedLetters }) => {

    const renderedLetters = guessedLetters.sort().map((letter, i) => {
        return <span className="rendered__letter" key={i}> {letter} </span>
    })

    return (
        <div>
            <h4 className="rendered">{renderedLetters}</h4>
        </div>
    );
}

export default GuessedLetters;