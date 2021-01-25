def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def salvesta_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+'\n')
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas


def tolkimine():
    pass

def oshibka():
    pass

def proverka():
    pass

list_rus=loe_failist("rus.txt")
list_ee=loe_failist("ee.txt")
print(list_rus)
print(list_ee)

while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4 ==> ")
    if v=='1':
        tolkimine()
    elif v=='2':
        rus_sona=input("Введи слово на русском ==> ")
        ee_sona=input("Sisesta sõna eesti keeles ==> ")
        list_rus=salvesta_failisse('rus.txt',rus_sona)
        list_ee=salvesta_failisse('ee.txt',ee_sona)
        print(list_rus)
        print(list_ee)
    elif v==3:
        oshibka()
    elif v==4:
        proverka()



