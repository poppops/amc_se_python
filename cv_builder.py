'''
 - Name
 - Occupation
 - Synopsis
 - Qualifications
'''

cv_builder={
    'name':{
        'first_name':'Jesus',
        'last_name': 'Burges'
    },
    'occupation':'Anime Character',
    'synopsis':'Hi there my name is Jesus Burges member of the Black Beard Pirates',
    'qualiifications':[
        {
            'name':'First School Leaving Certificate',
            'description': 'I stole it from my neighbour'
        },
        {
            'name':'Pirate Certificate',
            'description': 'Had it once my head was wanted'     
        }
    ]
}

'''
CV For first_name last_name
occupation

About Me
synopsis

Qualifications
----
qualfication_name  
qualification_description
----
'''

'''
Enhance the CV builder program to accept the required information from a user.

Ask the user for their;

- First Name
- Last Name
- Occupation
- Synopsis (A brief description)
- Qualifications*

* You could ask the user how many qualifications they want to add and based on their response request
the information you need.

Use the information received to populate a CV Builder object and when they are ready, print their CV to the screen.

'''