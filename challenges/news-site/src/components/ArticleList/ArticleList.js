import React, { Component } from 'react';
import ArticleTeaser from '../ArticleTeaser/ArticleTeaser.js';
import { ListGroup, ListGroupItem, InputGroup, Input } from 'reactstrap';

class ArticleList extends Component {
  render() {
    const { articles, handleSearch } = this.props;
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
}

export default ArticleList;


// Functional solution:
// function ArticleList({ articles, handleTitleClick }) {
//   return (
//     <ListGroup>
//       {articles.map((article, index) => (
//         <ListGroupItem>
//           <ArticleTeaser {...article} id={ index + 1 }
//              handleTitleClick={handleTitleClick} />
//         </ListGroupItem>
//       ))}
//     </ListGroup>
//   );
// }
