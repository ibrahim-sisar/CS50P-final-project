# **🎬 CS50P Final Project Video Script - FileSorter**

## **🎤 Introduction (0:00 - 0:30)**
📌 **Objective:** Introduce the project, its purpose, and how it relates to CS50P.  
🎥 **Visual:** Show a cluttered folder with random files.

**🎙️ Script:**  
*"Hello everyone! My name is ibrahim abu al roos, and this is my final project for **CS50P: Introduction to Programming with Python**. The project is called **FileSorter**, a Python script that **automatically organizes files** into categorized folders based on their extensions."*

*"If you’ve ever had a messy **Downloads** folder full of random files, FileSorter is here to help! Let’s see how it works."*

---

## **⚙️ How It Works (0:30 - 1:00)**
📌 **Objective:** Explain the logic behind the script.  
🎥 **Visual:** Open `file.json` and show different categories.

**🎙️ Script:**  
*"FileSorter works by scanning a specified directory and **categorizing files** based on their extensions. It reads from a configuration file called `file.json`, which defines which extensions belong to which categories."*

*"For example, `Documents` include `.pdf`, `.docx`, and `.pptx`, while `Images` include `.jpg`, `.png`, and `.gif`. If a file type is **not listed**, it gets placed in an **‘Other’** folder."*

*"Users can also **add new categories dynamically**, making FileSorter fully **customizable**!"*

---

## **💻 Running the Script (1:00 - 1:40)**
📌 **Objective:** Show how to use FileSorter in real-world scenarios.  
🎥 **Visual:** Open terminal and execute the script.

**🎙️ Script:**  
*"Let’s see FileSorter in action! Here, I have a **messy folder** with mixed files—some PDFs, images, MP3s, and text files."*

*"To organize them, I simply run:"*
```sh
python main.py path/to/your/folder
```
## 🎥 (Show script running, moving files into folders.)

"And just like that, everything is neatly sorted into their respective folders!"

## ➕ Adding Custom Categories (1:40 - 2:10)
### 📌 Objective: Demonstrate how users can customize FileSorter.
### 🎥 Visual: Show interactive input for adding a new category.

### 🎙️ Script

"One great feature of FileSorter is that you can add new file categories dynamically. Let’s say I want to organize `.csv` files separately under a category called Spreadsheets. I just run the script and select the option to add a new category."

### 🎥 (Show interactive input process.)

"Now, when I run the script again, `.csv` files will automatically move to the Spreadsheets folder!"

## 🧪 Testing with Pytest (2:10 - 2:40)
### 📌 Objective: Showcase the importance of testing.
### 🎥 Visual: Show pytest running and passing tests.

### 🎙️ Script:
"To ensure FileSorter is reliable, I implemented unit tests using pytest. These tests verify that files are categorized correctly, directories are created, and files are moved safely."
"To run the tests, simply execute:"

### 🎥 (Show passing test results.)
"This guarantees that FileSorter functions correctly in different scenarios."

## 🚀 Future Improvements & Conclusion (2:40 - 3:10)
### 📌 Objective: Highlight potential improvements and encourage engagement.
### 🎥 Visual: Show a roadmap or GitHub repo.

### 🎙️ Script:
"While FileSorter is already useful, I plan to expand its functionality by adding:"
- 🔹 Sorting by file size, date, and type
- 🔹 A graphical user interface (GUI) for easier interaction
- 🔹 Multi-threading for faster performance

"The full project source code is available on my GitHub repository at: [GitHub Link]. Feel free to check it out, contribute, or suggest improvements!"

"Thank you for watching my CS50P final project! I hope you found it useful, and I look forward to continuing my journey in Python programming. Happy coding! 🚀"

#### 🎥 (End with a clean desktop and closing screen with GitHub link.)