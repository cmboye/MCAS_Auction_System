#MCAS system with GUI written by CB 3/6/24.
#Check for packages needed and download if not available
import importlib.util
import re
package_name = 'tkinter' ##Check if needed packages are available
spec = importlib.util.find_spec(package_name) ##Can I check multiple at once?
if spec is None:
    print(package_name +" is not installed")

#Configure GUI:
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
def reg_window(): ##Window opened when registering sellers
    seller_window = Toplevel(root)
    seller_window.title("Register Seller")
    seller_window.geometry("300x200")  ##Set the size of the new window
    label1 = Label(seller_window, image = patt)
    label1.place(x = 0, y = 0)
    seller_ID = StringVar() ##Take input and save
    bag_count = StringVar() ##Take input and save
    ttk.Label(seller_window, text="Seller ID:").pack(pady=10)
    entry1=Entry(seller_window, textvariable=seller_ID)
    entry1.pack()
    ttk.Label(seller_window, text="Bag count:").pack(pady=10)
    entry2=Entry(seller_window, textvariable=bag_count)
    entry2.pack()
    def val_inputs_reg(): ##Define the function to save registration screen inputs
        input_vector1 = entry1.get()
        input_vector2 = entry2.get()
        if not input_vector1 or not input_vector2: ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please fill in both input fields.")
            return
        while not re.match("^[-a-zA-Z ]{1,3}$", input_vector1):
            tkinter.messagebox.showinfo("Error", "Seller ID must be 1-3 letters.") ##Require 1-3 letters
            return
        if re.search(input_vector1,"DON",re.IGNORECASE): ##ignore case
            while not re.match("^[1-9][0-9]*$", input_vector2): ##If DON, require a number >0 (may have >50 donations)
                tkinter.messagebox.showinfo("Error", "Bag count must be a number >0. Please do not enter leading 0s")
                return
        else:
            while not re.match("^([1-9]|[1-4]\\d|50)$", input_vector2):
                tkinter.messagebox.showinfo("Error", "Bag count must be 1-50. Please do not enter leading 0s") #If not DON, require a number 1-50
                return
        ##If they pass error handling, append vectors to some globally defined vectors? Or add as rows for a df. These should also create however many rows for the bag IDs, etc.
        seller_window.destroy()

    button = ttk.Button(seller_window, text="Save", command=val_inputs_reg)
    button.pack()

def data_window(): ##Window opened when viewing auction data: look into pandastable
    seller_window = Toplevel(root)
    seller_window.title("Current auction data")
    seller_window.geometry("300x200")  ##Set the size of the new window
    label1 = Label(seller_window, image = patt)
    label1.place(x = 0, y = 0)

root = Tk()
#root.bind("<Return>", returnPressed)  ##Later I need to add something like this to make enter key work
root.iconbitmap("mcas.ico") ##Set icon
root.title('MCAS Auction') ##Set window name
root.geometry("1000x500") ##Make sure GUI fits to screen? Make this adaptive somehow?? Fix this later
patt = PhotoImage(file = "pattern.png")
bacg = PhotoImage(file = "bg.png") ##Add background... Eventually I will add a lot of white space to right/bottom
label2 = Label( root, image = bacg)
label2.place(x = 0, y = 0)
frm = ttk.Frame(root, padding=10)
frm.grid()
s=ttk.Style();s.configure('.', background='white') ##Use a white bg for ttk
ttk.Label(frm, text="MCAS Auction", font=("TkDefaultFont",25)).grid(column=0, row=0) ##Ideally I will later remove this from grid
ttk.Button(frm, text="Register seller", command=reg_window).grid(column=2, row=0)
ttk.Button(frm, text="Start auction", command=root.destroy).grid(column=3, row=0)
ttk.Button(frm, text="View data", command=data_window).grid(column=4, row=0)
ttk.Button(frm, text="Cash out", command=root.destroy).grid(column=5, row=0)
ttk.Button(frm, text="Pay sellers", command=root.destroy).grid(column=6, row=0)
ttk.Button(frm, text="Save auction", command=root.destroy).grid(column=7, row=0)
ttk.Button(frm, text="Start auction", command=root.destroy).grid(column=8, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=9, row=0) ##Button to exit program... need to add warning
root.mainloop()

#Allow the user to load previous seller information
seller_info=read.csv('seller_info.csv') #This contains seller information from previous auctions. This information will be printed as a header in the seller's payout summary

#Set defaults for variables that are customizable
bag_limit=50
dollar_amnt=1
club_percent=0.30
seller_ID_pattern="[A-Z]"[1-3] #Should be an uppercase number 1-3 digits long
buyer_n_pattern="%03d" #Require buyer number to be three digits?

#Reset items with each auction
auction_file=input()##Enter name of auction file
if{any(list.files==auction_file, read.csv(auction_file.csv),else(write.file(auction_file.csv)))} ##Check if it exists, if not initialize a new file (which will reset number of seller items)

#Init new seller
##Function that automatically generates new seller ID
sellid_fun=function(f,l){
str_extract(f,1,l,2) ##First letter in first name, 2 letters in last name
##Check that it is 1-3 letters and that it does not match an existing entry
str_extract(f,2,l,1) ##First 2 letters in first name, 1 letter in last name
str_extract(f,3) ##First 3 letters in first name
str_extract(l,3) ##First 3 letters in last name
paste(random(paste(f,l),3)) ##Random 3 letters in name
paste(random([A-Z]),3) ##Random 3 letters
##Make sure I convert seller ID to uppercase
return(sell_ID)
}
##Need multiple inputs here: first/last, address, phone number, email, number of items
f=input('First name: ')
l=input('Last name: ')
ad=input('Address: ')
phone=input('Phone number: ')
email=input('E-mail: ')
bag_count=input('Number of items to register (bag count): ')
sell_ID=sellid_fun(f,l)
##Write this info to seller_info.csv

#Register sellers
ttk.Button(frm, text="Register seller", command=).grid(column=1, row=0) ##Button to open register seller screen
sellertemp=input('Seller_ID: ')
ftemp=input('First name: ')
ltemp=input('Last name: ')
##First check which fields have been entered
if(sellertemp=NULL, fltemp=paste(ftemp,ltemp), str_extract(fltemp,paste(first,last)), else(str_extract(sellertemp,sell_ID)))
bag_count=input('Number of items to register (bag count): ')
##If there are multiple matches, how do I let user choose? Also, be sure to PROMPT if user wants to add new seller (Y/N) button; best if I can autofill first/last?
##Need to make sure new sellers are automatically saved?
##Check bag count !> 50... might be a problem for DON?

#Init system to log auction sales. Need a good way to start/end files? Also, be sure to convert seller ID string to uppercase only
ttk.Button(frm, text="Start auction", command=).grid(column=1, row=0)
df=join(auction_file,seller_info[grep('sell_ID','bag_count')]) ##Grab registered seller IDs and number of items to create a nearly empty table
main_assign_fun<-function(a,b,c,d){} ##Function to assign below information
sell_ID=input('Seller ID: ')
##Convert seller ID to uppercase
itm_nmbr=input('Item number: ')
##Check item number is 1-2 digits
price=input('Sale price: ')
buyer_number=input('Buyer number: ')
##Check buyer number is 3 digits or NULL
if{sell_ID=NULL,print("Please enter seller ID."), ##Below checks for missing data and produces error messages
else(itm_nmbr=NULL,print("Please enter item number.")),
else(price=NULL,print("Please enter price.")),
else(main_assign_fun(sell_ID,itm_nmbr,price,buyer_number))
}
df$item_number<-paste(df$sell_ID,df$itm_nmbr)
##Display warning if price >99. Did you enter buyer number or price?
##Skip buyer number if not entered, as we do for cash sales
##Calculate variables that will be displayed in real time
df$club_sales=if{price*club_percent<dollar_amnt, club_sales=1, else, club_sales=club_percent*price}
df$total_sales=sum(df$price)
df$bag_count=length(unique(df$item_number))
##As this runs, keep track of total sales, total number of items entered, and money that will go to the club
##Display warning if this is a duplicate entry for the item number
##Display warning if this number exceeds the number of items this seller registered
##Deny entry with an error message if this seller has not been registered yet... will need a consistent db of all sellers, and a dynamic one per auction... reset number of items registered to 0 each time?
##Require buyer number to be a number from 0-999.

#Init user-friendly display of raw table
ttk.Button(frm, text="View data", command=).grid(column=1, row=0) ##Create a button that will open the raw table
return(df)##Display this a table in a specific order... this can be read-only (that might be best?... have a different button for writing?)

#Init billing system (summarize table by buyer number)
ttk.Button(frm, text="Cash out", command=).grid(column=1, row=0) ##Create button in main GUI to open this menu
##How was this done before? Do I create a unique list of seller IDs and auto-print each??? Might make this is a sub-menu or something... Maybe also make a user-friendly way to cancel printing?
buytemp=input('Buyer number: ')##Enter the buyer number
return(subset(df,df$buyer_number==buytemp)) ##Return certain information for this buyer
##Need to create an easy way to have this interact with the printer

#Init seller payout system:
ttk.Button(frm, text="Pay sellers", command=).grid(column=1, row=0) ##Create button to open the prompt for the payout system
selltemp=input('Seller number: ')##Enter seller ID
y=subset(df,df$sell_ID==selltemp)
seller_payout=y$price-y$club_sales ##Seller will get the raw price minus the club's share
##Match to seller's ID to seller database too, and print their information as a header?
##Need to create an easy way to have this interact with the printer

#Configure printing:
##https://stackoverflow.com/questions/30329924/how-to-print-directly-without-showing-print-dialog-using-python-script-in-window

#Save auction file
ttk.Button(frm, text="Save auction", command=).grid(column=1, row=0) ##Create a save button such that you can save the current auction df, try to avoid any overwrite prompts
write.table(df,file="") ##Save file as auction_file.csv

#It would be best if I can include a warning message before closing the window (a reminder to save everything)
