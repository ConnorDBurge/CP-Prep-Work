import React, { Component } from 'react';
import VideoItem from '../VideoItem/VideoItem';

const VideoList = ({ videos, onVideoSelect }) => {

    const videoItems = videos.map(video => {
        return <VideoItem video={video} onVideoSelect={onVideoSelect} />
    })

    return (
        <div className="ui divided relaxed list">
            {videoItems}
        </div>
    );
}

export default VideoList;