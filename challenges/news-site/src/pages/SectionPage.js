import React, { Component, useState, useEffect } from 'react';
import ArticleAPI from '../api/ArticlesAPI';
import ArticleList from '../components/ArticleList/ArticleList';


const SectionPage = (props) => {

    const [articles, setArticles] = useState([]);
    const [section, setSection] = useState(null);

    useEffect(() => {
        const articles = async () => {
            try {
                setSection(props.match.params.sectionID);
                const fetchedArticles = await ArticleAPI.fetchArticlesBySection(section);
                setArticles(fetchedArticles);
            } catch (err) {
                console.error(err);
            }
        }
        articles()
    });

    return (
        <div>
            <ArticleList articles={articles} />
        </div>
    );
}

export default SectionPage;

// class SectionPage extends Component {
//     state = {
//         articles: []
//     }

//     async componentDidMount() {
//         try {
//             const section = this.props.match.params.sectionID;
//             const fetchedArticles = await ArticleAPI.fetchArticlesBySection(section);
//             this.setState({ articles: fetchedArticles });
//         } catch (err) {
//             console.error(err);
//         }
//     }

//     render() {
//         return (
//             <div>
//                 <ArticleList articles={this.state.articles} />
//             </div>
//         );
//     }
// }

// export default SectionPage;