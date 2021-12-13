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
        if isinstance(inital_age, int) and (inital_age <= 103):
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


