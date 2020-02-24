import psycopg2

conn = psycopg2.connect("dbname=surf_info user=admin2 password=admin22 host=localhost")


cur = conn.cursor()

cur.execute("select * from surf_data")
rows = cur.fetchall()
print(rows)