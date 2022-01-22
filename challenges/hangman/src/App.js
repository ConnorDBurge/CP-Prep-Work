import './App.css';
import PuzzleWord from './components/PuzzleWord/PuzzleWord';
import GuessForm from './components/GuessForm/GuessForm';
import { useState } from 'react';

function App() {
  const [puzzleWord, setPuzzleWord] = useState('vina');

  return (
    <div className="App">
      <h1>Hang Man</h1>
      <PuzzleWord />
      <GuessForm />
    </div>
  );
}

export default App;
