import React from 'react';
import SearchBar from '../SearchBar/SearchBar';
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
                Found {this.state.images.length} images.
            </div>
        );
    }
}

export default App;
