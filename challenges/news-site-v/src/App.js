import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import HomePage from './pages/HomePage.js';
import ArticlePage from './pages/ArticlePage.js';
import SectionPage from './pages/SectionPage.js';
import AddArticle from './pages/AddArticle.js';

class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <div>
            <AppNav />
            <Route exact path="/" component={HomePage} />
            <Route exact path="/articles/:articleID" component={ArticlePage} />
            <Route exact path="/sections/:sectionID" component={SectionPage} />
            <Route exact path="/add-article" component={AddArticle} />
          </div>
        </Router>
      </div>
    );
  }
}

export default App;