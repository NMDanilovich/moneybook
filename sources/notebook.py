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
    def __init__(self, valume = "Money.db") -> None:
        super().__init__(valume)

    def new_notebook(self, book_name):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {book_name} (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME,
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
    def __init__(self, name, connection:sql.Connection = None, valume:str = "None") -> None:
        self.book_name = name
        self.connection = connection
        
        if self.connection == None:
            self.connection = sql.connect(valume)

        self.cursor = self.connection.cursor()

    def get_name(self):
        print(f"Имя рабочей записной книжки: {self.book_name}")
        return self.book_name

    def view(self, period="day"):
        date_now = datetime.datetime.now()
        
        if "l" in period:
              l = period.count("l")
        else:
              l = 0

        if "day" in period or "-d" in period:
                        date = int(datetime.datetime.strftime(date_now, '%Y%m%d')) - l
                        self.cursor.execute(f"""SELECT * FROM '{self.book_name}' WHERE date == {date}""")

        elif "month" in period or "-m" in period:
                        if len(str(date_now.month - l)) == 1:
                              start = "0" + str(date_now.month - l)
                              stop = "0" + str(date_now.month + 1 - l)

                        start = str(date_now.year) + start + "00"
                        stop = str(date_now.year) + stop + "00"

                        self.cursor.execute(f"""SELECT * FROM '{self.book_name}' WHERE date BETWEEN {start} and {stop}""")
                        

        elif "year" in period or "-y" in period:
                        start = str(date_now.year - l) + "0000"
                        stop = str(date_now.year + 1 - l) + "0000"
                        self.cursor.execute(f"""SELECT * FROM '{self.book_name}' WHERE date BETWEEN {start} and {stop}""")

        elif "all" in period or "-a" in period:
                        self.cursor.execute(f"""SELECT * FROM '{self.book_name}'""")
        
        
        else:
            print("Используйте флаги опции или сокращенные флаги:")
            print("     moneybook view [-d][dey]    - записи за сегодня")
            print("     moneybook view [-m][month]  - записи за этот месяц")
            print("     moneybook view [-y][year]   - записи за этот год")
            print("     moneybook view [-a][all]    - записи за все время")
            return exit(1)


        results = self.cursor.fetchall()
        
        if results:
            print("Результаты просмотра:")
            for val in results:
                print(*val, sep="\t|")
        return results

    def entry(self, amount: float, tag: str):
            data = datetime.datetime.now()
            data = datetime.datetime.strftime(data, '%Y%m%d')
            
            self.cursor.execute(
                f"""INSERT INTO {self.book_name} (date, tag, amount) 
                VALUES (?, ? ,?)""",
                (data, tag, amount,))
            self.connection.commit()

    # def correct(self):
    #     pass

    # def delete(self):
    #     pass

