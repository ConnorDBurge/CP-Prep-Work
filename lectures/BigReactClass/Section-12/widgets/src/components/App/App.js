import React, { useState } from 'react';
import Accordion from '../Accordion/Accordion';
import Search from '../Search/Search';
import Dropdown from '../Dropdown/Dropdown';
import Translate from '../Translate/Translate';

const App = () => {

    const items = [
        {
            title: 'What is React?',
            content: 'React is a front end JavaScript framework'
        },
        {
            title: 'Why use React?',
            content: 'React is a favorite library among engineers'
        },
        {
            title: 'How do you use React?',
            content: 'You use React by creating components'
        }
    ];

    const options = [
        {
            label: 'The Color Red',
            value: 'red'
        },
        {
            label: 'The Color Blue',
            value: 'blue'
        },
        {
            label: 'The Color Green',
            value: 'green'
        }
    ];

    const [selected, setSelected] = useState(JSON.stringify(options[0]));
    const [color, setColor] = useState(JSON.parse(selected).value); // red
    const [showDropdown, setShowDropdown] = useState(true);

    const selectedChange = (option) => {
        setSelected(option);
        const object = JSON.parse(option);
        setColor(object.value)
    }

    return (
        <div>
            {/* <button onClick={() => setShowDropdown(!showDropdown)}>Toggle Dropdown</button>
            {showDropdown ?
                <Dropdown options={options} selected={selected} onSelectedChange={selectedChange} color={color} /> : null} */}
            <Translate />
        </div>
    );
}

export default App;