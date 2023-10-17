# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:24:00 2023

@author: Don Jeffrey
"""

from tkinter import*
root=Tk()
root.title("RANDOM COUNTRY - 2") 
root.geometry("500x400")
import random 


Country_list = []
Capital_list = []

input = Entry(root)
input.place(relx=0.5,rely=0.1,anchor=CENTER)


input2 = Entry(root)
input2.place(relx=0.5,rely=0.2,anchor=CENTER)

List_label = Label(root,text="COUNTRIES LIST :  ",wraplength=80)
randomFrnd_label = Label(root,text="RANDOM COUNTRY :   ")

List_label2 = Label(root,text="CAPITALS LIST :  ",wraplength=80)
randomCapital_label = Label(root,text="RANDOM CAPITAL :   ")


def addCntry():
    countryName = str(input.get())
    Country_list.append(countryName)
    List_label["text"]="\n"+"COUNTRIES LIST :  "+str(Country_list)
    
    capitalName = str(input2.get())
    Capital_list.append(capitalName)
    List_label2["text"]="\n"+"CAPITAL LIST :  "+str(Capital_list)
    

    
def RandNum():
    cntry_num = random.randint(0,len(Country_list)-1)
    randomFrnd_label["text"] = "RANDOM COUNTRY :   "+Country_list[cntry_num]
    
    capital_num = random.randint(0,len(Capital_list)-1)
    randomCapital_label["text"] = "RANDOM COUNTRY :   "+Capital_list[capital_num]
    
  


btn1 = Button(root,text="ADD COUNTRY",command=addCntry,bg="blue",fg="white")
btn2 = Button(root,text="RANDOM COUNTRY",command=RandNum,bg="blue",fg="white")


List_label.place(relx=0.2,rely=0.3,anchor=CENTER)
randomFrnd_label.place(relx=0.5,rely=0.7,anchor=CENTER)

List_label2.place(relx=0.8,rely=0.3,anchor=CENTER)
randomCapital_label.place(relx=0.5,rely=0.8,anchor=CENTER)

btn1.place(relx=0.5,rely=0.3,anchor=CENTER)
btn2.place(relx=0.5,rely=0.9,anchor=CENTER)


root.mainloop()