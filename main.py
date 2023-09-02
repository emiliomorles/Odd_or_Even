print("This program will tell you if the number is an odd number or an even number.")

number = int(input("Which number do you want to check? "))
number_result = number % 2

if number_result == 0:
  print("This number is an even number.")
else:
  print("This is an odd number.")
print("If you want to try it again please press the RUN button.")