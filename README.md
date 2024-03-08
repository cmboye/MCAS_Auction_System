# MCAS Auction system
## Instructions for basic usage
### Adding new sellers
1. Click the 'New seller' button (or skip directly to seller registration, see below).
2. Enter seller information, and the program will display an automatically-generated seller ID.
3. Click 'save'. To register the seller, see 'seller registration' section below.
### Setting up the auction file
When first starting up the program, it will prompt the user to enter the auction name. This will automatically load an auction file if it already exists, or otherwise if a new auction name is entered, then a new file will be created. This file will contain all the information on sales within an auction.
#### Seller registration
1. Click the 'Seller registration' button.
2. Enter the seller ID OR first and last name (please do not enter both!).
3. The program should automatically find the seller. If the seller has not sold with us before, the program should automatically open the new seller window (see steps a and b below).
  a. Enter the seller information.
  b. The program will automatically generate a seller ID.
4. Enter the number of items to register for the auction.
5. The program should then prompt the user to print a seller registration page.
#### Entering auctioned items
1. Click the 'Auction entry' button.
2. Enter the fields as prompted. You can leave the buyer number blank for cash sales.
3. Hit 'enter' to save.
#### Cashing out buyers
1. Click the 'Cash out' button.
2. Input the buyer number.
3. The program should display the items bought and their price, as well as the total owed by the buyer.
#### Seller payout
1. Click the 'Seller payout' button.
2. The program should display the items sold, the price it was sold as, what portion goes to the club, and what portion is paid to the seller. This should prompt the user to print this page.
##First-time setup
When running on a new computer, no seller information will be available. To keep seller information, a file named 'seller_info.csv' containing seller information (please note the format MUST be as follows: '') can be imported. The program will automatically use this file if it is in the '' directory.
## Restrictions on user entries
1. Seller IDs must consist of letters and can be 1-3 letters long. Note that the program will automatically convert the seller ID to capital letters regardless of how it was entered.
2. Buyer numbers are 3 digits long, ranging from 000-999.
## Warning messages
The program will provide a warning message in the following scenarios. In these cases, the user can proceed past the warning message and still execute the action.
1. A seller has over 50 registered items (please see customization section on how to update the bag limit if needed).
2. The sale price is over $99 (it will prompt the user to check that they have not entered the buyer number).
3. An item number has been entered twice. Note that the program will let you enter the same item number twice and retain both entries, but it is advisable to instead determine what the correct item number was.
4. There was an attempt to enter a seller that was not registered for this auction.
## Error messages
The program will provide an error message in the following scenarios. Please note that means the action the user was attempting could not be carried out.
1. Seller ID format is incorrect: Seller ID must be 1-3 letters.
2. Buyer number format is incorrect: Buyer number must be a 3 digit number 000-999.
3. There was an attempt to enter a seller ID that does not exist in the current seller database.
## Customization
To enter the customization screen, click the 'customization' button. A warning will pop up to avoid any accidental changes, and a warning will appear whenever the user tries to save any customizations. There will be some buttons depending on what is to be customized.
1. Minimum dollar amount: This changes the minimum dollar amount retained by the club per sale. To change, simply update the 1.00 to the applicable number. If you wish to remove a minimum dollar amount, then change this setting to 0.00.
2. Percent of sale: This is the percent of sale retained by the club. Please note that it is represented as a proportion, not a percentage, so 30% would be entered as 0.30 for example. Please note this percentage is only used when the amount exceeds the dollar amount.
3. Bag limit: Currently a warning will appear if a user tries to register over 50 items for a seller. Please update this number to change when the warning appears.
4. Seller ID: Currently a seller ID must be 1-3 letters (no case sensitivity). To update this, the user will need to know regex and enter an applicable pattern.
5. Buyer number: Currently a buyer number must be three digits, ranging from 000 to 999. To update this, the user will need to know regex and enter an applicable pattern.
NOTE: If there were any issues with accidental customization, please simply download the program again. Any other customizations that were purposeful will have to be redone.
