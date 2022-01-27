import React, { Component } from 'react';
import VideoItem from '../VideoItem/VideoItem';

const VideoList = ({ videos }) => {

    const videoItems = videos.map(video => {
        return <VideoItem />
    })

    return (
        <div>
            <ul>
                {videoItems}
            </ul>
        </div>
    );
}

export default VideoList;