import React from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import UsersAPI from '../api/UsersAPI';

const LoginPage = () => {

    const handleFormSubmit = (event) => {
        event.preventDefault();
        console.log(event.target.email.value);
        console.log(event.target.password.value);

        let credentials = {
            email: event.target.email.value,
            password: event.target.password.value
        }

        UsersAPI.login(credentials);
    }

    return (
        <div>
            <Card className="m-auto" style={{ width: '50%' }}>
                <Card.Body>
                    <Card.Title>Login Page</Card.Title>
                    <Form className="m-3" onSubmit={(e) => handleFormSubmit(e)}>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Email</Form.Label>
                            <Form.Control type="text" placeholder="Email" name='email' required />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" name='password' required />
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>
                </Card.Body>
            </Card>
        </div>
    );
}

export default LoginPage;