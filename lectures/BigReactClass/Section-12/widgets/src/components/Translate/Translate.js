import React, { useState, useEffect } from 'react';
import Dropdown from '../Dropdown/Dropdown';

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

    return (
        <div>
            <Dropdown selected={language} onSelectedChange={setLanguage} options={options} />
        </div>
    );
}

export default Translate;