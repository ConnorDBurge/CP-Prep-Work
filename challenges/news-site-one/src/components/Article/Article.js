import React, { Component } from 'react';

class Article extends Component {
  render() {

    const { title, created_date, abstract, byline, image } = this.props;

    return (
      <div>
        <h1>{title}</h1>
        <p>{created_date}</p>
        {byline ? <h2>{byline}</h2> : null}
        {image ? <img src={image} /> : null}
        <p>{abstract}</p>
      </div>
    )
  }
}

export default Article;
