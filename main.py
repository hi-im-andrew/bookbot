def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count(book):
    return len(book.split())

def count_chars(book):
    frequencies = {}
    for word in book.split():
        for letter in word.lower():
            if letter not in frequencies.keys():
                frequencies[letter] = 1
            else:
                frequencies[letter] += 1
    return frequencies

print(f"Words: {count(main())}")
for (char, freq) in count_chars(main()).items():
    print(f"{char} appears {freq} times")