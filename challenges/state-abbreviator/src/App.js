import './App.css';
import stateData from './statedata/index.js';
import { useState } from 'react';

function App() {

  const [selectedState, setSelectedState] = useState(null);

  const displayDropDownOptions = () => {
    return stateData.map((state, index) => {
      return <option key={index} value={state['alpha-2']}>{state['name']}</option>
    });
  }

  const handleChange = (event) => {
    setSelectedState(event.target.value);
  }

  return (
    <div className="App">
      <h1>Select State From Dropdown Menu</h1>
      <select onChange={handleChange}>
        {displayDropDownOptions()}
      </select>
      <h1>
        {selectedState}
      </h1>
    </div>
  );
}

export default App;
