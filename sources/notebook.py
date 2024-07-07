import sqlite3 as sql
import datetime

class NotebookManager:
    def __init__(self, valume: str) -> None:
        self.connection = sql.connect(valume)
        self.cursor = self.connection.cursor()

        self.notebooks = dict()

    def new_notebook(self, book_name):
        raise NotImplementedError()

    def open_notebook(self):
        raise NotImplementedError()

    # def close_notebook(self):
    #     raise NotImplementedError()  

    # def delete_notebook(self):
    #     raise NotImplementedError()

class MoneyManager(NotebookManager):
    def __init__(self, valume = "Money") -> None:
        super().__init__(valume)

    def new_notebook(self, book_name):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {book_name} (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            datatime DATETIME,
            tag TEXT,
            amount FLOAT)
        ''')
        self.connection.commit()

        return self.open_notebook(book_name)
        
    def open_notebook(self, name):

        if name not in self.notebooks:
            book = Notebook(name, self.connection, self.cursor)
            self.notebooks[name] = book

        return self.notebooks[name]


class Notebook(object):
    def __init__(self, name, connection, cursor) -> None:
        self.book_name = name
        self.connection = connection
        self.cursor = cursor 

    def view(self, period):
        print("Просмотр:")
        self.cursor.execute(f"SELECT * FROM '{self.book_name}'")
        for entry in self.cursor.fetchall():
            for val in entry:
                print(str(val), end="|")
            print("\n")

    def entry(self, amount: float, tag: str):
            self.cursor.execute(
                f"""INSERT INTO {self.book_name} (datatime, tag, amount) 
                VALUES (?, ? ,?)""",
                (datetime.datetime.now(), tag, amount,))
            self.connection.commit()

    # def correct(self):
    #     pass

    # def delete(self):
    #     pass

