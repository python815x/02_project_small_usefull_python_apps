# binary search : searches a number by taking 0 index and last index and divides the list of numbers by two to split
# them

# write a function that takes a list and target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop

def binary_search(target_list, element):
    middle = 0
    start = 0
    end = len(target_list)
    steps = 0
    while start <= end:
        print("Step", steps, ":", str(target_list[start:end + 1]))

        steps += 1
        middle = (start + end) // 2

        if element == target_list[middle]:
            return print(f'Searched is element: {middle}, took the algorithm {steps} steps')
        elif element < target_list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


target_list = [x for x in range(0, 250)]
element = 124

binary_search(target_list, element)
