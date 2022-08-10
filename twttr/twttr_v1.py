def main():
# Create a loop loop within a for loop
## 1st for loop will ierate through each index of the string input (range of length of string)
## 2ns for loop will iterate through the Vowel Array/List and find IF Statement exist in string input
## Replace that index of string input w/ ('')

    sentence = input('What is the tweet? ')
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


    sentence_length = range(len(sentence), -1, -1)
    print(sentence_length)

    for i in sentence_length:
        for vowel in vowelList:
            if sentence[i] == vowel:
                sentence = sentence.replace(sentence[i], '', 1)

    print(sentence)

main()