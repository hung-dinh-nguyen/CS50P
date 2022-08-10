def main():

    def convert(time):
        # Convert parameters to an array
        arr = time.split(':')
        # Create variables to equal values in array. Then, sum them.
        x = float(arr[0])
        y = float(arr[1]) / 60
        z = round(x + y, 2)
        # Return sum
        return z

# Determine Food Time 
    def food(time):
        if 7 <= time <= 8:
            return 'breakfast time'
        elif 12 <= time <= 13:
            return 'lunch time'
        elif 18 <= time <= 19:
            return 'dinner time'

# Input variable and convert to float
    value = input('What is the time? ')
    clock = convert(value)

# Check what time it is
    foodTime = food(clock)
    print(foodTime)

main()


