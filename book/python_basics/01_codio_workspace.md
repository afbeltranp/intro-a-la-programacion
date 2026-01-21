---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Codio Workspace

## **Learning Objectives**  
- ✅ Understand how to **create** and **manage project files** in Codio.  
- ✅ Learn to access and execute **commands** using the Codio terminal.  
- ✅ Identify and use essential tools like the **code editor**, **file tree**, and **terminal**.

<iframe 
    src="https://mediasite.video.ufl.edu/Mediasite/Play/5a471bb798f64030bfd4f196059d74d21d" 
    width="540" 
    height="360" 
    allowfullscreen 
    style="border: none;">
</iframe>

## **Understanding Your Workspace in Codio**  
In Codio, you're working on a **virtual machine**, which is like a remote computer hosted elsewhere. Knowing how to use the **terminal** is crucial for efficiently navigating and managing your development environment.

## **The Terminal**  
The terminal is a **text-based interface** that lets you interact with your virtual machine. Instead of using a graphical interface (like clicking with a mouse), you **type commands** to control your environment.

With the terminal, you can:
- **Navigate directories** (folders),
- **List files** in a directory,
- **Manipulate files**, and
- **Execute commands** directly in your virtual environment.

## **Accessing the Terminal in Codio**  
You can access the terminal by going to **Tools > Terminal** in the menu. In some workspaces, the terminal may already be visible.

## **Little Exercise: Navigating Directories and Listing Files in the Terminal**  
Let's get familiar with using the terminal by performing some basic tasks like navigating directories and listing files.

### **1. Check Your Current Directory**  
To see the current directory you're in, type:

```bash
pwd
```
The `pwd` command stands for "print working directory" and shows you the full path of your current directory.

### **2. List Files and Folders**  
To see the contents of your current directory, type:

```bash
ls
```
The `ls` command lists all files and folders in the current directory.

### **3. Navigate to a Folder**  
To change into a different directory, type:

```bash
cd foldername
```
Replace `foldername` with the actual name of the directory you want to enter. The `cd` command stands for "change directory."

### **4. Go Back to the Previous Directory**  
To go back one level to the parent directory, type:

```bash
cd ..
```
This command moves you up one level in the directory structure.

### **5. Create a New Directory**  
To create a new folder, type:

```bash
mkdir newfoldername
```
Replace `newfoldername` with the name of the folder you want to create. The `mkdir` command stands for "make directory."

### **6. Remove a Directory (optional, be careful with this)**  
If you want to remove a directory, type:

```bash
rmdir foldername
```
Replace `foldername` with the name of the directory you want to delete. The `rmdir` command removes the directory. **Be cautious**—this will permanently delete the folder if it is empty.

### **7. Create a New File with `touch`**

To create an empty file, type:

```bash
touch filename.txt
```

Replace `filename.txt` with the name you want to give your file. The `touch` command creates a new, empty file if it does not already exist. If the file already exists, `touch` will update its timestamp instead of changing its contents.

### **8. Delete a File (be careful with this)**

To remove a file, type:

```bash
rm filename.txt
```

Replace `filename.txt` with the name of the file you want to delete. The `rm` command stands for "remove."

⚠️ **Warning:** Once deleted with `rm`, the file cannot be recovered from the terminal. Make sure you really want to remove it before running this command.

## **Making Your Workspace Yours**  
To make your workspace more personalized and visually pleasing, use the **View** option in the Codio workspace.  
Go to **View > File Tree** to see your project files. You can adjust the font size, terminal color, or editor theme to match your preferences.

## **The File Tree**  
The **File Tree** is a graphical interface that shows you the folders and files in your project. This is similar to the **Explorer** or **Finder** on your local machine. You can:
- Drag and drop files,
- Create directories, and
- Navigate through your project.

However, remember that certain tasks in Codio, like manipulating files and directories, still require the use of the terminal.

## **Key Takeaways**  
- **The terminal** is an essential tool in Codio, allowing you to control your virtual machine by typing commands.  
- You can **navigate directories**, **list files**, **create directories**, and **remove directories** using basic commands.  
- Personalize your workspace by adjusting settings such as font size and theme, and use the **File Tree** for a graphical file management experience.

**Next Steps**: Practice using the terminal to navigate directories and manage files, and explore customizing your Codio workspace to suit your needs.

## **Question: Terminal Drill**

Follow these steps in Codio's terminal. Use the commands you learned to complete each task.

### 1) Locate Yourself

* Use the command that **prints your working directory**.
* **Hint:** You should be in the **/home/codio/workspace** directory. If you are not in this directory, use the command that **changes your directory** to get to the right place.

### 2) What's Here?

* Use the command that **lists files and folders** in your current location.

### 3) Start a Mini Project

* **Create** a new folder named `mini_project` using the command that **makes a directory**.
* Verify it exists by **listing** your current directory.

### 4) Go Inside

* **Change directories** into `mini_project`.
* Confirm your location using the command that **prints the working directory**.

### 5) Make Two Files

* **Create** two empty files named `notes.txt` and `data.log` using the command that **creates empty files**.
* Verify they exist by **listing** the directory.

### Quizzes

To take a quiz, simply click on the cards to select your answer and get immediate feedback.

Quizzes may include multiple-choice questions, numeric responses, or short text answers.

#### Example

```{code-cell} ipython3
:tags: ["remove-input"]
from jupyterquiz import display_quiz

import json

questions = [
  {
    "question": "What is the correct answer?",
    "type": "multiple_choice",
    "answers": [
      {
        "answer": "This is the correct answer",
        "correct": True,
        "feedback": "Correct, this is the correct answer."
      },
      {
          "answer": "This is not the correct answer",
          "correct": False,
          "feedback": "No, this is not the correct answer."
      },
      {
          "answer": "This is also not the correct answer",
          "correct": False,
          "feedback": "Incorrect. This is not the correct answer."
      }
    ]
  },
  {
    "question": "What is the correct answer? (Hint: It's 42)",
    "type": "numeric",
    "precision": 2,
    "answers": [
      {
        "type": "value",
        "value": 42,
        "correct": True,
        "feedback": "Correct, 42 is the answer."
      },
      {
        "type": "value",
        "value": 24,
        "correct": False,
        "feedback": "Incorrect, 24 is not the answer."
      },
      {
        "type": "default",
        "feedback": "Try again."
      }
    ]
  },
  {
    "question": "Who is the king of the jungle?",
    "type": "string",
    "answers": [
        {
            "answer": "Lion",
            "correct": True,
            "feedback": "Correct, the lion is often referred to as the king of the jungle.",
            "match_case": False,
            "fuzzy_threshold": 0.8
        },
        {
            "answer": "Not Lion",
            "correct": False,
            "feedback": "Wrong, the lion is considered the king of the jungle.",
        }
    ]
  }
]


display_quiz(questions)
```

### Code-Along and Exercises

For code-along snippets and exercises, you can run the code directly within the book. Click the {fa}`rocket` → {guilabel}`Live Code` button at the top of the page to enable the interactive environment.

This will allow you to run, edit, and experiment with the code snippets, as well as attempt the embedded exercises and tests.

```{note}
Wait for the kernal status to become "ready" before you start coding. You can see this at the top of your screen.
```

#### Example

```{code-cell} ipython3

import matplotlib.pyplot as plt
import numpy as np

num_points = 100 # Change this value to plot more or fewer points
x = np.random.rand(num_points)
y = np.random.rand(num_points)
plt.scatter(x, y)
plt.title(f"Scatter Plot of {num_points} Random Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

#### Example

<!-- question:id=square -->

```{code-cell} ipython3
:class: thebelab-input
# Write a function that returns the square of a number
def square(x):
    # Your code here
    pass
```

<!-- test:for=square -->

```{code-cell} ipython3
:class: thebelab-hidden
# Hidden test cell (but runs when user clicks Run All)
try:
    assert square(3) == 9
    print("✅ Correct")
except Exception as e:
    print(f"❌ Incorrect: {e}")
```

```{important}
Your code edits are saved locally in your browser's storage, so you can return later and pick up where you left off - as long as **Live Code** mode is enabled. This applies to all editable code cells throughout the book.

To reset the book and remove all saved edits, simply clear your browser's local storage.
```