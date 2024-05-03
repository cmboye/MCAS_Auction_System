##TO DO: resolve current NameError, check save sellers/load sellers. Work on new/find seller screen, seller and buyer checkouts. Make reg sheets? Seller and buyer checkout sheets?

#MCAS system with GUI written by CB 3/6/24.
required_packages = ['tkinter', 're', 'pandas','numpy'] #Check for packages needed
for package_name in required_packages:
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(package_name + " is not installed")

import importlib.util #Import libs
import re
import pandas as pd
import numpy as np
import os
import random

#Configure GUI:
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter import ttk
bags = [] ##Init variable to store bags
auc_club_tot = 0 ##Init variable to store club total
df2 = pd.DataFrame(columns=['Bag ID', 'Price', 'Buyer']) ##Init variable to store auction info
club_dollar=1
club_prc=.30

def load_data(file_path): ##Before anything, read seller file if present:
    try:
        dat = pd.read_csv(file_path)
        return dat
    except FileNotFoundError:
        return pd.DataFrame()

file_path = os.path.join(os.path.expanduser('~'),'Documents','seller_info.tsv'
slrs = load_data(file_path)

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

def new_window(): ##Window opened when registering sellers
    global slrs
    new_window = Toplevel(root)
    new_window.iconbitmap("mcas.ico")
    new_window.title("New Seller")
    new_window.geometry("300x550")  ##Set the size of the new window
    label1 = Label(new_window, image = patt)
    label1.place(x = 0, y = 0)
    new_window.attributes('-topmost', 'true')
    frst = StringVar() ##Take input and save
    lst = StringVar()
    addr = StringVar()
    st = StringVar()
    zip = StringVar()
    phn = StringVar()
    email = StringVar()
    bag_count = StringVar()
    ttk.Label(new_window, text="First name:").pack(pady=10)
    entry1=Entry(new_window, textvariable=frst)
    entry1.pack()
    ttk.Label(new_window, text="Last name:").pack(pady=10)
    entry2=Entry(new_window, textvariable=lst)
    entry2.pack()
    ttk.Label(new_window, text="Address:").pack(pady=10)
    entry3=Entry(new_window, textvariable=addr)
    entry3.pack()
    ttk.Label(new_window, text="State:").pack(pady=10)
    entry4=Entry(new_window, textvariable=st)
    entry4.pack()
    ttk.Label(new_window, text="Zip code:").pack(pady=10)
    entry5=Entry(new_window, textvariable=zip)
    entry5.pack()
    ttk.Label(new_window, text="Phone:").pack(pady=10)
    entry6=Entry(new_window, textvariable=phn)
    entry6.pack()
    ttk.Label(new_window, text="E-mail:").pack(pady=10)
    entry7=Entry(new_window, textvariable=email)
    entry7.pack()
    ttk.Label(new_window, text="Bag count:").pack(pady=10)
    entry8=Entry(new_window, textvariable=bag_count)
    entry8.pack()
    def val_inputs_new():
        global slrs
        input_vector1 = entry1.get().upper()
        input_vector2 = entry2.get().upper()
        input_vector3 = entry3.get()
        input_vector4 = entry4.get()
        input_vector5 = entry5.get()
        input_vector6 = entry6.get()
        input_vector7 = entry7.get()
        input_vector8 = entry8.get()
        if not input_vector1 or not input_vector2: ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please fill in both first and last name.")
            return
        while not re.match("^\d{5}+", input_vector5):
            tkinter.messagebox.showinfo("Error", "Zip code should only contain digits.")
            return
        while not re.match("^\d{5}+", input_vector6):
            tkinter.messagebox.showinfo("Error", "Phone number should only contain digits.")
            return
        while not re.match("^([1-9]|[1-4]\\d|50)$", input_vector8):
            tkinter.messagebox.showinfo("Error", "Bag count must be 1-50. Please do not enter leading 0s") #If not DON, require a number 1-50
            return
        def generate_random_id(first_name, last_name, existing_ids):
            first_initial = first_name[0].upper() ##Prioritize first letters to make it memorable
            last_initial = last_name[0].upper()
            while True:
                random_letters = [random.choice(first_initial+last_initial)]
                random_letters += [random.choice(first_name+last_name) for _ in range(random.randint(0, 2))]
                random_id = ''.join(random_letters).upper()
                if random_id not in existing_ids:
                    return(random_id)
        tmp_ID =  generate_random_id(input_vector1,input_vector2,slrs['ID'])
        tkinter.messagebox.showinfo("Seller ID", "Seller ID: "+str(tmp_ID)) ##Maybe I can use something other than a messagebox to make it less annoying?
        new_row = {'ID': tmp_id, 'First': input_vector1,'Last': input_vector2, 'Address': input_vector3, 'State': input_vector4, 'Zip': float(input_vector5),'Phone': float(input_vector6), 'E-mail': input_vector7}
        slrs = pd.concat([slrs, pd.DataFrame([new_row])], ignore_index=True)##Put all user entry info into a df
        global bags ##Make the variable global
        ids = [tmp_ID + "-" + str(i) for i in range(1, int(input_vector8) + 1)] ##If they pass error handling, populate all bags for that seller
        idst = set(ids)
        bagst = set(bags)
        bagst.update(idst) ##Only keep unique IDs
        bags = list(bagst) ##Keep a list of all bags across all sellers
        new_window.destroy()

    button = ttk.Button(new_window, text="Save", command=val_inputs_new) ##NameError: name 'slrs' is not defined error
    entry2.bind('<Return>', lambda event=None: val_inputs_new())
    entry2.bind('<Return>', lambda event=None: val_inputs_new())
    entry1.bind('<Tab>', focus_next_entry)
    entry2.bind('<Tab>', focus_next_entry)
    button.pack()

def reg_window(): ##Window opened when registering sellers
    seller_window = Toplevel(root)
    seller_window.iconbitmap("mcas.ico")
    seller_window.title("Register Seller")
    seller_window.geometry("300x200")  ##Set the size of the new window
    label1 = Label(seller_window, image = patt)
    label1.place(x = 0, y = 0)
    seller_window.attributes('-topmost', 'true')
    seller_ID = StringVar() ##Take input and save
    bag_count = StringVar() ##Take input and save
    ttk.Label(seller_window, text="Seller ID:").pack(pady=10)
    entry1=Entry(seller_window, textvariable=seller_ID)
    entry1.pack()
    ttk.Label(seller_window, text="Bag count:").pack(pady=10)
    entry2=Entry(seller_window, textvariable=bag_count)
    entry2.pack()
    ##Add a button to search for seller ID if needed, maybe also add new seller button here?
    def val_inputs_reg(): ##Define the function to save registration screen inputs
        input_vector1 = entry1.get().upper()
        input_vector2 = entry2.get()
        if not input_vector1 or not input_vector2: ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please fill in both input fields.")
            return
        while not re.match("^[-a-zA-Z ]{1,3}$", input_vector1):
            tkinter.messagebox.showinfo("Error", "Seller ID must be 1-3 letters.") ##Require 1-3 letters
            return
        if re.search(input_vector1,"DON",re.IGNORECASE): ##ignore case.
            while not re.match("^[1-9][0-9]*$", input_vector2): ##If DON, require a number >0 (may have >50 donations). I think this can be broken so double-check
                tkinter.messagebox.showinfo("Error", "Bag count must be a number >0. Please do not enter leading 0s")
                return
        else:
            while not re.match("^([1-9]|[1-4]\\d|50)$", input_vector2):
                tkinter.messagebox.showinfo("Error", "Bag count must be 1-50. Please do not enter leading 0s") #If not DON, require a number 1-50
                return
        global bags ##Make the variable global
        ids = [input_vector1 + "-" + str(i) for i in range(1, int(input_vector2) + 1)] ##If they pass error handling, populate all bags for that seller
        idst = set(ids)
        bagst = set(bags)
        bagst.update(idst) ##Only keep unique IDs
        bags = list(bagst) ##Keep a list of all bags across all sellers
        seller_window.destroy()

    button = ttk.Button(seller_window, text="Save", command=val_inputs_reg)
    entry2.bind('<Return>', lambda event=None: val_inputs_reg())
    entry2.bind('<Return>', lambda event=None: val_inputs_reg())
    entry1.bind('<Tab>', focus_next_entry)
    entry2.bind('<Tab>', focus_next_entry)
    button.pack()

def data_window(): ##Window opened when viewing auction data
    data_window = Toplevel()
    data_window.iconbitmap("mcas.ico")
    data_window.title("Auction Data")
    data_window.geometry("600x800")
    tree = ttk.Treeview(data_window,columns=("bags", "price", "buyer"), show='headings')#, "Seller IDs", "Number")) ##Display
    tree.heading("bags", text="Bag IDs")
    tree.heading("price", text="Price")
    tree.heading("buyer", text="Buyer")
    scrollbar = Scrollbar(data_window, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    df1 = pd.DataFrame({'Bag ID': bags})
    df1['Bag ID'] = df1['Bag ID'].astype(str)##Force keys to both be strings
    df2['Bag ID'] = df2['Bag ID'].astype(str)
    df3 = df1.merge(df2, on='Bag ID',how='left') ##Match bag IDs and add price, buyer
    df3['Alpha'] = df3['Bag ID'].str.extract('([a-zA-Z]+)')##Idea for sorting without leading 0s: extract alphabetical part and numeric part into new cols. sort by alpha then numeric. sort accordingly, then remove columns
    df3['Num'] = df3['Bag ID'].str.extract('(\d+)')
    df3['Num'] = df3['Num'].str.zfill(2)
    df3['Num'] = df3['Num'].astype(int)
    df_sorted = df3.sort_values(by=['Alpha', 'Num'])
    df_sorted.drop(columns=['Alpha', 'Num'], inplace=True)
    for i, row in df_sorted.iterrows(): ##Then need to convert back to vectors for treeview
        tree.insert("", tkinter.END, text=str(i), values=row.tolist())
    tree.pack(pady=5, padx=5, expand=True, fill="both")
    close_button = Button(data_window, text="Close", command=data_window.destroy)
    close_button.pack(side="bottom", pady=5)
    data_window.mainloop()

def auction_window():
    auction_window = Toplevel(root)
    auction_window.iconbitmap("mcas.ico")
    auction_window.title("Enter auction sales")
    auction_window.geometry("300x450")  ##Set the size of the new window
    label1 = Label(auction_window, image = patt)
    label1.place(x = 0, y = 0)
    auction_window.attributes('-topmost', 'true')
    sell_ID = StringVar() ##Take input and save
    bag = StringVar() ##Take input and save
    prc = StringVar() ##Take input and save
    byr = StringVar() ##Take input and save
    ttk.Label(auction_window, text="Seller ID:").pack(pady=10)
    entry1=Entry(auction_window, textvariable=sell_ID)
    entry1.pack()
    ttk.Label(auction_window, text="Bag number:").pack(pady=10)
    entry2=Entry(auction_window, textvariable=bag)
    entry2.pack()
    ttk.Label(auction_window, text="Price:").pack(pady=10)
    entry3=Entry(auction_window, textvariable=prc)
    entry3.pack()
    ttk.Label(auction_window, text="Buyer:").pack(pady=10)
    entry4=Entry(auction_window, textvariable=byr)
    entry4.pack()
    def val_inputs_enter(): ##Define the function to save registration screen inputs
        input_vector1 = entry1.get().upper()
        input_vector2 = entry2.get()
        input_vector3 = entry3.get()
        input_vector4 = entry4.get()
        global df2
        global auc_club_tot
        global auc_enter_bag
        global auc_tot
        global auc_tot_bag
        if not input_vector1 or not input_vector2 or not input_vector3: ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please fill in input fields 1-3.")
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
        if (input_vector1 + "-" + str(input_vector2)) in df2['Bag ID'].values: ##Double-check that bag information has not already been entered
            row = df2[df2['Bag ID'] == input_vector1 + "-" + str(input_vector2)]
            if (pd.notna(row['Price'].iloc[0])):
                tkinter.messagebox.showinfo("Error", "Information has already been entered for this bag ID.")
        bag_id = input_vector1 + "-" + str(input_vector2) ##If seller ID and bag number pass error handling, then concatenate
        if not bag_id in bags: ##Now check bag ID has already been registered
            tkinter.messagebox.showinfo("Error", "Entered bag information does not exist. Was buyer registered for the number of items?") ##Later I could force new entries to be added to bags. Maybe that is better?
            return
        if not input_vector3.isdigit():
            tkinter.messagebox.showinfo("Error", "Please enter a valid number for the price.") ##Later I could force new entries to be added to bags. Maybe that is better?
            return
        if int(input_vector3) > 99:
            response=tkinter.messagebox.askyesno("Warning","Price >$99. Please confirm you did not enter buyer number. Accept entry?")##If price >99 display warning (best if I can do this without opening a new window for minimal disruption)
            if not response:
                return
        if input_vector4 == "": ##Check buyer number is blank or a 3 digit number (allow leading 0s)
            input_vector4=("Cash")##Save
        elif not input_vector4.isdigit() or len(input_vector4) != 3:
            tkinter.messagebox.showinfo("Error", "Please enter a 3 digit number or leave blank.")
            return
        else:
            input_vector4=(input_vector4)##Save
        new_row = {'Bag ID': bag_id, 'Price': float(input_vector3),'Buyer': input_vector4}
        df2 = pd.concat([df2, pd.DataFrame([new_row])], ignore_index=True)##Put all user entry info into a df
        sell_ID.set("") # Clear entry fields after saving
        bag.set("")
        prc.set("")
        byr.set("")
        auc_tot=df2['Price'].fillna(0).sum()##Calculate metrics in an easy-to-update way
        if float(input_vector3)*club_prc < club_dollar:
            auc_mcas_prc=round(club_dollar,2)
        else:
            auc_mcas_prc=round(float(input_vector3)*club_prc,2)
        auc_club_tot += auc_mcas_prc
        auc_enter_bag=len(df2['Bag ID'])
        auc_tot_bag=len(bags)
        lab1.config(text="Total sales: $"+str(auc_tot))
        lab2.config(text="Club sales: $" +str(auc_club_tot))
        lab3.config(text="Entered bag count: " +str(auc_enter_bag))
        lab4.config(text="Total bag count: " +str(auc_tot_bag))
        return

    ttk.Button(auction_window, text="Save", command=val_inputs_enter).pack(pady=10)
    lab1=ttk.Label(auction_window,text="Total sales: Enter a bag to start counter")##Display totals in auction window
    lab1.pack(pady=10)
    lab2=ttk.Label(auction_window,text="Club sales: Enter a bag to start counter")
    lab2.pack(pady=10)
    lab3=ttk.Label(auction_window,text="Entered bag count: Enter a bag to start counter")
    lab3.pack(pady=10)
    lab4=ttk.Label(auction_window,text="Total bag count: Enter a bag to start counter")
    lab4.pack(pady=10)
    entry1.bind('<Return>', lambda event=None: val_inputs_enter())
    entry2.bind('<Return>', lambda event=None: val_inputs_enter())
    entry3.bind('<Return>', lambda event=None: val_inputs_enter())
    entry4.bind('<Return>', lambda event=None: val_inputs_enter())
    entry1.bind('<Tab>', focus_next_entry)
    entry2.bind('<Tab>', focus_next_entry)
    entry3.bind('<Tab>', focus_next_entry)
    entry4.bind('<Tab>', focus_next_entry)
    return

def save_window():
    save_window = Toplevel(root)
    save_window.iconbitmap("mcas.ico")
    save_window.title("Save auction data")
    save_window.geometry("300x200")  ##Set the size of the new window
    label1 = Label(save_window, image = patt)
    label1.place(x = 0, y = 0)
    save_window.attributes('-topmost', 'true')
    auc_time = StringVar() ##Take input and save
    yr = StringVar() ##Take input and save
    ttk.Label(save_window, text="Fall or Winter auction? (used in save file name):").pack(pady=10)
    entry1=Entry(save_window, textvariable=auc_time)
    entry1.pack()
    ttk.Label(save_window, text="Year (used in save file name):").pack(pady=10)
    entry2=Entry(save_window, textvariable=yr)
    entry2.pack()
    def val_inputs_save():
        input_vector1 = entry1.get().lower()
        input_vector2 = entry2.get()
        if not input_vector1 or not input_vector2: ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please fill in both input fields.")
            return
        if not input_vector1.isalpha() : ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please enter letters only for fall/winter.")
            return
        if not input_vector2.isdigit() : ##Basic error handling
            tkinter.messagebox.showinfo("Error", "Please enter numbers only for year.")
            return
        df1 = pd.DataFrame({'Bag ID': bags})
        df1['Bag ID'] = df1['Bag ID'].astype(str)##Force keys to both be strings
        df2['Bag ID'] = df2['Bag ID'].astype(str)
        df3 = df1.merge(df2, on='Bag ID',how='left') ##Match bag IDs and add price, buyer
        df3['Alpha'] = df3['Bag ID'].str.extract('([a-zA-Z]+)')
        df3['Num'] = df3['Bag ID'].str.extract('(\d+)')
        df3['Num'] = df3['Num'].str.zfill(2)
        df3['Num'] = df3['Num'].astype(int)
        df_sorted = df3.sort_values(by=['Alpha', 'Num'])
        df_sorted.drop(columns=['Alpha', 'Num'], inplace=True)##Reconstruct df_sorted
        fpath = input_vector1 + str(input_vector2) + ".tsv"
        complete_path = os.path.join(os.path.expanduser('~'), 'Documents', fpath)
        df_sorted.to_csv(complete_path, sep='\t', index=False)##Save with winter/fall and year
        slrs.to_csv(os.path.join(os.path.expanduser('~'),'Documents','seller_info.tsv'),sep='\t', index=False)##Add something here to also save seller files
        tkinter.messagebox.showinfo("Success", "Auction file successfully saved as " + complete_path)
        save_window.destroy()

    ttk.Button(save_window, text="Save", command=val_inputs_save).pack(pady=10)
    entry1.bind('<Return>', lambda event=None: val_inputs_save())
    entry2.bind('<Return>', lambda event=None: val_inputs_save())
    entry1.bind('<Tab>', focus_next_entry)
    entry2.bind('<Tab>', focus_next_entry)

def load_file():
    global df2
    global bags
    doc_folder = os.path.join(os.path.expanduser('~'), 'Documents')
    filep = filedialog.askopenfilename(initialdir=doc_folder)
    try:
        with open(filep, 'r') as file:
            df2 = pd.read_csv(filep, delimiter='\t', na_values='')
            tkinter.messagebox.showinfo("Success", f"File '{filep}' loaded.")
    except FileNotFoundError:
        tkinter.messagebox.showinfo("Error", f"File '{filep}' not found.")
    bags=df2['Bag ID'].tolist()

def quit_confirmation():
    msg_box = tkinter.messagebox.askquestion("Exit", "Are you sure you want to exit? Please make sure you saved first.",icon="warning")
    if msg_box == "yes":
     root.destroy()

root = Tk()
#root.bind("<Return>", returnPressed)  ##Later I need to add something like this to make enter key work
root.iconbitmap("mcas.ico") ##Set icon
root.title('MCAS Auction') ##Set window name
root.geometry("1050x500") ##Make sure GUI fits to screen? Make this adaptive somehow?? Fix this later
patt = PhotoImage(file = "pattern.png")
bacg = PhotoImage(file = "bg.png") ##Add background... Eventually I will add a lot of white space to right/bottom
label2 = Label( root, image = bacg)
label2.place(x = 0, y = 0)
frm = ttk.Frame(root, padding=10)
frm.grid()
s=ttk.Style();s.configure('.', background='white') ##Use a white bg for ttk
ttk.Label(frm, text="MCAS Auction", font=("TkDefaultFont",25)).grid(column=0, row=0)
ttk.Button(frm, text="New seller", command=new_window).grid(column=1, row=0)
ttk.Button(frm, text="Register seller", command=reg_window).grid(column=2, row=0)
ttk.Button(frm, text="Auction entry", command=auction_window).grid(column=3, row=0)
ttk.Button(frm, text="View data", command=data_window).grid(column=4, row=0)
ttk.Button(frm, text="Cash out", command=root.destroy).grid(column=5, row=0)
ttk.Button(frm, text="Pay sellers", command=root.destroy).grid(column=6, row=0)
ttk.Button(frm, text="Load auction", command=load_file).grid(column=7, row=0)
ttk.Button(frm, text="Save auction", command=save_window).grid(column=8, row=0)
ttk.Button(frm, text="Settings", command=root.destroy).grid(column=9, row=0)
ttk.Button(frm, text="Quit", command=quit_confirmation).grid(column=10, row=0) ##Button to exit program...
root.mainloop()

#Below is a bunch of pseudocode and notes:
#Allow the user to load previous seller information
seller_info=read.csv('seller_info.csv') #This contains seller information from previous auctions. This information will be printed as a header in the seller's payout summary

#Set defaults for variables that are customizable

#Register sellers
ttk.Button(frm, text="Register seller", command=).grid(column=1, row=0) ##Button to open register seller screen
sellertemp=input('Seller_ID: ')
ftemp=input('First name: ')
ltemp=input('Last name: ')
##First check which fields have been entered
if(sellertemp=NULL, fltemp=paste(ftemp,ltemp), str_extract(fltemp,paste(first,last)), else(str_extract(sellertemp,sell_ID)))
##If there are multiple matches, how do I let user choose? Also, be sure to PROMPT if user wants to add new seller (Y/N) button; best if I can autofill first/last?
##Need to make sure new sellers are automatically saved?

#Init billing system (summarize table by buyer number)
##How was this done before? Do I create a unique list of seller IDs and auto-print each??? Might make this is a sub-menu or something... Maybe also make a user-friendly way to cancel printing?
buytemp=input('Buyer number: ')##Enter the buyer number
return(subset(df,df$buyer_number==buytemp)) ##Return certain information for this buyer
##Need to create an easy way to have this interact with the printer

#Init seller payout system:
selltemp=input('Seller number: ')##Enter seller ID
y=subset(df,df$sell_ID==selltemp)
seller_payout=y$price-y$club_sales ##Seller will get the raw price minus the club's share
##Match to seller's ID to seller database too, and print their information as a header?
##Need to create an easy way to have this interact with the printer

#Configure printing:
##https://stackoverflow.com/questions/30329924/how-to-print-directly-without-showing-print-dialog-using-python-script-in-window
