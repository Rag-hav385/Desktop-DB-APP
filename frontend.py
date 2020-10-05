'''
A program that stores this book information:
Title , Author
Year , ISBN

User can :

View all records
Search an entry
Add entry
Update entry
Delete
close

'''
from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])





def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def searach_command():
    list1.delete(0,END)
    for row in backend.search(tittle_txt.get(),Author_txt.get(),Year_txt.get(),ISBN_txt.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(tittle_txt.get(),Author_txt.get(),Year_txt.get(),ISBN_txt.get())
    list1.delete(0,END)
    list1.insert(END,(tittle_txt.get(),Author_txt.get(),Year_txt.get(),ISBN_txt.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],tittle_txt.get(),Author_txt.get(),Year_txt.get(),ISBN_txt.get())


    


window = Tk()
window.wm_title("Raghav's Book Store")



#labels
l1 = Label(window,text ="Tittle")
l1.grid(row = 0 , column = 0)

l2 = Label(window,text ="Author")
l2.grid(row = 0 , column = 2)

l2 = Label(window,text ="Year")
l2.grid(row = 1 , column = 0)

l2 = Label(window,text ="ISBN")
l2.grid(row = 1 , column = 2)

#Entries
tittle_txt = StringVar()
e1 = Entry(window,textvariable = tittle_txt )
e1.grid(row = 0 , column = 1)

Author_txt = StringVar()
e2 = Entry(window,textvariable = Author_txt )
e2.grid(row = 0 , column = 3)

Year_txt = StringVar()
e3 = Entry(window,textvariable = Year_txt )
e3.grid(row = 1 , column = 1)

ISBN_txt = StringVar()
e4 = Entry(window,textvariable = ISBN_txt )
e4.grid(row = 1 , column = 3)

list1 = Listbox(window,height = 6, width = 35)
list1.grid(row = 2,column = 0 , rowspan = 6 , columnspan = 2)

#scrollbar
sb1 = Scrollbar(window)
sb1.grid (row = 2 , column = 2 , rowspan = 6 )

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>' , get_selected_row)


#buttons
b1 = Button(window , width = "12" , text = "View All" , command = view_command)
b1.grid(row = 2 , column = 3)

b1 = Button(window , width = "12" , text = "Search Entry",command = searach_command)
b1.grid(row = 3 , column = 3)

b1 = Button(window , width = "12" , text = "Add Entry", command = add_command)
b1.grid(row = 4 , column = 3)

b1 = Button(window , width = "12" , text = "Update" , command = update_command)
b1.grid(row = 5 , column = 3)

b1 = Button(window , width = "12" , text = "Delete" , command = delete_command)
b1.grid(row = 6 , column = 3)

b1 = Button(window , width = "12" , text = "Close" , command = window.destroy)
b1.grid(row = 7 , column = 3)





window.mainloop()









