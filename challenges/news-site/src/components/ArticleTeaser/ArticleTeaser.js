import React, { Component } from 'react';
import { Link, Outlet } from 'react-router-dom';
import { Card } from 'react-bootstrap';

class ArticleTeaser extends Component {
  render() {
    /* Note: the { created_date: createdDate } syntax in this destructure is
        taking the value of created_date from this.props and setting it to
        a new variable called createdDate
    */
    const { id, title, created_date: createdDate } = this.props;
    return (
      <Card>
        <Card.Header><Link to={`/articles/${id}`}>{title}</Link></Card.Header>
        <Card.Body>
          <Card.Subtitle className="mb-2 text-muted">{createdDate}</Card.Subtitle>
        </Card.Body>
        <Outlet />
      </Card>
    )
  }
}

export default ArticleTeaser;


// Functional solution:
// function ArticleTeaser({ id, title, created_date: createdDate, handleTitleClick }) {
//   return (
//     <div>
//       <a onClick={ () => handleTitleClick(id) }>{ title }</a>
//       <p>{ createdDate }</p>
//     </div>
//   );
// }
