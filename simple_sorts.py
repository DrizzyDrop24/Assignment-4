# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: 

# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Modified by: Sahara Bangura

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def selection_sort(lst):
    n = len(lst)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key