import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import News from './data/news.json';
import navItems from './data/navItems.json';
import AppNav from './components/AppNav/AppNav.js';
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage';
class App extends Component {
  constructor(props) {
    super(props);
    const randomArticleIndex = Math.floor(Math.random() * News.length);
    const randomArticle = News[randomArticleIndex];

    this.state = {
      navItems: navItems
    }
  }

  render() {
    const { navItems } = this.state

    return (
      <div>
        <h1>AppNav Component</h1>
        <hr />
        <AppNav navItems={navItems} handleNavClick={(clickedItem) => console.log(clickedItem)} />
        <Router>
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route exact path="/articles/:articleID" element={<ArticlePage />} />
          </Routes>
        </Router>
      </div>
    );
  }
}

export default App;
