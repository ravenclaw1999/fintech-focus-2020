samira = {"name": "Samira Chowdhury", "username": "human12", "email": "human12@madeupdomain.com", "birthday": "November 23", "followers": 50, "location": "NY", "Following":50}
susan = {"name": "Susan Nguyen", "username": "sue", "email": "susan@madeupdomain.com", "birthday": "January 16", "followers": 10, "location": "NY", "Following":9}
karen = {"name": "Karen Coder", "username": "karry", "email": "karen@madeupdomain.com", "birthday": "August 10", "followers": 0, "location": "NJ", "Following":0}

profile = input("Whose profile do you want to see?")

if profile == "karen": 
    print(karen["name"] + "has a birthday of " + karen["birthday"])
elif profile == "samira":
    print(samira["name"] + "has a birthday of " + samira["birthday"])
else: 
    print(susan["name"] + "has a birthday of " + susan["birthday"])


if profile == "karen": 
    print(karen)
elif profile == "samira":
    print(samira)
else:
    print(susan)