from tkinter import *
import requests

def make_request(data):
    url = "http://127.0.0.1:8000/users/"    
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())


root = Tk()

e = Entry(root, width=50, borderwidth=5,fg='white')
e.pack()
e.insert(0, "chris")

def submitHandler():
    data = {
        "name": e.get(),
        "age": 25
    }
    make_request(data)


button = Button(root, text='Submit', command=submitHandler)
button.pack()

root.mainloop()