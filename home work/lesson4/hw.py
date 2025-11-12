import csv
import json
from os import write


def countWord(p):
    with open(p,'r',encoding='utf-8') as file:
        contact =file.read()
        word=contact.split()
        return len(word)
with open('a.txt','w',encoding='utf-8') as myfile:
    myfile.write("hello everyone!! 😍😊😍😊")
print(countWord('a.txt'))

def people(list):
    with open('people_list.csv', 'w', encoding='utf-8') as myfile:
        contact =csv.writer(myfile)
        contact.writerow(['First Name', 'Last Name', 'Age', 'Place of Residence'])
        contact.writerow(list)

people_list = [
    ['John', 'Doe', 30, 'New York'],
    ['Jane', 'Smith', 25, 'London'],
    ['Peter', 'Jones', 40, 'Paris']
]
people(people_list)
def readData(dataDic):
    with open('data.json', 'w') as myfile:
        json.dump(dataDic,myfile)
    with open('data.json', 'r') as my:
        data=json.load(my)
    print(data)

my_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "cooking"],
    "is_student": False
}
readData(my_data)