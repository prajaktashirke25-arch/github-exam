def find_greatest_of_two(num1, num2):

    if num1 > num2:
        return num1
    else:
        return num2

# Test the function
a, b = 57, 84
result = find_greatest_of_two(a, b)
print(f"The greatest number between {a} and {b} is: {result}")
