import model
from tkinter import  *
from tkinter import ttk

root = None
frm = None
entry_tel = None
entry_fio = None
lable_tel = None
lable_fio = None
butt_new = None
butt_search = None
sprav =  None

def createMenu():
    global root
    global frm
    global sprav
    root = Tk()
    frm = ttk.Frame(root, padding=600)
 
    # меню
    mainmenu = Menu(root)
    root.config(menu = mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Выгрузить в xml", command = model.SaveFile)
    filemenu.add_command(label="Выход", command = root.destroy)
    mainmenu.add_cascade(label="Файл", menu = filemenu)

    sprmenu = Menu(mainmenu, tearoff=0)
    sprmenu.add_command(label="Показать", command=ShowSprav)
    sprmenu.add_command(label="Поиск по имени", command=ShowSearchFio)
    sprmenu.add_command(label="Поиск по телефону", command=ShowSearchTel)
    sprmenu.add_command(label="Добавить запись", command=ShowNew)
    mainmenu.add_cascade(label="Справочник", menu=sprmenu)

    sprav = Text()
    sprav.pack()
    root.mainloop()

def ShowSprav():
    # выводит справочник
    sprav.delete("1.0","end")
    Spr = model.ReadSprav()
    sprav.insert("1.0", model.PrintSprav(Spr))

def ShowNew():
    # показывает элемены для ввода новой записи
    global root
    global entry_tel
    global entry_fio
    global lable_tel
    global lable_fio
    global butt_new
    lable_tel = Label(root, text="Введите телефон")
    lable_tel.pack(side=LEFT)
    entry_tel = Entry(root)
    entry_tel.pack(side=LEFT)
    lable_fio = Label(root, text="Введите имя")
    lable_fio.pack(side=LEFT)
    entry_fio = Entry(root)
    entry_fio.pack(side=LEFT)
    butt_new = Button(root, text="Добавить", command=AddT)
    butt_new.pack(side=LEFT)

def ShowSearchTel():
    # выводит элементы для поиска по телефону 
    global root
    global lable_tel
    global entry_tel
    global butt_search
    lable_tel = Label(root, text="Введите телефон")
    lable_tel.pack(side=LEFT)
    entry_tel = Entry(root)
    entry_tel.pack(side=LEFT)
    butt_search = Button(root, text="Искать", command=SearchTel)
    butt_search.pack(side=LEFT)

def ShowSearchFio():
    # выводит элементы для поиска по ФИО 
    global root
    global entry_fio
    global lable_fio
    global butt_search
    lable_fio = Label(root, text="Введите имя")
    lable_fio.pack(side=LEFT)
    entry_fio = Entry(root)
    entry_fio.pack(side=LEFT)
    butt_search = Button(root, text="Искать", command=SearchFio)
    butt_search.pack(side=LEFT)

    

def AddT():
    # добавление новой записи
    model.AddTel(entry_tel.get(), entry_fio.get())
    entry_fio.pack_forget()
    entry_tel.pack_forget()
    lable_tel.pack_forget()
    lable_fio.pack_forget()
    butt_new.pack_forget()


def SearchTel():
    # поиск по телефону
    sprav.delete("1.0","end")
    Spr = model.SearchForTel(entry_tel.get())
    if Spr == {}:
        sprav.insert("1.0","Ничего не наидено" )
    else:
        sprav.insert("1.0", model.PrintSprav(Spr))
    entry_tel.pack_forget()
    lable_tel.pack_forget()
    butt_search.pack_forget()
    
def SearchFio():
    # поиск по ФИО
    sprav.delete("1.0","end")
    Spr = model.SearchForFio(entry_fio.get())
    if Spr == {}:
        sprav.insert("1.0","Ничего не наидено" )
    else:
        sprav.insert("1.0", model.PrintSprav(Spr))

    entry_fio.pack_forget()
    lable_fio.pack_forget()
    butt_search.pack_forget()