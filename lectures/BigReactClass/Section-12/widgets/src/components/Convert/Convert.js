import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Convert = (language, text) => {
    const lang = JSON.parse(language); // language is coming in a string
    const [translation, setTranslation] = useState('');
    const [debounceText, setDebounceText] = useState(text);

    useEffect(() => {
        const timerId = setTimeout(() => {
            setDebounceText(text)
        }, 500)

        return () => {
            clearTimeout(timerId)
        }
    }, [text]);

    useEffect(() => {
        axios.post('https://translation.googleapis.com/language/translate/v2',
            {},
            {
                params: {
                    "q": debounceText,
                    "source": "en",
                    "target": lang.value,
                    "format": "text",
                    "key": 'AIzaSyCHUCmpR7cT_yDFHC98CZJy2LTms-IwDlM'
                }
            }).then((response) => {
                setTranslation(response.data.data.translations[0].translatedText);
            }).catch((error) => {
                setTranslation(error.message);
            })
    }, [debounceText, language]);

    return (
        <div>
            <h3>{translation}</h3>
        </div>
    );
}

export default Convert;