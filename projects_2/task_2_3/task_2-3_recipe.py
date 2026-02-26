culture_medium_name = input("Название среды: ").upper()
agar_concentration = input("Концентрация агара (%): ")
sterilization_temperature = input("Температура стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as report:

    report.write(f"{culture_medium_name}\n\n")
    report.write(f"{agar_concentration}\n")
    report.write(f"{sterilization_temperature}\n")

print ("\nФайл 'recipe.txt' успешно сформирован!")


