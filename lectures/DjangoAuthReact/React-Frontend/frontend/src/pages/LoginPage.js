import React, { useContext } from 'react';
import AuthContext from '../context/AuthContext';


const LoginPage = () => {

    let { loginUser } = useContext(AuthContext)

    return (
        <form onSubmit={loginUser}>
            <input type="text" name="username" placeholder="Username" />
            <input type="password" name="password" placeholder="Password" />
            <button type="submit">Login</button>
        </form>
    );
}

export default LoginPage;