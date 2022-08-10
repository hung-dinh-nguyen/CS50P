def main():
    import emoji

    emoji_str = input('What is the emoji? ')
    new_emoji = emoji.emojize(emoji_str, language='alias')
    print(f'Output: {new_emoji}')


main()