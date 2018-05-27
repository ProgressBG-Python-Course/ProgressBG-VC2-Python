print("{:~^45}".format(" Simple while loop "))
i = 1
while i<=5 :
	print(i)
	i += 1


print("\n{:~^45}".format(" Example: sum all numbers in [1..100] "))
i = 1
sum = 0
while i <= 100:
	sum += i
	i += 1
print("sum = ", sum)

print("\n{:~^45}".format(" Task: sum even numbers in [1..100] "))
i = 1
sum = 0
while i<=100:
	if i%2 == 0:
		sum += i
	i += 1
print("sum = ", sum)	


print("\n{:~^45}".format(" Example of else clause in while "))
i = 1
while i <= 5:
	# if i==3 : break
	print(i)
	i += 1
else:
	print("Condition is not true when i = ", i)


print("\nEnter number, but not 0")
user_number = int(input("Enter a number, but not 0, please: "))
while user_number == 0:
	user_number = input("Enter a number, but not 0, please: ")
print("Your number is ", user_number)
