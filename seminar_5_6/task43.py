#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

array = [1, 2, 3, 5, 1, 5, 3, 10]
print(list(filter(lambda el: array.count(el) == 1, array)))
