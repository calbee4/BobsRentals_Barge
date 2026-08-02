# ------------------------------
# Name: Jordyn Barge
# Assignment: Final Part 1
# ------------------------------

from datetime import datetime, timedelta

# --------------------
# Class Area
# --------------------

# Customer class

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

            if intValue <= 0:
                raise Exception("intID should be greater than 0")
            else:
                self.__intID = intValue
        except ValueError:
            raise Exception("intID should be a whole number")



# Shop class

class Shop:
    # Class properties

    intInventoryRented = 0
    fltProfitAccumulated = 0

    def __init__(self):
        Ski = Skis()
        Snowboard = Snowboards()

        # Operating hours and days per week

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
    def intDaysInWeek(self, intValue):
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

    # Display Inventory: Displays the inventory from all of the equipment
    def Display_Inventory(self):
        Skis.Display_Inventory()
        Snowboards.Display_Inventory()

    # Accumulate Profit: Adds to fltProfitAccumulated
    def Accumulate_Profit(fltAmount):
        try:
            fltAmount = float(fltAmount)

            if fltAmount < 0:
                fltAmount = 0

            Shop.fltProfitAccumulated += fltAmount
        except ValueError:
            raise Exception("fltAmount must be a number")



# Equipment class

class Equipment:
    # Class properties

    intInventory = 0
    fltHourlyRate = 0
    fltDailyRate = 0
    fltWeeklyRate = 0

    def __init__(self):
        pass
    
    # Set Inventory: Sets the inventory of the provided Class (should be a subclass of Equipment) to intAmount. Any number < 0 is set to 0.
    def Set_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                Class.intInventory = 0
            else:
                Class.intInventory = intAmount
        except ValueError:
            raise Exception("intAmount must be a number")

    # Add Inventory: Adds to the inventory of the provided Class (should be a subclass of Equipment) by intAmount. Any number < 0 is set to 0.
    def Add_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                intAmount = 0
            
            Class.intInventory += intAmount
        except ValueError:
            raise Exception("intAmount must be a number")

    # Reduce Inventory: Subtracts from the inventory of the provided Class (should be a subclass of Equipment) by intAmount. Any number < 0 is set to 0. Prints a message if the reduced amount would make the inventory drop below 0.
    def Reduce_Inventory(Class, intAmount):
        try:
            intAmount = int(intAmount)

            if intAmount < 0:
                intAmount = 0

            if Class.intInventory - intAmount < 0:
                print("Can't reduce inventory by " + str(intAmount) + ". Inventory is currently at " + str(Class.intInventory))
            else:
                Class.intInventory -= intAmount
                Shop.intInventoryRented += intAmount
        except ValueError:
            raise Exception("intAmount must be a number")



# Equipment class > Skis class

class Skis(Equipment):
    # Class properties

    fltHourlyRate = 15
    fltDailyRate = 50
    fltWeeklyRate = 200

    def __init__(self, intQuantity = None):
        Equipment.__init__(self)

        # If not instantiated with an inventory quantity, prompt the user to provide it.
        if intQuantity == None:
            Skis.Request_Inventory()
        else:
            try:
                intQuantity = int(intQuantity)
                Skis.Set_Inventory(intQuantity)
            except ValueError:
                Skis.Request_Inventory()

    # Request Inventory: Prompts the user to set the daily inventory.
    def Request_Inventory():
        intQuantity = Get_Valid_Integer("How much inventory is there for Skis today?: ", intRangeMin = 0)
        Skis.Set_Inventory(intQuantity)

    # Set Inventory: Inherited from super, but automatically passes the Skis class
    def Set_Inventory(intAmount):
        Equipment.Set_Inventory(Skis, intAmount)

    # Add Inventory: Inherited from super, but automatically passes the Skis class.
    def Add_Inventory(intAmount):
        Equipment.Add_Inventory(Skis, intAmount)

    # Reduce Inventory: Inherited from super, but automatically passes the Skis class.
    def Reduce_Inventory(intAmount):
        Equipment.Reduce_Inventory(Skis, intAmount)

    # Display Inventory: Display the inventory of Skis.
    def Display_Inventory():
        print("\tSkis on hand:", Skis.intInventory)



# Equipment class > Snowboards class

class Snowboards(Equipment):
    # Class properties

    fltHourlyRate = 10
    fltDailyRate = 40
    fltWeeklyRate = 160

    def __init__(self, intQuantity = None):
        Equipment.__init__(self)

        # If not instantiated with an inventory quantity, prompt the user to provide it.
        if intQuantity == None:
            Snowboards.Request_Inventory()
        else:
            try:
                intQuantity = int(intQuantity)
                Snowboards.Set_Inventory(intQuantity)
            except ValueError:
                Snowboards.Request_Inventory()

    # Request Inventory: Prompts the user to set the daily inventory.
    def Request_Inventory():
        intQuantity = Get_Valid_Integer("How much inventory is there for Snowboards today?: ", intRangeMin = 0)
        Snowboards.Set_Inventory(intQuantity)

    # Set Inventory: Inherited from super, but automatically passes the Snowboards class
    def Set_Inventory(intAmount):
        Equipment.Set_Inventory(Snowboards, intAmount)

    # Add Inventory: Inherited from super, but automatically passes the Snowboards class
    def Add_Inventory(intAmount):
        Equipment.Add_Inventory(Snowboards, intAmount)

    # Reduce Inventory: Inherited from super, but automatically passes the Snowboards class
    def Reduce_Inventory(intAmount):
        Equipment.Reduce_Inventory(Snowboards, intAmount)

    # Display Inventory: Display the inventory of Snowboards.
    def Display_Inventory():
        print("\tSnowboards on hand:", Snowboards.intInventory)



# Rental class

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

    # Quote Rental: Returns a rental quote useing the formula Equipment Rate of EquipmentBasis * EquipmentQuantity * RentalTime. The Rental Basis and the Rental Time can be set to compare different types of offerings for the customer.
    def Quote_Rental(self, strRentalBasis = None, fltRentalTime = None):
        fltPrice = 0

        # If strRentalBasis isn't recognized, set it to None
        if strRentalBasis != "Hourly" and strRentalBasis != "Daily" and strRentalBasis != "Weekly":
            strRentalBasis = None

        # If strRentalBasis is None, use the one already on the rental
        if strRentalBasis == None:
            strRentalBasis = self.strRentalBasis

        # If fltRentalTime is provided, validate it
        if fltRentalTime != None:
            try:
                fltRentalTime = float(fltRentalTime)
            except ValueError:
                fltRentalTime = None

        # If fltRentalTime is None, use the one already on the rental
        if fltRentalTime == None:
            fltRentalTime = self.fltRentalTime

        # Set the price to the equipment's rate per the rental basis
        if strRentalBasis == "Hourly":
            fltPrice = self.clsEquipment.fltHourlyRate
        elif strRentalBasis == "Daily":
            fltPrice =  self.clsEquipment.fltDailyRate
        else:
            fltPrice = self.clsEquipment.fltWeeklyRate

        # Multiply by the rental time and the quantity
        fltPrice *= fltRentalTime * self.intRentalQuantity

        # If the rental quantity is 3-5 items, include a 25% discount
        if self.intRentalQuantity >= 3 and self.intRentalQuantity <= 5:
            fltPrice *= .75

        return fltPrice

    # Start Rental: Checks if the requested items are in stock before activating the rental.
    def Start_Rental(self):
        blnRentalSuccess = True
        intInventory = self.clsEquipment.intInventory

        if self.blnActive:
            blnRentalSuccess = False
            print("This rental is already active!")

        if intInventory == 0 and blnRentalSuccess:
            blnRentalSuccess = False
            print("There's no more equpiment to rent! Come back later to request a rental")

        if intInventory - self.intRentalQuantity < 0 and blnRentalSuccess:
            blnRentalSuccess = False 
            print("Rental quantity is larger than the equipment available! Current maximum rental request is", intInventory)

        if blnRentalSuccess:
            self.clsEquipment.Reduce_Inventory(self.intRentalQuantity)
            self.blnActive = True

    # Checkout: Compares the current rental total to the Weekly and Daily rental basis to see if the customer can save some money, before providing a total and deactivating the rental.
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

            Shop.Accumulate_Profit(fltTotal)

            self.Return_Rental()

            return fltTotal
        else:
            print("This rental is not active!")

    # Return Rental: Deactivates the rental and returns the inventory.
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

# Global Variables

blnValidated = bool(False)



# Main

def main():
    # Make the shop
    SnowShop = Shop()
    SnowShop.Display_Inventory()

    # Create first customer
    Customer1 = Customer("Bob", 1)

    # Create Bob's Rental
    Customer1_Rental = Rental(Customer1, Snowboards, "Hourly", 5, 4)

    # Start the rental
    Customer1_Rental.Start_Rental()

    # How does it affect the inventory...?
    SnowShop.Display_Inventory()

    # Print a quote (does not automatically switch to best deal)
    print(Customer1_Rental.Quote_Rental())

    # Print a checkount (automatically switches to best deal)
    print(Customer1_Rental.Checkout())

    # See if we can reactivate stored rentals
    Customer1_Rental.Start_Rental()

    # Verify inventory
    SnowShop.Display_Inventory()

    # Check if the double rental affects the accumulating rental count
    print(SnowShop.intInventoryRented)

    # Check out
    Customer1_Rental.Checkout()

    # Verify inventory
    Skis.Display_Inventory()

    # Customer 2 walks in
    Customer2 = Customer("Anne", 2)

    # Check if we can make 2 rentals for her
    Customer2_Rental1 = Rental(Customer2, Skis, "Daily", 2, 3)
    Customer2_Rental2 = Rental(Customer2, Snowboards, "Daily", 2, 3)

    # Customer 1 is greedy and starts his rental again
    Customer1_Rental.Start_Rental()

    # Start Customer 2's rental
    Customer2_Rental1.Start_Rental()
    Customer2_Rental2.Start_Rental()

    # Check inventory
    SnowShop.Display_Inventory()

    # Checkout customer 1 so customer 2 can start their rental
    Customer1_Rental.Checkout()
    Customer2_Rental2.Start_Rental()

    # How does this affect inventory?
    SnowShop.Display_Inventory()

    # Checkout customer 2
    Customer2_Rental1.Checkout()
    Customer2_Rental2.Checkout()


main()

