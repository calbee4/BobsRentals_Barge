# ------------------------------
# Name: Jordyn Barge
# Assignment: Final Part 1
# ------------------------------

from datetime import datetime, timedelta

# --------------------
# Class Area
# --------------------

class Customer:
    def __init__(self, strName, intID, strRentalBasis = "", fltRentalTime = 0, intRentalQuantity = 0):
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



class Shop:
    def __init__(self):
        Ski = Skis()
        Snowboard = Snowboards()

    def Display_Inventory(self):
        Skis.Display_Inventory()
        Snowboards.Display_Inventory()
        print("Total inventory")



class Equipment:
    def __init__(self):
        pass
    
    def Set_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                Class.intInventory = 0
            else:
                Class.intInventory = intAmount
        except ValueError:
            raise Exception("intAmount must be a number")

    def Add_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                intAmount = 0
            
            Class.intInventory += intAmount
        except ValueError:
            raise Exception("intAmount must be a number")

    def Reduce_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                intAmount = 0

            if Class.intInventory - intAmount < 0:
                print("Can't reduce inventory by " + str(intAmount) + ". Inventory is at " + str(Class.intInventory))
            else:
                Class.intInventory -= intAmount
        except ValueError:
            raise Exception("intAmount must be a number")



class Skis(Equipment):
    def __init__(self, intQuantity = None):
        Equipment.__init__(self)

        if intQuantity == None:
            Skis.Request_Inventory()
        else:
            try:
                intQuantity = int(intQuantity)
                Skis.Set_Inventory(intQuantity)
            except ValueError:
                Skis.Request_Inventory()

    def Request_Inventory():
        intQuantity = Get_Valid_Integer("How much inventory is there for Skis today?: ", intRangeMin = 0)
        Skis.Set_Inventory(intQuantity)

    def Set_Inventory(intAmount):
        Equipment.Set_Inventory(Skis, intAmount)

    def Add_Inventory(intAmount):
        Equipment.Add_Inventory(Skis, intAmount)

    def Reduce_Inventory(intAmount):
        Equipment.Reduce_Inventory(Skis, intAmount)

    def Display_Inventory():
        print("\tSkis on hand:", Skis.intInventory)



class Snowboards(Equipment):
    def __init__(self, intQuantity = None):
        Equipment.__init__(self)

        if intQuantity == None:
            Snowboards.Request_Inventory()
        else:
            try:
                intQuantity = int(intQuantity)
                Snowboards.Set_Inventory(intQuantity)
            except ValueError:
                Snowboards.Request_Inventory()

    def Request_Inventory():
        intQuantity = Get_Valid_Integer("How much inventory is there for Snowboards today?: ", intRangeMin = 0)
        Snowboards.Set_Inventory(intQuantity)

    def Set_Inventory(intAmount):
        Equipment.Set_Inventory(Snowboards, intAmount)

    def Add_Inventory(intAmount):
        Equipment.Add_Inventory(Snowboards, intAmount)

    def Reduce_Inventory(intAmount):
        Equipment.Reduce_Inventory(Snowboards, intAmount)

    def Display_Inventory():
        print("\tSnowboards on hand:", Snowboards.intInventory)

# --------------------
# Function Area
# --------------------



# ------------------------------
# Function Name: Validate Integer
# Function Purpose: Validate an integer, within an optional inclusive range.
# ------------------------------
def Validate_Integer(intInput, intRangeMax = None, intRangeMin = None):
    if intRangeMin != None and intRangeMax != None:
        if intRangeMax < intRangeMin:
            intRangeMax = intRangeMin

    try:
        intInput = int(intInput)
        if intRangeMax != None and intInput > intRangeMax:
            print("Maximum input must be less than", intRangeMax + 1)
        elif intRangeMin != None and intInput < intRangeMin:
            print("Minimum input must be", intRangeMin, "or greater")
        else:
            global blnValidated
            blnValidated = True
    except ValueError:
        intInput = int(0)
        strOutput = "Input must be a whole number"

        if intRangeMin != None:
            strOutput += ", minimum " + str(intRangeMin)

        if intRangeMax != None:
            strOutput += ", maximum " + str(intRangeMax)

        print(strOutput)
    return intInput



# ------------------------------
# Function Name: Get Valid Integer
# Function Purpose: Yields the program until the user enters a valid integer. An optional inclusive range can be set.
# ------------------------------
def Get_Valid_Integer(strMessage, intRangeMax = None, intRangeMin = None):
    intInput = int(0)
    global blnValidated
    while blnValidated is False:
        intInput = input(strMessage)
        intInput = Validate_Integer(intInput, intRangeMax, intRangeMin)
    blnValidated = False
    print()
    return intInput



# --------------------
# Main Area
# --------------------

# --------------------
# Global Variables
# --------------------
blnValidated = bool(False)

def main():
    SnowShop = Shop()
    SnowShop.Display_Inventory()

main()

