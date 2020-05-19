# Learn Python Notes

## Print and Input Values

```python
# Use single or double quotes for strings
print('Hello World!')

# Break lines with \n
print('One line\nSecond line')

# Input values
name = input('Enter your name: ')
print(name)
```

## Commments
```python
# Use hashtag character for line comment
```

## Variables
```python
# You don't need to declare a variable,
# just use it directly
name = 'Winston'

# Use underscore for clean varable_names
full_name = 'Winston Churchill'
```

## Strings
```python
# You can joint strings with '+'
full_name = first_name + ' ' + last_name

# Some Functions for string modifications
name.upper() # Uppercase
name.lower() # Lowercase
name.captialize() # First letter in uppercase
name.count('a') # How many 'a' chars are there?

# Formatting strings
full_name = f'{first_name} {last_name}'
# or
full_name = '{} {}'.format(first_name, last_name)

# Getting only first letter from strings
initials = first_name[0:1] + last_name[0:1] 
```

## Math with Numbers
```python
# Use +, -, *, / to do a math
area = a * b
# Use ** for exponent
side ** 2
```

## Type Conversion
```python
str(56) # Converts number to string '56'
int('56') # Converts string '56' to a number 56
float(56) # Converts integer 56 to float 56.0
```

## Workings with Dates
```python
# Getting current date
from datetime import datetime # Imports library
# Can be used without importing as 'datetime.datetime.now()'
current_date = datetime.now() # .now() gets current date

# Counting with time deltas
from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = current_date + one_day

current_date.month # Get month from date
current_date.day # Get day from date
current_date.year # get year from date
current_date.hour
current_date.minute

# Parsing time form a string
birthday = input('Enter birthday (dd/mm/yy)): ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
```

## Handling Errors by Exceptions
```python
try:
    print(1/0) # Division by zero
except ZeroDivisionError as e:
    print('Division by zero is not allowed.')
else:
    print('Something else went wrong.')
finally:
    print('This is our cleanup code.')
```

## Using Conditions
```python
if price < 1000.0:
    delivery = .0
else:
    delivery = 100.0
print(price + delivery)

# Using of elif (else if) and else
if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.10
else:
    tax = 0.0
```

## Comparison values
```python
if country == 'Canada': # == is a compare operator
    print('The country is Canada')

# Using 'or'
if country == 'Canada' or country == 'U.S.':
    print(something)

# Using 'and'
if country == 'Canada' and city == 'Otawa':
    print(something)

# Is the value in one of the value in the list?
if country in('Canada', 'U.S.'):
    print(something)
```

## Booleans
```python
task_done = True
task_done = False
if task_done:
    print('The task is done')
```

## Collections
### Lists
```python
names = ['Christopher', 'Suzan'] # List collections with two items
score = [] # Empty list
names.append('Franz') # Add new item to the end of list
print(names) # Print all the list items
print(names[2]) # Print the 3rd item (0, 1, 2)

len(names) # Get number of items in the list
names.insert(1, 'Bill') # Insert 'Bill' before index 1
names.sort() # Sort the list
names.range[0:2] # Get range of list from index 0 to 2
names.range[:2] # The same
```
### Arrays
```python
from array import array
scores = array('d')
scores.append(97)
```

### Arrays vs. Lists
>**Arrays** can contain *only numerical types* (integers, floats, etc.) Arrays have to be imported.
>
>**Lists** can contain *a mix of types*. Stores everything.

## Dictionaries
Directories are *key-value* data types. Can be used as lists but with *keys* instead of indexes.
```python
output = {'continue': 'Do you want to continue?'}
output['start'] = 'Do you want to start?'}
print(output['start']) # Prints 'Do you want to start?'
```

> Be careful with mixing **'** and **"** in strings:
> ```python
> print(f"The 3rd plane is {selected_plane['producer']}.")
> ```

## Loops
```python
for item in ['item1', 'item2']: # For iterates the list
    print(item)

for number in range(0, 3): # List from 0 with 3 numbers
    print(number)

while index < 5:
    print(index)
    index = index + 1 # Index updating must be here
    break # or use 'break' to exit loop
```

## Functions
```python
def say_hello():
    print('Hello')

say_hello() # Prints 'Hello'

# Function with parameter
def say_hello(name):
    return f'Hello {name}!'

print(say_hello('Karl')) # Prints Hello Karl

# Default function parematers
def say_hello(name, official=False):
    if official == True:
        return f'Hi {name}!'
    else:
        return f'Good morning Mr. {name}!'

# Using named parameters
print(say_hello(name='Karl', official=True))
```

## How to exit program
```python
import sys
sys.exit()
```

## Moduels and Packages
### Modules
```python
# Three different ways, one same result:

# Import module as namespace
import helpers # helpers.py must exist
helpers.display('Something')

# Import all into current namespace
from helpers import *
display('Something')

# Import specific items into current namespace
from helpers import display
display('Something')
```
### Packages
Packages are public collections of modules.
```python
# Install an individual package
pip install colorama

# Install from a list of packages
# The textfile contains just a list of packages
pip install -r requirements.txt 
```

## Virtual Environments
Packages are by default installed globally. It's not always good thing for version management etc. Virtual environments can be used to contain and manage packages locally. I's just a folder.
```python
# Install virtual environment
pip install virtualenv

# Windows systems
python -m venv <folder_name>

# macOS/Linux
virtualenv <folder_name>

# Using virtual environment
<folder_name>\Scripts\Activate.bat # For cmd.exe
<folder_name>\Scripts\Activate.ps1 # For PowerShell
<folder_name>/Scripts/activate # For WSL bash shell
<folder_name>/bin/activate # For macOS/Linux bash shell
```

## Calling an API
```python
# pip and import requests library
pip install requests

import requests, json

SUBSCRIPTION_KEY = '<key>'
address = 'api.openweathermap.org/data/2.5/weather'
params = {'q': 'Prague', 'appid': SUBSCRIPTION_KEY}

response = requests.post(address, params=params)
print(response.json())
```
## Working with JSON
```python
import json

person_dict = {'first': 'George', 'last': 'Harrison'}
person_dict['city'] = 'Liverpool'
# Convert the dictionary object to JSON
person_json = json.dumps(person_dict)

# Hierarchy is done by creating a dictionary as value
# of dictionary or list in the value of dictionary
```

## Environment Variables
```python
import os
os_version = os.getenv('OS')
print(os_version)

# Use environment variables to store sensitive
# information (keys, connection strings etc.)
# Add information to .env file and load in code:
# PASSWORD=My secret password
# Do not upload .env file anywhere, add to gitignore!
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv('PASSWORD')
```

# Advanced Python
## Type Hints
```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

## Documenting Functions
```python
'''
Returns a complete greeting for given name

Description text

Parameters:
first_argument
secornd_argument
'''
```

## Lambda Expressions

A lambda function is a small anonymous function.

Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: ```lambda a, b: a+b```.

Lambda functions can be used wherever function objects are required.

```python
x = lambda a : a + 10
print(x(5))
```

## Classes

```python
class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
    def say_hello(self):
        # Method
        print('Hello, ' + self.name)

presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()
```

### Properties

```python
class Presenter():
    def __init__(self, name):
        self.name = name # Setting the property

    @property
    def name(self): # Gets property value
        return self.__name

    @name.setter
    def name(self, value): # Sets property value
        self.__name = value
```

### Inheritance
```python
class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, I am ' + self.name)

class Student(Person): # Student from Person
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)

greg = Person('Greg')
greg.say_hello()

student = Student('Rowley', 'MIT')
student.say_hello()
student.sing_school_song()

# Functions can be overriden by re-defining:
def __str__():
    print('This is object')

```

## Multiple Inheritance (Mixins)
Mixins are classes derived from multiple classes.
```python
class Loggable:
    def __init__(self):
        self.title = ''
    def log(self)
        print('Log message from ' self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to ' + self.server)

def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()

# Define mixin class
class SqlDatabase(Connection, Loggable)
    def __init__(self):
        self.title = 'SQL Connection Demo'
        self.server = 'Some_server'

sql_connection = SqlDatabase()
framework(sql_connection)

class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging...'

framework(JustLog)
```

## Managing the File System

```python
from pathlib import Path

# Current working directory
cwd = Path.cwd() 
# Combine parts to create full file name
new_file = Path.joinpath(cwd, 'new_file.txt')
# Does this file exists?
new_file.exists()
# Parent directory
parent = cwd.parent
# Is the parent object directory?
parent.is_dir()
# Is this a file?
parent.is_file()

# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)

# Create demo file
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

demo_file.name # Get file name
demo_file.suffix # Get the file extension
demo_file.parent.name # Get the folder of file
demo_file.stat().st_size # Get the size
```
### Sterams
```python
stream = open(file_name, mode, buffer_sze)
```
| Mode | Description                |
|:----:|----------------------------|
| r    | Read                       |
| w    | Truncate and Write         |
| a    | Append if file exists      |
| x    | Write, fail if file exists |
| +    | Updating (read/write)      |
| t    | Text (default)             |
| b    | binary                     |

```python
# Read text file
stream = open('./demo.txt', 'rt') # Read as text
if stream.readable():
    print(stream.read(1)) # Get first letter
    stream.seek(0) # Move to start
    for plane in stream.readlines():
        print(plane)


# Write text file
stream = open('./output.txt', 'wt') # Write as text
if stream.writable():
    stream.write('H') # Write 'H'
    stream.writelines('\n'.join(['A', 'B', 'C']))
    stream.close()

# Using with
with open('./output.txt', 'wt') as stream:
    stream.write('Lorem ipsum')
# There is no need to close stream if using 'with'
```

## Asynchronous Operations

```python
from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay} second timer')
        return text

async def main():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    async with aiohttp.ClientSession() as session:
        # Setup our tasks and get them running
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

        # Simulate other processing
        await asyncio.sleep(1)
        print('Doing other work')

        # Let's go get our values
        two_result = await two_task
        three_result = await three_task

        # Print our results
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(main())
```

## Graphical User Internafaces with Tkinter
```python
# Minimal Tkinter application
import tkinter as tk
window = tk.Tk()
```

https://realpython.com/python-gui-tkinter/


