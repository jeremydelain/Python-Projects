from abc import ABC, abstractmethod

class rent(ABC):
    def rentDue(self, amount):
        print('Rent due: ', amount)
    #function with an argument, no specific data
    @abstractmethod
    def payment(self, amount)
        pass

class rentPayment(rent):
    #define implementation of parent class
    def payment(self,amount):
        print('Your rent of {} exceeds your checking account balance'.format(amount))

obj = rentPayment()
obj.rent('$1200')
obj.payment('$1200')
