def double_numbers(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2

my_list = [1, 2, 3, 4]
double_numbers(my_list)
print(my_list)  # Output: [2, 4, 6, 8]
