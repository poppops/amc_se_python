'''
   The dictionary below contains information about a few prominent artists.

   Interrogate the dictionary to provide the following information:

   1. What is Burna Boy's real name?
   2. How many Instagram followers does Tiwa Savage have?
   3. Which albums has Wizkid released?
   4. Update Rema's YouTube followers to 2 million.
   5. What is the description of Burna Boy's "Twice as Tall" album?
   6. Add a new album for Tiwa Savage called "Water & Garri" with the description "A blend of Afrobeats and soulful R&B, released in 2021."
   7. Extract and print the birthdates of all the artists in the dictionary.
'''

celebrities = {
    "Burna Boy": {
        "real_name": "Damini Ebunoluwa Ogulu",
        "date_of_birth": "1991-07-02",
        "followers": {
            "Instagram": 15000000,
            "Twitter": 7000000,
            "YouTube": 3500000
        },
        "albums": {
            "African Giant": "Released in 2019, this album blends Afrobeat with reggae, dancehall, and pop influences.",
            "Twice as Tall": "Released in 2020, this Grammy-winning album showcases Burna Boy's global Afrobeats sound."
        }
    },
    "Wizkid": {
        "real_name": "Ayodeji Ibrahim Balogun",
        "date_of_birth": "1990-07-16",
        "followers": {
            "Instagram": 16000000,
            "Twitter": 9000000,
            "YouTube": 2500000
        },
        "albums": {
            "Made in Lagos": "Released in 2020, this album highlights a laid-back, international Afrobeats sound.",
            "Ayo": "Released in 2014, this album solidified Wizkid's status as a global Afrobeats star."
        }
    },
    "Tiwa Savage": {
        "real_name": "Tiwatope Savage",
        "date_of_birth": "1980-02-05",
        "followers": {
            "Instagram": 13000000,
            "Twitter": 6000000,
            "YouTube": 2000000
        },
        "albums": {
            "Celia": "Released in 2020, this album celebrates women’s empowerment and personal growth.",
            "Once Upon a Time": "Released in 2013, Tiwa’s debut album featuring a fusion of Afropop and R&B."
        }
    },
    "Rema": {
        "real_name": "Divine Ikubor",
        "date_of_birth": "2000-05-01",
        "followers": {
            "Instagram": 10000000,
            "Twitter": 3000000,
            "YouTube": 1500000
        },
        "albums": {
            "Rave & Roses": "Released in 2022, this album blends Afrobeats with trap and global pop influences."
        }
    }
}

print(f"1. Burna Boys real name is {celebrities['Burna Boy']['real_name']}");
print(f"2. Tiwa Savage has {celebrities['Tiwa Savage']['followers']['Instagram']} instagram followers")
print(f"3. Wizkid has released the following albums: ")

for album in celebrities['Wizkid']['albums'].keys():
    print(f"\t- {album}")

celebrities['Rema']['followers']['YouTube'] = 2000000
print(f"4. Rema now has {celebrities['Rema']['followers']['YouTube']} YouTube followers")
print(f"5. Burna Boy's Twice as Tall album is as described as: {celebrities['Burna Boy']['albums']['Twice as Tall']}")

#    6. Add a new album for Tiwa Savage called "Water & Garri" with the description "A blend of Afrobeats and soulful R&B, released in 2021."
celebrities['Tiwa Savage']['albums']['Water & Garri'] = "A blend of Afrobeats and soulful R&B, released in 2021."
print(f"6. Tiwa Savage has released the following albums: ")
for album in celebrities['Tiwa Savage']['albums'].keys():
    print(f"\t- {album}: {celebrities['Tiwa Savage']['albums'][album]}")

#   7. Extract and print the birthdates of all the artists in the dictionary.
for celebrity in celebrities:
    print(f'{celebrity} birthday is {celebrities[celebrity]['date_of_birth']}')
