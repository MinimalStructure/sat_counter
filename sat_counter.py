#! python3
#satcounter
#written by Minimal Structure
#Enter your wallets and all of the sats inside. The program will add your sats
#8/18/2018
#wwww.tippin.me/MinimalStructur

import os, pprint, shutil, shelve, math
from pathlib import Path

#TODO create a csv file with all of the information
#encrypt that csv file.


#create an empty dictionary using user get_user_input
wallet_info = {}

#set flag that lets us know we want to know what' is in your wallet?
whats_in_your_wallet = True

while whats_in_your_wallet:
    #prompt user for wallet name and sats in wallet
    #todo raise exceptions
    
    wallet_name =  input("\nWhat's the wallet name?  ")
    
    sats = int(input("\nHow many sats are in this wallet?  "))
    
    
    #store the responses in a dictionary
    wallet_info[wallet_name] = sats

    #ask if the user has anymore wallets
    repeat = input("\nDo you have anymore wallets? ")
    #if repeat != 'yes'.lower() or 'no'.lower():
        #raise Exception("Answer should be yes or no")
    if repeat.lower() == 'no':
        whats_in_your_wallet = False
        #adding wallets is complete

print("==== Wallets ====")
for wallet_name, sats in wallet_info.items():
    print(wallet_name + " has " + str(sats) + "in it.")

# adds the satoshis of all wallets and store them in a variable
total_satoshis = sum(wallet_info.values())
#convert satoshis to bitcoin
total_bitcoin = (total_satoshis * 0.00000001)
#print the sats and bitcoin
text1 = '\n\nYou have a total of ' + str(total_satoshis) + ' satoshis. \n'
text2 = '\n\nWhich is ' + str(total_bitcoin) + ' BTC.'

print(text1)
print(text2)
#first, concatinate the text you want to Print
file_info = text1 + text2
#next write that concatination to a file on your desktop


print(file_info)


#TODO:, Create this into a csv file
#Todo: Encrypt the file on your desktop

#get tthe USD value from the sats using webscraping and the amount of sats in the fild
#TODO: Get the USD value of total_sats






#This part of the code is not working yet

stacked = open('c:\\users\\marc\\desktop\\sats_stacked.txt', 'w')
stacked.write('You have a total of ' + str(total_satoshis) + 'satoshis.' + 'This is equal to ' + str(total_bitcoin) + ' bitcoin.')
stacked.close()


'''
I still need to handle exceptions.  I also want to use the shelf module to write a csv file instead of a txt file. 

'''
