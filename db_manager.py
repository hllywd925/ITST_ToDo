from tinydb import TinyDB, Query
import datetime

"""db = TinyDB('dbs/event_db.json', sort_keys=True, indent=4, separators=(',', ': '))
User = Query()
db.insert({'name': 'John', 'age': 22})
db.search(User.name == 'John')

{'d': 19, 'm': 10, 'y': 2022}
"""


class DBManager:
    def __init__(self):
        self.db = TinyDB('dbs/event_db.json', sort_keys=True, indent=2, separators=(',', ': '))

    def newevent(self):

        self.db.insert({
            'type': 'event',
            'eventname': 'testevent',
            'date': '19.10.2022'
        })

    def search_date(self, date):
        penis = Query()
        print(d.db.search(penis.date == date))


if __name__ == "__main__":
    d = DBManager()

    print('Herzlich Willkommen')
    print('Was möchten Sie machen?')
    print('Event erstellen = 1, Events anzeigen = 2, Events suchen = 3')
    choice = input()

    if choice == '1':
        d.newevent()

    if choice == '2':
        for item in d.db:
            print(item)
