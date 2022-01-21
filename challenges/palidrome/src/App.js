import './App.css';
import { useState } from 'react';

const App = () => {
	const [isPal, setIsPal] = useState(false);

	const handleChange = (event) => {
		console.log(isPalindrome(event.target.value))
	}

	const isPalindrome = (input) => {
		let string = input.toString().toLowerCase()
		const chars = string.split('').filter((char) => {
			return char.match('[a-z0-9]')
		})

		while (chars.length > 1) {
			if (chars[0] !== chars[chars.length - 1]) {
				return setIsPal(false)
			} else {
				chars.pop()
				chars.shift()
			}
		}
		return setIsPal(true)
	}

	return (
		<div className="App">
			<h1>Is this a palindrome?</h1>
			<input type="text" name="palindrome" onChange={handleChange} />
			<div>{isPal ? 'True' : 'False'}</div>
		</div>
	);
}

export default App;
