amount_of_proteins = int(input("Введите массу белков (г): "))
amount_of_fats = int(input("Введите массу жиров (г): "))
amount_of_carbs = int(input("Введите массу углеводов (г): "))

calories = int((amount_of_proteins*4)+(amount_of_fats*9)+(amount_of_carbs*4))

print(f"{calories}" "ккал")