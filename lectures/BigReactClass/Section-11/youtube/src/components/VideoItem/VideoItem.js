import React, { Component } from 'react';
import './styles/VideoItem.css';

const VideoItem = ({ video, onVideoSelect }) => {
    return (
        <div className="item video-item" onClick={() => onVideoSelect(video)}>
            <img className="ui image video-item__img" src={video.snippet.thumbnails.medium.url} alt={video.snippet.title} />
            <div className="content">
                <h3 className="header">{video.snippet.title}</h3>
            </div>
        </div>
    );
}

export default VideoItem;