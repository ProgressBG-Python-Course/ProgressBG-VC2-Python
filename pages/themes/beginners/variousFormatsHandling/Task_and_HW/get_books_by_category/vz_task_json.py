import json
import urllib.request

addr = 'https://progressbg-python-course.github.io/ProgressBG-VC2-Python/pages/themes/beginners/variousFormatsHandling/Task_and_HW/get_books_by_category/pythonbooks.revolunet.com.issues.json'
with urllib.request.urlopen(addr) as url:
    data = json.load(url)
    i = 1
    for book in data['books']:
        if book['level'] == 'Advanced':
            print('{}."{}"'.format(i, book['title']))
            print("         [{}]".format(book['author']))
            print("          {}".format(book['url']))
            i += 1
