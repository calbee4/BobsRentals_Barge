 ------------------------------
 Name: Jordyn Barge
 Assignment: Final Part 1
 Course: CPDM 120
 ------------------------------

 ------------------------------
 DESCRIPTION:
 Bobs Rentals is a program designed to simulate the experience of running a rental shop for snowboards and skis. It accurately keeps track of customer information, equipment inventory, and running totals of sales and rented equipment.
 ------------------------------

 ------------------------------
CLASSES:
Customer Class:
    The Customer class contains rudimentary customer information, just their name and ID.
    Instance Properties:
      strName: A required string.
      intID: A required integer.

 Shop Class:
    The Shop class contains running totals, such as the amount of equipment rented out all day and accumulated sales. It instantiates all the types of equipment.
    Class Properties:
      intInventoryRented: An integer that's used to keep track of all inventory rented through the day.
      fltProfitAccumulated: A float that's used to keep track of the profit accumulated through the day.
    Class Methods:
      Accumulate Profit(fltAmount: float): Adds fltAmount to fltProfitAccumulated.
    Instance Properties:
      fltHoursInDay: A float that's used to determine the operating hours of the shop per day.
      intDaysInWeek: An integer that's used to determine the operating days of the shop per week.
    Instance Methods:
      Display Inventory: Displays the inventory from all the equipment.

 Equipment Class:
    The Equipment class contains all the information needed to create subclasses of other equipment.
    Class Properties:
      intInventory: An integer used to track the amount of inventory on hand for the equipment.
      fltHourlyRate: A float used to determine the hourly rate of rental for the equipment.
      fltDailyRate: A float used to determine the daily rate of rental for the equipment.
      fltWeeklyRate: A float used to determine the weekly rate of rental for the equipment.
    Class Methods:
      Set Inventory(Class: class, intAmount: integer): Sets the inventory of the provided Class (should be a subclass of Equipment) to intAmount. Any number < 0 is set to 0.
      Add Inventory(Class: class, intAmount: integer): Adds to the inventory of the provided Class (should be a subclass of Equipment) by intAmount. Any number < 0 is set to 0.
      Reduce Inventory(Class: class, intAmount: integer): Subtracts from the inventory of the provided Class (should be a subclass of Equipment) by intAmount. Any number < 0 is set to 0. rints a message if the reduced amount would make the inventory drop below 0.

 Skis Class:
    Skis class inherits the Equipment class and is used to manage the Skis.
    Class Properties:
      intInventory: Inherited from Equipment.
      fltHourlyRate: Inherited from Equipment.
      fltDailyRate: Inherited from Equipment.
      fltWeeklyRate: Inherited from Equipment.
    Class Methods:
      Set Inventory(intAmount: integer): Inherited from Equipment. Passes Skis as Class.
      Add Inventory(intAmount: integer): Inherited from Equipment. Passes Skis as Class.
      Reduce Inventory(intAmount: integer): Inherited from Equipment. Passes Skis as Class.
      Request Inventory: Prompts the user to set the daily inventory.
      Display Inventory: Display the inventory of Skis.
      
 Snowboards Class:
    Snowboard class inherits the Equipment class and is used to manage the Snowboards.
    Class Properties:
      intInventory: Inherited from Equipment.
      fltHourlyRate: Inherited from Equipment.
      fltDailyRate: Inherited from Equipment.
      fltWeeklyRate: Inherited from Equipment.
    Class Methods:
      Set Inventory(intAmount: integer): Inherited from Equipment. Passes Snowboards as Class.
      Add Inventory(intAmount: integer): Inherited from Equipment. Passes Snowboards as Class.
      Reduce Inventory(intAmount: integer): Inherited from Equipment. Passes Snowboards as Class.
      Request Inventory: Prompts the user to set the daily inventory.
      Display Inventory: Display the inventory of Snowboards.
      
 Rental Class:
    Rental class is used to manage each rental from each customer. Rentals can be reactivated for later use.
    Instance Properties:
      instCustomer: Required, must be a customer instance.
      clsEquipment: Required, must be a subclass of equipment.
      strRentalBasis: Required string, must be "Hourly", "Daily", or "Weekly". Used to determine the type of rental basis.
      fltRentalTime: Required float, used to determine the amount of time the rental is active.
      intRentalQuantity: Required integer, used to determine the amount of items being rented.
      strCheckoutCode: String used if a discount code is provided.
      blnActive: Boolean used to determine if the rental is currently active.
    Instance Methods:
      Quote Rental(strRentalBasis: string or None, fltRentalTime: float or None): Returns a rental quote useing the formula Equipment Rate of EquipmentBasis * EquipmentQuantity * RentalTime. The Rental Basis and the Rental Time can be set to compare different types of offerings for the customer.
      Start Rental: Checks if the requested items are in stock before activating the rental.
      Checkout: Compares the current rental total to the Weekly and Daily rental basis to see if the customer can save some money, before providing a total and deactivating the rental.
#      Return Rental: Deactivates the rental and returns the inventory.
# ------------------------------
