from tkinter import*
from PIL import ImageTk,Image
home=Tk()
home.title("Cab Booking")
home.geometry("2010x2000")
def search():
      pass
def find():
    from geopy.geocoders import Nominatim
    from geopy import distance
    print(pickup_entry.get())
    print(drop_entry.get())
    geocode = Nominatim(user_agent="I know")
    l1 = pickup_entry.get()
    l2 = drop_entry.get()
    c1 = geocode.geocode(l1)
    c2 = geocode.geocode(l2)
    lat1, lon1 = c1.latitude, c1.longitude
    lat2, lon2 = c2.latitude, c2.longitude
    place1 = (lat1, lon1)
    place2 = (lat2, lon2)
    dis = distance.distance(place1, place2)
    Distance1 = Label(home, text="Distance :", fg="red", font=("cambria", 30, "bold")).place(x=600, y=565)
    des=IntVar()
    des.set(dis)
    dis_entry1 = Entry(home, textvariable=des, bg="white", bd=7, font=("canbria", 15, "bold")).place(x=800, y=570,width=200,height=50)
    km=Label(home,text="Km",fg="red",font=("cambria",30,"bold")).place(x=1000,y=565)

#Scroll bar
scroll_bar=Scrollbar(home).pack(side=RIGHT,fill=Y)

#Frames
upper_frame=Frame(home,bg="#2a0096").place(x=0,y=0,width=2010,height=365)
search_frame=Frame(home,bg="white",bd=1,relief=RAISED).place(x=150,y=120,width=1000,height=200)
pages_frame=Frame(home,bg="white",bd=4,relief=SUNKEN).place(x=250,y=40,width=800,height=95)
#distance_frame=Frame(home,bg="white",bd=5,relief=SUNKEN).place()
#Images
home_image=ImageTk.PhotoImage(Image.open("home (1).png").resize((50,50)))
cab_image=ImageTk.PhotoImage(Image.open("taxi.png").resize((66,66)))
contact_image=ImageTk.PhotoImage(Image.open("contact.png").resize((50,50)))
about_image=ImageTk.PhotoImage(Image.open("about.png").resize((50,50)))
login_image=ImageTk.PhotoImage(Image.open("key.png").resize((50,50)))
arrow_image=ImageTk.PhotoImage(Image.open("right-arrow.png").resize((50,50)))
taxi_image=ImageTk.PhotoImage(Image.open("route.png").resize((250,250)))
#Button
home_button=Button(home,image=home_image,bg="white",bd=0).place(x=390,y=55)
cab_button=Button(home,image=cab_image,bg="white",bd=0).place(x=505,y=49)
contact_button=Button(home,image=contact_image,bg="white",bd=0).place(x=638,y=55)
about_button=Button(home,image=about_image,bg="white",bd=0).place(x=738,y=55)
login_button=Button(home,image=login_image,bg="white",bd=0).place(x=850,y=55)
search_button=Button(home,text="Search",bg="red",bd=5,font=("cambria",16,"bold"),fg="white",command=search).place(x=560,y=322,width=100,height=40)
distance_search=Button(home,text="Find",bg="red",bd=5,font=("cambria",16,"bold"),fg="white",command=find).place(x=1100,y=500,width=100,height=48)
#Labels
home_label=Label(home,text="Home",bg="white",font=("cambria",10,"bold")).place(x=395,y=110)
cab_label=Label(home,text="Cab booking",bg="white",font=("cambria",10,"bold")).place(x=500,y=110)
contact_label=Label(home,text="Contact us",bg="white",font=("cambria",10,"bold")).place(x=625,y=110)
about_label=Label(home,text="About us",bg="white",font=("cambria",10,"bold")).place(x=735,y=110)
login_label=Label(home,text="Login/Sign up",bg="white",font=("cambria",10,"bold")).place(x=835,y=110)
arrow_button=Label(home,image=arrow_image,bg="white",bd=0).place(x=585,y=210)
taxi_label=Label(home,image=taxi_image,bd=0).place(x=200,y=370)
From_label=Label(home,text="From :",font=("canbria",25,"bold"),fg="red").place(x=550,y=500)
to_label=Label(home,text="To :",font=("canbria",25,"bold"),fg="red").place(x=850,y=500)

# text for cab search
from_search=Label(home,text="Enter pickup location",font=("cambria",25,"bold"),bg="white",bd=0).place(x=200,y=150)
to_search=Label(home,text="Enter destination ",font=("cambria",25,"bold"),bg="white",bd=0).place(x=750,y=150)
distance=Label(home,text="Here you can find \ndistance between your journey",fg="black",font=("cambria",30,"bold")).place(x=600,y=380)
#enrty widgets
from_entry=StringVar()
to_entry=StringVar()
pickup_entry=StringVar()
drop_entry=StringVar()
from_entry1=Entry(home,textvariable=from_entry,bg="white",bd=7).place(x=260,y=215,width=220,height=50)
to_entry1=Entry(home,textvariable=to_entry,bg="white",bd=7).place(x=760,y=215,width=220,height=50)
pickup_entry1=Entry(home,textvariable=pickup_entry,bg="white",bd=7,font=("canbria",15,"bold")).place(x=670,y=500,width=160,height=50)
drop_entry1=Entry(home,textvariable=drop_entry,bg="white",bd=7,font=("canbria",15,"bold")).place(x=930,y=500,width=160,height=50)
menu=Menu(home)
home.config(menu=menu)
bar=Menu(menu,tearoff=0)
menu.add_cascade(label="bar",menu=bar)
bar.add_command(label="hi")

home.mainloop()