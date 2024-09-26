import hashlib
import argparse

def user_passwords():

    file = open("passwords.txt", "r")

    for word in file:
        split_char = ":"
        word = word.split(split_char)

        user_name = word[0]
        user_password = word[1]

        file = open("wordlist.txt", "r")

        for word in file:
            sha256_hash = hashlib.sha256()
                    
            sha256_hash.update(word.encode('utf-8'))

            word = sha256_hash.hexdigest()
            hashed_pass = word
            
            if hashed_pass == user_password:
                for word in file:
                    hashed_pass = word
                    user_password = hashed_pass

                login = (user_name, user_password)
                login = ":".join(login)

                print(login)


    file.close()
        


user_passwords()