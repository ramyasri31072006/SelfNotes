
a = 15 #global

def doSomething():
    a = 10 #local
    print("inside : ",a) #10
doSomething()
print("outsid : ",a) #15

def doSomething():
    global a  # treats this a as global
    a = 10 #local (changes both local and global value to 10)
    print("inside : ",a) # 10
doSomething()
print("outsid : ",a) # 10


def doSomething():
    globals()['a']  = 10 # changes globally value
    a= 20  #consider this a is now local val and prints the value
    print("inside : ",a) # 20
doSomething()
print("outside : ",a) # 10
