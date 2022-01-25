import React from 'react';
import './styles/ImageList.css';
import ImageCard from '../ImageCard/ImageCard';

const ImageList = (props) => {

    const images = props.images.map((image) => {
        return <ImageCard
            image={image}
            key={image.id}
            className="image-list__item" />
    });

    return (
        <div className="image-list">{images}</div>
    );
}

export default ImageList;