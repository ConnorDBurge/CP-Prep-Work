import React, { useState } from 'react';
import Puzzle from '../Puzzle/Puzzle';
import Input from '../Input/Input';
import GuessedLetters from '../GuessedLetters/GuessedLetters';

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

    // words[Math.floor(Math.random() * words.length)]
    const [puzzle, setPuzzle] = useState("northwestward");
    const [guessedLetters, setGuessedLetters] = useState(['n', 't', 'r', 'd']);

    return (
        <div>
            <h1>Welcome to Hangman</h1>
            <Puzzle puzzle={puzzle} guessedLetters={guessedLetters} />
            <Input />
            <GuessedLetters />
        </div>
    );
}

export default App;