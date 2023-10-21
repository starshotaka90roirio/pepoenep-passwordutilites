from passgen import *

print("""
.______  _______ .______  .___________. _______ .__   __.  _______ .______      
|   _  \|   ____||   _  \ |           ||   ____||  \ |  | |   ____||   _  \     
|  |_)  |  |__   |  |_)  ||  .--.   __||  |__   |   \|  | |  |__   |  |_)  |    
|   ___/|   __|  |   ___/ |  |  |  |   |   __|  |  . `  | |   __|  |   ___/     
|  |    |  |____ |  |     |  '--'  |   |  |____ |  |\   | |  |____ |  |         
| _|    |_______|| _|     |_______/    |_______||__| \__| |_______|| _| password utilites\n\n\n""")


# Asks the user if they want to crack or generate a password.
while True:
      mainquestion = input("Do you want to generate or crack a password? (g/c)\n")



# if the answer is g, for generate it will generate a password.
      if mainquestion == "g" or mainquestion == "G":
            if __name__ == "__main__":
                  try:
                        length = int(input("Enter the length of the password: "))
                        if length <= 0:
                              print("Password length should be greater than 0.")
                        else:
                              password = generate_password(length)
                              print("Generated Password:", password)
                  except ValueError:
                        print("Invalid input. Please enter a valid length for the password.")

      elif mainquestion == "c" or mainquestion == "C":
            predefined_password = input("Enter predefined password: ")
            wordlist = input("Enter file name that contains potential passwords. (ex. wordlist.txt, crack.txt, target.txt etc.): ")
            try:
                  with open("wordlist.txt", "r") as file:
                        passwords = file.read().splitlines()

                  foundmatch = False

                  for Cpassword in passwords:
                        if Cpassword == predefined_password:
                              print("Password cracked! Password: ", Cpassword)
                              foundmatch = True
                                    
                  if not foundmatch:
                        print("Password not cracked...")

            except FileNotFoundError:
                  print("file was NOT found.")

      elif mainquestion == "e" or mainquestion == "exit":
            break
      else:
            print("what")