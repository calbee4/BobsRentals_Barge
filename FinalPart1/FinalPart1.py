# ------------------------------
# Name: Jordyn Barge
# Assignment: Final Part 1
# ------------------------------

from datetime import datetime, timedelta
from typing import Self

# --------------------
# Class Area
# --------------------

class Customer:
    def __init__(self, strName, intID, strRentalBasis = None, fltRentalTime = None, intRentalQuantity = None):
        self.strName = strName
        self.intID = intID
        self.__strRentalBasis = strRentalBasis
        self.__fltRentalTime = fltRentalTime
        self.__intRentalQuantity = intRentalQuantity

    @property
    def strName(self):
        return self.__strName

    @property
    def intID(self):
        return self.__intID

    @property
    def strRentalBasis(self):
        return self.__strRentalBasis

    @property
    def fltRentalTime(self):
        return self.__fltRentalTime

    @property
    def intRentalQuantity(self):
        return self.__intRentalQuantity

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

            if intValue <= 0:
                raise Exception("intID should be greater than 0")
            else:
                self.__intID = intValue
        except ValueError:
            raise Exception("intID should be a whole number")

    @strRentalBasis.setter
    def strRentalBasis(self, strValue):
        if strValue == "Hourly" or strValue == "hourly":
            self.__strRentalBasis = "Hourly"
        elif strValue == "Daily" or strValue == "daily":
            self.__strRentalBasis = "Daily"
        elif strValue == "Weekly" or strValue == "weekly":
            self.__strRentalBasis = "Weekly"
        else:
            raise Exception("strRentalBasis must be Hourly, Daily, or Weekly")

    @fltRentalTime.setter
    def fltRentalTime(self, fltValue):
        try:
            fltValue = float(fltValue)

            if fltValue < 0:
                raise Exception("fltRentalTime should be 0 or greater")
            else:
                self.__fltRentalTime = fltValue
        except ValueError:
            raise Exception("fltRentalTime should be a number")

    @intRentalQuantity.setter
    def intRentalQuantity(self, intValue):
        try:
            intValu = int(intValue)

            if intValue < 0:
                raise Exception("intRentalQuantity should be 0 or greater")
            else:
                self.__intRentalQuantity = intValue
        except ValueError:
            raise Exception("intRentalQuantity should be a number")





# --------------------
# Function Area
# --------------------

# --------------------
# Main Area
# --------------------

def main():
    pass

main()

