import React, { Component } from 'react';
import { Navbar } from 'reactstrap';
import { Link } from 'react-router-dom';

class AppNav extends Component {
  render() {
    const { navItems, handleNavClick } = this.props;

    return (
      <Navbar color="light">
        {navItems.map((navItem, index) =>
          <Link to={`/sections/:${navItem.value}`} key={index}>{navItem.label}</Link>
        )}
      </Navbar>
    )
  }
}

export default AppNav;


// Functional solution:
// function AppNav({ navItems, handleNavClick }) {
//   return (
//     <Navbar color="light">
//       {navItems.map((navItem) =>
//         <a href="#" onClick={() => handleNavClick( navItem.value )} >
//           { navItem.label } |
//         </a>
//       )}
//     </Navbar>
//   );
// }
