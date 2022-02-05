import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import HomePage from './pages/HomePage.js';
import ArticlePage from './pages/ArticlePage.js';
import SectionPage from './pages/SectionPage.js';
import AddArticle from './pages/AddArticle.js';
import LoginPage from './pages/LoginPage.js';

class App extends Component {

	state = {
		userInfo: null
	}

	setUserInfo = (userInfoObject) => {
		this.setState({ userInfo: userInfoObject })
	}

	render() {
		return (
			<div>
				<Router>
					<div>
						<AppNav />
						<Route exact path="/" component={HomePage} />
						<Route exact path="/articles/:articleID" component={ArticlePage} />
						<Route exact path="/sections/:sectionID" component={SectionPage} />
						<Route exact path="/add-article" >
							<AddArticle userInfo={this.state.userInfo} />
						</Route>
						<Route exact path="/login">
							<LoginPage userInfo={this.state.userInfo} setUserInfo={this.setUserInfo} />
						</Route>
					</div>
				</Router >
			</div >
		);
	}
}

export default App;