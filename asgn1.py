# Homework 1
# Nina Rao

import sys
import pathlib
import re
import pickle
import pandas as pd


# Person class that contains information related to an Employee
class Person:
    def __init__(self, last, first, mi, idnum, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.idnum = idnum
        self.phone = phone

    def display(self):
        print('\nEmployee id: ' + self.idnum)
        print('\t' + self.first, self.mi, self.last)
        print('\t' + self.phone)


# This function does data preprocessing
def process_lines(text):  # takes a list as parameter and returns a dictionary
    persons = {}

    df = pd.DataFrame(text)
    df = pd.DataFrame(df[0].str.split(',').values.tolist())
    df.columns = ['Last', 'First', 'MI', 'ID', 'Phone']

    for index, row in df.iterrows():
        # last name
        if not re.match(r"^[A-Z]{1}[a-z]+$", row['Last']):
            df.loc[index, 'Last'] = row['Last'].capitalize()

        # first name
        if not re.match(r"^[A-Z]{1}[a-z]+$", row['First']):
            df.loc[index, 'First'] = row['First'].capitalize()

        # middle initial
        if not row['MI']:
            df.loc[index, 'MI'] = 'X'
        if not row['MI'].isupper():
            df.loc[index, 'MI'] = row['MI'].upper()

        # employee id
        if not re.match(r"^[A-Z]{2}[0-9]{4}$", row['ID']):
            newID = row['ID']
            while not re.match(r"^[A-Z]{2}[0-9]{4}$", newID):
                print("ID invalid: " + newID)
                print("ID is two letters followed by 4 digits")
                newID = input("Please enter a valid id: ")
            df.loc[index, 'ID'] = newID

        # phone number
        if not re.match(r"^([0-9]{3})-([0-9]{3})-([0-9]{4})$", row['Phone']):
            match = re.search(r"^(\d{3})[\s.-]?(\d{3})[\s.-]?(\d{4})$", row['Phone'])
            dash = '-'
            df.loc[index, 'Phone'] = dash.join(match.groups())

        # create person object and check for duplicate ID
        p = Person(row['Last'], row['First'], row['MI'], row['ID'], row['Phone'])
        if row['ID'] in persons.keys():
            print("Error: could not add person, employee ID " + row['ID'] + " already exists")
        else:
            persons[row['ID']] = p

    #print(df)

    return persons


# main
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: please enter a filename and a relative path as a system arg')
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

    employees = process_lines(text_in[1:])  # get rid of heading line

    # pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # output formatted employees
    print('\n\nEmployee List:')

    for emp_id in employees_in.keys():
        employees_in[emp_id].display()
