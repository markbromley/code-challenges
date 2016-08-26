# You have an array of integers, and for each index you weant to find the product
# of every integer except the integer at that index

# Write a function get_products_of_all_ints_except_at_index() that takes a list 
# of integers and returns an array of the products.

# e.g. [1, 7, 3, 4] =>   [7*3*4, 1*3*4, 1*7*4, 1*7*3] = [84, 12, 28, 21]

# Do not use division in your solution.

# QUESTIONS
# Edge cases - zeros in list, list of size 1 or 2?
# List of integers?

# Solution 1
def get_products_of_all_ints_except_at_index_1(lst):
    """
    Time complexity O(n^2).
    Space complexity O(n).
    """
    export_lst = []
    for idx, val in enumerate(lst):
        new_value = None
        for idx_2, val_2 in enumerate(lst):
            if idx != idx_2:
                if new_value == None:
                    new_value = val_2
                else:
                    new_value *= val_2
        export_lst.append(new_value)
    return export_lst 

# Solution 2
def get_products_of_all_ints_except_at_index_2(lst):
    """
    Time complexity O(n).
    Space complexity O(n).
    """
    # Create a return list
    return_products = [1] * len(lst)

    # Create the list of integers after each index
    i = len(lst) - 1
    backward_product_so_far = 1
    while i > 0:
        backward_product_so_far *= lst[i]
        return_products[i - 1] = backward_product_so_far
        i -= 1

    # Multiply the list by the values - before - each index
    i = 0
    forward_product_so_far = 1
    while i <= len(lst) - 2:
        forward_product_so_far *= lst[i]
        return_products[i + 1] *= forward_product_so_far
        i += 1

    return return_products


if __name__ == "__main__":
    lst = [1,7,3,4]
    print get_products_of_all_ints_except_at_index_1(lst)
    print get_products_of_all_ints_except_at_index_2(lst)