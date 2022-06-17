import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('pizza_hp.db')
    cur = base.cursor()
    if base:
        print('Database connected OK!')
    base.execute('CREATE TABLE IF EXISTS menu (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_data(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()