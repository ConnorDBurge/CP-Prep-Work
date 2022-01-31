import React, { Component } from 'react';
import { useNavigate } from 'react-router-dom' // used in function components
import ArticleList from '../components/ArticleList/ArticleList.js'
import News from '../data/news.json';

class HomePage extends Component {
  render() {
    return (
      <div>
        <ArticleList articles={News} />
      </div>
    );
  }
}

export default HomePage;
