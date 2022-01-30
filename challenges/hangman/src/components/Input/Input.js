import React, { useState, useEffect } from 'react';
import './styles/Input.css';

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
        <div className='input'>
            <input
                type="text"
                value='' // resets the input to blank
                onChange={(e) => setLetter(e.target.value)}
                className='input__box'
            />
        </div>
    );
}

export default Input;