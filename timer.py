import tkinter as tk
import time
from tkinter import messagebox
root = tk.Tk()
root.geometry('400x350')
root.title('Timer')
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()
hour.set('00')
minute.set('00')
second.set('00')
hourlabel  = tk.Label(root,text='Hours',font=("Arial",10,'bold'))
hourlabel.place(x=60,y=10)
minutelabel = tk.Label(root,text='Minutes',font=("Arial",10,'bold'))
minutelabel.place(x=110,y=10)
secondlabel = tk.Label(root,text='Seconds',font=("Arial",10,'bold'))
secondlabel.place(x=165,y=10)
hourentry = tk.Entry(root,width=3,font=("Arial",18),textvariable=hour)
hourentry.place(x=60,y=40)
minuteentry = tk.Entry(root,width=3,font=("Arial",18),textvariable=minute)
minuteentry.place(x=110,y=40)
secondentry = tk.Entry(root,width=3,font=("Arial",18),textvariable=second)
secondentry.place(x=165,y=40)


def startTimer():
	update_hrs = tk.Label(root,text="12",font=("Arial",20,'bold'))
	update_hrs.place(x=60,y=200)
	colonlabel = tk.Label(root,text=":",font=("Arial",20,'bold'))
	colonlabel.place(x=100,y=200)
	update_mins = tk.Label(root,text="12",font=("Arial",20,'bold'))
	update_mins.place(x=120,y=200)
	colonlabel1 = tk.Label(root,text=":",font=("Arial",20,'bold'))
	colonlabel1.place(x=160,y=200)
	update_secs = tk.Label(root,text="12",font=("Arial",20,'bold'))
	update_secs.place(x=180,y=200)
	temp = int(hour.get())*3600 + int(minute.get())*60+int(second.get())
	print(temp)
	while temp>-1:
		mins,secs = divmod(temp,60) #quotient=mins remainder=secs
		print(mins,secs)
		hours =0 
		if mins>60:
			hours,mins = divmod(mins,60)

		hour.set('00')
		minute.set('00')
		second.set('00')
		update_hrs.config(text=hours)
		update_mins.config(text=mins)
		update_secs.config(text=secs)
		root.update()
		time.sleep(1)

		if temp == 0:
			messagebox.showinfo("Timer","Times UP!",parent=root)
		temp -= 1

btn =  tk.Button(root,text='Start Timer',command=startTimer)
btn.place(x=70,y=120)
root.mainloop()