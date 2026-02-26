operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as report:
  
  report.write("ОПЕРАТОР "f"\t{operator_name}\n")
  report.write("ЗНАЧЕНИЕ "f"\t{pressure_value}")

  print("\nДанные успешно сохранены в sensor_log.txt ")
