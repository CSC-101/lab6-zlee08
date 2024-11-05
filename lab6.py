import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(books: list[data.Book]):
    for i in range(len(books) - 1):
        min_idx = i
        for j in range(i + 1, len(books)):  # finding the smallest
            if books[j].title < books[min_idx].title:
                min_idx = j

        if min_idx != i:  # swapping
            temp = books[i]
            books[i] = books[min_idx]
            books[min_idx] = temp

    return books

#Part 2
def swap_case(words: str) -> str:
    return ''.join(
        [char.lower() if char.isupper() else char.upper() if char.islower() else char for char in words])

# Part 3
def str_translate(words: str, old:str, new:str) -> str:
    result = ""
    for char in words:
        if char == old:
            result += new
        else:
            result += char
    return result

# Part 4
def histogram(line: str) -> dict:
    words = line.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts