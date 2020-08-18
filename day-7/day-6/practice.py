# define the class
class Contact:
    location = "East Coast"
    # define the init method
    def __init__(self, name, phone, email, company, address):
        # instance variables - will be different for every contact
        self.name = name
        self.phone = phone
        self.email = email
        self.company = company
        self.address = address
        # class variables - will be the SAME for every contact in the class

    # creating a method in a class
    def greeting(self):
        return self.name + ", hey, what's up????"

contact1 = Contact("Gail", "201-555-5555", "gailsemail@gmail.com", "Twitter", "123 Sesame Street")
# print(contact1)
# print(contact1.phone)
# print(contact1.name)
# contact1.name = "Susan"
# print(contact1.name)

# print(contact1.greeting())
print(contact1.location)