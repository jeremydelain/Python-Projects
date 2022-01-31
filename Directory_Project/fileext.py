import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg')
conn = sqlite3.connect('fileext.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extensions(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")
    for item in fileList:
        if item.endswith('.txt'):
            cur.execute("INSERT INTO tbl_extensions(col_filename) VALUES(?)", (item,))
            conn.commit()
            print(item)
conn.close()
