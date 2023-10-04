import sqlite3

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

