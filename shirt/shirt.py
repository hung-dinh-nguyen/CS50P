def main():

    image = find()
    resize_paste_save(image)

"""
1. 1. Import the necessary modules
    a) PIL, sys
2. Create If Statments to sys.exit
    a) Exit if sys.argv != 3
    b) Exit if find('.png') < 0 and find('.jpg') < 0 and find('.jpeg') < 0 and find('.PNG') < 0 and find('.JPG') < 0 and find('.JPEG') < 0
3. try: Open argv[1] Image
    a) except FileNotFoundError: sys.exit()
4. Resize Image 1
    a) Find shirt.png using shirt.size
    b) resize Image 1 accordingly
5. Paste shirt.png on top of Image 1
6. Save fusion image

"""

def find():
    from PIL import Image
    import sys

    if len(sys.argv) != 3:
        sys.exit('Not 3 command-line arguments')

    elif sys.argv[1].find('.png') < 0 and sys.argv[1].find('.jpg') < 0 and sys.argv[1].find('.jpeg') < 0 and sys.argv[1].find('.PNG') < 0 and sys.argv[1].find('.JPG') < 0 and sys.argv[1].find('.JPEG') < 0:
        sys.exit('Not an Image file')

    elif sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1]:
        sys.exit('Different File Extensions')

    else:
        try:
            return Image.open(sys.argv[1])

        except FileNotFoundError:
            sys.exit('File does not exist')

def resize_paste_save(image):
    from PIL import Image
    from PIL import ImageOps
    import sys

    shirt = Image.open('shirt.png')
    shirt_size = shirt.size

    new_image = ImageOps.fit(image, shirt_size)
    new_image.paste(shirt, shirt)

    return new_image.save(sys.argv[2])

if __name__ == '__main__':
    main()