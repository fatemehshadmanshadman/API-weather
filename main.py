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
inselec=0
temp=0 
  
# ----- root
root =Tk()
root.title("Weather")
root.geometry('460x390')
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
weather=Label(body,bg=back1, fg=fore, font=("tahoma",20),text=f"{hour}:00 is {temps[hour]} C")
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
zero0=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[0])
zero0.pack(side="left",padx=5)
one1=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[1])
one1.pack(side="left",padx=5)
two2=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[2])
two2.pack(side="left",padx=5)
three3=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[3])
three3.pack(side="left",padx=5)
four4=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[4])
four4.pack(side="left",padx=4)
five5=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[5])
five5.pack(side="left",padx=4)
six6=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[6])
six6.pack(side="left",padx=4)
seven7=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[7])
seven7.pack(side="left",padx=4)
eight8=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[8])
eight8.pack(side="left",padx=4)
nine9=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[9])
nine9.pack(side="left",padx=5)
ten0=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[10])
ten0.pack(side="left",padx=5)
ten1=Label(weathers ,bg=back2, fg=fore, font=("tahoma",10),text=temps[11])
ten1.pack(side="left",padx=5)

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

#---- weathers PM
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

#---- function
days=["Sat","Sun","Mon","Tue","Wed","Thur","Fri"]
for i in range(len(days)):  #change now day color
    if day.startswith(days[i]):
        index=i

def isSat():
    changeColor(index=0)
    check(flag=0)
            
def isSun():
    changeColor(index=1)
    check(flag=1)
    
def isMon():
    changeColor(index=2)
    check(flag=2)
    
def isTue():
    changeColor(index=3)
    check(flag=3)
    
def isWed():
    changeColor(index=4)
    check(flag=4)

def isThur():
    changeColor(index=5)
    check(flag=5)

def isFri():
    changeColor(index=6)
    check(flag=6)
        
def check(flag): 
    temp= 7-index+flag
    if temp==1: #24 - 47
        zero0.config(text=temps[24])
        one1.config(text=temps[25])
        two2.config(text=temps[26])
        three3.config(text=temps[27])
        four4.config(text=temps[28])
        five5.config(text=temps[29])
        six6.config(text=temps[30])
        seven7.config(text=temps[31])
        eight8.config(text=temps[32])
        nine9.config(text=temps[33])
        ten0.config(text=temps[34])
        ten1.config(text=temps[35])
        ten2.config(text=temps[36])
        ten3.config(text=temps[37])
        ten4.config(text=temps[38])
        ten5.config(text=temps[39])
        ten6.config(text=temps[40])
        ten7.config(text=temps[41])
        ten8.config(text=temps[42])
        ten9.config(text=temps[43])
        two0.config(text=temps[44])
        two1.config(text=temps[45])
        two2.config(text=temps[46])
        two3.config(text=temps[47])

    if temp==2: #48 - 71
        zero0.config(text=temps[48])
        one1.config(text=temps[49])
        two2.config(text=temps[50])
        three3.config(text=temps[51])
        four4.config(text=temps[52])
        five5.config(text=temps[53])
        six6.config(text=temps[54])
        seven7.config(text=temps[55])
        eight8.config(text=temps[56])
        nine9.config(text=temps[57])
        ten0.config(text=temps[58])
        ten1.config(text=temps[59])
        ten2.config(text=temps[60])
        ten3.config(text=temps[61])
        ten4.config(text=temps[62])
        ten5.config(text=temps[63])
        ten6.config(text=temps[64])
        ten7.config(text=temps[65])
        ten8.config(text=temps[66])
        ten9.config(text=temps[67])
        two0.config(text=temps[68])
        two1.config(text=temps[69])
        two2.config(text=temps[70])
        two3.config(text=temps[71])

    if temp==3: #72 - 95
        zero0.config(text=temps[72])
        one1.config(text=temps[73])
        two2.config(text=temps[74])
        three3.config(text=temps[75])
        four4.config(text=temps[76])
        five5.config(text=temps[77])
        six6.config(text=temps[78])
        seven7.config(text=temps[79])
        eight8.config(text=temps[80])
        nine9.config(text=temps[81])
        ten0.config(text=temps[82])
        ten1.config(text=temps[83])
        ten2.config(text=temps[84])
        ten3.config(text=temps[85])
        ten4.config(text=temps[86])
        ten5.config(text=temps[87])
        ten6.config(text=temps[88])
        ten7.config(text=temps[89])
        ten8.config(text=temps[90])
        ten9.config(text=temps[91])
        two0.config(text=temps[92])
        two1.config(text=temps[93])
        two2.config(text=temps[94])
        two3.config(text=temps[95])    

    if temp==4: #96 - 119
        i=96
        zero0.config(text=temps[i])
        i+=1
        one1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        three3.config(text=temps[i])
        i+=1
        four4.config(text=temps[i])
        i+=1
        five5.config(text=temps[i])
        i+=1
        six6.config(text=temps[i])
        i+=1
        seven7.config(text=temps[i])
        i+=1
        eight8.config(text=temps[i])
        i+=1
        nine9.config(text=temps[i])
        i+=1
        ten0.config(text=temps[i])
        i+=1
        ten1.config(text=temps[i])
        i+=1
        ten2.config(text=temps[i])
        i+=1
        ten3.config(text=temps[i])
        i+=1
        ten4.config(text=temps[i])
        i+=1
        ten5.config(text=temps[i])
        i+=1
        ten6.config(text=temps[i])
        i+=1
        ten7.config(text=temps[i])
        i+=1
        ten8.config(text=temps[i])
        i+=1
        ten9.config(text=temps[i])
        i+=1
        two0.config(text=temps[i])
        i+=1
        two1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        two3.config(text=temps[i])
        
    if temp==5: #120 - 143
        i=120
        zero0.config(text=temps[i])
        i+=1
        one1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        three3.config(text=temps[i])
        i+=1
        four4.config(text=temps[i])
        i+=1
        five5.config(text=temps[i])
        i+=1
        six6.config(text=temps[i])
        i+=1
        seven7.config(text=temps[i])
        i+=1
        eight8.config(text=temps[i])
        i+=1
        nine9.config(text=temps[i])
        i+=1
        ten0.config(text=temps[i])
        i+=1
        ten1.config(text=temps[i])
        i+=1
        ten2.config(text=temps[i])
        i+=1
        ten3.config(text=temps[i])
        i+=1
        ten4.config(text=temps[i])
        i+=1
        ten5.config(text=temps[i])
        i+=1
        ten6.config(text=temps[i])
        i+=1
        ten7.config(text=temps[i])
        i+=1
        ten8.config(text=temps[i])
        i+=1
        ten9.config(text=temps[i])
        i+=1
        two0.config(text=temps[i])
        i+=1
        two1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        two3.config(text=temps[i])
        
    if temp==6: #144 - 168
        i=144
        zero0.config(text=temps[i])
        i+=1
        one1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        three3.config(text=temps[i])
        i+=1
        four4.config(text=temps[i])
        i+=1
        five5.config(text=temps[i])
        i+=1
        six6.config(text=temps[i])
        i+=1
        seven7.config(text=temps[i])
        i+=1
        eight8.config(text=temps[i])
        i+=1
        nine9.config(text=temps[i])
        i+=1
        ten0.config(text=temps[i])
        i+=1
        ten1.config(text=temps[i])
        i+=1
        ten2.config(text=temps[i])
        i+=1
        ten3.config(text=temps[i])
        i+=1
        ten4.config(text=temps[i])
        i+=1
        ten5.config(text=temps[i])
        i+=1
        ten6.config(text=temps[i])
        i+=1
        ten7.config(text=temps[i])
        i+=1
        ten8.config(text=temps[i])
        i+=1
        ten9.config(text=temps[i])
        i+=1
        two0.config(text=temps[i])
        i+=1
        two1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        two3.config(text=temps[i])
        
    if temp==7: #0 - 23
        i=0
        zero0.config(text=temps[i])
        i+=1
        one1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        three3.config(text=temps[i])
        i+=1
        four4.config(text=temps[i])
        i+=1
        five5.config(text=temps[i])
        i+=1
        six6.config(text=temps[i])
        i+=1
        seven7.config(text=temps[i])
        i+=1
        eight8.config(text=temps[i])
        i+=1
        nine9.config(text=temps[i])
        i+=1
        ten0.config(text=temps[i])
        i+=1
        ten1.config(text=temps[i])
        i+=1
        ten2.config(text=temps[i])
        i+=1
        ten3.config(text=temps[i])
        i+=1
        ten4.config(text=temps[i])
        i+=1
        ten5.config(text=temps[i])
        i+=1
        ten6.config(text=temps[i])
        i+=1
        ten7.config(text=temps[i])
        i+=1
        ten8.config(text=temps[i])
        i+=1
        ten9.config(text=temps[i])
        i+=1
        two0.config(text=temps[i])
        i+=1
        two1.config(text=temps[i])
        i+=1
        two2.config(text=temps[i])
        i+=1
        two3.config(text=temps[i])

def changeColor(index):
    if index==0:
        sat.config(fg=back1)
        sun.config(fg=fore2)
        mon.config(fg=fore2)
        tue.config(fg=fore2)
        wen.config(fg=fore2)
        thur.config(fg=fore2)
        fri.config(fg=fore2)
    elif index==1:
        sat.config(fg=fore2)
        sun.config(fg=back1)
        mon.config(fg=fore2)
        tue.config(fg=fore2)
        wen.config(fg=fore2)
        thur.config(fg=fore2)
        fri.config(fg=fore2)
    elif index==2:
        sat.config(fg=fore2)
        sun.config(fg=fore2)
        mon.config(fg=back1)
        tue.config(fg=fore2)
        wen.config(fg=fore2)
        thur.config(fg=fore2)
        fri.config(fg=fore2)
    elif index==3:
        sat.config(fg=fore2)
        sun.config(fg=fore2)
        mon.config(fg=fore2)
        tue.config(fg=back1)
        wen.config(fg=fore2)
        thur.config(fg=fore2)
        fri.config(fg=fore2)
    elif index==4:
        sat.config(fg=fore2)
        sun.config(fg=fore2)
        mon.config(fg=fore2)
        tue.config(fg=fore2)
        wen.config(fg=back1)
        thur.config(fg=fore2)
        fri.config(fg=fore2)
    elif index==5:
        sat.config(fg=fore2)
        sun.config(fg=fore2)
        mon.config(fg=fore2)
        tue.config(fg=fore2)
        wen.config(fg=fore2)
        thur.config(fg=back1)
        fri.config(fg=fore2)
    elif index==6:
        sat.config(fg=fore2)
        sun.config(fg=fore2)
        mon.config(fg=fore2)
        tue.config(fg=fore2)
        wen.config(fg=fore2)
        thur.config(fg=fore2)
        fri.config(fg=back1)

#---- days
days=Frame(root, bg=fore)
days.place(x=0, y=360, width=500, height=30)
sat=Button(days, bg=fore, fg=fore2, text="SAT", border=0,command=isSat)
sat.pack(side="left", padx=5)
sun=Button(days, bg=fore, fg=fore2, text="SUN", border=0,command=isSun)
sun.pack(side="left", padx=7)
mon=Button(days, bg=fore, fg=fore2, text="MON", border=0,command=isMon)
mon.pack(side="left", padx=7)
tue=Button(days, bg=fore, fg=fore2, text="TUE", border=0,command=isTue)
tue.pack(side="left", padx=7)
wen=Button(days, bg=fore, fg=fore2, text="WEN", border=0,command=isWed)
wen.pack(side="left", padx=7)
thur=Button(days, bg=fore, fg=fore2, text="THU", border=0,command=isThur)
thur.pack(side="left", padx=7)
fri=Button(days, bg=fore, fg=fore2, text="FRI", border=0,command=isFri)
fri.pack(side="left", padx=7)

changeColor(index)
          
root.mainloop()