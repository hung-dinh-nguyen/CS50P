def main():
    fileName = input('What is the file name? ').lower().strip()

    def fileJudge(file):
        if file.find('gif') > -1:
            return 'image/gif'
        elif file.find('jpg') > -1:
            return 'image/jpeg'
        elif file.find('jpeg') > -1:
            return 'image/jpeg'
        elif file.find('png') > -1:
            return 'image/png'
        elif file.find('pdf') > -1:
            return 'application/pdf'
        elif file.find('txt') > -1:
            return 'text/plain'
        elif file.find('zip') > -1:
            return 'application/zip'
        else:
            return 'application/octet-stream'

    print(fileJudge(fileName))

main()