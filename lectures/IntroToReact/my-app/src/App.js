import './App.css';
import Message from './Message';
import MessageClass from './MessageClass';

function App() {
  return (
    <div>
      <Message greeting="Hello" />
      <MessageClass greeting="World" />
    </div>
  );
}

export default App;
