t = int(input())
def nestedRangesCount(ranges, n):

    result = []
    result1 = [0 for i in range(n)]
    result2 = [0 for i in range(n)]

    # Iterating over all the ranges.
    for i in range(n):

        # Start and End value of the 'i'th range: [X, Y].
        x = ranges[i][0]
        y = ranges[i][1]

        # Iterating over all the other ranges.
        for j in range(n):

            # If 'i'th and 'j'th ranges are same, then skip the below steps.
            if (i == j):
                continue

            # Start and End value of the 'j'th' range: [A, B].
            a = ranges[j][0]
            b = ranges[j][1]

            # The 'i'th range contains the 'j'th range.
            if (x <= a and y >= b):
                result1[i] += 1

            # The 'i'th range is contained by the 'j'th range.
            if (x >= a and y <= b):
                result2[i] += 1
    
    result.append(result1)
    result.append(result2)
    
    return result