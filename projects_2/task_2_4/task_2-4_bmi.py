weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = float(weight / ((height/100 )** 2))

print("Отчет о состоянии здоровья")
print("Рост: \t"f"{height}" "см \nВес:\t "f"{weight}" "кг" )
print("Ваш ИМТ: " f"{bmi:.2f}")
