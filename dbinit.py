import sqlite3

def insertstudent(sname, phnum, plang, jdate):
    dbf = 'strings.db'
    cn = sqlite3.connect(dbf)
    cur = cn.cursor()
    # table creation
    cur.execute("INSERT INTO student ( name, phnum, proglang, joindate ) VALUES ( ?, ?, ?, ? );", (sname, phnum, plang, jdate))
    # cleanup
    cn.commit()
    cn.close()

def create_tables():
    dbf = 'strings.db'
    cn = sqlite3.connect(dbf)
    cur = cn.cursor()
    # table creation
    cur.execute('''create table student (
      name text,
      phnum text,
      proglang text,
      joindate text
    )''')
    # cleanup
    cn.commit()
    cn.close()


if __name__ == '__main__':
    create_tables()


