from tkinter import *
from datetime import *
import requests

URL='https://api.open-meteo.com/v1/forecast?latitude=35.6944&longitude=51.4215&hourly=temperature_2m&timezone=Europe%2FMoscow'
location="delhi technological university"
PARAM={'adress':location}
info=requests.get(url=URL,params=PARAM)
data=info.json()
temps=data["hourly"]["temperature_2m"]

live=datetime.now()
hour=live.hour
day=live.strftime('%A')

# variables
back1="#0000CC"
fore="white"
back2="#CC0066"
fore2="black"
inxsel=0
# ----- root
root =Tk()
root.title("Weather")
root.geometry('460x400')
root.resizable(False,False)

#---- header
header=Frame(root,bg=fore)
header.place(x=0,y=0,width=500,height=40)
title=Label(header,bg=fore,fg=fore2,text="Weather", font=("tahoma",20))
title.pack(side="left")

#---- now
body=Frame(root,bg=back1)
body.place(x=0,y=40,height=120,width=500)
now=Label(body,bg=back1,fg=fore,text="Now", font=("tahoma",15))
now.grid(row=2,column=0,pady=20)
tehran=Label(body,bg=back1,fg=fore,text="Tehran", font=("tahoma",20))
tehran.grid(row=3,column=0,padx=10)
weather=Label(body,bg=back1, fg=fore, font=("tahoma",20),text=f"{temps[hour]} C")
weather.grid(row=3,column=3,padx=100)

#---- hours AM
hours=Frame(root,bg=back2)
hours.place(x=0,y=160,width=500,height=50)
zero=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="00")
zero.pack(side="left",padx=6)
one=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="01")
one.pack(side="left",padx=6)
two=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="02")
two.pack(side="left",padx=6)
three=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="03")
three.pack(side="left",padx=6)
four=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="04")
four.pack(side="left",padx=6)
five=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="05")
five.pack(side="left",padx=6)
six=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="06")
six.pack(side="left",padx=6)
seven=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="07")
seven.pack(side="left",padx=6)
eight=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="08")
eight.pack(side="left",padx=6)
nine=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="09")
nine.pack(side="left",padx=6)
ten=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="10")
ten.pack(side="left",padx=6)
elev=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="11")
elev.pack(side="left",padx=6)

#---- weathers AM
weathers=Frame(root,bg=back2)
weathers.place(x=0,y=210,width=500,height=50)
zero=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[0])
zero.pack(side="left",padx=5)
one=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[1])
one.pack(side="left",padx=5)
two=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[2])
two.pack(side="left",padx=5)
three=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[3])
three.pack(side="left",padx=5)
four=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[4])
four.pack(side="left",padx=4)
five=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[5])
five.pack(side="left",padx=4)
six=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[6])
six.pack(side="left",padx=4)
seven=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[7])
seven.pack(side="left",padx=4)
eight=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[8])
eight.pack(side="left",padx=4)
nine=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[9])
nine.pack(side="left",padx=5)
ten=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[10])
ten.pack(side="left",padx=5)
elev=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[11])
elev.pack(side="left",padx=5)

#---- hours PM
hours=Frame(root,bg=back2)
hours.place(x=0,y=260,width=500,height=50)
zero=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="12")
zero.pack(side="left",padx=6)
one=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="13")
one.pack(side="left",padx=6)
two=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="14")
two.pack(side="left",padx=6)
three=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="15")
three.pack(side="left",padx=6)
four=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="16")
four.pack(side="left",padx=6)
five=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="17")
five.pack(side="left",padx=6)
six=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="18")
six.pack(side="left",padx=6)
seven=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="19")
seven.pack(side="left",padx=6)
eight=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="20")
eight.pack(side="left",padx=6)
nine=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="21")
nine.pack(side="left",padx=6)
ten=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="22")
ten.pack(side="left",padx=6)
elev=Label(hours,bg=back2, fg=fore, font=("tahoma",15),text="23")
elev.pack(side="left",padx=6)

#---- weathers AM
weathers=Frame(root,bg=back2)
weathers.place(x=0,y=310,width=500,height=50)
ten2=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[12])
ten2.pack(side="left",padx=5)
ten3=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[13])
ten3.pack(side="left",padx=5)
ten4=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[14])
ten4.pack(side="left",padx=5)
ten5=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[15])
ten5.pack(side="left",padx=5)
ten6=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[16])
ten6.pack(side="left",padx=4)
ten7=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[17])
ten7.pack(side="left",padx=4)
ten8=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[18])
ten8.pack(side="left",padx=4)
ten9=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[19])
ten9.pack(side="left",padx=4)
two0=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[20])
two0.pack(side="left",padx=4)
two1=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[21])
two1.pack(side="left",padx=5)
two2=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[22])
two2.pack(side="left",padx=5)
two3=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[23])
two3.pack(side="left",padx=5) 


root.mainloop()