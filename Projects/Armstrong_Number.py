num = input("Please enter your number:")
num_len = int(len(num))

final = 0
for ch in num:
    final += int(ch)**num_len
if final == int(num):
    print("Your number is an Armstrong Number.")
else:
    print("Your number is NOT an Armstrong Number.")