# # # def greeting():
# # #     print("Hello, Pereakpo")


# # # greeting()

# # # def greeting(first_nama, last_name):
# # #     print("Hello,", first_nama, last_name)
# # #     print(f"Welcome bak, {first_nama} {last_name}")


# # # greeting("Pereapko", "Kokowa")

# # def user_grade(grade1, grade2):
# #     return (grade1 + grade2) / 2


# # ayoola = user_grade(50, 100)
# # if ayoola > 60:
# #     print("Pass")
# # elif ayoola > 50:
# #     print("Just dey go")
# # else:
# #     print("Repeat Class")


# # def user_grade2(grade1, grade2):
# #     result = (grade1 + grade2) / 2
# #     if result > 60:
# #         print("Pass")
# #     elif result > 50:
# #         print("let my people go")
# #     else:
# #         print("Repeat Class")


# # user_grade2(10, 100)


# # -------- LIST COMPREHENSION -------

# # numbers = [1, 2, 3, 4, 5]
# # for n in numbers:
# #     print(n * 2)


# # salaries = [200000, 100000, 300000]
# # for salary in salaries:
# #     print(salary + (salary * 0.25))


# salaries = [200000, 100000, 300000]
# increment = []
# for salary in salaries:
#     new_salary = salary + (salary * 0.25)
#     increment.append(new_salary)

# print(increment)


# # -------- LIST COMPREHENSION -------
# # APPROACH USING LIST COMPREHENSION

# values = [10, 20, 30]
# new_values = [value * 2 for value in values]
# print(new_values)


# # MANUAL

# values = [10, 20, 30]
# new_values = []
# for value in values:
#     result = value * 2
#     new_values.append(result)

# print(new_values)


# -------------- BUILT-IN MODULES AND LIBRARIES ----------------
#  Mathematical Operations

import math

print(math.sqrt(81))
print(math.pi)
print(math.factorial(5))
print(math.cos(90))
print(math.tan(90))
print(math.sin(90))
