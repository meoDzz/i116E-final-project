import copy
from math import sqrt
from joblib import Parallel, delayed
import time
import multiprocessing as mp


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combinadic_int(n, k):
    """
    Calculate the combinadic of n and k
    ----------###---------
    Parameter:
    Input:
      n: <int>
          The total number element
      k: <int>
          The number element of subset
    Output:
      number_of_comb: <int>
          The number of combination
    """
    if n == 0:
        return 0
    numerator   = factorial(n)
    denominator = factorial(k) * factorial(n - k)

    if n < k:
        print("result n < k", numerator / denominator)
    return numerator / denominator


def choose(n, k, limit):
    """
    This function finds the value of n when nCk, k are known
      E.g: nCk = n! / k!(n-k)!
    -------------###----------------
    Parameter:
    Input:
      k: <int>
          The value of choosen element
      n: <int>
          The number of list element
      limit: <int>
          The limitation value of combinadic of an Integer
    Output:
      n_sub: <int>
          The value of total number element in sub combination
      limit_sub: <int
          The remaing limitation : "limit_sub" = "nCk_value" - "limit"
    -------------###-----------------
    Return n_sub, limit_sub
    """
    # Check k and n
    if k > n:
        print("Error -----  k > n")
        return 0, 0
    else:
        # Initialize the value
        comb = []
        limit_sub = 0
        n_sub = n
        while True:
            if limit > 0:
                nCk_value = combinadic_int(n_sub, k)
                # if nCk_value == 1:
                # return n_sub, limit_sub
                if nCk_value <= limit:
                    limit_sub = limit - nCk_value
                    # print(limit_sub)
                    return n_sub, limit_sub
                else:
                    n_sub = n_sub - 1
            else:
                n_sub = k - 1
                return n_sub, limit_sub
        return -1, -1


def element_one_comb(n, k, limit):
    """
    This function wil find all value "n_sub" for the combinadic of interger
    -----------###-----------
    repeat the choose
    """
    # Initialize the first element
    n_sub = n
    k_sub = k
    limit_sub = limit
    comb = []
    for i in range(k):
        n_sub, limit_sub = choose(n_sub, k_sub, limit_sub)
        comb.append(n_sub)
        # print(" k_sub", k_sub)
        if k_sub > 0:
            k_sub = k_sub - 1

        # print("limit_sub", limit_sub)
        # limit = limit_sub
    return n_sub, comb


def generate_multi_core(n, k, element):
    n_sub_comb_test2, out = element_one_comb(n, k, element)
    return out


"""
This is a testing section for main function
"""
start_time = time.time()
number_of_cpu = mp.cpu_count()
n = 6
k = 4

# factorial_test = factorial(n)
combinadic_int_test = combinadic_int(n, k)

# limit_value = 0
# n_sub_test1, limit_sub = choose(n, k, limit_value)

# limit_value = 1
# n_sub_comb_test2, out = element_one_comb(n, k, limit_value)

list_input = list(range(int(combinadic_int_test)))
print("list_input", list_input)

# combs_result = Parallel(n_jobs=number_of_cpu)(delayed(generate_multi_core)(n, k, i) for i in list_input)
combs_result = Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(generate_multi_core)(n, k, i) for i in list_input)
finishing_time = time.time()

total_running_time = finishing_time - start_time

"""
Result section
"""

print("combinadic_int_test : ", combinadic_int_test)
# print("factorial_test      : ", factorial_test)
# print("n_sub value         : ", n_sub_test1)
# print("n_sub_comb_test2    : ", n_sub_comb_test2)
# print("Combination ", out)
print("total_running_time", total_running_time)
print("combs_result", combs_result)
