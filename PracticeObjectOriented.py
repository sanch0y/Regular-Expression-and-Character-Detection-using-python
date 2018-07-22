class Square:
    def __init__(self, height = "0", width = "0"):

        self.height = height
        self.width = width

    @property
    def height(self):
        print("retriving the height")
        return self.__height

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("give a number")


    @property
    def width(self):
        print("retriving the width")
        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("give a number")

    def getArea(self):
        return float(self.__height) * float(self.__width)

def main():
    aSquare = Square()

    height = input("enter height : ")
    width = input("enter width : ")

    aSquare.height = height
    aSquare.width = width

    print("your height", aSquare.height)
    print("your width", aSquare.width)
    print("your Area", aSquare.getArea())
main()

