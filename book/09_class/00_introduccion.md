# Overview 
# This week will be on Classes and Inheritance

---

## What to Expect from this Module

In this module we will go over **Classes:**
  - Reviewing what a class is and what an object is.
  - Going over how to make classes in Python and how to use them.
---

### 1. **Classes vs Objects**

- Understand the **concept of classes and objects** in programming.

---

### 2. **Properties and Methods**

- Explore how properties and methods interact in a class.

---

### 3. Special Methods

- Learn about special class methods and their purpose.

---

### 4. **Using classes**

- How do we use classes in practice?
---

### 5. Debugging Demo

- What kinds of bugs appear when writing and using classes, and how do we solve them?

---
### 6. **Overall Demo**

- A programming question testing all of the above topics.
  - This will be a weekly occurrence.


# Classes vs Objects

### **Learning Objectives:**  
- ✅ Understand the **concept of classes and objects** in programming.  
- ✅ Learn how **classes define blueprints** and **objects represent real instances** of those blueprints.  
- ✅ Recognize how **classes and objects relate to real-world concepts.**  

---

<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/9205bada48d34c4e8ca83f37bc9983f01d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

### **What is a Class?**  
A **class** is a **blueprint** or **template** for creating objects. It defines the properties (**attributes**) and behaviors (**methods**) that the objects will have. However, a class itself is **not an object**, but rather a structure that describes how objects of that type should behave.

#### **Real-World Analogy:**  
Think of a **blueprint for a house**. The blueprint defines how the house should look—how many rooms, doors, and windows it has—but the blueprint itself **is not a house**. It is just a plan.  

Let's say `Car` is a **class** that defines attributes (`brand`, `color`) and a behavior (`drive()` method). It is **not yet an actual car**—just a description of one.  

---

### **What is an Object?**  
An **object** is an **instance of a class**. When a class is used to create an object, the object gets its own **actual values** for the attributes and can use the methods defined in the class.  

#### **Real-World Analogy:**  
A **specific house built from a blueprint** is an object. Each house (object) follows the same general structure (class) but has its **own unique characteristics** (color, address, owner).  

#### **Programming Example:**  
```python
my_car = Car("Toyota", "Red")  # Creating an object (instance of Car)
print(my_car.drive())  # Output: The Red Toyota is driving.
```
`my_car` is an **object**, an **actual car** based on the `Car` class.  

---

### **Key Differences Between Classes and Objects**  

| Feature | Class | Object |
|---------|-------|--------|
| Definition | A blueprint or template | An actual instance created from the class |
| Exists in Memory? | No, only a definition | Yes, takes up memory when created |
| Can Store Data? | No, only defines attributes | Yes, has actual values for attributes |
| Can Perform Actions? | No, only defines methods | Yes, can execute methods |

---

### **Why Use Classes and Objects?**  
**Code Reusability** - Define a class once, create many objects from it.  
**Organization** - Helps structure large programs by grouping related data and functions.  
**Scalability** - Makes it easy to modify and extend functionality.  

By understanding classes and objects, programmers can **model real-world entities efficiently**, making code more **structured and reusable!**

# Properties and Methods

### **Learning Objectives:**  
- ✅ Understand what **properties (attributes)** and **methods (functions)** are in a class.  
- ✅ Learn how properties store object data and methods define object behaviors.  
- ✅ Explore how properties and methods interact in a class.  

---

<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/82469023659040fa995578e247d9a8531d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

### **What are Properties?**  
**Properties** (also called **attributes**) are **variables stored inside an object** that define its characteristics. Each object has its **own values** for the properties.  

#### **Example:**  
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Property
        self.color = color  # Property
```
Here, `brand` and `color` are **properties** that store information about a `Car` object.  

#### **Using Properties in an Object:**  
```python
my_car = Car("Toyota", "Red")
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red
```
**Each object stores its own values for these properties.**  

---

### **What are Methods?**  
**Methods** are **functions inside a class** that define an object's **behaviors**. They can modify properties, perform actions, or return values based on the object's data.  

#### **Example: Adding a Method to a Class**  
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):  # Method
        return f"The {self.color} {self.brand} is driving."
```

#### **Calling a Method on an Object:**  
```python
my_car = Car("Toyota", "Red")
print(my_car.drive())  # Output: The Red Toyota is driving.
```
**Methods allow objects to perform actions.**  

---

### **Properties vs. Methods: Key Differences**  

| Feature  | Properties (Attributes) | Methods |
|----------|------------------------|---------|
| Definition | Store object data | Define object behaviors |
| Type | Variables | Functions |
| Access | `object.property` | `object.method()` |
| Example | `car.color` -> `"Red"` | `car.drive()` -> `"The Red Toyota is driving."` |

---

### **Modifying Properties with Methods**  
Methods can **change property values**, allowing objects to update their data dynamically.  

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def repaint(self, new_color):
        self.color = new_color  # Modify property
        return f"The car is now {self.color}."

my_car = Car("Toyota", "Red")
print(my_car.repaint("Blue"))  # Output: The car is now Blue.
print(my_car.color)  # Output: Blue
```
**Methods can update object properties and perform actions.**

---

### **How to Find and Use Classes in Libraries**  

When using a **Python library**, we often interact with classes provided by the module. To understand how to use them, follow these steps:  

1. **Read the Official Documentation**  
   - Visit the module's documentation (e.g., [Python `csv` module](https://docs.python.org/3/library/csv.html)).  
   - Look for sections like **Classes** or **Methods**.  
   - In the case of the `csv` module in the menu on the left you'll see '**Reader Objects**' and '**Writer Objects**'.

2. **Find the Available Classes**  
   - The `csv` module has classes like **`csv.reader`** and **`csv.writer`**.  
   - These classes **provide methods** to read and write CSV files.  

3. **Use the Class and Its Methods**  
   - Create an **object** from the class.  
   - Call the class's **methods** to perform actions.

### **Example: Using `csv.reader` and `csv.writer`**  

#### **1. Reading a CSV File (`csv.reader`)**  
The `csv.reader` **class** helps read CSV files **row by row**.  

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)  # Creating an object of the csv.reader class
    for row in reader:  
        print(row)  # Each row is a list of values
```
**Here, `reader` is an object** of the `csv.reader` class, and we use its methods to read file contents.

#### **2. Writing to a CSV File (`csv.writer`)**  
The `csv.writer` **class** helps write data into a CSV file.  

```python
import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Creating an object of the csv.writer class
    writer.writerows(data)  # Using the writer object's method
```
**Here, `writer` is an object** of the `csv.writer` class, and we call `writerows()` to write multiple rows at once.

---

### **Why Use Properties and Methods?**  
**Encapsulation** - Keeps data and behavior together inside objects.  
**Reusability** - Define once, use for multiple objects.  
**Data Integrity** - Methods can control how properties are modified.  

Understanding **properties and methods** is **essential** for building well-structured, object-oriented programs!

---

### Question

In `song.py`, you will create a **`Song`** class that meets the following specifications:

---

### **Attributes**

Each `Song` object should have the following attributes:

* `name` *(str)* — the title of the song
* `artist` *(str)* — the artist’s name
* `length` *(float)* — the song’s duration in minutes

---

### **Methods**

#### `__init__(self, name, artist, length)`

* The class constructor.
* Initializes a new `Song` object using the given `name`, `artist`, and `length` values.

#### `get_length_in_seconds(self)`

* Returns the song's length converted from minutes to seconds.
* Example:

  ```python
  my_song = Song("tv off", "Kendrick Lamar", 3.7)
  print(my_song.get_length_in_seconds())
  ```

  Output:

  ```plaintext
  222.0
  ```

---

# Special Methods

### **Learning Objectives:**  
- ✅ Understand special methods like `__init__`, `__str__`, and how they work.
- ✅ Learn how to define getters and setters in a class.
---

<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/37f2928c57164f6caa781bfe2487b00c1d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

### **Special Methods in Python Classes**  
Python classes have special methods that allow you to define behavior for operations like object initialization, string representation, and data access. These methods make your objects behave like built-in Python types and allow for greater control over how data is handled. 

#### **[1]`__init__:` The Constructor Method**  
The `__init__` method is a special method used for initializing objects. It's called automatically when an object is created from a class.
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title      # Property
        self.author = author    # Property
        self.year = year        # Property
```
The `__init__` method initializes the object’s properties when it is created. It takes arguments (e.g., title, author, year) and assigns them to the instance.

#### **[2]`__str__`: String Representation Method**  
The `__str__` method defines how an object is represented when you print it or convert it to a string. This method is useful for making your objects more readable when output.

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
```

Now, when you print a Book object, Python will call the `__str__` method to provide a human-readable string representation:

```python
my_book = Book("1984", "George Orwell", 1949)
print(my_book)  # Output: '1984' by George Orwell (1949)
```
#### **[3]Getters and Setters**  
Getters and setters are methods that allow you to get or set the value of an object's attribute. This approach is part of the encapsulation principle, where the internal details of the object are hidden and controlled.

```python
class Book:
    def __init__(self, title, author, year):
        self._title = title  # Use _ to indicate private attribute
        self._author = author
        self._year = year

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        if len(title) > 1:
            self._title = title
        else:
            print("Title is too short!")

    def __str__(self):
        return f"'{self._title}' by {self._author} ({self._year})"

```

Here, the `get_title` method retrieves the title value, and the `set_title` method sets the value while enforcing a condition (e.g., the title must have more than one character).
```python
my_book = Book("1984", "George Orwell", 1949)

# Access the title using the getter
print(my_book.get_title())  # Output: 1984

# Change the title using the setter
my_book.set_title("Animal Farm")
print(my_book.get_title())  # Output: Animal Farm

# Try setting an invalid title
my_book.set_title("A")  # Output: Title is too short!

```
---

### Question

You are given a class in `movie.py` that already has a constructor. Your task is to **define the `__str__` method** so that when an object of this class is printed, it displays a nicely formatted description of a movie. Then, you will construct a Movie object based on user input and print it with your newly defined method.

#### **Instructions:**

1. Define the `__str__` method inside the `Movie` class.
2. The method should return a string describing the movie in the format:
   `"Movie: <title> (Directed by <director>, <year>)"`
3. Call the class constructor to create a `Movie` object based on user input.
4. Call your newly defined `__str__` method using `print()`.

# Classes in practice

### **Learning Objectives:**  
- ✅ Understand how to define and use classes across multiple files in Python.

- ✅ Explore how to create multiple objects of the same class and call their methods.

---
<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/80ee019f7a684cb5a0f08db54b0914e21d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

### **How to Use Classes in Different Files?**  
**Properties** (also called **attributes**) are **variables stored inside an object** that define its characteristics. Each object has its **own values** for the properties.  

In Python, we often organize our code by separating classes into their own files. This helps in keeping the code modular, easier to maintain, and reusable across different parts of a project.

Step-by-Step Guide to Using Classes Across Files:
[1] Define the Class in a Separate File
[2] Import the Class in Your Main Script
[3] Create Objects and Use Methods


### **[1] How to Use Classes in Different Files?**  
Let's say you are building a program that involves books. You would define the Book class in its own file (e.g., `book.py`).
```python
# book.py
class Book:
    def __init__(self, title, author, year):
        self.title = title      # Property
        self.author = author    # Property
        self.year = year        # Property

    def __str__(self):       # Method
        return f"'{self.title}' by {self.author} ({self.year})"
```
**Here, we define a class called Book. The class has properties like title, author, and year, and a method called get_details() which returns a formatted string.**  

### **[2] How to Use Classes in Different Files?**  
Once the class is defined in book.py, you can import it into another file (e.g., `main.py`) where you want to create and use objects of this class.


```python
# main.py
from book import Book   # Importing the Book class from book.py

# Creating a list of Book objects
books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

# Iterate through the list and print details of each book
for book in books:
    print(book)
```

In `main.py`, we import the Book class using from book import `Book`. We then create multiple `Book` objects and store them in a list. The method `get_details()` is called on each object to print information about the book.
### **[3] Creating Multiple Objects**  
Each time you instantiate a class, you create an object. In the above example, we created three objects of the `Book` class:
```python
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
```

These are individual objects with their own values for title, author, and year. They all share the same class definition but hold unique data.



---



Here’s a clearer and more polished version of your instructions with consistent formatting and improved readability:

---

### **Question**

You will now **expand the `Song` class** in `song.py` and use it in your main program `practice.py`.

---

### **Part 1: Expanding the `Song` Class**

In `song.py`, update your **`Song`** class to include the following:

#### **Attributes**

Each `Song` object should have:

* `name` *(str)* — the title of the song
* `artist` *(str)* — the artist’s name
* `length` *(float)* — the song’s duration in minutes

#### **Methods**

##### `__init__(self, name, artist, length)`

* Initializes a new `Song` object with the provided `name`, `artist`, and `length`.

##### `__str__(self)`

* **This is the new method you are adding.**
* Returns a string formatted as follows:

  ```
  '<name>' by <artist> (<length>)
  ```
* **Hint:** Review the *Special Methods* section if you need help defining `__str__`.

##### Note: You won't be using `get_length_in_seconds()` in this question.

---

### **Part 2: Using the `Song` Class**

In `practice.py`, do the following:

1. **Import** the `Song` class from `song.py`.
2. Create a function called `print_songs()` that:

   * Takes a list of `Song` objects as an argument.
   * Prints each song in the list using the string returned by its `__str__` method.

---

### **Example**

```python
# practice.py

from song import Song

def print_songs(song_list):
    for song in song_list:
        print(song)

# Example usage:
songs = [
    Song("tv off", "Kendrick Lamar", 3.7),
    Song("Alright", "Kendrick Lamar", 3.5)
]

print_songs(songs)
```

**Expected Output:**

```
'tv off' by Kendrick Lamar (3.7)
'Alright' by Kendrick Lamar (3.5)
```

---



{Check It!|assessment}(code-output-compare-963298979)



|||guidance
```python
class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    
    def __str__(self):
        return f"'{self.name}' by {self.artist} ({self.length})"
```
```python
from song import Song

# Create a list of Song objects
songs = [
    Song("tv off", "Kendrick Lamar", 3.7),
    Song("Blinding Lights", "The Weeknd", 3.5)
]

# Print details of each song
for song in songs:
    print(song)
```
|||

# Debugging Demo

## **Learning Goal**

By the end of this activity, you will be able to **identify and fix common class-related bugs in Python**, including:

* Missing or incorrect use of `self`
* Uninitialized or incorrectly referenced attributes
* Misspelled attribute names
* Incorrect method parameter lists
* `__str__` methods that print instead of return

---

## **Part 1 — Tutorial: Common Class Bugs (Using a `Student` Class)**

Let’s start with a few examples using a `Student` class.

---

### **Bug #1 — Missing `self` in Method Definitions**

#### **Problem**

```python
class Student:
    def __init__(name, major):
        name = name
        major = major
```

`self` is missing, so nothing is bound to the instance.

When you try to create a `Student` object like this:

```python
s1 = Student("Alice", "Math")
```

You'll get this error.

```
TypeError: Student.__init__() takes 2 positional arguments but 3 were given
```

---

### **Why It Happens**

* Python always provides the instance (`self`) as the first argument for instance methods.
* If you forget to include it in the method definition, the call passes one extra argument.
* The mismatch triggers a `TypeError`.

---

### **Fix**

Add `self` as the first parameter in the constructor (and all instance methods):

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
```


---

### **Bug #2 — Forgetting `self.` When Assigning or Accessing Attributes**

#### Problem

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(name)
```

Calling `introduce` won't print anything.

If you instead forget `self.` during assignment:

```python
class Student:
    def __init__(self, name, major):
        name = name
        self.major = major

    def introduce(self):
        print(self.name)
```

When calling `introduce`, you get this error:

```
AttributeError: 'Student' object has no attribute 'name'
```

#### Fix

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(self.name)
```

Use `self.` so that each attribute belongs to the instance.

---

### **Bug #3 — Misspelling Attribute Names**

#### Problem

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

s1 = Student("Alice", "Math")
print(s1.nam)
```

Raises:

```
AttributeError: 'Student' object has no attribute 'nam'
```

#### Fix

Always double-check spelling — Python is case-sensitive.

---

### **Bug #4 — `__str__` Prints Instead of Returns**

#### Problem

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        print(f"{self.name} majors in {self.major}")
```

When you do `print(student1)`, it prints `None`.

#### Fix

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return f"{self.name} majors in {self.major}"
```

---

## **Part 2 — Debugging Exercise (Using a `Pet` Class)**

Now, it's your turn!

`pet.py` defines a `Pet` class with the **same types of bugs** you just learned about.

Your task is to **debug** it so that it runs correctly and produces the expected output.

---

### **Expected Output (After Debugging)**

```plaintext
Buddy just turned 4!
Max is a dog who is 4 years old.
```

---

## **Hints for Students**

* Does every method include `self` in the parameters?
* Are all attributes stored with `self.`?
* Are the method names and attribute names spelled the same throughout?
* Does `__str__` **return** a string instead of printing?
* Is every attribute initialized in `__init__`?

---

|||guidance
## **Example Fixed Version (Instructor Reference)**

```python
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"{self.name} just turned {self.age}!")

    def rename(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"{self.name} is a {self.species} who is {self.age} years old."

# Main program
pet1 = Pet(name, species, age)

pet1.birthday()
new_name = input("What would you like to rename your pet to? ")
pet1.rename(new_name)
print(pet1)
print("Your pet's name is:", pet1.name)
```
|||

### **Output (After Fixing)**

```plaintext
Enter your pet's name: Bella
Enter your pet's species: cat
Enter your pet's age: 4
Bella just turned 5!
What would you like to rename your pet to? Cleo
Cleo is a cat who is 5 years old.
Your pet's name is: Cleo
```

# Overall Demo

## Objective:

The goal of this exercise is to implement a Car class in `car.py` that models real-world vehicles using attributes and behaviors. You will then use this class in a separate file, `overall.py`, to create car objects from user input, store them in a dictionary by their unique IDs, and allow users to modify their properties during the session. To achieve this goal make sure to use the help given in `overall.py` and in `utils.py`

<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/0397a88a727b4b6eabe866072c36a3a01d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

---

## Step 1: Define the `Car` Class (`car.py`)

Create the `Car` class in the file **`car.py`**.

### **Attributes**

Each `Car` object should include the following attributes:

* **car_id** (`str`): A unique identifier for the car (e.g., `"CAR001"`).
* **brand** (`str`): The car’s manufacturer (e.g., `"Toyota"`, `"Ford"`).
* **year** (`int`): The year the car was manufactured.
* **color** (`str`): The color of the car.
* **mileage** (`float`): The total miles driven. Defaults to `0.0`.

### **Methods**

Implement the following methods:

* `__init__(self, car_id, brand, year, color, mileage=0.0)`
  Initializes all attributes with the provided values.

* `change_color(self, new_color)`
  Updates the car’s color to `new_color`.

* `drive(self, miles)`
  Increases the car’s mileage by the specified number of miles.

* `__str__(self)`
  Returns a formatted description of the car in this format:

  ```plaintext
  CAR001 - 2020 Red Toyota with 15000.0 miles
  ```

---

## Step 2: Review Helper Functions (`utils.py`)

In a separate file named **`utils.py`**, the following utility functions are defined for you. These functions will help you interact with the `Car` class in your main program.

### **Functions**

#### `create_car_from_input()`

Use this function in **Step 3 (Add a new car)**.
It prompts the user for car details, constructs a `Car` object, and returns it.

```python
from car import *

def create_car_from_input():
    car_id = input("Enter car ID (e.g., CAR001):\n")
    brand = input("Enter car brand:\n")
    year = int(input("Enter car year:\n"))
    color = input("Enter car color:\n")
    mileage = float(input("Enter mileage:\n"))
    return Car(car_id, brand, year, color, mileage)
```

---

#### `display_cars(car_dict)`

Use this function in **Step 4 (View all cars)**.
It takes a dictionary of cars and prints each car using its `__str__` method.

```python
def display_cars(car_dict):
    for car in car_dict.values():
        print(car)
```

---

## Step 3: Complete the Main Program (`overall.py`)

You are given a partially completed main program in **`overall.py`**.
This script provides a menu for users to interact with the `Car` class and manage multiple car objects.

Your task is to **complete the missing parts (marked with TODO comments)** by using the functions from `utils.py` and the methods from the `Car` class.

---

### **1. Import Statements**

At the top of `overall.py`, import `utils.py` and `car.py`.

These imports let you:

* Create new cars using the helper function `create_car_from_input()`
* Display all cars using the helper function `display_cars()`
* Access the `Car` class and its methods (`drive` and `change_color`)

---

### **2. Dictionary Setup**

The variable `cars` is already provided for you:

```python
cars = {}
```

This dictionary will store all the `Car` objects you create.

* **Key:** The car's ID (e.g., `"CAR001"`)
* **Value:** The corresponding `Car` object

Example:

```python
cars["CAR001"] = Car("CAR001", "Toyota", 2020, "Red", 15000.0)
```

---

### **3. Completing Each Menu Option**

You will fill in the missing code for each menu choice in the `main()` function.

#### **Option 1 - Add a New Car**

Use the `create_car_from_input()` function from `utils.py` to get a new `Car` object from user input. Then, print the car object.

Store it in the `cars` dictionary using its `car_id` as the key. Then, print:

```plaintext
Car added.
```

---

#### **Option 2 - View All Cars**

Use the `display_cars()` function from `utils.py` to print all the cars currently in the dictionary.

---

#### **Option 3 - Drive a Car**

The program already asks the user which car they want to drive and how many miles to drive. Your task is to look up the car in the dictionary, and call the `drive()` method on that `Car` object.

Then, print:

```plaintext
Mileage updated.
```

Lastly, print the updated car information.

---

#### **Option 4 - Paint a Car**

The program already asks the user which car they want to paint and the color they would like to paint it. Your task is to look up the car in the dictionary, and call the `change_color()` method.

Then, print:

```plaintext
Color updated.
```

Lastly, print the updated car information.

---

#### **Option 5 - Exit**

This option is already complete -- it ends the program with a goodbye message:

```plaintext
Goodbye!
```
---

#### **Example Run 1 — Add a New Car**

**Input:**

```plaintext
1
CAR001
Toyota
2020
Red
15000
```

**Output:**

```plaintext
CAR001 - 2020 Red Toyota with 15000.0 miles
Car added.
```

---

#### **Example Run 2 — View All Cars**

**Input:**

```
2
```

**Output:**

```plaintext
CAR001 - 2020 Red Toyota with 15000.0 miles
```

---

#### **Example Run 3 — Drive a Car**

**Input:**

```plaintext
3
CAR001
200
```

**Output:**

```plaintext
Mileage updated.
CAR001 - 2020 Red Toyota with 15200.0 miles
```

---

#### **Example Run 4 — Paint a Car**

**Input:**

```plaintext
4
CAR001
Blue
```

**Output:**

```plaintext
Color updated.
CAR001 - 2020 Blue Toyota with 15200.0 miles
```

---

#### **Example Run 5 — Exit Program**

**Input:**

```plaintext
5
```

**Output:**

```plaintext
Goodbye!
```

---

