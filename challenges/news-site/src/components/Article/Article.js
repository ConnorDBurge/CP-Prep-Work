import React, { Component } from 'react';
import { Card } from 'react-bootstrap';

class Article extends Component {
  render() {
    const { title, created_date: createdDate, abstract, byline, multimedia } = this.props;
    return (
      <div>
        <Card>
          {byline && <Card.Header>{byline}</Card.Header>}
          <Card.Body>
            <Card.Title>{title}</Card.Title>
            <Card.Subtitle>{createdDate}</Card.Subtitle>
            <Card.Text>{abstract}</Card.Text>
            {multimedia && <img src={multimedia[0].url} />}
          </Card.Body>
        </Card>
      </div>
    )
  }
}

export default Article;


// Functional solution:
// function Article({ title, created_date: createdDate, abstract, byline, image }) {
//   return (
//     <div>
//       <h1>{ title }</h1>
//       <p>{ createdDate }</p>
//       { byline && <h2>{byline}</h2> }
//       { image && <img src={image} /> }
//       <p>{ abstract }</p>
//     </div>
//   );
// }
