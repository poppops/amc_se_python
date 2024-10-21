userProfile = {
    "firstName": "Suhmayah",
    "lastName": "Banda",
    "favouriteColor": "red",
}

userProfile["favouriteColor"] = "green"
userProfile["favouriteDrink"] = "Dark and Stormy"
# print(userProfile)
#
'''
 Read the information from the file user_profile.txt
 and create a dictionary in the format described above
'''

user_data = {}

user_db = open("user_profile.txt", "r")

for userProp in user_db:
    keyValuePair = userProp.split(":")
    key = keyValuePair[0]
    value = keyValuePair[1].strip("\n")
    user_data[key] = value

user_db.close()

print("Dynamic User Data", user_data)