def main():
    list = {}
    sorted_list = []

    while True:
        try:
            item = input().upper()
            if list[item] > 0:
                list[item] += 1
        except KeyError:
            list[item] = 1
        except EOFError:
            break

# for loop through list to find and pull key/value
# The key/value will be put into elements within individual dict within a list using .append({})
### maybe can't be sort() | Must check another time

# Another option is to create a list within list. Then, sort() by that method.
## This method works. But it sorts by the first element in the list, so food must be first.

    for food in list:
        sorted_list.append([food, list[food]])

    sorted_list.sort()

    for index in range(len(sorted_list)):
        print(sorted_list[index][1], sorted_list[index][0])


main()