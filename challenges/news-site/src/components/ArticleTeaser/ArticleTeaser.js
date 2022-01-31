import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class ArticleTeaser extends Component {
  render() {
    /* Note: the { created_date: createdDate } syntax in this destructure is
        taking the value of created_date from this.props and setting it to
        a new variable called createdDate
    */
    const { id, title, created_date: createdDate, handleTitleClick } = this.props;
    return (
      <div>
        <Link to={`/articles/${id}`}>{title}</Link>
        <p>{createdDate}</p>
      </div>
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
