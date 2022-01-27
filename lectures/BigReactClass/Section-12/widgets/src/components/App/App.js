import React from 'react';
import Accordion from '../Accordion/Accordion';

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
    ]

    return (
        <div>
            <Accordion items={items} />
        </div>
    );
}

export default App;