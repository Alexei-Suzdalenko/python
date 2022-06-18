import sqlite3 as lite

appConexion = lite.connect('ejemplo_base_sqlite.db')
appCursor   = appConexion.cursor()
# appCursor.execute("CREATE TABLE user (id INTEGER, name VARCHAR(50), email VARCHAR(50))")
# appCursor.execute("CREATE TABLE productos (ID INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(50), precio INTEGER(11), seccion VARCHAR(50))")

# insertar un registro
# appCursor.execute("INSERT INTO user VALUES (1, 'alexei', 'saron@gmail.com')"); appConexion.commit()

# isertar una lista de tuplas
# listUsers = [
#     (2, 'alexei2', 'saron2@gmail.com'),
#     (3, 'alexei3', 'saron3@gmail.com'),
#     (4, 'alexei4', 'saron4@gmail.com')
# ]
# appCursor.executemany("INSERT INTO user VALUES (?,?,?)", listUsers); appConexion.commit()

# leer de la base datos
appCursor.execute('SELECT * FROM user')
listUsers = appCursor.fetchall()
print(listUsers[0][2])

appConexion.close()