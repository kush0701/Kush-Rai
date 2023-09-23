def sum_numbers_in_list():
    input_str = input("Enter a list of numbers separated by spaces: ")
    number_strings = input_str.split()
    total_sum = 0
    for num_str in number_strings:
        
            num = int(num_str)
            total_sum += num
        
    print(f"Sum of the numbers in the list: {total_sum}")
sum_numbers_in_list()
