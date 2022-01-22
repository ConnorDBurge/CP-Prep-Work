const PuzzleWord = (props) => {
    const { puzzleWord } = props;

    /* Create an array of objects that represent the letters in the puzzle word. 
    Each object has a letter property and a guessed property. 
    The guessed property is set to false for each letter. */
    const puzzleWordGuesses = puzzleWord.split('')
        .map((a) => {
            return {
                letter: a,
                guessed: false
            }
        })

    /**
     * This function takes in the puzzleWordGuesses array and returns a string of letters that have
     * been guessed correctly. 
     * 
     * The function loops through the array and checks if the letter has been guessed. If it has, it
     * returns the letter. If it hasn't, it returns an underscore. 
     * 
     * The function then joins the letters together and returns the string.
     * @returns The function is returning the displayWord.
     */
    const display = () => {
        const displayWord = puzzleWordGuesses
            .map((a) => {
                if (a.guessed) {
                    return a.letter
                } else {
                    return '_'
                }
            })
        return displayWord.join(' ')
    }

    return (
        <div>
            <h2>{display()}</h2>
        </div>
    );
}

export default PuzzleWord;