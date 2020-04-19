no_of_numbers = int(input("How many numbers will you enter (max:20) : "))
while no_of_numbers > 20:
    no_of_numbers = int(input("How many numbers will you enter (max:20) : "))

num_arr = {}
temp = 0

for i in range(no_of_numbers):
    num_arr[i] = int(input("Enter a number : "))

for i in range(no_of_numbers):
    for j in range(no_of_numbers):
        if num_arr[i] < num_arr[j]:
            if i > j:
                temp = num_arr[i]
                num_arr[i] = num_arr[j]
                num_arr[j] = temp

for i in range(no_of_numbers):
    print(num_arr[i])

