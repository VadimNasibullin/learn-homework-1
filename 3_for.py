"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

for phones_sum in phones:
  print(f' Cуммарное количество продаж для ', phones_sum['product'], sum(phones_sum['items_sold']))

for phones_avg in phones:
  product = phones_avg['product']
  sum_phones = sum(phones_avg['items_sold'])
  phones_avg = sum_phones/len(phones_avg['items_sold'])
  print(f'Среднее количество продаж для ', product, phones_avg)

summ_all = 0
for all_phones in phones:
  product = all_phones['product']
  sum_phones = sum(all_phones['items_sold'])
  summ_all += sum_phones
  print(f'Cуммарное количество продаж всех товаров', summ_all) 

sum_all = 0
for phones_avg in phones:
  product = phones_avg['product']
  sum_phones = sum(phones_avg['items_sold'])
  phones_avg = sum_phones/len(phones_avg['items_sold'])
  sum_all += phones_avg
  print(f'Cреднее количество продаж всех товаров', sum_all)


