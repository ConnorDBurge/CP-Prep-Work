import React, { useState, useEffect } from 'react';
import Dropdown from '../Dropdown/Dropdown';
import Convert from '../Convert/Convert';

const Translate = () => {

    const options = [
        {
            label: 'Afrikaans',
            value: 'af'
        },
        {
            label: 'Arabic',
            value: 'ar'
        },
        {
            label: 'Hindi',
            value: 'hi'
        }
    ]

    const [language, setLanguage] = useState(JSON.stringify(options[0]));
    const [text, setText] = useState('');


    return (
        <div>
            <div className="ui form">
                <div className="field">
                    <label htmlFor="input">Enter text</label>
                    <input
                        id="input"
                        type="text"
                        value={text}
                        onChange={(e) => setText(e.target.value)} />
                </div>
            </div>
            <Dropdown
                selected={language}
                onSelectedChange={setLanguage}
                options={options}
                label='Select a language' />
            <hr />
            <h3 className='ui header'>Output</h3>
            <Convert language={language} text={text} />
        </div>
    );
}

export default Translate;