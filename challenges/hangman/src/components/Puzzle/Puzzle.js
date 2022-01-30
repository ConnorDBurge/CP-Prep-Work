import React from 'react';
import './styles/styles.css';

const Puzzle = ({ puzzle, guessedLetters, setGuessedLetters }) => {

    const puzzleLetters = puzzle.split(''); // splits puzzle word into list

    // gets number of incorrect letters guessed
    const wrongLetters = guessedLetters.filter((letter) => {
        return !puzzleLetters.includes(letter);
    }).length

    // renders puzzle word with correct guesses
    const renderedPuzzle = puzzleLetters.map((letter, i) => {
        if (wrongLetters < 6 && guessedLetters.includes(letter)) {
            return <span className="rendered__letter" key={i}> {letter} </span>;
        } else {
            return <span className="rendered__letter" key={i}> _ </span>;
        }
    })

    // alerts user when 6 attempts have been reached
    if (wrongLetters >= 6) {
        setGuessedLetters([]);
        alert(`You freaking lost!\nThe word was: ${puzzle}`);
    }

    return (
        <div>
            <h2 className="rendered">{renderedPuzzle}</h2>
        </div>
    );
}

export default Puzzle;