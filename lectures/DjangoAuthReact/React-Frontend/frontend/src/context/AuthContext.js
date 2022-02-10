import React, { createContext, useState, useEffect } from 'react';
import jwt_decode from 'jwt-decode';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext()
export default AuthContext;

export const AuthProvider = ({ children }) => {

    const authentication = localStorage.getItem('authTokens')
        ? JSON.parse(localStorage.getItem('authTokens'))
        : null;
    let [authTokens, setAuthTokens] = useState(authentication);
    const userInfo = localStorage.getItem('authTokens')
        ? jwt_decode(localStorage.getItem('authTokens'))
        : null;
    let [user, setUser] = useState(userInfo);
    let [loading, setLoading] = useState(true);

    let navigate = useNavigate();

    const BASE_URL = 'http://localhost:8000/api/token/'

    const loginUser = async (event) => {
        event.preventDefault();
        console.log('Form Submitted')
        let response = await fetch(BASE_URL,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'username': event.target.username.value,
                    'password': event.target.password.value
                })
            })
        let data = await response.json()
        if (response.ok) {
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            navigate('/')
        }
    }

    const logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        navigate('/')
    }

    const updateToken = async () => {
        let response = await fetch(BASE_URL + 'refresh/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'refresh': authTokens?.refresh
                })
            })
        let data = await response.json()
        if (response.ok) {
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
        } else loginUser()

        if (loading) setLoading(false)
    }

    useEffect(() => {
        if (loading) updateToken()
        let fourMinutes = 1000 * 60 * 4
        let interval = setInterval(() => {
            if (authTokens) updateToken()
        }, fourMinutes)
        return () => clearInterval(interval)
    }, [authTokens, loading])

    let contextData = {
        user,
        authTokens,
        loginUser,
        logoutUser
    }

    return (
        <AuthContext.Provider value={contextData}>
            {loading ? null : children}
        </AuthContext.Provider >
    )
}