# Memory data storing module used for test
#


class memory_store(object):
    _db = None

    def get():
        if not memory_store._db:
            memory_store._db = memory_store()
        return memory_store._db

    def release():
        memory_store._db = None

    def __init__(self, ):
        self._data = {}

    def connect(self):
        return self._data

    def disconnect(self):
        pass

    def table_exist(self, table):
        return table in self._data

    def row_exist(self, table, id):
        return self.table_exist(table) and id in self._data[table]

    def create_table(self, table):
        if self.table_exist(table):
            return False
        self._data[table] = {}
        return True

    def drop_table(self, table):
        if not self.table_exist(table):
            return False
        del self._data[table]
        return True

    def create_row(self, table, id, data):
        if not self.table_exist(table):
            return False
        if self.row_exist(table, id):
            return False
        self._data[table][id] = data
        return True

    def get_rows_id(self, table):
        if not self.table_exist(table):
            return []
        return self._data[table].keys()

    def store(self, table, id, data):
        if not self.table_exist(table):
            self.create_table(table)
        if not self.row_exist(table, id):
            self.create_row(table, id, data)

        self._data[table][id] = data
        return True

    def restore(self, table, id):
        if not self.table_exist(table) or not self.row_exist(table, id):
            return ''
        return self._data[table][id]

    def backup(self):
        data = {}
        for table in self._data.keys():
            data[table] = {}
            for id in self._data[table]:
                data[table][id] = self._data[table][id]
        return data

    def restore_backup(self, data):
        for table in list(data.items()):
            table_name = table[0]
            for row in list(table[1].items()):
                id = row[0]
                self.store(table_name, id, row[1])
        return True
