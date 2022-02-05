import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';
import ArticleAPI from '../api/ArticlesAPI';

const AddArticle = () => {

    const [articleSubmitted, setArticleSubmitted] = useState(false);

    const handleFormSubmit = (event) => {
        event.preventDefault();
        const article = {
            'title': `${event.target.title.value}`,
            'byline': `${event.target.byline.value}`,
            'abstract': `${event.target.abstract.value}`
        }
        ArticleAPI.addArticle(article)
            .then((res) => {
                setArticleSubmitted(true);
            });
    }


    return (
        <div>
            <h1 className="m-3">Add Article</h1>
            {articleSubmitted
                ? <Alert variant="success" >Article Successfully Submitted</Alert>
                : <Form className="m-3" onSubmit={(e) => handleFormSubmit(e)}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Title</Form.Label>
                        <Form.Control type="text" placeholder="Title" name='title' />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>ByLine</Form.Label>
                        <Form.Control type="text" placeholder="ByLine" name='byline' />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Abstract</Form.Label>
                        <Form.Control type="text" placeholder="Abstract" name='abstract' />
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>}
        </div>
    );
}

export default AddArticle;