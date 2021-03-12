# 🦠 Fun COVID Tracker Challenge 🦠

Copy and paste the below code into a python editor/interpreter, complete the tasks within the script, keeping to within the hashed boundaries (note: this is a similar format to both your CWs). Setting: You are an enthusiatic student at Imperial College London and are tired of waiting for the Government to release a contact tracing app. You decide to take the matter into your own hands..... 

This program generates a unique code for each person in the virtual world, when a person arrives at a location, the person's unique code is logged at that location. In addition to this, on arrival and departure, the program checks to see which other codes are logged at that location. At the end of the day, any positive COVID cases are reported and the corresponding code associated with the infected person is sent out. People can then check whether they have come into contact with this person at some point in the day, and so determine if they should isolate or not!

## Bonus: 
- Identify 1 weakness with this contact tracing programe and fix it. Do this through a new class which inherits from the Person class. I will be interested to see your final implementations, if you would like to share your solutions with me, please copy and paste your code into an email and send to harry.coppock@imperial.ac.uk and we can chat about the best implementations in the next tutorial!

_hints_: 
* what happens when someone visits a location and leaves before the
other people at the location leave?
* the contact list is never wiped.... a system removing old entries
would be better. 
* In our example Luca tests positive, this means that Harry has to 
self isolate, does this mean that everyone in contact with Harry
that day also needs to isolate?

```python 
import random

class Location:
    '''
    A class used for defining locations in our virtual COVID space and who is 
    currently there.
    note: as this a virtual problem, proximity between people cannot be calculated
    through GPS or bluetooth.
    '''

    def __init__(self, name):
        self.name = name
        # people at that location at that specific time
        self.people_present = set()

    def add_person(self, person_code):
        self.people_present.add(person_code)
    
    def remove_person(self, person_code):
        # Task 1:
        # write a method which removes a persons code from the people_present
        # set
        ########################################################################
        # Code start
        ########################################################################

        ########################################################################
        # Code end
        ########################################################################

    
class Person:
    def __init__(self, name, email, start_loc):
        self.name = name
        self.email = email
        self.loc = start_loc

        # for privacy sake a person shall share their unique code not their name
        self.unique_code = self.gen_unique_code()

        # set containing codes of the people which the person has been in contact with
        self.contact_list = set()

        # send code to start location
        self.loc.add_person(self.unique_code)


    def gen_unique_code(self, length=20):
        '''
        Method which generates a random code for the person of length, length
        '''
        # Task 2: complete this function
        ########################################################################
        # Code start
        ########################################################################

        ########################################################################
        # Code end
        ########################################################################
        
    
    def move_location(self, new_location):
        '''
        Method which moves the person
        input:
        new_location: type --> class instance
        '''

        # check to see who is here and log unique codes
        self.register_contacts()
        # Task 3:
        # remove the person's code from the location that is being left, move and
        # add it to the new location
        ########################################################################
        # Code start
        ########################################################################
        # remove code from current location:

        # move

        # add unique code to new location:

        ########################################################################
        # Code end
        ########################################################################

        # check to see who is here
        self.register_contacts()


    def register_contacts(self):
        # Task 4:
        # see who else is here and log their codes
        ########################################################################
        # Code start
        ########################################################################

        ########################################################################
        # Code end
        ########################################################################

    
    def check_to_isolate(self, covid_list):
        if any(code in self.contact_list for code in covid_list):
            print(f'{self.name} needs to self isolate')
        else:
            print(f'{self.name} does NOT need to self isolate')


if __name__ == "__main__":
    # instantiate some locations:
    imperial_cluster = Location('Imperial College London computer cluster')
    h_bar = Location('Postgraduate Bar')
    imperial_library  = Location('Imperial College London Library')
    vna = Location('Victoria and Albert Museum')
    natural_history = Location('Natural History Museum')
    imperial_gym = Location('Ethos')

    # some people
    harry = Person('Harry', 'hgc19@ic.ac.uk', imperial_cluster)
    joe = Person('Joe', 'j.stacey20@ic.ac.uk', vna)
    luca = Person('Luca', 'lg16@ic.ac.uk', imperial_gym)
    william = Person('William', 'wh18@ic.ac.uk', h_bar)

    # people go about their day
    harry.move_location(imperial_gym)
    luca.move_location(imperial_cluster)
    william.move_location(imperial_cluster)
    joe.move_location(imperial_gym)
    joe.move_location(h_bar)
    harry.move_location(h_bar)
    
    print(f'Harry has been in contact with the following anonymous codes: {harry.contact_list}')

    # luca has tested positive for COVID
    # This should return that everyone apart from Joe needs self isolate.

    covid_codes =  [luca.unique_code]

    harry.check_to_isolate(covid_codes)
    joe.check_to_isolate(covid_codes)
    luca.check_to_isolate(covid_codes)
    william.check_to_isolate(covid_codes)
```
