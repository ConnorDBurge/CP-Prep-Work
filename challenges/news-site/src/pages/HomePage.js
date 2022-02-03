import React, { Component } from 'react';
import ArticleList from '../components/ArticleList/ArticleList.js'
import ArticleAPI from '../api/ArticlesAPI';

class HomePage extends Component {

	state = {
		news: []
	}

	async componentDidMount() {
		try {
			const articles = await ArticleAPI.fetchArticles();
			this.setState({ news: articles });
		} catch (err) {
			console.error(err);
		}
	}

	handleSearch = async (event) => {
		try {
			const articles = await ArticleAPI.searchArticles(event.target.value);
			this.setState({ news: articles });
		} catch (err) {
			console.error(err);
		}
	}

	render() {
		return (
			<div>
				<ArticleList articles={this.state.news} handleSearch={this.handleSearch} />
			</div>
		);
	}
}

export default HomePage;


// Functional solution:
// function HomePage() {
//   return (
//     <div>
//       <ArticleList articles={News}
//         handleTitleClick={(articleID) => props.history.push(`/articles/${articleID}`)} />
//     </div>
//   );
// }
