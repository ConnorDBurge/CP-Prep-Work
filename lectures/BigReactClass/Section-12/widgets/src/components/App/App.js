import React from 'react';
import Accordion from '../Accordion/Accordion';
import Search from '../Search/Search';

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
            <Search />

        </div>
    );
}

export default App;