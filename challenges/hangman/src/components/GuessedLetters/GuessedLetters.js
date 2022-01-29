import React from 'react';

const GuessedLetters = ({ guessedLetters }) => {

    const renderedLetters = guessedLetters.sort().map((letter, i) => {
        return <li key={i}>{letter}</li>;
    })

    return (
        <div>
            <ul>
                {renderedLetters}
            </ul>
        </div>
    );
}

export default GuessedLetters;