def main():
    text = input("Enter Text Here ")

    def convert(emoticon):
      emoticon1 = emoticon.replace(':)', '🙂')
      emoticon2 = emoticon1.replace(':(', '🙁')
      return emoticon2
      
    print(convert(text))

main()