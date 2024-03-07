#MCAS system with GUI written by CB 3/6/24. Updated by CB on 3/7/24.
#Configure GUI:
load.file()##Load in GUI graphics
##Make sure GUI fits to screen?
##Lock window size? Or make this adaptive somehow??

#Allow the user to load previous seller information
seller_info=read.csv('seller_info.csv') #This contains seller information from previous auctions. This information will be printed as a header in the seller's payout summary

#Set defaults for variables that are customizable
bag_limit=50
dollar_amnt=1
club_percent=0.30
seller_ID_pattern=[aA-zZ]
buyer_n_pattern=[000-999]

#Reset items with each auction
auction_file=input()##Enter name of auction file
if{any(list.files==auction_file, read.csv(auction_file.csv),else(write.file(auction_file.csv)))} ##Check if it exists, if not initialize a new file (which will reset number of seller items)

#Init new seller
##Need multiple inputs here: first/last, address, phone number, email, number of items
new_seller=input() #Requirements: Seller_ID consists of 1-3 letters. Automatically convert to uppercase

#Register sellers
sellertemp=input()
OR
fltemp=input()
##Enter seller first, last and/or seller ID. If not present, prompted to register a new seller (see above section).
if{sellertemp=seller_ID, input(),else new_seller}
if{fltemp=paste(firstlast), input(),else new_seller}

#Init system to log auction sales. Need a good way to start/end files? Also, be sure to convert seller ID string to uppercase only
df=join(auction_file,seller_info)
df$item_number<-paste(df$sell_ID,df$itm_nmbr)
##Display warning if price >99. Did you enter buyer number or price?
##Skip buyer number if not entered, as we do for cash sales
##Calculate variables that will be displayed in real time
df$club_sales=if{price*club_percent<dollar_amnt, clube_sales=1, else, club_sales=club_percent*price}
df$total_sales=sum(df$price)
df$bag_count=length(unique(df$item_number))
##As this runs, keep track of total sales, total number of items entered, and money that will go to the club
##Display warning if this is a duplicate entry for the item number
##Display warning if this number exceeds the number of items this seller registered
##Deny entry with an error message if this seller has not been registered yet... will need a consistent db of all sellers, and a dynamic one per auction... reset number of items registered to 0 each time?
##Require buyer number to be a number from 0-999.

#Init user-friendly display of raw table
##Create a button that will open the raw table
return(df)##Display this a table in a specific order... this can be read-only (that might be best?... have a different button for writing?)

#Init billing system (summarize table by buyer number)
##Create button in main GUI to open this menu
buytemp=input()##Enter the buyer number
return(subset(df,df$buyer_number==buytemp)) ##Return certain information for this buyer
##Need to create an easy way to have this interact with the printer

#Init seller payout system:
##Create button to open the prompt for the payout system
selltemp=input()##Enter seller ID
y=subset(df,df$seller_ID==selltemp)
seller_payout=y$price-y$club_sales ##Seller will get the raw price minus the club's share
##Match to seller's ID to seller database too, and print their information as a header?
##Need to create an easy way to have this interact with the printer

#Configure printing:
##https://stackoverflow.com/questions/30329924/how-to-print-directly-without-showing-print-dialog-using-python-script-in-window

#Save auction file
##Create a save button such that you can save the current auction df, try to avoid any overwrite prompts
write.table(df,file="") ##Save file as auction_file.csv
