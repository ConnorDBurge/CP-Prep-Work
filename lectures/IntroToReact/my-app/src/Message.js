import { useState } from 'react'

function Message(props) {
    const [myValue, setMyValue] = useState("something")

    return (
        <div>
            <h1>{props.greeting}</h1>
        </div>
    );
}



export default Message;