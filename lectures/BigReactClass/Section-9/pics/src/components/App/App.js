import React from 'react';
import SearchBar from '../SearchBar/SearchBar';
import ImageList from '../ImageList/ImageList';
import pexels from '../../API/pexels';

class App extends React.Component {

    state = {
        images: []
    }

    onSearchSubmit = async (term) => {
        const response = await pexels.get('search', {
            params: {
                query: term
            }
        });

        this.setState({ images: response.data.photos });
    }

    render() {
        return (
            <div className="ui container" style={{ marginTop: '10px' }}>
                <SearchBar onSubmit={this.onSearchSubmit} />
                <ImageList images={this.state.images} />
            </div>
        );
    }
}

export default App;
