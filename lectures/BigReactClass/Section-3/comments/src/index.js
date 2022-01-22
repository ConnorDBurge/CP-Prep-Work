import React from 'react';
import ReactDOM from 'react-dom';
import faker from 'faker';
import CommentDetail from './CommentDetail/CommentDetail';
import ApprovalCard from './ApprovalCard/ApprovalCard';

const App = () => {
    return (
        <div className="ui container comments">
            <ApprovalCard>
                <h4>Warning!</h4>
                Are you sure you want to do this?
            </ApprovalCard>
            <ApprovalCard>
                <CommentDetail
                    avatar={faker.image.image()}
                    author="Sam"
                    timeAgo="Today at 4:45pm"
                    text="Nice blog post" />
            </ApprovalCard>
            <ApprovalCard>
                <CommentDetail
                    avatar={faker.image.image()}
                    author="Alex"
                    timeAgo="Today at 2:00pm"
                    text="I think we should talk" />
            </ApprovalCard>
            <ApprovalCard>
                <CommentDetail
                    avatar={faker.image.image()}
                    author="Connor"
                    timeAgo="Yesterday at 5:00pm"
                    text="This is some text" />
            </ApprovalCard>

        </div>
    );
}

ReactDOM.render(<App />, document.querySelector('#root'))