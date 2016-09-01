# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

# Solution 1, assuming no negative numbers
lst = [1,4,-7,-7,2,9]
lst.sort()
print lst
a,b,c = lst[-3:]
print a*b*c

# Solution 2
#[-10, -10, 1, 3, 2] => 300
lst = [-10, -10, 1, 3, 2]
lst.sort()
a,b = lst[:2]
c,d,e = lst[-3:]
cur_max = -1
if a < 0 and b < 0:
    if (a * b * e) > cur_max:
        cur_max = a * b * e
if (c * d * e) > cur_max:
    cur_max = c * d * e
print cur_max

# Solution 3
# if K > 3 or variable

