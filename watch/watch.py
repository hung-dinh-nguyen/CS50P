import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    try:
        src = re.search(r'src="([\w:/\.]+)"', s)
    except:
        return None

    try:
        link = src.group(1)
    except:
        return None

    if re.search(r'^(?:https?://)(?:www\.)?', link):
        if matches := re.search(r'youtube\.com/embed/(.+)', link):
            code = matches.group(1)
        else:
            return None
    else:
        return None

    short_yt = 'https://youtu.be/'
    new_link = short_yt + code

    return new_link

if __name__ == '__main__':
    main()

"""
1. Create a regex that is ('src=(.+")') and find the matching string
2. Create a variable equal to that matching string
3. Create another regex that verifies the URL is real
4. Create yet one more regex to verify that it is from YouTube
5. One more time, create a regex to capture the special link code
6. Combine special link code with the shorter, sharable youtu.be/
"""