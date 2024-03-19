from utils import utils
import class_Category,class_Product

# Сохраняю json файл в data_category
data_category = utils.get_list()
# Создаю пустой список list_category
list_category = []

# Запускаю цикл чтоба перебраль индексы категорий
for i in range (len(data_category)):
    # Создаю пустой список list_products в нутри цикла бля его очистки после итерации списка
    list_products = []
    # Запускаю цикл чтоба перебраль индексы продуктов
    for j in range (len(data_category[i]['products'])):
        path_product = data_category[i]['products'][j]
        # Добавляю в list_products объекты класса Product
        product = class_Product.Product(path_product['name'], path_product['description'], path_product['price'], path_product['quantity'])
        list_products.append(product)
    print(list_products)
    products = list_products
    #category = class_Category.Category(data_category[i]['name'], data_category[i]['description'], data_category[i]['products'])
    category = class_Category.Category(data_category[i]['name'], data_category[i]['description'], products)
    list_category.append(category)
print(list_category[0].products)

