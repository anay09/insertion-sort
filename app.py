no_of_numbers = int(input("How many numbers will you enter (max:20) : "))
while no_of_numbers > 20:
    no_of_numbers = int(input("How many numbers will you enter (max:20) : "))

num_arr = {}
for i in range(no_of_numbers):
    num_arr[i] = int(input("Enter a number : "))

