def main():
# Create a loop loop within a for loop
## 1st for loop will ierate through each index of the string input (range of length of string)
## 2ns for loop will iterate through the Vowel Array/List and find IF Statement exist in string input
## Replace that index of string input w/ ('')

    sentence = input('What is the tweet? ')
    print(sentence)
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letter_list = list(sentence)
    print(letter_list)

    sentence_length = range(len(letter_list) - 1, -1, -1)
    print(sentence_length)

    for i in sentence_length:
        for vowel in vowel_list:
            if letter_list[i] == vowel:
                letter_list[i] = ''

    new_sentence = ''.join(letter_list)
    print(new_sentence)

main()