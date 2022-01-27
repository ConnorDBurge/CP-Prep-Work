import React, { Component } from 'react';
import VideoItem from '../VideoItem/VideoItem';

const VideoList = ({ videos }) => {

    const videoItems = videos.map(video => {
        return <VideoItem video={video} />
    })

    return (
        <div className="ui divided relaxed list">
            {videoItems}
        </div>
    );
}

export default VideoList;