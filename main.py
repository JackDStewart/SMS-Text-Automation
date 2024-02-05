# Author: Anthony Teciorowski and Jack Stewart, Alpha Sigma Phi - Cal Poly SLO

import csv
import os

def send_message(phone_number, message):
    os.system('osascript sendMessage.applescript {} "{}"'.format(phone_number, message)) # pretty musch running command in terminal #shell command

# open the csv file
with open('rush.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # create a list to store phone numbers
    phone_numbers = []

    total_texts = 0
    # loop through the csv file
    for line in csv_reader:

        #get the first name from column B by delimiting by spaces or commas
        first_name = line[1].split(' ')[0].split(',')[0]
        # get the message from column K
        message = 'Hey ' + first_name + ", this is Jack with Alpha Sig. We had a great time getting to know you this week at rush and we'd love to have you out to our Smoker and Poker event tonight night at 6 p.m. at 299 Albert. The event is in formal attire. We look forward to seeing you there!"
        # format phone number in column G to be 11 characters, 1 for +, 10 for phone number
        phone_number = line[3]
        phone_number = phone_number.replace(' ', '')
        phone_number = phone_number.replace('(', '')
        phone_number = phone_number.replace(')', '')
        phone_number = phone_number.replace('-', '')
        phone_number = phone_number.replace('+', '')
        # add 1 to the beginning of the phone number if not already there
        if phone_number == None or phone_number == '':
            continue
        if phone_number[0] != '1': 
            phone_number = '1' + phone_number    
        # if column I lowercased is not yes, skip the row (for invites)
        # if line[8].lower() != 'yes':
        #    continue      
        # add the phone number to the list
        if phone_number in phone_numbers:
            continue
        phone_numbers.append(phone_number)
        print(phone_number)
        print(message)
        print(first_name)
        total_texts += 1
        send_message(phone_number, message)
        print("text sent")

    #print all the counters
    print("Total number of texts sent: " + str(total_texts))


# close the csv file
csv_file.close()