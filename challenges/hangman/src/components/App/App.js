import React, { useState } from 'react';
import Puzzle from '../Puzzle/Puzzle';
import Input from '../Input/Input';
import GuessedLetters from '../GuessedLetters/GuessedLetters';
import './styles/App.css';

const App = () => {

    const words = [
        "marriageproof",
        "minionette",
        "unlichened",
        "electrocardiographic",
        "hippophagy",
        "polyphore",
        "debellate",
        "zyga",
        "antedonin",
        "hirudinean",
        "foremastman",
        "metapolitics",
        "bianisidine",
        "gros",
        "superindifferent",
        "collar",
        "maculose",
        "unphysically",
        "narrowish",
        "Bartonia",
        "inadherent",
        "arbitrary",
        "forefeelingly",
        "palame",
        "vina",
        "northwestward",
        "dog"
    ]

    // 
    const [puzzle, setPuzzle] = useState(words[Math.floor(Math.random() * words.length)]);
    const [guessedLetters, setGuessedLetters] = useState([]);

    return (
        <div className="container">
            <div className="app">
                <h1 className="app__header">Welcome to Hangman</h1>
                <Puzzle puzzle={puzzle} guessedLetters={guessedLetters} setGuessedLetters={setGuessedLetters} />
                <Input puzzle={puzzle} guessedLetters={guessedLetters} setGuessedLetters={setGuessedLetters} />
                <GuessedLetters guessedLetters={guessedLetters} />
            </div>
        </div>
    );
}

export default App;