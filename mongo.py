# импортируем pymongo
import pymongo
import numpy as np

# соединяемся с сервером базы данных 
# (по умолчанию подключение осуществляется на localhost:27017)
conn = client = pymongo.MongoClient('localhost', 27017)



# выбираем базу данных
db = conn.test



# выбираем коллекцию документов
coll = db.mycoll
nympy_collection = db.numpy


# осуществляем добавление документа в коллекцию,
# который содержит поля name и surname - имя и фамилия
doc = {"name": "Иван", "surname": "Иванов"}
coll.save(doc)
array = np.arange(1,10)
nympy_collection.save(array)



# выводим все документы из коллекции coll
# for item in coll.find():
#     print(item)



# подсчет количества людей с именем Петр

def mongo_find(collection, find_string=None):
        return [item for item in collection.find({'name':"Tom"})]

def mongo_add(array):
    pass


"""
# добавляем ко всем документам новое поле sex - пол
coll.update({}, {"$set": {"sex": "мужской"}})

# всем Петрам делаем фамилию Новосельцев и возраст 25 лет
coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})

# увеличиваем всем Петрам возраст на 5 лет
coll.update({"name": "Петр"}, {"$inc": {"age": 5}})

# сбрасываем у всех документов поле name
coll.update({}, {"$unset": {"name": 1}})

# удаляем людей с возрастом более 20 лет
# другие условия $gt - больше, $lt - меньше, 
# $lte - меньше или равно, $gte - больше или равно, $ne - не равно
coll.remove({"age": {"$gt": 20}})

# удаляем все документы коллекции
coll.remove({})
"""

if __name__ == '__main__':
    print(
        mongo_find(db.users)
    )