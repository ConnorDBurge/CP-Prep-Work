class BubbleSort:

    def __init__(self, array):
        self.sorted = self.bubble_sort(array)

    # My solution
    def sort(self, array):
        self.swaps = 0  # track number of swaps through entire sort
        self.iterations = 0  # number of passes through entire array
        while True:
            sort_again = False
            prev = 0  # pointer at the beginning
            current = 1  # pointer ine step in front of prev pointer
            self.iterations += 1  # counts passes through entire array
            while current < len(array):  # while we have not reached the end
                if array[current] < array[prev]:  # check to swap elements
                    array[current], array[prev] = array[prev], array[current]
                    sort_again = True  # sort array one more time
                    self.swaps += 1  # counts number of swap functions
                prev += 1  # move prev pointer forward
                current += 1  # move current pointer forward
            if not sort_again:
                break  # finished if no swaps were made
        return array  # returns a sorted array

    # Other solution
    def bubble_sort(self, sequence):
        swapped = True  # flag to resort array
        while swapped:  # stays true if swaps > 0
            swapped = False  # set False, change to true when 'if' below is True
            # i stops at second to last index, so 'i + 1' doesn't throw an IndexOutOfBounds Error
            for i in range(len(sequence) - 1):
                if sequence[i] > sequence[i + 1]:  # [0] > [1] during first iteration
                    sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                    swapped = True  # flags True to stay in while loop
        return sequence  # returns sequence sorted in place
