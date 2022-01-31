import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import navItems from './data/navItems.json';
import AppNav from './components/AppNav/AppNav.js';
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage';
class App extends Component {
  state = {
    navItems: navItems
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
            <Route path="/" element={<HomePage />} />
            <Route path="/articles/:articleID" element={<ArticlePage />} />
          </Routes>
        </Router>
      </div>
    );
  }
}

export default App;
