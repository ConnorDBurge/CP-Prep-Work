import './App.css';
import stateData from './statedata/index.js';
import { useState } from 'react';
import USState from './components/USState.js';
import Select from 'react-select';

function App() {

  const [selectedState, setSelectedState] = useState(null);

  const displayDropDownOptions = () => {
    return stateData.map((state, index) => {
      return <option key={index} value={state['alpha-2']}>{state['name']}</option>
    });
  }

  const handleChange = (state) => {
    setSelectedState(state.value);
  }

  return (
    <div className="App">
      <h1>Select State From Dropdown Menu</h1>
      <Select
        options={stateData}
        onChange={handleChange} />
      <USState state={selectedState} />
    </div>
  );
}

export default App;
