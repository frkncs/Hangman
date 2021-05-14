from random import randint

word_list = []

with open("english_word_list.txt", encoding="utf8") as f:
    word_list = f.readlines()

random_word_index = randint(0, len(word_list) - 1)

random_selected_word = word_list[random_word_index]

random_selected_word = random_selected_word[0:len(random_selected_word) - 1]

random_selected_word_set = set()

for i in random_selected_word:
    if i != " ":
        random_selected_word_set.add(i)

known_letters = []

life = len(random_selected_word)

name = input("\nWhat Is Your Name?: ")

print(f"\nHello {name}, Hangman is starting...")

while True:

    heKnow = False

    placeholder_text = ""

    print(f"\nYou left {life} life")

    if life <= 0:
        print("\nGame Over! You Lose!")
        print(f"\nWord Is: {random_selected_word}")
        break

    for letter in random_selected_word:

        knowningLetter = False

        for x in known_letters:
            if letter == x:
                placeholder_text += letter
                knowningLetter = True

        if knowningLetter == False:
            if (letter == " "):
                placeholder_text += " "
            else:
                placeholder_text += "-"

    print(f"\n\n{placeholder_text}\n\n")

    if len(known_letters) >= len(random_selected_word_set):
        print("You Win!")
        break

    entered_letter = input("Enter A Letter: ")

    if (entered_letter == "tellmeanswer"):
        print(random_selected_word)

    if len(entered_letter) != 1:
        print("\nYou can only enter 1 letter!")
    elif entered_letter in known_letters:
        print("\nYou already know this letter!")
    else:
        for i in random_selected_word:
            if (entered_letter == i):
                print("\nRight!")
                known_letters.append(entered_letter)
                heKnow = True
                break

        if heKnow == False:
            print("\nWrong!")
            life -= 1
