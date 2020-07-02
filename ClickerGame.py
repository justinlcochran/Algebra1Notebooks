from tkinter import *
import time

root=Tk()
root.geometry("400x200")
root.configure(bg="gray")
hope = 0
clonetroopers=0
atrtwalkers=0
clonetroopers_cost=10
atrtwalkers_cost=1000
def refresh():
    global root
    global hope
    hope_now.set(hope)
    root.after(500,refresh)

def generate_hope():
    global hope
    hope += 1
    hope_now.set(hope)  

def hire_clonetrooper():
    global clonetroopers_cost
    global clonetroopers
    global hope
    if hope>=clonetroopers_cost:
        clonetroopers+=1
        hope-=clonetroopers_cost
        clonetroopers_cost=int(clonetroopers_cost*1.1)
        hope_now.set(hope)
        clonetroopers_now.set(clonetroopers)
        text_box.delete(1.0,"end-1c")
        text_box.insert("end-1c","Just like in the simulations.")
        print("Just like in the simulations.")
    else:
        text_box.delete(1.0,"end-1c")
        text_box.insert("end-1c","You need more hope to inspire a Clone Trooper.")
        print("You need more hope to inspire a new Clone Trooper.")

def hire_atrtwalkers():
    global atrtwalkers_cost
    global atrtwalkers
    global hope
    if hope>=atrtwalkers_cost:
        atrtwalkers+=1
        hope-=atrtwalkers_cost
        atrtwalkers_cost=int(atrtwalkers_cost*1.5)
        hope_now.set(hope)
        atrtwalkers_now.set(atrtwalkers)
        text_box.delete(1.0,"end-1c")
        text_box.insert("end-1c","Mount up, trooper.")
        print("Just like in the simulations.")
    else:
        text_box.delete(1.0,"end-1c")
        text_box.insert("end-1c","You need more hope to construct an ATRT Walker.")
        print("You need more hope to inspire a new Clone Trooper.")


text_box=Text(root, width=40, height=2, bg="gray")
text_box.grid(row=10,columnspan=8,padx=0,pady=0)
text_box.config(wrap="word", bg="white")

generate_hope_frame = Frame(root)
generate_hope_frame.grid(row=1, column=1, padx=10, pady=10,sticky="w")
generate_hope_frame.config(bg="gray", width=25, height=10)
generate_hope_count_frame = Frame(root)
generate_hope_count_frame.grid(row=1, column=2, padx=10, pady=10, sticky="w")
generate_hope_count_frame.config(bg="gray", width=10, height=10)
generate_hope_button = Button(generate_hope_frame, text="Generate Hope", width=25, command=generate_hope)
generate_hope_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

generate_clonetrooper_frame=Frame(root)
generate_clonetrooper_frame.grid(row=2,column=1,padx=10,pady=10,sticky="w")
generate_clonetrooper_frame.config(bg="gray", width=25, height=10)
generate_clonetrooper_count_frame = Frame(root)
generate_clonetrooper_count_frame.grid(row=2, column=2, padx=10, pady=10, sticky="w")
generate_clonetrooper_count_frame.config(bg="gray", width=10, height=10)
generate_clonetrooper_button=Button(generate_clonetrooper_frame,text="Hire Clone Trooper", width=25, command=hire_clonetrooper)
generate_clonetrooper_button.grid(row=1, column=1, padx=10, pady=10,sticky="w")

generate_atrtwalker_frame=Frame(root)
generate_atrtwalker_frame.grid(row=3,column=1,padx=10,pady=10,sticky="w")
generate_atrtwalker_frame.config(bg="grey", width=25, height=10)
generate_atrtwalker_count_frame = Frame(root)
generate_atrtwalker_count_frame.grid(row=3, column=2, padx=10, pady=10, sticky="w")
generate_atrtwalker_count_frame.config(bg="gray", width=10, height=10)
generate_atrtwalkers_button=Button(generate_atrtwalker_frame,text="Construct AT-RT Walker", width=25, command=hire_atrtwalkers)
generate_atrtwalkers_button.grid(row=1, column=1, padx=10, pady=10,sticky="w")


##------------- Label added  ------------------------------------
hope_now=IntVar()
Label(generate_hope_count_frame, textvariable=hope_now,bg="gray").grid(row=1, column=1, sticky="w")

clonetroopers_now=IntVar()
Label(generate_clonetrooper_count_frame, textvariable=clonetroopers_now, bg="gray").grid(row=1, column=1, sticky="w")

atrtwalkers_now=IntVar()
Label(generate_atrtwalker_count_frame, textvariable=atrtwalkers_now, bg="gray").grid(row=1, column=1, sticky="w")

def auto_hope():
    global root
    global hope
    global clonetroopers
    global aatewalkers
    hope += clonetroopers
    hope += 10*atrtwalkers
    root.after(1000, auto_hope)

auto_hope()
refresh()

root.mainloop()