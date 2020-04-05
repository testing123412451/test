# 1 словарь с ключем в виде русских букв и занченим транслита на англ
# 2 получаем слово от пользовтаеля 
# 3 перводим в строку
# 4 через цикл перебераем каждое знаечение и добавляем в новый список значение второе словаря 
# 5 соединяем список в строку
# 6 выводим пользовталею значение

# Список руский
letRu = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
# Список англ
letEN = 'a b v g d e yo zh z i j k l m n o p r s t u f h c ch sh shch " y \' e yu ya'.split()

# Функция для создания словаря из 2 списков 
def slovar(ru,en):
    translit_ruls = {}
    a = 0
    b = 0
    # Слияние списков в словарь
    for i in ru :
        translit_ruls[ ru[a] ] = en[b]
        a+=1
        b+=1
        
    Letter_rU.update(translit_ruls )
    # Letter_ru = translit_ruls.copy() ХУЛИ НЕ РАБОТАЕТ???????????????????
# Объвление словаря
Letter_rU = {}
# Вызов функции для слияния списков в словарь ^
slovar(letRu,letEN)

Slovo = "Артем"
# Slovo.lower()
# print(Slovo)
a = list(Slovo.lower())
print(a)
b = 0

# СЕЙЛООООР МУУУУУУУУУУНекрекр
# for key in Letter_rU:
#     if key == a[b]:
#         print("Da")
#         b = b + 1
#     else:
#         print("nO")