import os
import json
import sys
import re
import shutil

class File_sort:
    def __init__(self):
        self.dir = sys.argv[1]
    def get_file_names(self):
        dir = self.dir
        arr = {}
        for i in os.listdir(dir) :
            i = i.lower()
            if not os.path.isdir(dir+"\\"+i):
                if "." in i and self.get_file_ex(i.split(".")[-1]):
                    file_ex = self.get_file_ex(i.split(".")[-1])
                    if file_ex in arr:
                        arr[file_ex] += [i]
                    else:
                        arr[file_ex] = [i]
        return arr
    def mkdir(self,name):
        try:
            os.mkdir(self.dir+"\\"+name)
            return True
        except:
            return False
    def get_file_ex(self,ex):
        with open("file.json") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print("file is empty")
            except FileNotFoundError:
                print("Error: File not found")
            else:
                for key,value in data.items():
                    if ex in value:
                        return key
                else:
                    return 'none'
    def add_file_ex(self):
        ex=[]
        name = input("name: ")
        while True:
            inp = input("File extension [stop:ctl + d] ")
            if inp == '':
                break
            ex.append(inp)
        with open("file.json") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print("file is empty")
            except FileNotFoundError:
                print("Error: File not found")
            else:
                data[name] = ex
                with open("file.json",'w') as wfile:
                    json_f = json.dumps(data)
                    wfile.write(json_f)   
def main():
    file_sort = File_sort() 
    print("1.sort in folder     2.Add new category\n3.Show all categories")
    choice = int(input("Your choice: "))
    match choice:
        case 1:
            dic = file_sort.get_file_names()
            for key,value in dic.items():
                file_sort.mkdir(key)
                print("="*10,key,"="*10)
                for i in value:
                    print(f"- {i}")
        case 2:
            file_sort.add_file_ex()
        
if __name__ == "__main__":
    main()