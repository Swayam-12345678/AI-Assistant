import tkinter as tk
from tkinter import Entry,Label,Button
import webbrowser

#Define the main window
root=tk.Tk()
root.title("MY AI ASSISTANT")

#Adding background colour
root.configure(bg='skyblue')

#Define functiion to automate youtube search
def search_youtube():
    query=entry.get() #from entry object to get method use inputfield command typed to stores as query
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)


def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def search_instagram():
    username=entry.get().replace('@',"")
    url=f"https://www.instagram.com{username}"
    webbrowser.open(url)


def search_linkedin():
    username = entry.get().lstrip('@').strip()
    url = f"https://www.linkedin.com/in/{username}/"
    webbrowser.open(url)

#Create input field,labels,buttons
Label(root,text="Enter your command:").pack(pady=10)
entry=Entry(root,width=50)
entry.pack(pady=10)

Button(root,text="Search on youtube", command=search_youtube).pack(pady=5)
Button(root,text="Search on google", command=search_google).pack(pady=5)
Button(root,text="Search on instagram", command=search_instagram).pack(pady=5)
Button(root,text="Search on linkedin", command=search_linkedin).pack(pady=5)

#Run GUI event loop
root.mainloop()