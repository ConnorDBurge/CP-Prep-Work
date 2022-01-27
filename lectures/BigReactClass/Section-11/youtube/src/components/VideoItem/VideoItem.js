import React, { Component } from 'react';
import './styles/VideoItem.css';

const VideoItem = ({ video }) => {
    return (
        <div className="item video-item">
            <img className="ui image video-item__img" src={video.snippet.thumbnails.medium.url} alt={video.snippet.description} />
            <div className="content">
                <h1 className="header">{video.snippet.title}</h1>
            </div>
        </div>
    );
}

export default VideoItem;