# Basic creation and access
# Given:
# python
# a) Print the first fruit.
# b) Print the last fruit.
# c) Print the middle fruit (index 2).
# d) Print only the first three fruits using slicing.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[-1])
print(fruits[2])
print(fruits[0:3])


#  Append, insert, and remove
# Start with:
# python

# a) Append 40 to the end.
# b) Insert 15 at index 1.
# c) Remove the value 20.
# d) Remove the last element using pop().
# Write the final nums list after all steps.

nums = [10, 20, 30]
nums.append(40)
nums.insert(1,15)
nums.remove(20)
nums.pop()
print(nums)

#  Loop through a list
# Given:

# python

# a) Write a for loop to print each number.
# b) Write the same using a while loop with index.
# c) Print only the numbers greater than 5.

numbers = [5, 9, 2, 8, 1]
for i in numbers:
    print(i)
x = 0


while x < len(numbers):
    print(numbers[x])
    x = x+1
print("---------------------------------")
for i in numbers:
    if i > 5:
        print(i)

l2 =[x for x in numbers if x > 5]
print(l2)






# List comprehension (easy)
# Given:

# python

# a) Create a new list with squares of all numbers.
# b) Create a new list with only the even numbers.
# c) Create a new list where each even number is doubled, and odd numbers are kept as‑is.

nums = [1, 2, 3, 4, 5]
nums1 = [x**2 for x in nums]
print(nums1)

num2 = [x**2 if x%2==0 else x for x in nums]
print(num2)

