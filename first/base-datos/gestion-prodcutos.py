import sqlite3 as lite

appConexion = lite.connect('ejemplo_base_sqlite.db')
appCursor   = appConexion.cursor()
# appCursor.execute('''
#     CREATE TABLE productos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         codigo_art INTEGER,
#         nombre VARCHAR(50),
#         precion INTEGER,
#         seccion VARCHAR(20)
#     )
# ''')

res = appCursor.execute("INSERT INTO productos VALUES (null, 1, 'nombre', 1, 'seccion')")
print(res)

appConexion.commit()
appConexion.close
