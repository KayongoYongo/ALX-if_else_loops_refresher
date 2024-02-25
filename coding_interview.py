#!/usr/bin/python3

def return_total(n, nums=[]):
    """
    A script that returns the total value

    Args:
        n represents the size of the list
        nums: the list

    Return:
        Total value
    """
    total = 0

    for i in range(n):
        if i % 2 == 0:
            total += nums[i]
        else:
            total -= nums[i]

    if total % 2 == 0 and total % 3 != 0:
        return (total * 2)

    if total % 2 != 0 and total % 3 == 0:
        return (total * 3)

    if total % 2 == 0 and total % 3 == 0:
        return (total * 6)

    return total

new_value = return_total(3, [1,2,3])
print(new_value)
