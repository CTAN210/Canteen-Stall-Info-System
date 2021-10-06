from tkinter import *
from tkinter import ttk
from datetime import *
from PIL import ImageTk
from PIL import Image
import pandas as pd
from textwrap import *
from time import strftime
import datetime as t
import time
from tkcalendar import Calendar




 
###current time

class date_time:

    def display_time():

        global current_time, d  
        current_time = strftime('%I:%M:%S %p, %Y-%m-%d')   #hour(12hr time):minute:seconds:am/pm
        clock_label.config(text = current_time)
        clock_label.after(1000,date_time.display_time) #updates every 1000 milliseconds/1 second

        try:
               d = d1 #checks if user inputted date exist, if so set to user day
        except:       
               c = datetime.strptime(current_time, '%I:%M:%S %p, %Y-%m-%d')
               d = c.weekday() #else, checks current day of week 
        
    def get_date():

 
        #get code and break it to readable dates
              global date_label, button_date, d1, b, c, time_ampm_str

              try:

                     time_hour_str = cb_hour.get() #gets values of day, ..., from combobox in date_selection function
                     time_minute_str = cb_minute.get()
                     time_ampm_str = cb_ampm.get()
                     cal_date = str(cal.selection_get())

                     
                     a = time_hour_str + ":" + time_minute_str + ":00", time_ampm_str +",", cal_date #concatenates all info

                     b = ' '.join(a) #saves it in readable computer format

                     c = datetime.strptime(b, '%I:%M:%S %p, %Y-%m-%d')
                     d1 = c.weekday() #extracts day of week and stores it in d1
                     print(d1)
                     homepage.label_checktime()



                     try:
                         date_label.destroy() #checks for original user_set date and destroy it
                         
                         date_label = Label(homepage1, text = str(b), font= "helvetica 20 bold", bg= "lightsteelblue4", fg= "black")
                         date_label.place(relx=0.76,rely=0.032,anchor='center') #create a label for new user set date

                     except:

                         date_label = Label(homepage1, text = str(b), font= "helvetica 20 bold", bg= "lightsteelblue4", fg= "black")
                         date_label.place(relx=0.76,rely=0.032,anchor='center') #if first time setting date, create a label

                     dateselect.destroy()
              except:
                      
                     time.sleep(0.5)
              
               
    def clear_date():
       global d,b, d1, c
       
       try:
                date_label.destroy()

                del b
                del d1
                del c
                homepage.label_checktime()
                  
       except:
                pass


    #date selection widget
    def date_selection():
        global dateselect #allow for destruction
        global cal, cb_hour, cb_minute, cb_ampm
        global button_date

        date_geometry = '300x280+'+str(homepage1.winfo_rootx())+'+'+str(homepage1.winfo_rooty()-23)

        try:  
            dateselect.deiconify()  
        except:  
            dateselect = Tk()
            
        dateselect.lift()
        
        dateselect.title("Select Date")
        
        dateselect.configure(background="lightsteelblue4")
        dateselect.geometry(date_geometry)
        dateselect.resizable(width=False, height=False)

        Label(dateselect, text="Please select a time (hr/min) and date" ,fg="black",bg="lightsteelblue4",font="Helvetica 15 bold").place(relx=0,rely=0)
    

        hour = ("01","02","03","04","05","06","07","08","09","10","11","12")
        cb_hour = ttk.Combobox(dateselect,values = hour, width=2, state="readonly")
        cb_hour.place (relx = 0.05, rely= 0.1)

        minute = ("00","05","10","15","20","25","30","35","40","45","50","55")
        cb_minute = ttk.Combobox(dateselect,values = minute, width=2, state="readonly")
        cb_minute.place (relx = 0.2, rely= 0.1)
        
        ampm = ("PM","AM")
        cb_ampm = ttk.Combobox(dateselect,values = ampm, width=2,state="readonly")
        cb_ampm.place (relx = 0.35, rely= 0.1)

        year = int(strftime('%Y')) #captures the current date to display on tkinter calendar
        month = int(strftime('%m'))
        day = int(strftime('%d'))

        cal = Calendar(dateselect,font="Helvetica 14", selectmode='day',cursor="hand2", year=year, month=month, day=day, )
        cal.place(relx = 0.5, rely = 0.6,anchor='center')



        button_date = Button(dateselect, text = "Enter",height=2, width=10,command=date_time.get_date)
        button_date.place (relx = 0.8, rely = 0.15,anchor='center')
  

        
  
#return back to homepage (western)


#indian stall

class indian:

    def __init__(self):
        pass

    def open_indian():
        global current_geometry,homepage1 #defines global
        current_geometry = '600x800+'+str(homepage1.winfo_rootx())+'+'+str(homepage1.winfo_rooty()-23) #rechecks position of current window
        homepage1.destroy()
        indian.open_menu()    #calls class open menu function

    def back(): #back button returns to homepage
        global current_geometry #defines global
        current_geometry = '600x800+'+str(indian1.winfo_rootx())+'+'+str(indian1.winfo_rooty()-23) #rechecks position of current window
        indian1.destroy()
        homepage.open_menu()    #calls class open menu function

    def queue_time():
        global queuetime #allow for destruction
        global cb_length
        global button_length

        date_geometry = '200x70+'+str(indian1.winfo_rootx()+300)+'+'+str(indian1.winfo_rooty()+113)

        try:  
            queuetime.deiconify()  
        except:  
            queuetime = Tk()
            
        queuetime.lift()
        
        queuetime.title("Select No. of People")
        
        queuetime.configure(background="lightsteelblue4")
        queuetime.geometry(date_geometry)
        queuetime.resizable(width=False, height=False)
        
        length = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")
        cb_length = ttk.Combobox(queuetime, values = length, width = 2)
        cb_length.place (relx = 0.2, rely = 0.3,anchor='center')


        button_length = Button(queuetime, text = "Enter",height=2, width=12,command=indian.get_length)
        button_length.place (relx = 0.65, rely = 0.35,anchor='center')

        
    def get_length():

        time_length_str = cb_length.get()
        print(time_length_str)

        expected_time = int(time_length_str) * 2.5
        expected_time_str = "Expected waiting time: "+str(expected_time) +" min"

        time = Label(queuetime, text=expected_time_str,fg="black",bg="lightsteelblue4",font="Helvetica 12 bold")
        time.place(relx=0.5,rely=0.8,anchor='center')
        
    def open_menu(): #generates the whole menu
        
        global indian1, wallpaper, clock_label
 
        indian1 = Tk()
        indian1.title("Indian")
        indian1.configure(background="lightsteelblue4")
        indian1.geometry(current_geometry) #creates window at position of homepage
        indian1.resizable(width=False, height=False)
        
        df_indian = pd.read_excel ('Indian_Stall.xlsx').to_dict()
        
        print (df_indian)

        count=1

        Label(indian1, text="Indian Delicacies",fg="white",bg="lightsteelblue4",font="Times 37 bold").grid(row=count,column=1,columnspan=20)

        count+=1
        Label(indian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        
        count+=1
        Label(indian1, text="  Menu",fg="white",bg="lightsteelblue4",font="Times 25 bold").grid(row=count,column=1,sticky=W)
        Button(indian1, text="Waiting Time",fg="black",bg="lightsteelblue4",font="Times 25 bold",command=indian.queue_time).grid(row=count,column=5,sticky=W)
        count+=1

        Label(indian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        count_left,count_right = count,count


        #left
        for i in range(len(df_indian['Food'])):
            
            try:
                Label(indian1, text=df_indian['Food'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_left,column=1,sticky=W)
                Label(indian1, text=df_indian['Price'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_left,column=3,sticky=W)

                count_left+=1  

                characters_indian_description = 0
                
                while len(str(df_indian['Description'][i])) > characters_indian_description:

                    for line in wrap(str(df_indian['Description'][i]), width=40, break_long_words=False):
                                
                        Label(indian1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_left,column=1,columnspan=3,sticky=W)
                        characters_indian_description += 40
                        
                        count_left +=1
            
            except:
                print("NIL")


        #right

        for i in range(len(df_indian['Food'])):
            
            try:
                Label(indian1, text=df_indian['Food2'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_right,column=5,sticky=W)
                Label(indian1, text=df_indian['Price2'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_right,column=8,sticky=E)

                count_right+=1  

                characters_indian_description = 0
                
                while len(str(df_indian['Description2'][i])) > characters_indian_description:

                    for line in wrap(str(df_indian['Description2'][i]), width=40, break_long_words=False):
                                
                        Label(indian1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_right,column=5,columnspan=3,sticky=W)
                        characters_indian_description += 40
                        
                        count_right +=1
            
            except:
                print("NIL")

        #  set row (count) to largest row (either left or right)         
        
        if count_left>=count_right:
            count = count_left
        else:
            count = count_right


        for i in range(10,count-5):
            Label(indian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=4)
            Label(indian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=2)
            Label(indian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=6)
          
        Label(indian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        Button(indian1, text="Back", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=indian.back).grid(row=count,column=5)


class vegetarian:

    def __init__(self):
        pass

    def open_vegetarian():
        global current_geometry,homepage1 #defines global
        current_geometry = '600x800+'+str(homepage1.winfo_rootx())+'+'+str(homepage1.winfo_rooty()-23) #rechecks position of current window
        homepage1.destroy()
        vegetarian.open_menu()    #calls class open menu function

    def back(): #back button returns to homepage
        global current_geometry #defines global
        current_geometry = '600x800+'+str(vegetarian1.winfo_rootx())+'+'+str(vegetarian1.winfo_rooty()-23) #rechecks position of current window
        vegetarian1.destroy()
        homepage.open_menu()    #calls class open menu function

    def queue_time():
        global queuetime #allow for destruction
        global cb_length
        global button_length

        date_geometry = '200x70+'+str(vegetarian1.winfo_rootx()+300)+'+'+str(vegetarian1.winfo_rooty()+113)

        try:  
            queuetime.deiconify()  
        except:  
            queuetime = Tk()
            
        queuetime.lift()
        
        queuetime.title("Select No. of People")
        
        queuetime.configure(background="lightsteelblue4")
        queuetime.geometry(date_geometry)
        queuetime.resizable(width=False, height=False)
        
        length = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")
        cb_length = ttk.Combobox(queuetime, values = length, width = 2)
        cb_length.place (relx = 0.2, rely = 0.3,anchor='center')


        button_length = Button(queuetime, text = "Enter",height=2, width=12,command=vegetarian.get_length)
        button_length.place (relx = 0.65, rely = 0.35,anchor='center')

        
    def get_length():

        time_length_str = cb_length.get()
        print(time_length_str)

        expected_time = int(time_length_str) * 2.5
        expected_time_str = "Expected waiting time: "+str(expected_time) +" min"

        time = Label(queuetime, text=expected_time_str,fg="black",bg="lightsteelblue4",font="Helvetica 12 bold")
        time.place(relx=0.5,rely=0.8,anchor='center')
        
    def open_menu(): #generates the whole menu
        
        global vegetarian1, wallpaper, clock_label
 
        vegetarian1 = Tk()
        vegetarian1.title("Vegetarian")
        vegetarian1.configure(background="lightsteelblue4")
        vegetarian1.geometry(current_geometry) #creates window at position of homepage
        vegetarian1.resizable(width=False, height=False)
        
        df_vegetarian = pd.read_excel ('vegetarian.xlsx').to_dict()
        
        print (df_vegetarian)

        count=1

        Label(vegetarian1, text="Vegetarian Delights",fg="white",bg="lightsteelblue4",font="Times 37 bold").grid(row=count,column=1,columnspan=20)

        count+=1
        Label(vegetarian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        
        count+=1
        Label(vegetarian1, text="  Menu",fg="white",bg="lightsteelblue4",font="Times 25 bold").grid(row=count,column=1,sticky=W)
        Button(vegetarian1, text="Waiting Time",fg="black",bg="lightsteelblue4",font="Times 25 bold",command=vegetarian.queue_time).grid(row=count,column=5,sticky=W)
        count+=1

        Label(vegetarian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        count_left,count_right = count,count


        #left
        for i in range(len(df_vegetarian['Food'])):
            
            try:
                Label(vegetarian1, text=df_vegetarian['Food'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_left,column=1,sticky=W)
                Label(vegetarian1, text=df_vegetarian['Price'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_left,column=3,sticky=W)

                count_left+=1  

                characters_vegetarian_description = 0
                
                while len(str(df_vegetarian['Description'][i])) > characters_vegetarian_description:

                    for line in wrap(str(df_vegetarian['Description'][i]), width=40, break_long_words=False):
                                
                        Label(vegetarian1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_left,column=1,columnspan=3,sticky=W)
                        characters_vegetarian_description += 40
                        
                        count_left +=1
            
            except:
                print("NIL")


        #right

        for i in range(len(df_vegetarian['Food'])):
            
            try:
                Label(vegetarian1, text=df_vegetarian['Food2'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_right,column=5,sticky=W)
                Label(vegetarian1, text=df_vegetarian['Price2'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_right,column=8,sticky=E)

                count_right+=1  

                characters_vegetarian_description = 0
                
                while len(str(df_vegetarian['Description2'][i])) > characters_vegetarian_description:

                    for line in wrap(str(df_vegetarian['Description2'][i]), width=40, break_long_words=False):
                                
                        Label(vegetarian1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_right,column=5,columnspan=3,sticky=W)
                        characters_vegetarian_description += 40
                        
                        count_right +=1
            
            except:
                print("NIL")

        #  set row (count) to largest row (either left or right)         
        
        if count_left>=count_right:
            count = count_left
        else:
            count = count_right


        for i in range(10,count-5):
            Label(vegetarian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=4)
            Label(vegetarian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=2)
            Label(vegetarian1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=6)
          
        Label(vegetarian1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        Button(vegetarian1, text="Back", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=vegetarian.back).grid(row=count,column=5)
                            
                            

class miniwok:

    def __init__(self):
        pass

    def open_miniwok():
        global current_geometry,homepage1 #defines global
        current_geometry = '600x800+'+str(homepage1.winfo_rootx())+'+'+str(homepage1.winfo_rooty()-23) #rechecks position of current window
        homepage1.destroy()
        miniwok.open_menu()    #calls class open menu function

    def back(): #back button returns to homepage
        global current_geometry #defines global
        current_geometry = '600x800+'+str(miniwok1.winfo_rootx())+'+'+str(miniwok1.winfo_rooty()-23) #rechecks position of current window
        miniwok1.destroy()
        homepage.open_menu()    #calls class open menu function

    def queue_time():
        global queuetime #allow for destruction
        global cb_length
        global button_length

        date_geometry = '200x70+'+str(miniwok1.winfo_rootx()+300)+'+'+str(indian1.winfo_rooty()+113)

        try:  
            queuetime.deiconify()  
        except:  
            queuetime = Tk()
            
        queuetime.lift()
        
        queuetime.title("Select No. of People")
        
        queuetime.configure(background="lightsteelblue4")
        queuetime.geometry(date_geometry)
        queuetime.resizable(width=False, height=False)
        
        length = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")
        cb_length = ttk.Combobox(queuetime, values = length, width = 2)
        cb_length.place (relx = 0.2, rely = 0.3,anchor='center')


        button_length = Button(queuetime, text = "Enter",height=2, width=12,command=indian.get_length)
        button_length.place (relx = 0.65, rely = 0.35,anchor='center')

        
    def get_length():

        time_length_str = cb_length.get()
        print(time_length_str)

        expected_time = int(time_length_str) * 2.5
        expected_time_str = "Expected waiting time: "+str(expected_time) +" min"

        time = Label(queuetime, text=expected_time_str,fg="black",bg="lightsteelblue4",font="Helvetica 12 bold")
        time.place(relx=0.5,rely=0.8,anchor='center')
        
    def open_menu(): #generates the whole menu
        
        global miniwok1, wallpaper, clock_label
 
        miniwok1 = Tk()
        miniwok1.title("Mini Wok")
        miniwok1.configure(background="lightsteelblue4")
        miniwok1.geometry(current_geometry) #creates window at position of homepage
        miniwok1.resizable(width=False, height=False)
        
        df_miniwok = pd.read_excel ('Miniwok.xlsx').to_dict()
        
        print (df_miniwok)

        count=1

        Label(miniwok1, text="Mini Wok",fg="white",bg="lightsteelblue4",font="Times 37 bold").grid(row=count,column=1,columnspan=20)

        count+=1
        Label(miniwok1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        
        count+=1
        Label(miniwok1, text="  Menu",fg="white",bg="lightsteelblue4",font="Times 25 bold").grid(row=count,column=1,sticky=W)
        Button(miniwok1, text="Waiting Time",fg="black",bg="lightsteelblue4",font="Times 25 bold",command=miniwok.queue_time).grid(row=count,column=5,sticky=W)
        count+=1

        Label(miniwok1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        count_left,count_right = count,count


        #left
        for i in range(len(df_miniwok['Food'])):
            
            try:
                Label(miniwok1, text=df_miniwok['Food'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_left,column=1,sticky=W)
                Label(miniwok1, text=df_miniwok['Price'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_left,column=3,sticky=W)

                count_left+=1  

                characters_miniwok_description = 0
                
                while len(str(df_miniwok['Description'][i])) > characters_miniwok_description:

                    for line in wrap(str(df_miniwok['Description'][i]), width=40, break_long_words=False):
                                
                        Label(miniwok1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_left,column=1,columnspan=3,sticky=W)
                        characters_miniwok_description += 40
                        
                        count_left +=1
            
            except:
                print("NIL")


        #right

        for i in range(len(df_miniwok['Food'])):
            
            try:
                Label(miniwok1, text=df_miniwok['Food2'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_right,column=5,sticky=W)
                Label(miniwok1, text=df_miniwok['Price2'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_right,column=8,sticky=E)

                count_right+=1  

                characters_miniwok_description = 0
                
                while len(str(df_miniwok['Description2'][i])) > characters_miniwok_description:

                    for line in wrap(str(df_miniwok['Description2'][i]), width=40, break_long_words=False):
                                
                        Label(miniwok1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_right,column=5,columnspan=3,sticky=W)
                        characters_miniwok_description += 40
                        
                        count_right +=1
            
            except:
                print("NIL")

        #  set row (count) to largest row (either left or right)         
        
        if count_left>=count_right:
            count = count_left
        else:
            count = count_right


        for i in range(10,count-5):
            Label(miniwok1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=4)
            Label(miniwok1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=2)
            Label(miniwok1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=6)
          
        Label(miniwok1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        Button(miniwok1, text="Back", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=miniwok.back).grid(row=count,column=5)
                            




#western stall

class western:

    def __init__(self):
        pass


    def back(): #back button returns to homepage
        global current_geometry #defines global
        current_geometry = '600x800+'+str(western1.winfo_rootx())+'+'+str(western1.winfo_rooty()-23) #rechecks position of current window
        western1.destroy()
        homepage.open_menu()    #calls class open menu function

    def back2():
        global current_geometry #defines global
        current_geometry = '600x800+'+str(western2.winfo_rootx())+'+'+str(western2.winfo_rooty()-23) #rechecks position of current window
        western2.destroy()
        homepage.open_menu()    #calls class open menu function
        
    def previous():
        global current_geometry #defines global
        current_geometry = '600x800+'+str(western2.winfo_rootx())+'+'+str(western2.winfo_rooty()-23) #rechecks position of current window
        western2.destroy()
        western.open_menu()

    def queue_time():
        global queuetime #allow for destruction
        global cb_length
        global button_length

        date_geometry = '200x70+'+str(western1.winfo_rootx()+300)+'+'+str(western1.winfo_rooty()+113)

        try:  
            queuetime.deiconify()  
        except:  
            queuetime = Tk()
            
        queuetime.lift()
        
        queuetime.title("Select No. of People")
        
        queuetime.configure(background="lightsteelblue4")
        queuetime.geometry(date_geometry)
        queuetime.resizable(width=False, height=False)
        
        length = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")
        cb_length = ttk.Combobox(queuetime, values = length, width = 2)
        cb_length.place (relx = 0.2, rely = 0.3,anchor='center')


        button_length = Button(queuetime, text = "Enter",height=2, width=12,command=indian.get_length)
        button_length.place (relx = 0.65, rely = 0.35,anchor='center')

        
    def get_length():

        time_length_str = cb_length.get()
        print(time_length_str)

        expected_time = int(time_length_str) * 2
        expected_time_str = "Expected waiting time: "+str(expected_time) +" min"

        time = Label(queuetime, text=expected_time_str,fg="black",bg="lightsteelblue4",font="Helvetica 12 bold")
        time.place(relx=0.5,rely=0.8,anchor='center')    


    def open_western():
        global current_geometry,homepage1 #defines global
        current_geometry = '600x800+'+str(homepage1.winfo_rootx())+'+'+str(homepage1.winfo_rooty()-23) #rechecks position of current window
        homepage1.destroy()
        western.open_menu()    #calls class open menu function


    def special_menu():
           
        global current_geometry, western2 #defines global
        current_geometry = '600x800+'+str(western1.winfo_rootx())+'+'+str(western1.winfo_rooty()-23) #rechecks position of current window
        western1.destroy()


        western2 = Tk()
        western2.geometry(current_geometry) #creates window at position of homepage
        western2.resizable(width=False, height=False)
        western2.configure(background="lightsteelblue4")
        western2.title("Special Menu")


        df_western_special = pd.read_excel ('Western_Stall_Special.xlsx').to_dict()
        
        print (df_western_special)

        count=1

        Label(western2, text="SURF & TURF",fg="white",bg="lightsteelblue4",font="Times 37 bold").grid(row=count,column=1,columnspan=20)

        count+=1
        Label(western2, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        
        count+=1
        Label(western2, text=" Special Menu",fg="white",bg="lightsteelblue4",font="Times 25 bold").grid(row=count,column=1,sticky=W)
        count+=1

        Label(western2, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1


        count_left,count_right = count,count


        #left
        for i in range(len(df_western_special['Food'])):
               
            if d == df_western_special["Datepython"][i]:
                   
                   try:
                       Label(western2, text=df_western_special['Food'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_left,column=1,sticky=W)
                       Label(western2, text=df_western_special['Price'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_left,column=3,sticky=W)

                       count_left+=1  

                       characters_western_description = 0
                
                       while len(str(df_western_special['Description'][i])) > characters_western_description:

                           for line in wrap(str(df_western_special['Description'][i]), width=40, break_long_words=False):
                                
                               Label(western2, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_left,column=1,columnspan=3,sticky=W)
                               characters_western_description += 40
                        
                               count_left +=1
            
                   except:
                       print("NIL")


        #right
        for i in range(len(df_western_special['Food2'])):
               
               if d == df_western_special["Datepython2"][i]:
            
                     try:
                             Label(western2, text=df_western_special['Food2'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_right,column=5,sticky=W)
                             Label(western2, text=df_western_special['Price2'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_right,column=8,sticky=E)

                             count_right+=1  
       
                             characters_western_description = 0
                
                             while len(str(df_western_special['Description2'][i])) > characters_western_description:

                                  for line in wrap(str(df_western_special['Description2'][i]), width=40, break_long_words=False):
                                
                                      Label(western2, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_right,column=5,columnspan=3,sticky=W)
                                      characters_western_description += 40
                        
                                      count_right +=1
            
                     except:
                            print("NIL")

        #  set row (count) to largest row (either left or right)         
        
        if count_left>=count_right:
            count = count_left
        else:
            count = count_right


        for i in range(10,count-5):
            Label(western2, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=4)
            Label(western2, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=2)
            Label(western2, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=6)
          
        Label(western2, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        Button(western2, text="Back", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=western.back2).grid(row=count,column=5)
        Button(western2, text="Previous", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=western.previous).grid(row=count,column=1)

    
    def open_menu(): #generates the whole menu
        
        global western1, wallpaper, clock_label
 
        western1 = Tk()
        western1.title("Western")
        western1.configure(background="lightsteelblue4")
        western1.geometry(current_geometry) #creates window at position of homepage
        western1.resizable(width=False, height=False)
        
        df_western = pd.read_excel ('Western_Stall.xlsx').to_dict()
        
        print (df_western)

        count=1

        Label(western1, text="SURF & TURF",fg="white",bg="lightsteelblue4",font="Times 37 bold").grid(row=count,column=1,columnspan=20)

        count+=1
        Label(western1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        
        count+=1
        Label(western1, text="  Menu",fg="white",bg="lightsteelblue4",font="Times 25 bold").grid(row=count,column=1,sticky=W)
        Button(western1, text="Waiting Time",fg="black",bg="lightsteelblue4",font="Times 25 bold",command=western.queue_time).grid(row=count,column=5,sticky=W)
        count+=1

        Label(western1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        count_left,count_right = count,count


        #left
        for i in range(len(df_western['Food'])):
            
            try:
                Label(western1, text=df_western['Food'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_left,column=1,sticky=W)
                Label(western1, text=df_western['Price'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_left,column=3,sticky=W)

                count_left+=1  

                characters_western_description = 0
                
                while len(str(df_western['Description'][i])) > characters_western_description:

                    for line in wrap(str(df_western['Description'][i]), width=40, break_long_words=False):
                                
                        Label(western1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_left,column=1,columnspan=3,sticky=W)
                        characters_western_description += 40
                        
                        count_left +=1
            
            except:
                print("NIL")


        #right

        for i in range(len(df_western['Food'])):
            
            try:
                Label(western1, text=df_western['Food2'][i],fg="white",bg="lightsteelblue4",font="Times 20").grid(row=count_right,column=5,sticky=W)
                Label(western1, text=df_western['Price2'][i],fg="white",bg="lightsteelblue4",font="Times 15").grid(row=count_right,column=8,sticky=E)

                count_right+=1  

                characters_western_description = 0
                
                while len(str(df_western['Description2'][i])) > characters_western_description:

                    for line in wrap(str(df_western['Description2'][i]), width=40, break_long_words=False):
                                
                        Label(western1, text=line,fg="white",bg="lightsteelblue4",font="none 10 italic").grid(row=count_right,column=5,columnspan=3,sticky=W)
                        characters_western_description += 40
                        
                        count_right +=1
            
            except:
                print("NIL")

        #  set row (count) to largest row (either left or right)         
        
        if count_left>=count_right:
            count = count_left
        else:
            count = count_right


        for i in range(10,count-5):
            Label(western1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=4)
            Label(western1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=2)
            Label(western1, text=" "*15,fg="white",bg="lightsteelblue4",font="Times 5").grid(row=i+4,column=6)
          
        Label(western1, text="_"*100,bg="lightsteelblue4",fg="white").grid(row=count,columnspan=10)
        count+=1

        Button(western1, text="Back", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=western.back).grid(row=count,column=5)
        Button(western1, text="Specials", bg="black",fg="black", height=2, width=10,font="helvetica 30 normal", command=western.special_menu).grid(row=count,column=1)
                            
#drinks stall

class drinks:

    def __init__(self):
        pass

    def open_drinks():
        global current_geometry, homepage1  # defines global
        current_geometry = '600x800+' + str(homepage1.winfo_rootx()) + '+' + str(
            homepage1.winfo_rooty() - 23)  # rechecks position of current window
        homepage1.destroy()
        drinks.open_menu()  # calls class open menu function

    def back():  # back button returns to homepage
        global current_geometry  # defines global
        current_geometry = '600x800+' + str(drinks1.winfo_rootx()) + '+' + str(drinks1.winfo_rooty() - 23)  # rechecks position of current window
        drinks1.destroy()
        homepage.open_menu()  # calls class open menu function

    def check_time():
        global morning, normal_time
        morning = False
        normal_time = True
        if c.hour >= 8 and time_ampm_str == 'AM':
            morning = True
            normal_time = False
        else:
            morning = False
            normal_time = True

    def check_current_time():
        global morning, normal_time
        morning = False
        normal_time = True
        current_datetime = datetime.strptime(current_time, '%I:%M:%S %p, %Y-%m-%d')
        if 8<=current_datetime.hour<12:
            morning = True
            normal_time = False
        else:
            morning = False
            normal_time = True




    def queue_time():
        global queuetime  # allow for destruction
        global cb_length
        global button_length

        date_geometry = '200x70+' + str(drinks1.winfo_rootx() + 300) + '+' + str(drinks1.winfo_rooty() + 113)

        try:
            queuetime.deiconify()
        except:
            queuetime = Tk()

        queuetime.lift()

        queuetime.title("Select No. of People")

        queuetime.configure(background="lightsteelblue4")
        queuetime.geometry(date_geometry)
        queuetime.resizable(width=False, height=False)

        length = (
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
        cb_length = ttk.Combobox(queuetime, values=length, width=2)
        cb_length.place(relx=0.2, rely=0.3, anchor='center')

        button_length = Button(queuetime, text="Enter", height=2, width=12, command=drinks.get_length)
        button_length.place(relx=0.65, rely=0.35, anchor='center')

    def get_length():

        time_length_str = cb_length.get()
        print(time_length_str)

        expected_time = int(time_length_str) * 2.5
        expected_time_str = "Expected waiting time: " + str(expected_time) + " min"

        time = Label(queuetime, text=expected_time_str, fg="black", bg="lightsteelblue4", font="Helvetica 12 bold")
        time.place(relx=0.5, rely=0.8, anchor='center')

    def open_menu_real():
        if morning == True and normal_time == False:
            df_drinks = pd.read_excel('Drinks_stall_morning.xlsx').to_dict()
        elif morning == False and normal_time == True:
            df_drinks = pd.read_excel('Drinks_stall_normal.xlsx').to_dict()

        print(df_drinks)

        count = 1
        if morning == True and normal_time == False:
            Label(drinks1, text="Drinks Stall (Breakfast)", fg="white", bg="lightsteelblue4", font="Times 37 bold").grid(row=count, column=1,columnspan=20)
        elif morning == False and normal_time == True:
            Label(drinks1, text="Drinks Stall", fg="white", bg="lightsteelblue4",font="Times 37 bold").grid(row=count, column=1,columnspan=20)
        count += 1
        Label(drinks1, text="_" * 100, bg="lightsteelblue4", fg="white").grid(row=count, columnspan=10)

        count += 1
        Label(drinks1, text="  Menu", fg="white", bg="lightsteelblue4", font="Times 25 bold").grid(row=count, column=1,
                                                                                                   sticky=W)
        Button(drinks1, text="Waiting Time", fg="black", bg="lightsteelblue4", font="Times 25 bold",
               command=drinks.queue_time).grid(row=count, column=5, sticky=W)

        count += 1

        Label(drinks1, text="_" * 100, bg="lightsteelblue4", fg="white").grid(row=count, columnspan=10)
        count += 1

        count_left, count_right = count, count

        # left
        for i in range(len(df_drinks['Food'])):

            try:
                Label(drinks1, text=df_drinks['Food'][i], fg="white", bg="lightsteelblue4", font="Times 20").grid(
                    row=count_left, column=1, sticky=W)
                Label(drinks1, text=df_drinks['Price'][i], fg="white", bg="lightsteelblue4", font="Times 15").grid(
                    row=count_left, column=3, sticky=W)

                count_left += 1

                characters_drinks_description = 0

                while len(str(df_drinks['Description'][i])) > characters_indian_description:

                    for line in wrap(str(df_drinks['Description'][i]), width=40, break_long_words=False):
                        Label(drinks1, text=line, fg="white", bg="lightsteelblue4", font="none 10 italic").grid(
                            row=count_left, column=1, columnspan=3, sticky=W)
                        characters_drinks_description += 40

                        count_left += 1
            except:
                print("NIL")

            # right

        for i in range(len(df_drinks['Food'])):

            try:
                Label(drinks1, text=df_drinks['Food2'][i], fg="white", bg="lightsteelblue4", font="Times 20").grid(
                    row=count_right, column=5, sticky=W)
                Label(drinks1, text=df_drinks['Price2'][i], fg="white", bg="lightsteelblue4", font="Times 15").grid(
                    row=count_right, column=8, sticky=E)

                count_right += 1

                characters_drinks_description = 0

                while len(str(df_drinks['Description2'][i])) > characters_drinks_description:

                    for line in wrap(str(df_drinks['Description2'][i]), width=40, break_long_words=False):
                        Label(drinks1, text=line, fg="white", bg="lightsteelblue4", font="none 10 italic").grid(
                            row=count_right, column=5, columnspan=3, sticky=W)
                        characters_drinks_description += 40

                        count_right += 1

            except:
                print("NIL")

            #  set row (count) to largest row (either left or right)

        if count_left >= count_right:
            count = count_left
        else:
            count = count_right

        for i in range(10, count - 5):
            Label(drinks1, text=" " * 15, fg="white", bg="lightsteelblue4", font="Times 5").grid(row=i + 4,
                                                                                                 column=4)
            Label(drinks1, text=" " * 15, fg="white", bg="lightsteelblue4", font="Times 5").grid(row=i + 4,
                                                                                                 column=2)
            Label(drinks1, text=" " * 15, fg="white", bg="lightsteelblue4", font="Times 5").grid(row=i + 4,
                                                                                                 column=6)

        Label(drinks1, text="_" * 100, bg="lightsteelblue4", fg="white").grid(row=count, columnspan=10)
        count += 1

        Button(drinks1, text="Back", bg="black", fg="black", height=2, width=10, font="helvetica 30 normal",
               command=drinks.back).grid(row=count, column=5)

    def open_menu():  # generates the whole menu

        global drinks1, wallpaper, clock_label

        drinks1 = Tk()
        drinks1.title("Drinks Stall")
        drinks1.configure(background="lightsteelblue4")
        drinks1.geometry(current_geometry)  # creates window at position of homepage
        drinks1.resizable(width=False, height=False)
        try:
            if b != current_time:
                drinks.check_time()
                drinks.open_menu_real()

        except:
            NameError
            drinks.check_current_time()
            drinks.open_menu_real()





#main homepage
class homepage:

    def __init__(self):
        pass
    
    def label_checktime():
        try:
            print(c.hour)
            print(d1)
            if d1 == 5 or d1 == 6:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("closed1")
            elif 8<= c.hour< 20:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("open1")
            else:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("closed2")

        except:
            now = t.datetime.today()
            if now.weekday() == 5 or now.weekday() == 6:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("closed3")
            elif 8 <= now.hour <= 20:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("open2")
            else:
                label = Label(homepage1, image=directory1, borderwidth=0, highlightthickness=0, padx=0, pady=0)
                label.place(relx=0.5, rely=0.25, anchor='center')
                print("closed4")

    def open_menu():

        # define global variables for destroying and creating
        # define for access to relative x,y positions
        global homepage1, clock_label, date_label

        
        homepage1 = Tk()
        homepage1.geometry(current_geometry)
        homepage1.title("Northspine Foodcourt Directory")
        homepage1.configure(background="gray25")
        homepage1.resizable(width=False, height=False)

                                
        #defining global images (prevent garbage collection)
        global western1, drinks1,miniwok1,indian1,economicrice1,vegetarian1,wallpaper1,directory1, directory2

        wallpaper1 = PhotoImage(file="wallpaper.png")

        directory1 = PhotoImage(file="directory.png")
        directory2 = PhotoImage(file= "directory2.png")

        current_time = strftime('%I:%M:%S')  # create a variable called current_time first

        homepage.label_checktime()

        clock_label = Label(homepage1, text = current_time, font= "helvetica 20 bold", bg= "lightsteelblue4", fg= "black")
        clock_label.place(relx=0.76,rely=0.032,anchor='center')    
        date_time.display_time()

        try:
               date_label = Label(homepage1, text = str(b), font= "helvetica 20 bold", bg= "lightsteelblue4", fg= "black")
               date_label.place(relx=0.76,rely=0.032,anchor='center')
        except:
               pass

        date_picker = Button(homepage1, text = "Choose Date", font = "helvetica 20 bold", bg= "lightsteelblue4", command=date_time.date_selection).place(relx=0.15,rely=0.032,anchor='center')
        date_clearer = Button(homepage1, text = "Clear", font = "helvetica 20 bold",bg= "lightsteelblue4", command=date_time.clear_date).place(relx=0.35,rely=0.032,anchor='center')
        
        Label(homepage1, bg="lightsteelblue4").place(width = 570,height=415, relx=0.5,rely=0.72,anchor='center')

        Label(homepage1, text="What stall would you like to pick?",bg="lightsteelblue4",fg="white",font="helvetica 20 bold").place(relx=0.5,rely=0.5,anchor='center')


        
        
        western1 = PhotoImage(file="western.png")
        drinks1 = PhotoImage(file="drinks.png")
        miniwok1 = PhotoImage(file="miniwok.png")
        indian1 = PhotoImage(file="indian.png")
        economicrice1 = PhotoImage(file="economicrice.png")
        vegetarian1 = PhotoImage(file="vegetarian.png")

        Button(homepage1, text="Surf & Turf", height=90, width=250, image=western1, command=western.open_western,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.27,rely=0.6,anchor='center')

        Button(homepage1, text="Drinks", height=90, width=250, image=drinks1, command=drinks.open_drinks,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.73,rely=0.6,anchor='center')

        Button(homepage1, text="Economic Rice", height=90, width=250, image=economicrice1, command=western.open_western,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.27,rely=0.75,anchor='center')
        Button(homepage1, text="Vegetarian Delights", height=90, width=250, image=vegetarian1, command=vegetarian.open_vegetarian,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.73,rely=0.75,anchor='center')

        Button(homepage1, text="Indian Delicacies", height=90, width=250, image=indian1, command=indian.open_indian,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.27,rely=0.90,anchor='center')
        Button(homepage1, text="Mini Wok", height=90, width=250, image=miniwok1, command=miniwok.open_miniwok,borderwidth=0,highlightthickness = 0,padx=0,pady=0).place(relx=0.73,rely=0.90,anchor='center')



'''

month = StringVar()
combobox = ttk.Combobox(root_main, textvariable = month)
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

month.get()
'''

'''
# Radio Buttons

Option1 = Radiobutton( root_economic, text = "Option 1", variable = meat)

'''

'''
# User Input

entry_people  = Entry( root_x, width = 30)
entry_people.insert(0,"Enter the no. of pax")

entry.get()
entry.delete(0,END)

For password:
entry.config(show = "*")
entry.get()

'''

#Rendering of 1st function (homepage1)

global homepage_geometry

start = Tk()
start.geometry('600x800+100+100')
start.title("Loading")
start.configure(background="gray25")

current_geometry = '600x800+'+str(start.winfo_x())+'+'+str(start.winfo_y()) #ensures window is created at current window
start.destroy()
homepage.open_menu()



start.mainloop()






















