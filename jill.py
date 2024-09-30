import hashlib        #---------------------------------------  Allows the program to hash words
import argparse       #---------------------------------------  Allows the program to become a module

def user_passwords():
    c = 0
    file = open("passwords.txt", "r")       #-----------------  Opens the file containing the names and passwords

    for word in file:                   #---\ 
        split_char = ":"#                    |----------------  Separates the names from the passwords into separate strings
        word = word.split(split_char)   #---/

        user_name = word[0]             #---------------------  Defines the name as 'user_name'
        user_password = word[1]         #---------------------  Defines the password as 'user_password'

        file = open("wordlist.txt", "r")        #-------------  Opens the file containing a list of words that are possible passwords

        for word in file:       #--------------------\
            sha256_hash = hashlib.sha256()     #      \
            #                                          \
            sha256_hash.update(word.encode('utf-8'))#   |-----  Converts each word in the word list into a sha256 hash, and defines the hashed word as 'hashed_pass'
            #                                          /            
            word = sha256_hash.hexdigest()  #         /                     
            hashed_pass = word      #----------------/                  


        while hashed_pass[c] != user_password: #----------/---  Checks to see if any of the hashed words match the hashes of the user passwords                 -----------------|                  
            c = c + 1                          #---------/                                                                                                                       |
        #                                                                                                                                                                        |
        if hashed_pass[c] == user_password:    #-------------- Tells the program what to do if a match is made                                                                   |
            file = open("wordlist.txt", "r")   #--------------  Reopens the word list to access the possible passwords before they were converted into hashes                    |-------------------  THIS CODE DOES NOT WORK 
            for word in file:                  #------\                                                                                                                          |
                hashed_pass[c] = word[c]#              |------  Changes the hash of the user password to be the corresponding word from the word list                            |
                user_name = word[c]            #------/                                                                                                                          |
            break                              #                                                                                                                -----------------|
                                   

        login = (user_name, user_password)     #----------  Puts the user's name and password into two separate strings
        login = ":".join(login)                #----------  Combines the two strings by replacing the space with ':'


    file.close()
        


user_passwords()