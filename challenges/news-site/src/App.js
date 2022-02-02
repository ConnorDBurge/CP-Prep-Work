import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import navItems from './config/Sections.json';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import HomePage from './pages/HomePage.js';
import ArticlePage from './pages/ArticlePage.js';
import SectionPage from './pages/SectionPage';

class App extends Component {

  state = {
    navItems: navItems
  }

  render() {
    const { navItems } = this.state;

    return (
      <div>
        <Router>
          <AppNav navItems={navItems} />
          <div>
            <Route exact path="/" component={HomePage} />
            <Route exact path="/articles/:articleID" component={ArticlePage} />
            <Route exact path="/sections/:sectionID" component={SectionPage} />
          </div>
        </Router>
      </div>
    );
  }
}

export default App;


// Functional solution
// function App() {
//   const [ navItems, setNavItems ] = useState(navItems);

//   return (
//     <div>
//       <AppNav navItems={navItems} handleNavClick={(clickedItem) => console.log(clickedItem)} />
//       <Router>
//         <div>
//           <Route exact path="/" component={HomePage} />
//           <Route exact path="/articles/:articleID" component={ArticlePage} />
//         </div>
//       </Router>
//     </div>
//   );
// }
