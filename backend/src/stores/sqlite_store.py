# Postgresql data storing module
#
import sqlite3


class sqlite_store(object):
    _db = None

    def get():
        if not sqlite_store._db:
            sqlite_store._db = sqlite_store('poolman.db')
        return sqlite_store._db

    def release():
        sqlite_store._db = None

    def __init__(self, db):
        self._db = db
        self._con = None

    def connect(self):
        if self._con:
            return self._con
        self._con = sqlite3.connect(self._db)
        return self._con

    def disconnect(self):
        if self._con:
            self._con.close()
            self._con = None

    def table_exist(self, table):
        if self._con:
            try:
                cur = self._con.cursor()
                sql = "SELECT * FROM sqlite_master WHERE type='table' "
                sql += "AND name='" + table + "';"
                cur.execute(sql)
                rows = cur.fetchall()
            except Exception as e:
                return False
            return bool(len(rows))
        return False

    def row_exist(self, table, id):
        if self._con:
            try:
                cur = self._con.cursor()
                sql = "SELECT * FROM " + table + " WHERE ID='" + str(id) + "';"
                cur.execute(sql)
                rows = cur.fetchall()
            except Exception as e:
                return False
            return bool(len(rows))
        return False

    def create_table(self, table):
        if self._con:
            try:
                cur = self._con.cursor()
                sql = 'CREATE TABLE ' + table
                sql += '(ID TEXT PRIMARY KEY NOT NULL, data TEXT NOT NULL)'
                cur.execute(sql)
                self._con.commit()
            except Exception as e:
                return False
            return True
        return False

    def drop_table(self, table):
        if self._con:
            try:
                cur = self._con.cursor()
                cur.execute('DROP TABLE ' + table)
                self._con.commit()
            except Exception as e:
                return False
            return True
        return False

    def create_row(self, table, id, data):
        if self._con:
            try:
                cur = self._con.cursor()
                sql = "INSERT INTO " + table + "(ID,data) "
                sql += "VALUES('" + str(id) + "', '" + data + "')"
                cur.execute(sql)
                self._con.commit()
            except Exception as e:
                return False

            return True
        return False

    def get_rows_id(self, table):
        if self._con:
            try:
                cur = self._con.cursor()
                cur.execute("SELECT ID FROM " + table)
                records = cur.fetchall()
                data = []
                for r in records:
                    data.append(r[0])
            except Exception as e:
                return []
            return data
        return []

    def store(self, table, id, data):
        if not self.table_exist(table):
            self.create_table(table)
        if not self.row_exist(table, id):
            self.create_row(table, id, data)

        if self._con:
            try:
                cur = self._con.cursor()
                sql = 'UPDATE ' + table + ' SET data=\'' + data + '\' '
                sql += 'WHERE ID=\'' + str(id) + '\''
                cur.execute(sql)
                self._con.commit()
            except Exception as e:
                return False
            return True
        return False

    def restore(self, table, id):
        if not self.table_exist(table) or not self.row_exist(table, id):
            return ''
        if self._con:
            try:
                cur = self._con.cursor()
                sql = 'SELECT data FROM ' + table
                sql += ' WHERE ID=\'' + str(id) + '\''
                cur.execute(sql)
                records = cur.fetchall()
                data = records[0][0]
            except Exception as e:
                return None
            return data
        return None

    def backup(self):
        req_tables = "SELECT name FROM sqlite_master WHERE type = 'table' "
        req_tables += "ORDER BY name;"
        data = {}
        if self._con:
            try:
                cur = self._con.cursor()
                cur.execute(req_tables)
                records = cur.fetchall()
                for record in records:
                    table = record[0]
                    data[table] = {}
                    data_req = 'SELECT * FROM {table};'.format(table=table)
                    cur.execute(data_req)
                    rows = cur.fetchall()
                    for row in rows:
                        data[table][row[0]] = row[1]
            except Exception as e:
                return None
        return data

    def restore_backup(self, data):
        req_tables = "SELECT name FROM sqlite_master WHERE type = 'table' "
        req_tables += "ORDER BY name;"
        if self._con:
            try:
                cur = self._con.cursor()
                cur.execute(req_tables)
                records = cur.fetchall()
                for record in records:
                    table = record[0]
                    drop_req = 'DROP TABLE {table};'.format(table=table)
                    cur.execute(drop_req)
                self._con.commit()

                for table in list(data.items()):
                    table_name = table[0]
                    for row in list(table[1].items()):
                        id = row[0]
                        self.store(table_name, id, row[1])
            except Exception as e:
                return False
        return True
