def main():
# split('') string into an array
# run a for loop through the array to find any uppercase value using .isupper()
# if .isupper() is true, replace value/index at that point with ('_' + [i].lower())
# join array at the end to create final string

    camel = input('What is the camelCase? ')

    for index in range(len(camel)):
        if camel[index].isupper():
            camel = camel.replace(camel[index], ('_' + camel[index].lower()))

    return print(camel)

main()