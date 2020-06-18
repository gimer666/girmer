import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Rango.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    # Во-первых, мы создадим списки словарей, содержащих страницы, которые мы хотим добавить в каждую категорию.	    
    # Затем мы создадим словарь словарей для наших категорий.
    # Это может показаться немного запутанным, но это позволяет нам перебирать
    # каждую структуру данных и добавлять данные в наши модели.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"
         ,"views": 20},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"
         ,"views": 25},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"
         ,"views": 35}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"
         ,"views": 36},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"
         ,"views": 23},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"
         ,"views": 45}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"
         ,"views": 3},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"
         ,"views": 34}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes":64 },
            "Django": {"pages": django_pages, "views": 64, "likes":32 },
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes":16 }}

    # Если Вы хотите добавить больше категорий или страниц,
    # включите их в словари выше.
    
    # Показанный ниже код перебирает словарь cats, затем добавляет каждую категорию 
    # и соответствующие страницы для этой категории.	    
    # Если Вы используете Python 2.x, то используйте cats.iteritems()
    # смотри http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # для получения дополнительной информации о том, как правильно перебирать словарь.

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, cat_data):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = cat_data["views"]
    c.likes= cat_data["likes"]
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()