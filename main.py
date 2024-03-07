from pymongo import MongoClient, errors
from bson.objectid import ObjectId

# Налаштування з'єднання з MongoDB
client = MongoClient('mongodb+srv://nandr:rJuh13aIroTCgyM3@cluster0.9tj3azx.mongodb.net/?authMechanism=DEFAULT')
db = client['cats_db']
collection = db['cats']

# Додавання нового кота до колекції
def create_cat(name, age, features):
    try:
        cat_document = {
            "name": name,
            "age": age,
            "features": features
        }
        collection.insert_one(cat_document).inserted_id
        print(f"Кіт з ім'ям {name} був доданий.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні кота: {e}")

# Ввиведення всіх записів із колекції
def get_all_cats():
    try:
        cats = list(collection.find({}))
        for cat in cats:
            print(f"ID: {cat['_id']}")
            print(f"Ім'я: {cat['name']}")
            print(f"Вік: {cat['age']}")
            print("Особливості:")
            for feature in cat.get('features', []):
                print(f" - {feature}")
            print("-" * 30)
    except errors.PyMongoError as e:
        print(f"Помилка при читанні даних: {e}")

# Функція, яка виводить інформацію про кота за ім'ям
def get_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(f"ID: {cat['_id']}")
            print(f"Ім'я: {cat['name']}")
            print(f"Вік: {cat['age']}")
            print("Особливості:")
            for feature in cat.get('features', []):
                print(f" - {feature}")
            print("-" * 30)
    except errors.PyMongoError as e:
        print(f"Помилка при читанні даних: {e}")

# Функція, яка оновлює вік кота за ім'ям
def update_cat_age(name, age):
    try:
        collection.update_one({"name": name}, {"$set": {"age": age}})
        print(f"Вік кота змінено на {age}")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні даних: {e}")

# Функція, яка додає нову характеристику до списку features кота за ім'ям
def add_feature_to_cat(name, feature):
    try:
        collection.update_one({"name": name}, {"$push": {"features": feature}})
        print(f"Характеристику '{feature}' додано до {name}")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні даних: {e}")

# Функція для видалення запису з колекції за ім'ям тварини
def delete_cat_by_name(name):
    try:
        collection.delete_one({"name": name})
        print(f"{name} видалено з бази")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні даних: {e}")

# Функція для видалення всіх записів із колекції
def delete_all_cats():
    try:
        collection.delete_many({})
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні даних: {e}")

if __name__ == "__main__":
    # create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    # create_cat("мурзік", 5, ["любить гратися з м'ячиком", "спить на сонці", "муркає голосно"])
    # create_cat("лео", 2, ["ловить метеликів", "не боїться води", "має довгий хвіст"])
    # create_cat("пушок", 4, ["м'який", "любить сидіти на вікні", "дружелюбний до гостей"])
    # create_cat("сімба", 3, ["активний", "любить високі місця", "грається з іграшками"])
    # create_cat("нюша", 1, ["дуже маленька", "любить молоко", "завжди цікава"])

    # delete_all_cats()
    # print(get_all_cats())
    # print(get_cat_by_name("barsik"))
    # update_cat_age("barsik", 4)
    # add_feature_to_cat("barsik", "любить спати на подушці")
    delete_cat_by_name("сімба")
