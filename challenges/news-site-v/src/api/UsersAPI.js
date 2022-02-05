const BASE_URL = 'http://localhost:3001/api/users/login?include=user';

const login = async (credentials) => {
    try {
        const response = await fetch(BASE_URL, {
            headers: {
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(credentials)
        });
        return await response.json();
    } catch (err) {
        console.error(err);
    }
}

export default {
    login
}

// email: john@doe.com
// password: opensesame