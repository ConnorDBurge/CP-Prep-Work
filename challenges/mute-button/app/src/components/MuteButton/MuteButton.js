import React from 'react';
import OnIcon from '../../icons/on.svg';
import OffIcon from '../../icons/off.svg';

// // Class solution
// class MuteButton extends React.Component {
//     render() {
//         const { isMuted, toggleMute } = this.props;
//         return (
//             <button onClick={toggleMute}>
//                 {isMuted ?
//                     <img src={OffIcon} alt='AudioOff' /> :
//                     <img src={OnIcon} alt='AudioOn' />}
//             </button>
//         );
//     }
// }

// Function solution
const MuteButton = (props) => {
    const { isMuted, toggleMute } = props;
    return (
        <button onClick={toggleMute}>
            {isMuted ?
                <img src={OffIcon} alt='AudioOff' /> :
                <img src={OnIcon} alt='AudioOn' />}
        </button>
    );
}


export default MuteButton;