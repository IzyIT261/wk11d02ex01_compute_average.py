"""
PROGCON Week 11 - Compute Average Summary

1. Four Test Arrays:
    - [22, 9, 0, 17]
    - [22, 0, 49, 8]
    - [35, 13, 22, 0]
    - [10, 5, -4, 27]

2. Implementation Note:
    - Implements the flowchart logic with early exit and division safety.
"""
# Main Program Execution
test_arrays = [
  [22, 9, 0, 17],
    [22, 0, 49, 8],
    [35, 13, 22, 0],
    [10, 5, -4, 27]
]

numbers = [0] * (4)

numbers[0] = 22
numbers[1] = 9
numbers[2] = 0
numbers[3] = 17
total = 0
count = 0
index = 0
while index < len(numbers):
    if numbers[index] == 0:
        total = total + numbers[index]
        count = count + 1
        index = index + 1
    else:
        if count > 0:
            print(float(total) / count)
        else:
            print(0)
        break # Add this to stop the loop on early exit
