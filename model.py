import datetime as dt
import re

def ReadSprav():
    # читает файл, возвращает справочник
    data = open("Sprav.txt",encoding='utf-8')
    Spr = data.readlines()
    data.close()
    telSprav = {}
    for i in range(len(Spr)):
        telSprav[Spr[i].split("|")[0]] = Spr[i].split("|")[1]

    return telSprav

def PrintSprav(telSprav):
    # из справочника делает удобную строку вывода
    str = ""
    for k,v in telSprav.items():
        str += k +"  "+ v
    return str

def AddTel(tel, fio):
    # добавляет запись в файл
    data = open("Sprav.txt", "a", encoding ="UTF-8")
    data.write(f'\n{tel}|{fio}' )
    data.close()

def SearchForTel(tel):
    # ищет по телефону
    Sprav = ReadSprav()
    return {key:val for key,val in Sprav.items() if key == tel }


def SearchForFio(fio):
    Sprav = ReadSprav()
    return {key:val for key,val in Sprav.items() if fio.lower() in  val.lower()}

def SaveFile():
    # добавляет запись в файл
    Sprav = ReadSprav()
    data = open("Sprav.xml", "w", encoding ="UTF-8")
    for key, val in Sprav.items():
        data.write("<item>\n")
        data.write(f'   <tel>{key}</tel>\n' )
        data.write(f"   <name>{val[:-1]}</name>\n")
        data.write("</item>\n")
    data.close()


    

