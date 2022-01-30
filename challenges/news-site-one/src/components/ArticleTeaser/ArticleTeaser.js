import React, { Component } from 'react';

class ArticleTeaser extends Component {
  render() {

    const { id, title, created_date, handleTitleClick } = this.props;

    return (
      <div>
        <a href="#" onClick={() => handleTitleClick(id)}>{title}</a>
        <p>{created_date}</p>
      </div>
    )
  }
}

export default ArticleTeaser;
