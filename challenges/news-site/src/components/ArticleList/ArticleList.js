import React from 'react';
import ArticleTeaser from '../ArticleTeaser/ArticleTeaser.js';
import { ListGroup, ListGroupItem, InputGroup, Input } from 'reactstrap';

const ArticleList = ({ articles, handleSearch }) => {
  return (
    <div>
      <InputGroup>
        <Input onChange={(e) => handleSearch(e)} type="text" placeholder="Search" />
      </InputGroup>
      <ListGroup>
        {articles.map((article, index) => (
          <ListGroupItem key={index}>
            <ArticleTeaser {...article} id={index + 1} />
          </ListGroupItem>
        ))}
      </ListGroup>
    </div>
  );
}

export default ArticleList;