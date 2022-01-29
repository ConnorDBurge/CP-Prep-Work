import React, { useState, useEffect } from 'react';

const Puzzle = ({ puzzle, guessedLetters }) => {

    const puzzleLetters = puzzle.split('');
    const renderedPuzzle = puzzleLetters.map((letter, i) => {
        if (guessedLetters.includes(letter)) {
            return <span key={i}> {letter} </span>;
        } else {
            return <span key={i}> _ </span>;
        }
    })

    return (
        <div>
            <h2>{renderedPuzzle}</h2>
        </div>
    );
}

export default Puzzle;