import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        # connect = sqlite3.connect(self.path)
        # контекстный менеджер
        with sqlite3.connect(self.path) as connect:
            connect.execute(Queries.CREATE_REVIEW_DIALOG_TABLE)
            connect.execute(Queries.DROP_DISHES_CATEGORY_TABLE)
            connect.execute(Queries.CREATE_DISHES_CATEGORY_TABLE)
            connect.execute(Queries.POPULATE_DISHES_CATEGORY_TABLE)
            connect.execute(Queries.DROP_DISHES_TABLE)
            connect.execute(Queries.CREATE_DISHES_TABLE)
            connect.execute(Queries.POPULATE_DISHES_TABLE)

            connect.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            connect.execute(query, params)

    def fetch(self, query: str, params: tuple = None, fetchmany: bool = True):
        with sqlite3.connect(self.path) as connect:
            result = connect.execute(query, params)
            result.row_factory = sqlite3.Row

            if fetchmany:
                to_return = result.fetchall()
                return [dict(row) for row in to_return]
            else:
                to_return = result.fetchone()
                return dict(to_return)
