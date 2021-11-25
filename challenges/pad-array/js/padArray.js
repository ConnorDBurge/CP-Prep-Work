const pad = (array, minSize, value = null) => {
    var padded = array
    while (array.length < minSize) {
        padded.push(value)
    }
    return padded
}

module.exports = { pad }