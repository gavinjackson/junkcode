#here is an example of how we could trigger a notify from code (simply executing the notify command)

import psycopg2
import psycopg2.extensions

dbname = 'lnotify'
host = 'localhost'
user = 'lnotify'
password = 'password'

dsn = 'dbname=%s host=%s user=%s password=%s' % (dbname, host, user, password)

conn = psycopg2.connect(dsn)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("NOTIFY test1;")
curs.execute("NOTIFY test2;")
curs.close()
