import { Component } from 'react'

// class based Component
class MessageClass extends Component {
    render() {
        return (
            <div>
                <h1>{this.props.greeting}</h1>
            </div>
        )
    }
}

export default MessageClass;