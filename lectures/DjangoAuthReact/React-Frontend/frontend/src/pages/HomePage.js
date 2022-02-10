import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../context/AuthContext';

const HomePage = () => {

    let [notes, setNotes] = useState([])
    let { authTokens, logoutUser } = useContext(AuthContext)

    useEffect(() => { getNotes() }, [])

    const getNotes = async () => {
        const response = await fetch('http://localhost:8000/api/notes/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + authTokens.access
            }
        })
        let data = await response.json()
        if (response.ok) setNotes(data)
        else if (!response.statusText === 'Unauthorized') logoutUser()
    }

    console.log(notes)

    return (
        <div>
            <p>You are logged into the Home Page</p>
            <ul>
                {notes.map((note, index) => {
                    return <li key={index}>{note.body}</li>
                })}
            </ul>
        </div>
    );
}

export default HomePage;