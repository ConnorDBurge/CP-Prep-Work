import React, { Component } from 'react';
import ArticleTeaser from '../ArticleTeaser/ArticleTeaser.js'

class ArticleList extends Component {

  render() {

    const { articles, handleTitleClick } = this.props;

    const renderedArticleTeasers = articles.map((article, index) => {
      return (
        <ArticleTeaser
          key={index}
          id={index}
          title={article.title}
          created_date={article.created_date}
          handleTitleClick={() => handleTitleClick(index)} />
      )
    })

    return (
      <div>
        {renderedArticleTeasers}
      </div>
    );
  }
}

export default ArticleList;
