import os
import json
import sys
import shutil

class FileSorter:
    def __init__(self):
        # Ensure a directory argument is provided
        if len(sys.argv) < 2:
            print("Error: No directory specified.")
            sys.exit(1)
        self.dir = sys.argv[1]

    def get_file_names(self):
        """Get all files in the directory and categorize them based on extensions."""
        directory = self.dir
        file_categories = {}

        try:
            for file in os.listdir(directory):
                file_lower = file.lower()
                file_path = os.path.join(directory, file)

                # Check if it's a file and has an extension
                if os.path.isfile(file_path) and "." in file_lower:
                    category = self.get_file_category_f(file_lower)

                    if category in file_categories:
                        file_categories[category].append(file)
                    else:
                        file_categories[category] = [file]

        except FileNotFoundError:
            print(f"Error: Directory '{directory}' not found.")
            sys.exit(1)

        return file_categories

    def create_directory(self, name):
        """Create a new directory inside the main directory if it doesn't exist."""
        folder_path = os.path.join(self.dir, name)
        try:
            os.makedirs(folder_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory '{name}': {e}")

    def get_file_category(self, extension):
        """Retrieve file category based on extension from file.json."""
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
                for category, extensions in data.items():
                    if extension in extensions:
                        return category
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print("Warning: 'file.json' is missing or invalid.")
        
        return "other"  # Default category

    def add_file_category(self):
        """Allow user to add a new file category with associated extensions."""
        extensions = []
        name = input("Category name: ")

        print("Enter file extensions (Press Enter to stop):")
        while True:
            ext = input("File extension: ").strip()
            if not ext:
                break
            extensions.append(ext)

        try:
            with open("file.json", "r") as file:
                data = json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            data = {}

        data[name] = extensions
        with open("file.json", "w") as file:
            json.dump(data, file, indent=4)

    def move_file(self, source, destination):
        """Move file from one location to another."""
        try:
            shutil.move(source, destination)
        except OSError as e:
            print(f"Error moving file '{source}': {e}")

    def show_all_categories(self):
        """Display all file categories and their extensions."""
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
                for category, extensions in data.items():
                    print("=" * 20, category.upper(), "=" * 20)
                    for ext in extensions:
                        print(f"- {ext}")
                    print("=" * (40 + len(category)), "\n")
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print("Warning: 'file.json' is missing or invalid.")
    def get_file_ex(self,file_name):
        return file_name.split(".")[-1].lower()
    def get_file_category_f(self,file_name):
        file_name = file_name.lower()
        return self.get_file_category(self.get_file_ex(file_name))
def main():
    file_sorter = FileSorter()
    
    print("1. Sort files into folders")
    print("2. Add a new file category")
    print("3. Show all categories")
    
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    if choice == 1:
        file_dict = file_sorter.get_file_names()
        for category, files in file_dict.items():
            file_sorter.create_directory(category)
            print("=" * 10, category.upper(), "=" * 10)
            for file in files:
                src = os.path.join(file_sorter.dir, file)
                dest = os.path.join(file_sorter.dir, category, file)
                file_sorter.move_file(src, dest)
                print(f"- {file}")
    elif choice == 2:
        file_sorter.add_file_category()
    elif choice == 3:
        file_sorter.show_all_categories()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
