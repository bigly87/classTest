"""

Please not at MPC we comply with pep8 coding standards and 
Google Style Python Docstrings,
 please implement those techniques into your python script.


Class vs. Instance

Write a Person class with an instance variable `age` 
and a constructor that takes an integer `initial_age` as a parameter. 
The constructor must assign `initial_age` to `age` after validating the
 value in`initial_age`. In addition,
  you must write the following 
 instance methods:

1.`year_passes()` should increase the `age` instance variable by 1.
2.`what_am_i()` should perform the following conditional actions:
    1.if age < 13 print `You are young...`
    2.if `age >= 13` and `age < 18`, print `You are a teenager...`
    3.Otherwise, print `You are an adult...`  """

class Person:

    '''
    A Class to represnt a person.

    Attributes
    -----------
    initial_age : int

    Methoods
    --------
    what_am_i:
        check what category the given 'age' belongs to,
        based the mentioned conditions. 

    year_passes:
        increase the `age` instance variable by 1

    '''

    def __init__(self, inital_age):
        #assign  `initial_age` to `age` after validating the value in`initial_age`
        if type(inital_age) == int and (inital_age <= 103):
            self.age = inital_age
            print ("intial_age is a valid")
            print(self.age)
        else:
            print("given input must be a number and less/equal than 103")
        
 
    def what_am_i(self):
        #check the age instance value and print suited message.
    
        if (self.age >= 13 and self.age<18):
            print("You are a teenager...")
        elif (self.age < 13):
            print("You are young...")

        else:
             print("You are an adult")


    def year_passes(self):
        #increase the `age` instance variable by 1.
        self.age +=1 


person1 = Person(103)

#person2.what_am_i()


