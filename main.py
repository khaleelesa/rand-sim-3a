from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

#---question 1---
def count_articles(key,value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(key, value)
    return len(list(filtered))

#---question 2---
def is_article(key,value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(key, value)
    if not list(filtered):
        return False
    else:
        return True


#---question 3---
def longest_article(key,value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(key, value)
    resindex = 0 
    max_num = 0
    for i in filtered:
        if(max_num < int(i["pages"])):
            max_num = int(i["pages"])
            resindex = i 
    return resindex

print("Q1")
print(count_articles('title', 't4'))
print(count_articles('author', 'a1'))
print('')
print("Q2")
print(is_article('title', 't4'))
print(is_article('author', 'a0'))
print('')
print("Q3")
print(longest_article('author', 'a1'))

# print("Articles with a title of t4:")
# print(filter_CSV("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(filter_CSV("author", "a1"))
