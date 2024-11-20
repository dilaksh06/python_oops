print (format("-","-<5"),"Types of Python Comprehensions",format("-","->5"),
"\n\n\nList Comprehension\n\
Dictionary Comprehension\n\
Set Comprehension\n\
Generator Expression\n ")

print("List Comprehension")
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

print("Dictionary Comprehension")

squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {key: value for key, value in original.items() if value % 2 == 0}
print(filtered)  # Output: {'b': 2, 'd': 4}

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {key: value for key, value in original.items() if value % 2 == 0}
print(filtered)  # Output: {'b': 2, 'd': 4}


printf("Set Comprehension")

squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

vowels = {char for char in "hello world" if char in 'aeiou'}
print(vowels)  # Output: {'o', 'e'}


print("Generator Expression")

squares = (x**2 for x in range(5))
print(list(squares))  # Output: [0, 1, 4, 9, 16]


total = sum(x**2 for x in range(5))
print(total)  # Output: 30


