# ✍️ Assignment 1: User Signup Validator (Function-Based)
# Build a CLI tool that:

# Accepts input: username, email, and password

# Validates the email format (use in or regex)

# Checks password strength:

# Minimum 8 characters

# Contains at least 1 number

# Contains at least 1 special character

# 📌 Bonus: Save valid user data in a Dict.

# User '{userName}' registered successfully.

import re

UserData = []
def userSignUpValidator(userName,email,password):

    match = re.search(r"^\S+@\S+\.\S+$",email)
    matchNo = re.search(r'\d',password)
    matchSpecialChar = re.search("[^a-zA-Z0-9]",password)
    if match is None:
        print("Please Enter Correct Email")
        return
    
    if(len(password) < 8):
        print('Please Enter at Lease 8 chars for the pass')
        return
    
    if matchNo is None:
        print('Please Enter At Least One No')
        return
    if matchSpecialChar is None:
        print('Please Enter At Least one Special Character')
        return
    
    for user in UserData:
        if user["Email"] == email: 
            print("same Email Already Exist")
            return;

    
    currUserList = {"UserName": userName,"Email": email,"Password": password}
    UserData.append(currUserList)
    print(f"User: {userName} Registered successfully.")


userSignUpValidator('tushar','tushar786@gmail.com','tushar786@')
userSignUpValidator('Mehra','tushar@gmail.com','tushar2@22')
userSignUpValidator('Mehra','tushar@gmail.com','tushar2@22')
userSignUpValidator('Pooja','pooja@gmail.com','wadawd@22d2')