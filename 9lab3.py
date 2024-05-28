import csv

file_path = 'products.csv'
products = []

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        product = row[0]
        kolvo = int(row[1])
        price = int(row[2])
        products.append((product, kolvo, price))

summ = sum(kolvo * price for _, kolvo, price in products)

print("Нужно купить:")
for product, kolvo, price in products:
    print(f"{product} - {kolvo} шт. за {price} руб.")
print(f"Итоговая сумма: {summ} руб.")
