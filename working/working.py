import re


def main():
    print(convert(input("Hours: ")))
"""
1. split(' to ') the 12-hour string into a list w/ 2 elements
    a) starting time and ending time
2. Create a regex to determine if it is AM or PM
    a) AM route will not have 12 hours added
    b) PM route will add 12 hours
3. Create an empty 24 hr list
4. Create a regex to capture numbers prior to _AM or _PM
5. If len(numbers) == 1
    a) Convert numbers to int
    b) If int / 12 is greater than 1
        i) return ValueError
    c) Else return f"{int:2.f}:00"(integer with 2 places)
    d) return value to first index of 24 list
    e) repeat for other half
4. Else
    a) split(':') string to separate hours and minutes
    b) Run check for hours based on 12
    c) Run check for minutes based on 60
    d) Convert accordingly based on len(number) == 1 method
"""

def convert(s):
# Check if input is valid

    time_list = s.split(' to ')
    long_hour_clock = []

    if match := re.search('.+(AM|PM) to .+(AM|PM)', s):

# Start
    # AM Route
        if match_start := re.search('(.+) AM', time_list[0]):
            start = match_start.group(1)

            if len(start) <= 2:
                start_hour = start

                if (int(start_hour) / 12) < 1:
                    final_start_hour = start_hour.zfill(2)
                    final_start = final_start_hour + ':00'
                    long_hour_clock.append(final_start)

                elif int(start_hour) == 12:
                    start_hour = '00'
                    final_start = start_hour + ':00'
                    long_hour_clock.append(final_start)

                else:
                    raise ValueError

            else:
                start_list = start.split(':')
                start_hour = start_list[0]
                start_minute = start_list[1]

                if (int(start_hour) / 12) < 1 and (int(start_minute) / 60) < 1:
                    final_start_hour = start_hour.zfill(2)
                    start_list[0] = final_start_hour
                    final_start = ':'.join(start_list)
                    long_hour_clock.append(final_start)

                elif int(start_hour) == 12 and (int(start_minute) / 60) < 1:
                    final_start_hour = '00'
                    start_list[0] = final_start_hour
                    final_start = ':'.join(start_list)
                    long_hour_clock.append(final_start)

                else:
                    raise ValueError

        # PM Route
        if match_start := re.search('(.+) PM', time_list[0]):
            start = match_start.group(1)

            if len(start) <= 2:
                start_hour = start

                if (int(start_hour) / 12) < 1:
                    start_hour_int = int(start_hour)
                    new_start_hour = start_hour_int + 12
                    final_start_hour = f'{new_start_hour}'
                    final_start = final_start_hour + ':00'
                    long_hour_clock.append(final_start)

                elif int(start_hour) == 12:
                    start_hour = '12'
                    final_start = start_hour + ':00'
                    long_hour_clock.append(final_start)

                else:
                    raise ValueError

            else:
                start_list = start.split(':')
                start_hour = start_list[0]
                start_minute = start_list[1]

                if (int(start_hour) / 12) < 1 and (int(start_minute) / 60) < 1:
                    start_hour_int = int(start_hour)
                    new_start_hour = start_hour_int + 12
                    final_start_hour = f'{new_start_hour}'
                    start_list[0] = final_start_hour
                    final_start = ':'.join(start_list)
                    long_hour_clock.append(final_start)

                elif int(start_hour) == 12 and (int(start_minute) / 60) < 1:
                    final_start_hour = '12'
                    start_list[0] = final_start_hour
                    final_start = ':'.join(start_list)
                    long_hour_clock.append(final_start)

                else:
                    raise ValueError

    ##############################################################################################################

    # End
        # AM Route
        if match_end := re.search('(.+) AM', time_list[1]):
            end = match_end.group(1)

            if len(end) <= 2:
                end_hour = end

                if (int(end_hour) / 12) < 1:
                    final_end_hour = end_hour.zfill(2)
                    final_end = final_end_hour + ':00'
                    long_hour_clock.append(final_end)

                elif int(end_hour) == 12:
                    end_hour = '00'
                    final_end = end_hour + ':00'
                    long_hour_clock.append(final_end)

                else:
                    raise ValueError

            else:
                end_list = end.split(':')
                end_hour = end_list[0]
                end_minute = end_list[1]

                if (int(end_hour) / 12) < 1 and (int(end_minute) / 60) < 1:
                    final_end_hour = end_hour.zfill(2)
                    end_list[0] = final_end_hour
                    final_end = ':'.join(end_list)
                    long_hour_clock.append(final_end)

                elif int(end_hour) == 12 and (int(end_minute) / 60) < 1:
                    final_end_hour = '00'
                    end_list[0] = final_end_hour
                    final_end = ':'.join(end_list)
                    long_hour_clock.append(final_end)

                else:
                    raise ValueError

        # PM Route
        if match_end := re.search('(.+) PM', time_list[1]):
            end = match_end.group(1)

            if len(end) <= 2:
                end_hour = end

                if (int(end_hour) / 12) < 1:
                    end_hour_int = int(end_hour)
                    new_end_hour = end_hour_int + 12
                    final_end_hour = f'{new_end_hour}'
                    final_end = final_end_hour + ':00'
                    long_hour_clock.append(final_end)

                elif int(end_hour) == 12:
                    end_hour = '12'
                    final_end = end_hour + ':00'
                    long_hour_clock.append(final_end)

                else:
                    raise ValueError

            else:
                end_list = end.split(':')
                end_hour = end_list[0]
                end_minute = end_list[1]

                if (int(end_hour) / 12) < 1 and (int(end_minute) / 60) < 1:
                    end_hour_int = int(end_hour)
                    new_end_hour = end_hour_int + 12
                    final_end_hour = f'{new_end_hour}'
                    end_list[0] = final_end_hour
                    final_end = ':'.join(end_list)
                    long_hour_clock.append(final_end)

                elif int(end_hour) == 12 and (int(end_minute) / 60) < 1:
                    final_end_hour = '12'
                    end_list[0] = final_end_hour
                    final_end = ':'.join(end_list)
                    long_hour_clock.append(final_end)

                else:
                    raise ValueError

    else:
        raise ValueError

    final_clock = ' to '.join(long_hour_clock)

    if final_clock == '':
        raise ValueError
    else:
        return final_clock

if __name__ == "__main__":
    main()
