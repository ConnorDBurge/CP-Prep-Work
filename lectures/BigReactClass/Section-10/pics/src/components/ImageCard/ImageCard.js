import React, { Component } from 'react';

class ImageCard extends Component {
    constructor(props) {
        super(props);
        this.imageRef = React.createRef();
        this.state = { rowSpans: 0 }
    }

    componentDidMount = () => {
        this.imageRef.current.addEventListener('load', this.setSpans);
    }

    setSpans = () => {
        const height = this.imageRef.current.clientHeight;
        const rowSpans = Math.ceil(height / 10);
        this.setState({ rowSpans: rowSpans })
    }


    render() {
        const { src, alt } = this.props.image;

        return (
            <div style={{ gridRowEnd: `span ${this.state.rowSpans}` }}>
                <img src={src.medium} alt={alt} ref={this.imageRef} />
            </div >
        );
    }
}

export default ImageCard;