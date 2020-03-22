# @todo test with random selection
# @todo test with language selecting
# @todo don't remove \n from the last line in file

file_name = "7lessonPart1.txt"

# print("1. Test kroz ceo fajl")
print("Known words:")
print("1. English")
print("2. Serbian")

words_option = int(input())

if words_option < 1 or words_option > 2:
    print("Invalid option!")
    exit()

points = 0
max_points = 0

test_file = open(file_name, 'r')

for line in test_file:
    max_points += 1

test_file.seek(0)

i = 1

for line in test_file:

    if line.endswith("\n"):
        line = line[:-1]  # Remove '\n' from line

    words_lst = line.split("-")

    if words_option == 1:
        known_words = words_lst[0].split(",")       # Get all known words into one list
        expected_words = words_lst[1].split(",")    # Get all expected words into one list
    else:
        known_words = words_lst[1].split(",")       # Get all known words into one list
        expected_words = words_lst[0].split(",")    # Get all expected words into one list

    answer = False

    print(str(i) +". {} - ".format(known_words))

    inputed_word = input()

    if(inputed_word == "exit()"):
        exit()

    for awaited_word in expected_words:
        if inputed_word == awaited_word:
            answer = True

    if answer:
        print("\tTrue\n")
        points += 1
    else:
        print("--> " + expected_words[0] + "\n")

    i+=1

print("Result: " + str(points) + " of " + str(max_points) + " points")