import React, { useState, useEffect } from 'react';

const Input = ({ guessedLetters, setGuessedLetters, puzzle }) => {

    const [letter, setLetter] = useState('');
    const puzzleLetters = puzzle.split('');
    useEffect(() => {
        if (letter !== '' && !guessedLetters.includes(letter)) {
            const letters = [...guessedLetters]
            letters.push(letter);
            setGuessedLetters(letters);
        }
    }, [letter])

    return (
        <div>
            <input
                type="text"
                value='' // resets the input to blank
                placeholder="Enter a letter"
                onChange={(e) => setLetter(e.target.value)} />
        </div>
    );
}

export default Input;