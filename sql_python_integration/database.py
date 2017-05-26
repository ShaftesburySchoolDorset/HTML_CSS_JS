import sqlite3
conn = sqlite3.connect('database.db')

try:
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO TblUsers VALUES ('john smith','password')")
    conn.commit()

    # Retrieve a row of data
    t = ('john smith',)
    c.execute('SELECT * FROM TblUsers WHERE name=?', t)
    print(c.fetchone())

finally:
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()