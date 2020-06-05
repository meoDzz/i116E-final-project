"""This section is for main functions
"""
import numpy as np
import copy


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def nck_time(input_set, len_subset):
    tuso = factorial(len(input_set))
    mauso = factorial(len_subset) * factorial(len(input_set) - len_subset)

    return tuso / mauso


def check_last(input_list, ori_list):
    input_len = len(input_list)  # 2
    last_pos = input_len - 1  # 1
    max_index = len(ori_list) - 1  # 6
    output_list = [input_list]
    plus_1_last_elm = input_list.copy()  # [0,1]
    while plus_1_last_elm[last_pos] < max_index:
        plus_1_last_elm[last_pos] = plus_1_last_elm[last_pos] + 1
        output_list.append(plus_1_last_elm.copy())

    return output_list


def generate_combinations(n, k):
    """Generate all combinations from given n, k

    Parameters
    ----------
    n: Int

    k: Int

    Returns
    -------
    combinations: List(Int)
    """
    elements = list(range(n))
    combinations = []
    stack = []

    # Initialize first element in stack
    # first_elm = [] # todo: implement
    # stack.append(first_elm)
    first_elm = [elements[0]]
    max_elem = elements[len(elements) - 1]
    stack.append(first_elm)
    while len(stack) != 0:
        # pop an element from stack, call `elem_list`

        # check if length of elem equal to k true: check if last element of `elem_list` (`last_elem`) equal to n-1
        # true:  push `elem_list` to `combinations` false: increase `last_elem` by 1, then push back `elem_list` to
        # stack false: 1. get last element of `elem_list` (`last_elem`) 2. increase `last_elem` by 1, then push back
        # `elem_list` to stack, by e.g: [1] -> [2] 3. append new element that greater that has value: `last_elem` +
        # 1, by e.g: [1] -> [1,2], then push back `elem_list` to stack

        # pop an element from stack, call `elem_list`
        elem_list = stack.pop(len(stack) - 1)
        print("Elem_list before check k", elem_list)
        # check if length of elem_list equal to k
        if len(elem_list) < k:

            last_pos = len(elem_list) - 1
            # if elem_list(last_pos) < max_elem:
            # plus 1 in the last_elem
            elem_list_plus1 = elem_list.copy()
            elem_list_plus1[last_pos] = elem_list_plus1[last_pos] + 1
            if elem_list_plus1[last_pos] <= max_elem:
                stack.append(elem_list_plus1)
                print("elem_list_plus1 ", elem_list_plus1)

            # plus 1 in the last_elem then append in list ->  append in stack
            plus1 = elem_list[last_pos] + 1
            if plus1 <= max_elem:
                elem_list.append(plus1)
                stack.append(elem_list)
                print("elem_list add 1 new ", elem_list)
        else:
            # comb = []
            comb = check_last(elem_list, elements)
            print("length == k", elem_list)
            combinations.append(comb)

        # combinations.append(comb)

    return combinations


n = 5
k = 3

combs = generate_combinations(n, k)

print("generate_combinations", combs)

assert len(combs) == nck_time(range(n), k)
