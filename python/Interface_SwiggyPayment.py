'''
The Story Swiggy's Payment Probelm
You have all ordered fodd online, now time to payment
choose payment menthod
-> UPI
-> Credit / Debit Card
-> Swiggy Money (Wallet)
-> Net Banking
-> Cash on Delivery
Five options Behind that screen is code.
let's follow how that code evolved 
'''

def checkout(method,amount):
    if method == "UPI":
        return f"Paid ${amount} via UPI"
    elif method == "card":
        return f"Paid ${amount} via card"


'''clean Readable . Nothing wrong with this code'''
'''Month 3 -> Three Mothds'''
'''Net Banking , Wallet and Cash on Delivery

file                why it needs the chain
checkout.py          to chatge the customer
refund.py            to reverse a cancelled order
receipt.py           to print the right logs
analytics.py         to count usage per method
fraud_check.py       different rules per method
settlement.py        different bank timings

all this files will deal with payments right
now you need to add all this new 3 methods if checks in all 6 files
A coustmoer orders biryani for ₹450 using swiggy Money.The restaurant is closed.
The order auto-cancels.
The refund service runs its chain

if method == 'upi': ..
elif method == 'card: ...
elif method == 'wallet': ..
elif method == 'netbanking':..
elif method == 'cod':...
else :  None
no branch for "Swiggy_money" -> falls through , return None

no crash . No error  The function simply return None and system marked the refund as
processed

over the next 6 days : 11,000 coustomers ₹47 lakh in refunds that never happened

First Principle Thinking
Ask your self 

Q1) what is actually wrong with if/elif ?
it works. it's readable . so what's the problem
Ask your self: to add one new payment method, how many files must i edit ? And what 
happens if i forget one?

Q2) where should "how to pay UPI" live ?
right now, the knowledge of how UPI works is scattered across six files
should it be ? or should everything about UPI live in one place , and everything abount 
card in another ?
you already know the pillar that answers this . which one ?


'''
def checkout(method, amount):
    if method == "upi":
        return f"Paid ₹{amount} via UPI"
    elif method == "card":
        return f"Paid ₹{amount} via Card"
    elif method == "wallet":
        return f"Paid ₹{amount} via Wallet"
    else:
        return "Unknown payment method"

def refund(method, amount):
    if method == "upi":
        return f"Refunded ₹{amount} to UPI"
    elif method == "card":
        return f"Refunded ₹{amount} to Card"
    # 'wallet' branch forgotten!
    else:
        return None             

print("checkout upi   :", checkout("upi", 450))
print("checkout wallet:", checkout("wallet", 450))
print("refund   upi   :", refund("upi", 450))
print("refund   wallet:", refund("wallet", 450), "  ← SILENT FAILURE")


#-----------------------------idea 2 ------------------------------------------#
'''
classes and duck typing
let's apply what you already know . one class per payment method. Everything abount UPI 
lives in UPI.

'''
class UPI:
    def pay(self, amount):
        return f"Paid ₹{amount} via UPI"
    def refund(self, amount):
        return f"Refunded ₹{amount} to UPI"

class Card:
    def pay(self, amount):
        return f"Paid ₹{amount} via Card"
    def refund(self, amount):
        return f"Refunded ₹{amount} to Card"

class SwiggyMoney:
    def make_payment(self, amount): #'make_payment', not 'pay'
        return f"Paid ₹{amount} via Swiggy Money"
    # refund() missing entirely


def checkout(method, amount):              # no if/elif anywhere!
    return method.pay(amount)

print(checkout(UPI(), 450))
print(checkout(Card(), 450))
print(checkout(SwiggyMoney(), 450))

'''
This is genuinely a big improvement
Before                                             After
if/elif in 6 files                         zero if/elif - checkout is one line
Adding new method = edit 6 files           Adding a method = write 1 new class
UPI logic scattered                        UPI logic in one place 
silent None                                A loud AttributeError

checkout() never changes again. this is polymorphism doing real work

But two problems remain
Problem - 1 -> nothing says what a payment method must be..
you wrote make_payment instead of pay. Nothing told you the requried name.
you have to read other classes and guess.

Problem - 2 -> The errr still arrives too late
you write the code everything is good , python compiled everything is good, called SwiggyMoney()
called no problem , now pay got attribute Error

'''


#-------------------------> Idea 3 <-------------------------------------
'''most teams try this next , and it feels like interface'''
class PaymentMethod:
    """Base class. Subclasses must override everything."""
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")
    def refund(self, amount):
        raise NotImplementedError("Subclasses must implement refund()")


class SwiggyMoney(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} via Swiggy Money"
    # refund() still forgotten


sm = SwiggyMoney()
print("Instantiated fine :", type(sm).__name__)
print("Payment works     :", sm.pay(450))
print("Now a cancellation arrives...")
sm.refund(450)

'''
Better again! , the message now tells you exactly what to do. That is real progress
But look at when it fired. still at call time. we improved the message , we did not 
improve the timing. the bug reaches the production 

second Peoblem -> you just created a payment method that cannot pay. Nothing stopped 
you. The object can now be passed around your system and will fail to pay

'''

#-------------------------Introducing The Concept--------------------------------
'''
An interface is a promise about what an object can do, written in a place the computer
can check

'''

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    """The contract every Swiggy payment method must satisfy."""

    @abstractmethod
    def pay(self, amount):
        """Charge the customer. Return a confirmation string."""

    @abstractmethod
    def refund(self, amount):
        """Return money to the customer. Return a confirmation string."""

class UPI(PaymentMethod):
    def __init__(self, vpa):
        self.vpa = vpa
    def pay(self, amount):
        return f"Paid ₹{amount} from {self.vpa}"
    def refund(self, amount):
        return f"Refunded ₹{amount} to {self.vpa}"


upi = UPI("ashok@okaxis")
print(upi.pay(450))
print(upi.refund(450))


'''now watch the contract do its job'''

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): ...
    @abstractmethod
    def refund(self, amount): ...


class SwiggyMoney(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} via Swiggy Money"
    # refund() forgotten — exactly mistake


try:
    sm = SwiggyMoney()
except TypeError as e:
    print("BLOCKED:", e)

'''
Read that error message closely. it does not just say "You failed". it name that
exact method you forget
it happened on the developer's laptop, the first time you ran the code.
not after 11,000 customers waiting

'''

#-------------------Industry Level -----------------------------------
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Contract for every Swiggy payment method."""

    # ---------- REQUIRED ----------
    @property
    @abstractmethod
    def name(self) -> str:
        """Display name shown on the checkout screen."""

    @abstractmethod
    def pay(self, amount: float) -> str: ...

    @abstractmethod
    def refund(self, amount: float) -> str: ...

    @abstractmethod
    def is_available(self) -> bool:
        """False if this method can't be used right now."""

    # ---------- PROVIDED — written once, inherited by all ----------
    def receipt(self, amount: float) -> str:
        return f"--- SWIGGY RECEIPT ---\n Method: {self.name}\n Amount: ₹{amount}"

    def pay_with_fallback(self, amount, fallback=None):
        """Template method — built from the abstract operations above."""
        if self.is_available():
            return self.pay(amount)
        if fallback is not None:
            return f"[{self.name} unavailable] " + fallback.pay(amount)
        return f"[{self.name} unavailable] and no fallback given"

    def describe(self) -> str:
        status = "available" if self.is_available() else "unavailable"
        return f"<{type(self).__name__} name={self.name!r} {status}>"


class UPI(PaymentMethod):
    def __init__(self, vpa, server_up=True):
        self.vpa, self.server_up = vpa, server_up

    @property
    def name(self): return "UPI"

    def pay(self, amount): return f"Paid ₹{amount} from {self.vpa}"
    def refund(self, amount): return f"Refunded ₹{amount} to {self.vpa}"
    def is_available(self): return self.server_up


class SwiggyMoney(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance

    @property
    def name(self): return "Swiggy Money"

    def pay(self, amount):
        self.balance -= amount
        return f"Paid ₹{amount} from wallet (₹{self.balance} left)"

    def refund(self, amount):
        self.balance += amount
        return f"Refunded ₹{amount} to wallet (₹{self.balance} now)"

    def is_available(self): return self.balance > 0


upi = UPI("ashok@okaxis")
wallet = SwiggyMoney(balance=1000)

for m in (upi, wallet):
    print(m.describe())
    print(m.pay(450))
    print(m.receipt(450))
    print()

# UPI servers go down — fallback to the wallet
upi_down = UPI("ashok@okaxis", server_up=False)
print(upi_down.describe())
print(upi_down.pay_with_fallback(450, fallback=wallet))