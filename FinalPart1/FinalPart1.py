# ------------------------------
# Name: Jordyn Barge
# Assignment: Final Part 1
# ------------------------------

# --------------------
# Class Area
# --------------------

class Customer:
    def __init__(self, strName, intID):
        self.strName = strName
        self.intID = intID

    @property
    def strName(self):
        return self.__strName

    @property
    def intID(self):
        return self.__intID

    @strName.setter
    def strName(self, strValue):
        if strValue == "":
            raise Exception("strName should not be empty")
        else:
            self.__strName = strValue

    @intID.setter
    def intID(self, intValue):
        try:
            intValue = int(intValue)

            if intValue < 0:
                raise Exception("intID should be greater than 0")
            else:
                self.__intID = intValue
        except ValueError:
            raise Exception("intID should be a number")


# --------------------
# Function Area
# --------------------

# --------------------
# Main Area
# --------------------

def main():
    pass

main()

