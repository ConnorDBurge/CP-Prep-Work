class BubbleSort:

    def __init__(self, array):
        self.sorted = self.sort(array)

    def sort(self, array):
        self.swaps = 0  # track number of swaps through entire sort
        self.iterations = 0  # number of passes through entire array
        sorted = array  # array to edit in place
        while True:
            sort_again = False
            prev = 0  # pointer at the beginning
            current = 1  # pointer ine step in front of prev pointer
            self.iterations += 1
            while current < len(sorted):  # while we have not reached the end
                if sorted[current] < sorted[prev]:  # check to swap elements
                    self.swaps += 1
                    old_cur = sorted[current]  # store current variable
                    sorted[current] = sorted[prev]  # reset current to previous
                    sorted[prev] = old_cur  # set prev to cur old variable
                    sort_again = True  # sort array one more time
                prev += 1  # move prev pointer forward
                current += 1  # move current pointer forward
            if not sort_again:
                break  # finished if no swaps were made
        return sorted  # returns a sorted array
