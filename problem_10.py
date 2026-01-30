# Problem 10: Remove duplicates from a list
# Find and fix the error

numbers = [2,6,6,7,7,7,8,9,0,0]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"Unique numbers: {unique}")
