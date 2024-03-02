def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

print("# of vowels: " + str(count_vowels("hello world")))

for i in range(1, 21):
    print(i, end=" ")
    if (i % 2 == 0):
        print("- even")
    else:
        print("- odd")

def sum_of_integers(a, b):
    return a + b

print("sum: " + str(sum_of_integers(10, 9)))
