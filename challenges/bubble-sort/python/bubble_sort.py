class BubbleSort:

    def __init__(self, array):
        self.sorted = self.sort(array)

    def sort(self, array):
        self.swaps = 0  # track number of swaps
        sorted = array
        prev = 0
        current = 1
        while current < len(sorted):
            if sorted[current] < sorted[prev]:
                moved = sorted[current]
                sorted[current] = sorted[prev]
                sorted[prev] = moved
                prev = 0
                current = 1
                self.swaps += 1
            else:
                prev += 1
                current += 1
        return sorted


# print(f"Final result: {result}")
# print(f"Swaps: {swaps}")
