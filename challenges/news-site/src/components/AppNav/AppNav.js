import React from 'react';
import { Navbar } from 'reactstrap';
import { Link } from 'react-router-dom';

const AppNav = ({ navItems }) => {
  return (
    <Navbar color="light">
      {navItems.map((navItem, index) =>
        <Link to={`/sections/${navItem.value}`} key={index}>{navItem.label}</Link>
      )}
    </Navbar>
  );
}

export default AppNav;