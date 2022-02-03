import React, { Component } from 'react';
import { ListGroupItemHeading, ListGroupItemText } from 'reactstrap';
import { Link } from 'react-router-dom';

const ArticleTeaser = ({ id, title, created_date: createdDate }) => {
  return (
    <div key={id}>
      <ListGroupItemHeading>
        <Link to={`/articles/${id}`}>{title}</Link>
      </ListGroupItemHeading>
      <ListGroupItemText>{createdDate}</ListGroupItemText>
    </div>
  );
}

export default ArticleTeaser;