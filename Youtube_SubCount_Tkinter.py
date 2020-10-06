import tkinter
import requests
from bs4 import BeautifulSoup

count = ""
root= tkinter.Tk()
root.title("Youtube Subscriber Count")
root.geometry("200x200")

def All_Processing():
    link=Link_Entery.get()
    
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    week = soup.find(id="c4-primary-header-contents")
    if week!=None:
        element = week.find(class_="yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip")
        global count 
        count = element.get_text()
        view_label = tkinter.Label(root,text="Total Number Of Subscribers --> {} ".format(count)).grid(row=5,column=0)
    else:
        view_label = tkinter.Label(root,text="Please Check Your Internet Connection Or Enter A Valid Link").grid(row=5,column=0)

link = tkinter.Label(root,text="Enter The Link").grid(row=2,column=0)
Link_Entery = tkinter.Entry(root)
Link_Entery.grid(row=3,column=0)


submit_button = tkinter.Button(root,text="submit",command=All_Processing).grid(row=4,column=0)
root.mainloop()
