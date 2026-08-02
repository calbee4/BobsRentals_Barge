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



class Shop:
    def __init__(self):
        Ski = Skis()
        Snowboard = Snowboards()
        self.fltHoursInDay = 10
        self.intDaysInWeek = 7

    @property 
    def fltHoursInDay(self):
        return self.__fltHoursInDay 

    @property 
    def intDaysInWeek(self):
        return self.__intDaysInWeek

    @fltHoursInDay.setter
    def fltHoursInDay(self, fltValue):
        try:
            fltValue = float(fltValue)

            if fltValue < 0:
                raise Exception("fltHoursInDay must be 0 or greater")
            elif fltValue > 24:
                raise Exception("fltHoursInDay must be 24 or less")
            else:
                self.__fltHoursInDay = fltValue
        except ValueError:
            raise Exception("fltHoursInDay must be a number")

    @intDaysInWeek.setter
    def intDaysInWeel(self, intValue):
        try:
            intValue = int(intValue)

            if intValue < 0:
                raise Exception("intDaysInWeek must be 0 or greater")
            elif intValue > 7:
                raise Exception("intDaysInWeek must be 7 ir less")
            else:
                self.__intDaysInWeek = intValue 
        except ValueError:
            raise Exception("intDaysInWeek must be a whole number")

    def Display_Inventory(self):
        Skis.Display_Inventory()
        Snowboards.Display_Inventory()
        print("Total inventory")



class Equipment:
    intInventory = 0
    fltHourlyRate = 0
    fltDailyRate = 0
    fltWeeklyRate = 0
    intInventoryRented = 0
    fltProfitAccumulated = 0

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
                Class.intInventoryRented += intAmount
        except ValueError:
            raise Exception("intAmount must be a number")

    def Accumulate_Profit(Class, fltAmount):
        try:
            fltAmount = float(fltAmount)

            if fltAmount < 0:
                fltAmount = 0

            Class.fltProfitAccumulated += fltAmount
        except ValueError:
            raise Exception("fltAmount must be a number")



class Skis(Equipment):
    fltHourlyRate = 15
    fltDailyRate = 50
    fltWeeklyRate = 200

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

    def Accumulate_Profit(fltAmount):
        Equipment.Accumulate_Profit(Skis, fltAmount)



class Snowboards(Equipment):
    fltHourlyRate = 10
    fltDailyRate = 40
    fltWeeklyRate = 160

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

    def Accumulate_Profit(fltAmount):
        Equipment.Accumulate_Profit(Snowboards, fltAmount)



class Rental:
    def __init__(self, instCustomer, clsEquipment, strRentalBasis, fltRentalTime, intRentalQuantity, strCheckoutCode = None):
        self.instCustomer = instCustomer
        self.clsEquipment = clsEquipment
        self.strRentalBasis = strRentalBasis
        self.fltRentalTime = fltRentalTime 
        self.intRentalQuantity = intRentalQuantity
        self.strCheckoutCode = strCheckoutCode
        self.blnActive = False

    @property
    def strRentalBasis(self):
        return self.__strRentalBasis

    @property
    def fltRentalTime(self):
        return self.__fltRentalTime

    @property
    def intRentalQuantity(self):
        return self.__intRentalQuantity

    @property
    def strCheckoutCode(self):
        return self.__strCheckoutCode

    @property 
    def blnActive(self):
        return self.__blnActive 

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
                raise Exception("fltRentalTime must be 0 or greater")
            else:
                self.__fltRentalTime = fltValue
        except ValueError:
            raise Exception("fltRentalTime must be a number")

    @intRentalQuantity.setter
    def intRentalQuantity(self, intValue):
        try:
            intValue = int(intValue)

            if intValue < 0:
                raise Exception("intRentalQuantity must be 0 or greater")
            else:
                self.__intRentalQuantity = intValue
        except ValueError:
            raise Exception("intRentalQuantity must be a number")

    @strCheckoutCode.setter 
    def strCheckoutCode(self, strValue):
        strValue = str(strValue)
        self.__strCheckoutCode = strValue

    @blnActive.setter 
    def blnActive(self, blnValue):
        blnValue = bool(blnValue)
        self.__blnActive = blnValue

    def Quote_Rental(self, strRentalBasis = None, fltRentalTime = None):
        fltPrice = 0

        if strRentalBasis != "Hourly" and strRentalBasis != "Daily" and strRentalBasis != "Weekly":
            strRentalBasis = None

        if strRentalBasis == None:
            strRentalBasis = self.strRentalBasis

        try:
            fltRentalTime = float(fltRentalTime)
        except ValueError:
            fltRentalTime = None

        if fltRentalTime == None:
            fltRentalTime = self.fltRentalTime

        if strRentalBasis == "Hourly":
            fltPrice = self.clsEquipment.fltHourlyRate * fltRentalTime
        elif strRentalBasis == "Daily":
            fltPrice =  self.clsEquipment.fltDailyRate * fltRentalTime
        else:
            fltPrice = self.clsEquipment.fltWeeklyRate * fltRentalTime

        if self.intRentalQuantity >= 3 and self.intRentalQuantity <= 5:
            fltPrice *= .75

        return fltPrice

    def Start_Rental(self):
        blnRentalSuccess = True
        intInventory = self.clsEquipment.intInventory

        if self.blnActive:
            blnRentalSuccess = False
            print("This rental is already active!")

        if intInventory == 0:
            blnRentalSuccess = False
            print("There's no more equpiment to rent! Come back later to request a rental")

        if intInventory - self.intRentalQuantity < 0:
            blnRentalSuccess = False 
            print("Rental quantity is larger than the equipment available! Current maximum rental request is", intInventory)

        if blnRentalSuccess:
            self.clsEquipment.Reduce_Inventory(self.intRentalQuantity)
            self.blnActive = True

    def Checkout(self):
        if self.blnActive:
            fltTotal = 0

            if self.strRentalBasis == "Hourly":
                fltTotal = self.Quote_Rental()

                if fltTotal > self.Quote_Rental("Weekly", 1):
                    fltTotal = self.Quote_Rental("Weeekly", 1)
                elif fltTotal > self.Quote_Rental("Daily", 1):
                    fltTotal = self.Quote_Rental("Daily", 1)

            if self.strRentalBasis == "Daily":
                fltTotal = self.Quote_Rental()

                if fltTotal > self.Quote_Rental("Weekly", 1):
                    fltTotal = self.Quote_Rental("Weeekly", 1)

            if self.strRentalBasis == "Weekly":
                fltTotal = self.Quote_Rental()

            self.clsEquipment.Accumulate_Profit(fltTotal)
        else:
            print("This rental is not active!")

    def Return_Rental(self):
        if self.blnActive:
            self.blnActive = False 

            self.clsEquipment.Add_Inventory(self.intRentalQuantity)
        else:
            print("This rental is not active!")





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

