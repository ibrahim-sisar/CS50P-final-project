import os
import json
import sys
import re
import shutil

def main():
    print(os.getcwd())
    argv = sys.argv
    argc = len(argv)
    print("1.sort in folder     2.Add new category\n3.Show all categories")
    choice = int(input("Your choice: "))
    match choice:
        case 1:
            dic = get_file_name(argv[1])
            for key,value in dic.items():
                print(mkdir(key,argv[1]))
                print("="*10,key,"="*10)
                for i in value:
                    print(f"- {i}")
        case 2:
            ex_arr=[]
            name = input("name: ")
            while True:
                inp = input("File extension [stop:ctl + d] ")
                if inp == '':
                    break
                ex_arr.append(inp)
            add_file_ex(name,ex_arr)
        

def get_file_name(dir):
    arr = {}
    for i in os.listdir(dir) :
        i = i.lower()
        if not os.path.isdir(dir+"\\"+i):
            if "." in i and get_file_ex(i.split(".")[-1]):
                file_ex = get_file_ex(i.split(".")[-1])
                if file_ex in arr:
                    arr[file_ex] += [i]
                else:
                    arr[file_ex] = [i]
    return arr

def mkdir(name,dir):
    try:
        os.mkdir(dir+"\\"+name)
        return True
    except:
        return False

def get_file_ex(ex):
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

def add_file_ex(name,ex):
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
if __name__ == "__main__":
    main()