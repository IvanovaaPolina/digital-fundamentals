f = open("C:/Users/Polin/OneDrive/Рабочий стол/IvanovaPhyton/inventory.txt", "w", encoding="utf-8")

reagent_name = input("Название реагента: ")
quantity_of_reagent = input("Количество реагента: ")

print(f"Реактив {reagent_name} поступил на склад в количестве {quantity_of_reagent} шт.", file=f)

f.close()