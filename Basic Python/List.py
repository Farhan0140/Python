
#index : 0  1   2    3   4   5   6   7   8   9
List = [ 1, 23, 76, 123, 12, 99, 34, 10, 34, 54 ]
#index :-10 -9  -8  -7   -6  -5  -4  -3  -2  -1


print(List[5])   # 99
print(List[-5])  # 99

# [start, <end]
print(List[ :4])  #   [1, 23, 76, 123]
print(List[5: ])  #   [99, 34, 10, 34, 54]
print(List[: : -1])  #   [54, 34, 10, 34, 99, 12, 123, 76, 23, 1]
print(List[3: 7])  # [123, 12, 99, 34]


# [start, <end, step]
print(List[7: 3: -1])  # [10, 34, 99, 12]
print(List[1: 9: 2])  # [23, 123, 99, 10]




# -----------------------------
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
# >>> 2
fruits.count('tangerine')
# >>> 0
fruits.index('banana')
# >>> 3
fruits.index('banana', 4)  # Find next banana starting at position 4
# >>> 6
fruits.reverse()
# >>> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
# >>> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
# >>> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
# >>> 'pear'