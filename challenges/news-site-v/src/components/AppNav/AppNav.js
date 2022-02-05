import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Navbar } from 'reactstrap';
import navItems from '../../config/Sections.json';

class AppNav extends Component {
  render() {
    return (
      <Navbar color="light">
        <Link to={`/`}>HOME</Link>
        <Link to={`/add-article`}>NEW ARTICLE</Link>
        {navItems.map((navItem, index) =>
          <Link to={`/sections/${navItem.value}`} key={index} >
            {navItem.label}
          </Link>
        )}
        <Link to={`/login`}>LOGIN</Link>
      </Navbar>
    )
  }
}

export default AppNav;