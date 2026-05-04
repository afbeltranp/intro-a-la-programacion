# Module 10 Overview



This module brings together the tools and ideas you have used throughout the course and shows how they fit into real-world workflows. By the end of this module, you should understand not only how to write code, but how code is developed, executed, extended, and used beyond this course.

---

## **Learning Objectives:**
- Understand how and why libraries are used
- Learn what APIs are and how software uses them
- Learn how Jupyter Notebooks execute code and text
- Understand when cloud tools like Google Colab are useful
- Recognize how course concepts apply beyond this class

---

## **Topics Covered in This Module:**


### 1. **Generative AI Disclaimer**

- Module 10 marks some differences in the allowed use of generative AI for this course. Make sure to check it out.

---
### **2. Libraries**
- What a library is
- Why libraries are used instead of writing everything from scratch
- Examples of commonly used Python libraries

---

### **3. APIs**
- What an API is
- How programs request and receive data
- Examples of real-world API usage

---
### **4. API Authentication**
- How authentication protects APIs from unauthorized use
- How to get the proper User ID and check permissions
- learn about API keys
---

### **5. Google Colab**
- What Google Colab is and how to use Jupyter Notebooks
- How it compares to Codio and local environments
- When cloud-based notebooks are useful

---

### **6. Beyond This Course**
- How Python skills apply to real-world problems
- Next steps for continued learning
- How this course fits into larger technical workflows

---


# Generative AI

## **Expanded Use of Generative AI: A New Stage**

Up to this point in the course, you have been encouraged to use generative AI primarily to **understand concepts**, clarify syntax, and support your learning of core programming fundamentals.

Now that you will learn how to work with **libraries**, your use of AI should evolve.

Libraries introduce a large ecosystem of modules, functions, and terminology. It would take an enormous amount of time to manually learn every component. What matters most now is your ability to **use tools effectively, explore new functionality, and automate meaningful processes**.

Generative AI is one of those tools.

This stage is about helping you move forward with confidence.

---

## **How You Are Encouraged to Use AI**

You may now use AI more broadly to support your development process, including:

- Writing functions or full programs  
- Debugging errors and identifying problems  
- Explaining unfamiliar code  
- Creating test files or test data  
- Generating example inputs and outputs  
- Helping automate workflows  
- Exploring alternative implementation approaches  

These are real workflows used by professional developers.

---

## **Your Responsibility as the Developer**

Even when using AI, you are responsible for:

- Understanding the code you submit  
- Being able to explain how your solution works  
- Making meaningful design decisions  
- Ensuring your solution functions correctly  

AI is a tool to support your work. You remain in control of the process.

---

## **The Most Important Takeaway**

This module marks an important transition.

You are stepping into a world full of powerful libraries, tools, and systems designed to help you automate tasks and build efficiently.

You should leave this module feeling confident that you can:

- Learn new libraries without fear  
- Use AI to accelerate your workflow  
- Automate processes effectively  
- Build solutions using tools you have never seen before  

You already have the foundation.

Now you are learning how to use the tools that make you faster, more capable, and more effective.

---

## **Summary**

- Previously, AI was used primarily to support understanding.  
- Now, AI is encouraged as a broader development and automation tool.  
- Libraries introduce many tools that developers learn to use as needed.  
- AI helps you explore, build, test, and automate efficiently.  
- Your responsibility is to understand and guide the solutions you create.  
- The goal is for you to feel confident working in a world full of tools.

# Introduction to Libraries

## **Learning Objectives:**  
- Understand what **Python libraries** are and why they are useful.  
- Learn how to **install and import libraries** in Python.  
- Explore how to **find and read documentation** for libraries.  

---


## **What Are Python Libraries?**  
A **library** is a collection of **pre-written code** that provides useful functions, classes, and tools. Instead of writing everything from scratch, you can use **libraries** to speed up development and avoid reinventing the wheel.  

**Example:** Instead of manually handling CSV files, the **`csv`** library provides built-in methods to read and write them.  

---

## **Why Use Libraries?**  
Libraries help by:  
- **Saving time** - No need to write common functions yourself.  
- **Providing optimized performance** - Many libraries are faster than custom implementations.  
- **Expanding Python's capabilities** - Specialized libraries exist for tasks like data analysis, machine learning, and networking.  

---

## **Installing Libraries with `pip`**  
Python includes **some built-in libraries**, but others need to be installed separately in the **terminal** using `pip`, Python's package manager. This **must be done** before you run the script that needs the libraries. 
*Fun Fact:* Pip is actually a recursive acronym for "`pip` installs packages" so they actually could have made the first letter any other letter when naming it. 

#### **Installing a Library:**  
```sh
pip install numpy
```
This installs **NumPy**, a popular library for numerical computing.  

---

### **Importing and Using Libraries**  
After installation, libraries must be **imported** into your script before use.  

#### **Example: Importing and Using a Library**  
```python
import math  

print(math.sqrt(25))  # Output: 5.0
```
**`math` is a built-in library** that provides mathematical functions like `sqrt()`.  

You may also see libraries imported with an **alias (a shorter name)**. This is very common with third-party libraries.

#### **Example: Importing third party library with alias**  

```python
import numpy as np  

numbers = np.array([10, 20, 30, 40])
mean_value = np.mean(numbers)

print("Array:", numbers)
print("Mean:", mean_value)
```

Here:

- `numpy` is the full library name.
- `np` is a conventional alias used by most Python programmers. You could use a different one.
- `np.array() `creates an array.
- `np.mean()` calculates the average.

Using aliases makes your code shorter, cleaner, and easier to read, especially when working with libraries that are used frequently like `numpy`, pandas `(pd)`, or `matplotlib.pyplot` `(plt)`.

---
## **How to Find and Read Documentation**  
To use a library effectively, you need to understand its **functions and classes**.  

### **Ways to Find Documentation:**  
1. **Official Python Docs** - Visit [docs.python.org](https://docs.python.org/3/library/) for built-in modules.  
2. **Library-Specific Docs** - Example: NumPy's docs at [numpy.org/doc](https://numpy.org/doc/).  
3. **`help()` Function in Python** - View documentation inside Python:  
   ```python
   import math
   help(math)
   ```
4. **Google & Stack Overflow** - Search for examples and troubleshooting.  

---

### **Summary**  
- **Libraries extend Python's capabilities** by providing pre-written code.  
- **Some libraries are built-in**, while others require installation (`pip install`).  
- **Import libraries** before using them in your code.  
- **Read documentation** to understand available functions and best practices.

---

## ❓ Installation Knowledge Check:
{Check It!|assessment}(fill-in-the-blanks-1748263477)

---
## ❓ Missing Library Question

In the file `lib_intro.py` you will find code that uses `numpy`, `math`, `pandas` and `Faker`. Some of these libraries are are commonly used in engineering problems. The code itself does not contain any errors. However, running the code results in a **ModuleNotFoundError**. 

Using what you have learned above about installing libraries, debug the program so it does not crash. Do not forget that the issue **must be solved** in the terminal.


{Check It!|assessment}(code-output-compare-277795793)


# APIs


## **Learning Objectives:**
- Understand what an API is and what problem it solves  
- Learn how programs communicate using APIs  
- Recognize common real-world uses of APIs  
- Understand HTTP requests and status codes  

---

## **What Is an API?**
An API (Application Programming Interface) allows one program to request data or services from another program. Instead of directly accessing another system’s internal code or database, a program sends a request to the API and receives a response.

APIs make it possible for different software systems to work together in a controlled and secure way.

---

## **Why APIs Are Used**
APIs are used because they:
- Allow access to data without exposing internal systems  
- Standardize how requests and responses are handled  
- Make it easier to integrate services from different providers  

Without APIs, programs would need direct access to databases or internal code, which is unsafe and impractical.

---

## **How APIs Work (Conceptual Overview)**
At a high level, most APIs follow this process:
- A program sends a request for data or an action  
- The API receives and processes the request  
- The API sends back a response, often in a structured format such as JSON  

You do not need to know the internal implementation of an API to use it.

---

## **HTTP Requests**

Most web APIs use the HTTP protocol. When working with APIs, you will commonly see different types of requests:

- **GET** – Retrieve data from the server  
- **POST** – Send new data to the server  
- **PUT** – Update existing data  
- **PATCH** – Partially update existing data  
- **DELETE** – Remove data  

For example:
- A weather app uses a **GET** request to retrieve forecast data.
- A user registration form might use a **POST** request to send new user data to the server.

A response to an HTTP request typically has two parts: a **status code** and **JSON** data.

---


## What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight data format used to send and receive structured data — especially in web requests and APIs.

In Python, JSON looks very similar to a **dictionary**.

Example JSON:

```json
{
  "name": "Alice",
  "age": 20,
  "major": "Computer Science"
}
```

In Python, this becomes:

```python
{
  "name": "Alice",
  "age": 20,
  "major": "Computer Science"
}
```

Notice that:

* JSON objects use **key–value pairs**
* Keys are always **strings**
* The structure closely matches a Python dictionary

---

### Accessing JSON Data in Python

When you receive JSON in a request (for example, from an API), it is typically parsed into a Python dictionary.

You access values using dictionary syntax:

```python
data = {
    "name": "Alice",
    "age": 20
}

print(data["name"])   # Alice
print(data["age"])    # 20
```

---

### JSON and Class Attributes

Often, JSON data is converted into an object (an instance of a class).

For example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

If JSON is converted into this class, you access values using **dot notation**:

```python
student.name
student.age
```

So:

* Raw JSON → accessed like a **dictionary** (`data["key"]`)
* Converted to a class → accessed like an **attribute** (`object.key`)

---

### Constructing JSON for a Request

When sending JSON in a request, you typically build a Python dictionary first:

```python
payload = {
    "name": "Alice",
    "age": 20
}
```

This dictionary is then converted to JSON automatically by most frameworks.

---

### What You Need to Remember

* JSON is structured as key–value pairs (like a dictionary).
* Keys are strings.
* Parsed JSON behaves like a Python dictionary.
* If converted to a class, access values using dot notation.
* To send JSON, build a dictionary and let the framework convert it.

That’s all you need to construct and parse JSON in this course.

## **HTTP Status Codes**

When an API responds, it includes a **status code** that indicates whether the request was successful.

Status codes are grouped by category, based on the first number in the code.

## HTTP Status Codes

### ✅ 2xx — Success

| Status Code & Name | What It Means | What You Might Have Done |
|--------------------|--------------------------------|--------------------------|
| **200 OK** | The request worked and data was returned. | You sent a correct request and the API responded properly. |
| **201 Created** | A new item was successfully created. | You sent a valid POST request to create something. |
| **204 No Content** | The request worked, but there was nothing to return. | You successfully updated or deleted something, but there is no response data. |




### ❌ 4xx and 5xx — Errors

| Status Code & Name | What It Means | What You Might Have Done |
|--------------------|--------------------------------|--------------------------|
| **400 Bad Request** | The request was not formatted correctly. | You may have missing fields, incorrect JSON format, or invalid data types. |
| **401 Unauthorized** | Authentication is required or failed. | You forgot to include an API key, token, or your credentials are incorrect. |
| **403 Forbidden** | You are not allowed to access this resource. | You probably used the wrong URL. |
| **404 Not Found** | The requested resource does not exist. | The URL is probably incorrect. |
| **500 Internal Server Error** | Something went wrong on the server. | Your request may be valid, but the API itself encountered an issue. |
| **503 Service Unavailable** | The server is temporarily unavailable. | The API may be down — try again later. |

Status codes help developers quickly understand what happened after making a request.

---

## **Examples of API Usage**
APIs are commonly used for:
- Weather data  
- Financial and stock market data  
- Maps and location services  
- Social media platforms  
- AI and machine learning services  

When you use an app to check the weather or get directions, that app is usually calling one or more APIs.

---

## **APIs in Python**
Python can interact with APIs using libraries such as `requests`. In this course, API examples focus on understanding the concept rather than building complex applications.

Example structure of an API request (not executed):

```python
import requests

response = requests.get("https://api.example.com/data")

print(response.status_code)   # Shows the HTTP status code
print(response.json())        # Converts JSON response into Python data
```
---
## ❓ **Knowledge Check**
{Check It!|assessment}(fill-in-the-blanks-1104312946)

---

## ❓ API Question

The file **`api.py`** is intended to fetch the **current weather in whatever place you choose** using the **Open-Meteo Free Weather API** and display the weather conditions.

However, the program is currently **crashing** due to a bug.

Your task is to:

* Assign response to the value returned by `requests.get(url)` which is currently missing
* Ensure the program runs without crashing
* Confirm that it correctly outputs the current weather conditions for your location
* Have fun searching the weather of interesting places
* You can get the coordinates of different places by googling them

**coordinates list for some interesting locations**:
* **Paris**: 48.8575, 2.3514
* **New York**: 40.7128, -74.0060
* **Rome**: 41.8967, 12.4822
* **Washington DC**: 38.9073, -77.0369
* **Vancouver**: 49.2827, -123.1207

---

### Testing Your Fix

You can test your updated program by opening the terminal using the provided button. Once you believe your program is working correctly, run the test cases.

{Run code | terminal}(python3 api.py)


{Check It!|assessment}(test-1761657150)

# API Authentication

# API Authentication for Beginners

## Learning Objectives

By the end of this module, you should be able to:

- Understand why API authentication is necessary  
- Identify common types of API authentication methods  
- Use an API key in a Python request  
- Safely store authentication credentials  
- Make an authenticated API request using Python  

---

## Why Is Authentication Needed?

API authentication helps:

- Verify who is making the request  
- Prevent unauthorized access  
- Protect sensitive data  
- Limit abuse or misuse of services  
- Track usage of an API  

Authentication ensures that only approved users or applications are allowed to access protected resources.

---

## API Keys

An **API Key** is a unique string provided by a service to identify your application.

Example:
```python
api_key = "123456abcdef"
```

When making a request, the key is sent along with it so the server knows who you are.

---

## Example: Making an Authenticated API Request in Python

Below is a simple example using the `requests` library:

```python
import requests

url = "https://api.example.com/data"

headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

---

## Important Security Practices

**Never:**

- Share your API keys publicly  
- Hardcode keys into programs that others will see  

Instead:

- Store keys in **environment variables** by writing them to a `.env` file.
- Use configuration files that are not committed to version control  

Example:

```python
import os

api_key = os.getenv("API_KEY")
```

If `api_key` is in `.env`, then this code loads the `api_key`.

---

## Summary

API Authentication:

- Confirms identity  
- Controls access  
- Protects data  
- Enables secure communication between systems  

Understanding authentication is an important step in working with real-world APIs.

---

## ❓ NaviGator API Practice

You have a Python script that sends a request to NaviGator via the OpenAI API, but the script retrieves the api key from `.env` which contains your environmental variables for security reasons. In `.env` edit the place holder labeled (`<YOUR_NAVI_GATOR_KEY_HERE>`).  

Your task is to:

1. **Create your own NaviGator API key.**  
2. **Insert that key into the environment file** so that the request will authenticate correctly.  

When the student completes the code, the script should be able to talk to NaviGator without raising a *Missing API Key* error.

---

### Instructions

1. **Obtain your API key**  
   * Log in to the UI portal, https://it.ufl.edu/ai.  
   * On the Navigator Toolkit page, there’s an *API Keys* section. Click “Generate New Key”.
   * Choose `team models` for your model
   * Copy the key to your clipboard.

2. **Edit the .env file**    
   * Find the line that contains `<YOUR_NAVI_GATOR_KEY_HERE>`.  
   * Replace the placeholder entirely with your key.
3. **Run the script**  
   * The script should print the model's response to your prompt and not a Missing API Key error.
   * run your script with the button below:

{Run Code | terminal}(python3 NaviGator_API.py)


4. **Submit** – Once the script runs successfully, run the test case below.

**After you have completed these steps play around with different prompts by editing the message found in**
```python
response = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role": "user", "content": "What do you believe to be humanity's greatest strength"}],
)
```
**Hint: If you run into the ModuleNotFoundError what did the Introduction of Libraries section teach you to do in that case.**

---
### Context & Resources

- NaviGator Chat / Toolkit can be accessed at the University of Florida’s AI portal: https://it.ufl.edu/ai  
- For API keys, consult the Navigator Toolkit documentation: https://docs.ai.it.ufl.edu/docs/navigator_toolkit/intro  
- The sample script is already provided in the workspace (`NaviGator_API.py`).  

---

**Good luck, and enjoy your conversation with NaviGator!**
{Check It!|assessment}(test-1924026970)

# Google Colab

# Google Colab Interactive Tutorial

## What is Google Colab?

Google Colab (short for *Google Colaboratory*) is a free platform for writing and running Python code in a Jupyter Notebook environment.

It allows you to:

* Write and execute Python code in your browser
* Combine code, text, and output in the same document
* Access computing resources without installing anything
* Store and share notebooks through Google Drive

Colab is built on Jupyter Notebook technology, which means it uses the same `.ipynb` file format and cell-based structure (code cells and Markdown cells). 

This tutorial will guide you through:

1. Signing in correctly
2. Creating and running code cells
3. Using standard Python libraries (`math`, `numpy`)
4. Understanding differences between Colab and Jupyter
5. Performing file I/O in Colab
6. Saving work to Google Drive

---

## Step 0: Sign In Correctly (Required for Project 2)

Before continuing:

* Make sure you are signed into **Google Drive using your UFL email**
* You must use your **@ufl.edu account**
* This will be required for Project 2

To verify your account:

Click the profile icon in the top right corner and confirm you are using your UFL email.

---

## Step 1: Uploading The Notebook to Google Colab

1. View the File Tree in Codio.
2. Right-click the file `jupyter_notebook_tutorial.ipynb`
3. Click "Download".
4. Sign in to your Google Drive
5. Go to [https://colab.research.google.com](https://colab.research.google.com)
6. Click **Upload**
7. Select `jupyter_notebook_tutorial.ipynb` in your File Explorer/Finder.

If opening from Google Drive:

1. Upload the `.ipynb` file to Google Drive
2. Right-click the file
3. Choose **Open With → Google Colaboratory**

The rest of this tutorial will be in Google Colab in the notebook you just downloaded and uploaded to Google Colab.


**You will use the notebook to solve the following question:**

---
## ❓ Google Colab Practice
{Check It!|assessment}(multiple-choice-1900185481)
{Check It!|assessment}(multiple-choice-3842961273)
{Check It!|assessment}(fill-in-the-blanks-1945042307)


# Beyond This Course

#
## You Did Something Important

Take a moment to **recognize what you’ve accomplished**.

When you first started this course, programming may have seemed:

- Confusing  
- Intimidating  
- Overwhelming  
- Or even *completely out of reach*  

But **now?**

You’ve written **real code**.  
You’ve solved **real problems**.  
You’ve debugged **real errors**.  
You’ve built **real solutions**.

**That matters.**

---

## The Real Goal of This Course

The primary goal of this course was **never** to make you memorize syntax or complete assignments.

It was to help you understand something much more important:

> *You are **capable** of **learning** how to **program**.*

Programming is not about being naturally gifted or "just getting it."

It’s about:

- Trying  
- Failing  
- Debugging  
- Asking questions  
- Trying again  

Over and over until things begin to make sense.

---

## This Process Took Years to Develop

The learning experience you’ve gone through in this course did not happen overnight.

Educators, engineers, and developers have spent **years**:

- Researching how students learn technical skills  
- Designing beginner-friendly environments  
- Improving tools that support exploration  
- Creating pathways into engineering that are accessible to everyone  

So that *you* could begin your journey here.

---

## Where You Go From Here

**You are not expected to know everything right now**.

In fact — **no engineer ever does**.

What **you** now have is:

- A **foundation**  
- A **process**  
- A way to approach problems  
- And the **confidence** that you can learn new technical skills  

That is what **real growth in engineering** looks like.

We leave you with **Google Colab** so you can continue programming on your own, outside of Codio. Take Project 2 seriously so you can continue to apply the skills you've developed.

---

## We Could Not Be Happier With Your Progress

Learning how to program is **challenging**.

It takes **patience**.  
It takes **persistence**.  
It takes **courage** to keep going when things don’t work the first time.

And you did it.

We are incredibly proud of the **effort**, **resilience**, and **growth** you’ve shown throughout this course.

---

## Keep Building

This may be the end of the course,

but it’s **only the beginning** of your journey.

Keep asking **questions**.  
Keep **experimenting**.  
Keep **learning**.

**You belong here.**
