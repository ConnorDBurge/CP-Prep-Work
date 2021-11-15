from linear_search import linear_search, global_linear_search

print(linear_search(3, [1, 2, 3]) == 2)
print(linear_search(4, [1, 2, 3]) == None)
print(linear_search(13, [1, 2, 3]) == None)

print(global_linear_search("a", 'bananas') == [1, 3, 5])
