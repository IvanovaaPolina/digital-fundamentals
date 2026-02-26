capsules_number = int(input("Введите количество капсул (шт): "))
packing_capacity = int(input("Введите вместимость одной упоковки (шт):"))

packs = (capsules_number // packing_capacity)
surplus = (capsules_number % packing_capacity)

print("Отчет фасовочного цеха")
print("Полных упаковок: " f"\t{packs}")
print("Остаток капсул: " f"\t{surplus}")

