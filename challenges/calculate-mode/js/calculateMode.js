const calculateMode = (array) => {
    const mode = []
    const counts = {}
    let max = 0

    for (let i of array) { // track each count and max count
        counts[i] = isNaN(counts[i]) ? 1 : counts[i] += 1
        max = counts[i] > max ? counts[i] : max
    }

    for (let k of Object.keys(counts)) { // add modes to list
        if (counts[k] === max) {
            if (isNaN(Number(k))) {
                mode.push(k)
            } else {
                mode.push(Number(k))
            }
        }
    }

    return mode
}

module.exports = { calculateMode }