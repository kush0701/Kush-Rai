def reverse_string(input_string):  
    reversed_string = input_string[::-1]
    return reversed_string
sample_string=str(input("enter the string:"))
reversed_result = reverse_string(sample_string)
print("Original String:", sample_string)
print("Reversed String:", reversed_result)
