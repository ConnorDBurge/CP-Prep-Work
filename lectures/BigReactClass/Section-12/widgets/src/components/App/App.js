import React, { useState } from 'react';
import Accordion from '../Accordion/Accordion';
import Search from '../Search/Search';
import Dropdown from '../Dropdown/Dropdown';

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

    return (
        <div>
            <Dropdown options={options} selected={selected} onSelectedChange={setSelected} />
        </div>
    );
}

export default App;