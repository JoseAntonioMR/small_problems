"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Example:
 Input: [[1, 2], [2, 3], [4, 5]]
 Output: [[1, 3], [4, 5]]

 Input: [[1, 5], [2, 3]]
 Output: [[1, 5]]
"""
from copy import copy


def merge(intervals, start_index=0):
    """ Merge overlaping intervals (run test using phyton problem2.py -v)
    >>> intervals = [[1, 5], [2, 4], [6, 7]]
    >>> merge(intervals)
    [[1, 5], [6, 7]]

    >>> intervals = [[1, 2], [2, 3], [4, 5]]
    >>> merge(intervals)
    [[1, 3], [4, 5]]

    >>> intervals = [[1, 5], [2, 3]]
    >>> merge(intervals)
    [[1, 5]]

    >>> intervals = [[12, 13], [0, 3], [2, 4], [9, 10], [1, 3], [5, 8], [14, 15], [11, 14]]
    >>> merge(intervals)
    [[0, 4], [5, 8], [9, 10], [11, 15]]
    """
    # Sort the intervals in increasing order in the first iteration
    if start_index == 0:
        intervals = sorted(intervals, key=lambda x: x[0])
    # Iterating the intervals
    for i in range(start_index, len(intervals) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] > intervals[i + 1][1]:
                del intervals[i + 1]
                return merge(copy(intervals), start_index=i)
            else:
                new_start = intervals[i][0]
                new_end = intervals[i + 1][1]
                intervals[i] = [new_start, new_end]
                del intervals[i + 1]
                return merge(copy(intervals), start_index=i)
    return intervals

# intervals = [[1, 5], [2, 4], [6, 7]]
# print intervals
# merged = merge(intervals)
# print merged

# print "\n\n"
# intervals = [[1, 2], [2, 3], [4, 5]]
# print intervals
# merged = merge(intervals)
# print merged

# print "\n\n"
# intervals = [[1, 5], [2, 3]]
# print intervals
# merged = merge(intervals)
# print merged

# print "\n\n"
# intervals = [[12, 13], [0, 3], [2, 4], [9, 10], [1, 3], [5, 8], [14, 15], [11, 14]]
# print intervals
# merged = merge(intervals)
# print merged


if __name__ == '__main__':
    import doctest
    doctest.testmod()
