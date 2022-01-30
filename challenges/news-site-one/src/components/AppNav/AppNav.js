import React, { Component } from 'react';

class AppNav extends Component {
  render() {

    const { navItems, handleNavClick } = this.props;

    const renderedNavItems = navItems.map((item, i) => {
      return <a
        key={i}
        href="#"
        onClick={() => handleNavClick(item.value)}>
        {item.label}</a>
    })

    return (
      <nav>
        {renderedNavItems}
      </nav>
    )
  }
}

export default AppNav;
