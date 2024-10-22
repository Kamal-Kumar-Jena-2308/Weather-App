from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
tk=Tk()
locati=StringVar()
time1=StringVar()
temp1=StringVar()
dayni1=StringVar()
wndi=StringVar()
humidi=StringVar()
feels=StringVar()
type=StringVar()
def weather(key):
    global time2,locati,temp,dayni,type1,winds,humid,feelsl
    locat=locati.get()
    try:
        url=f"http://api.weatherapi.com/v1/current.json?key={key}&q={locat}"
        a=requests.get(url)
        json1=json.loads(a.text)
        time1.set(json1['current']['last_updated'])
        temp1.set(str(json1['current']['temp_c'])+'°C')
        if json1['current']['is_day'] == '0':
            dayni1.set('Day')
        else:
            dayni1.set('Night')
        type.set(json1['current']['condition']['text'])
        wndi.set(str(json1['current']['wind_kph'])+' Km/h')
        humidi.set(str(json1['current']['humidity'])+'%')
        feels.set(str(json1['current']['feelslike_c'])+'°C')
    except Exception as e:
        # print(type(e))
        if str(e)=='\'current\'':
            messagebox.showinfo(title='Location Error',message='The Entered Location Was Not Found!')
        else:
            messagebox.showinfo(title='Location Error',message='Cannot Connect to the Internet!\nTry Again!')

key='30b969c9133b49b9992183354230302' # Enter your API key here
loac=Entry(textvariable=locati,width=33,font="Comicsansms 15 bold").place_configure(height=28,x=155,y=50)
tk.geometry("600x600")
tk.config(background="black")
a=Label(text="Weather App",font="Arial 19 bold",foreground="White",background="black",borderwidth="5", relief=RAISED)
a.pack(pady=4)
a1=Label(text="Location", font="Comicsansms 9 bold").place(height=28,x=35,y=50)
b=Button(text='Go', command=lambda:[weather(key)]).place_configure(x=530,y=50,height=28)
a1=Label(text="Last Updated", font="Comicsansms 9 bold").place(height=28,x=35,y=400)
a2=Label(text="Temperature", font="Comicsansms 9 bold").place(height=28,x=35,y=150)
a3=Label(text="Day/Night", font="Comicsansms 9 bold").place(height=28,x=35,y=350)
a4=Label(text="Wind Speed", font="Comicsansms 9 bold").place(height=28,x=35,y=250)
a5=Label(text="Humidity", font="Comicsansms 9 bold").place(height=28,x=35,y=300)
a6=Label(text="Feels Like", font="Comicsansms 9 bold").place(height=28,x=35,y=200)
a7=Label(text="Weather", font="Comicsansms 9 bold").place(height=28,x=35,y=100)
time2=Entry(textvariable=time1,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=400)
temp=Entry(textvariable=temp1,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=150)
dayni=Entry(textvariable=dayni1,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=350)
winds=Entry(textvariable=wndi,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=250)
humid=Entry(textvariable=humidi,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=300)
feelsl=Entry(textvariable=feels,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=200)
type1=Entry(textvariable=type,font="Comicsansms 15 bold",width=33,state=DISABLED).place_configure(height=28,x=155,y=100)
tk.resizable(False,False)
z1=Label(text='Made By - Kamal Kumar Jena',font="Arial 19 bold",foreground="Yellow",background="black",borderwidth="5", relief=RAISED).place(x=50,y=500)
tk.title("Weather App - By Kamal Kumar Jena")
img=Image.open('img.jpg')
img=img.resize((80,80), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
z=Label(image=img).place(x=450,y=480)
tk.mainloop()