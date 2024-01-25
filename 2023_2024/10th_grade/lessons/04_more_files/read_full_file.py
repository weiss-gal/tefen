file_name = "./yesterday.txt"

print(f"Opening file {file_name} ...")
with open(file_name) as f:
    file_contents = f.read()

# calculate number of lines
line_count = len(file_contents.split('\n'))
print(f"Number of lines: {line_count}")

# calculate the number of words
word_count = len(file_contents.split())
print(f"Number of words: {word_count}")

# calculate the number of characters
char_count = len(file_contents)
print(f"Number of chars: {char_count}")

user_input = input("Press <enter> to print the file contents")
if user_input == "":
    print(file_contents)

