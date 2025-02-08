# **📂 FileSorter - Automated File Organizer**

## **📌 Project Summary**

**FileSorter** is a Python-based script designed to **automatically organize files** into categorized folders based on their extensions. It helps keep directories tidy by grouping files into logical categories such as "Documents," "Images," "Music," etc.

---

### **🔹 Features**

- ✅ **Automated File Sorting**: Moves files into predefined folders based on their extensions.
- ✅ **Customizable Categories**: Users can add new file categories interactively.
- ✅ **Dynamic Configuration**: Reads categories from a JSON file (`file.json`).
- ✅ **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- ✅ **Safe File Handling**: Ensures smooth movement of files without conflicts.

---

### **🔹 How It Works**

1. The script scans a given directory for files.
2. It reads `file.json` to determine which files belong to which category.
3. Files are moved into their respective folders.
4. Users can **add new categories** or **view existing ones**.

---

### **🔹 Usage**

Run the script with:

```sh
python main.py <directory_path>
```

### Example:

```sh
python main.py C:\Users\Username\Downloads
```

### 🛠 Future Enhancements

- ✅ Support for sorting by file size, date, or type.
- ✅ GUI version for easier usability.
- ✅ Multi-threading for faster sorting.
