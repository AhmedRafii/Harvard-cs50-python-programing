import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    #open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #open shirt
    shirtfile = Image.open("shirt.png")
    #get the size of the shirt
    size = shirtfile.size
    #resize muppet image to file shirt
    muppet = ImageOps.fit(imagefile, size)
    #paste the shirt in the muppet
    muppet.paste(shirtfile, shirtfile)
    #create a output with wearing cs50 shirt
    muppet.save(sys.argv[2])

def check_command_line():
    #check command line agrument
    if len(sys.argv) > 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    input_one = splitext(sys.argv[1])
    input_two = splitext(sys.argv[2])
    #check if it image file or not
    if check_extrension(input_one[1]) == False:
        sys.exit("Invalid output")
    if check_extrension(input_two[1]) == False:
        sys.exit("Invalid output")
    #check if extension of both files are the same
    if input_one[1].lower() != input_two[1].lower():
        sys.exit("Input and output have different extensions")


def check_extrension(file):
    if file in [".jpg", ".png", ".jpeg"]:
        return True
    return False



if __name__ == "__main__":
    check_command_line()
    main()
