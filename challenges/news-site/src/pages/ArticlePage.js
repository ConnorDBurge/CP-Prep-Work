import React from 'react';
import { useParams } from 'react-router-dom';
import Article from '../components/Article/Article.js'
import News from '../data/news.json';


const ArticlePage = () => {
  const params = useParams(); // grabs params from URL
  const article = News[params.articleID];
  return (
    <div>
      <Article {...article} />
    </div>
  );
}

export default ArticlePage;

