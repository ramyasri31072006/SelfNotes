'''
Traditional way of accesing data is using setter and getters.
(_) -->represent protected vairables i.e _salary
(__) --> represents private vairables i.e __salary
'''
from datetime import datetime
class User2:
    def __init__(self,username,email,password,isAdmin = False):
        self.username = username
        self._email = email # protected 
        self.password = password
        self.isAdmin = isAdmin
    def sayHiToUser(self,user):
        print(f"Sending message to {user.username} : Hi {user.username} , it's {self.username}")

    def getEmail(self):
        print(f"request time {datetime.now()}")
        return self._email
    
    def setEmail(self,newemail):
        if(self.isAdmin):
            if '@' in newemail:
                self._email = newemail

user1 = User2("Ashok","ashokm@gmail.com",123,True)
user2 = User2("Ram","ram1990@gmail.com",234,True)


user1.getEmail()

print(user1._email) # user1.email gives error ('User2' object has no attribute 'email')

#user1.email = "ashokoutlook.com" -->doesnot change value and doesn't raises error

print(user1.getEmail()) # "ashok@gmail.com"

user1.setEmail("don@gmail.com")

print(user1.getEmail())#"don@gmail.com"


# Python’s Take on Access Modifiers
# Unlike languages such as Java or C++, which enforce strict access control (like private or protected), Python takes a more relaxed approach. In Python:

# A single underscore (_) before a name (e.g., _attribute) is a convention indicating that something is intended for internal use within the class or module. This means it’s not part of the public API, and external code shouldn’t access it directly.
# However, Python doesn’t enforce this restriction. The attribute or method is still accessible from outside the class, but it signals to developers that it’s meant to be “protected” or “internal.”

# The “Consenting Adults” Philosophy
# Guido van Rossum’s "consenting adults" philosophy highlights Python’s emphasis on developer responsibility rather than strict rules. This philosophy suggests that:

# Developers are trusted to respect the convention of not accessing underscore-prefixed attributes or methods.
# Access is not prevented, as Python assumes that developers will act responsibly and won’t misuse or access “protected” members unless absolutely necessary.

# 2. Using properties

# This is the recommended approach in python. let's see why...

#The Consenting Adults Philosophy


class User3:
    def __init__(self,username,email,password,isAdmin = False):
        self.username = username
        self._email = email # protected 
        self.password = password
        self.isAdmin = isAdmin
    def sayHiToUser(self,user):
        print(f"Sending message to {user.username} : Hi {user.username} , it's {self.username}")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,newemail):
        if('@' in newemail):
            self._email = newemail
        else:
            print("not changed")


user = User3("Ashok","ashokm@gmail.com",123,True)
user2 = User3("Ram","ram1990@gmail.com",234,True)

print(user1.email)
user1.email = "don@gmail.com"
print(user1.email)

'''#if you want to write the setter, getter must exists
both setter and getter should have same name
@property changes method --> variable
i.e email() ---> email
bcoz of this reason we are calling user1.email = "Abc@gmail.com" instead userl.email("Abc@gmail.com)'''
