import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'root'
database = 'extraction'

# Simple routine to run a query on a database and print the results:
def insert_product(obj):
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name, review, description) VALUES (%s, %s, %s) RETURNING id;", (obj['name'], obj['review'], obj['description']))
    product_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return product_id

def insert_characteristics(obj):
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    cur.execute("INSERT INTO characteristics(information, description, product_id) VALUES (%s, %s, %s);", (obj['question'], obj['answer'], obj['product_id']))
    conn.commit()
    conn.close()

def insert_question(obj):
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    cur.execute("INSERT INTO questions(question, answer) VALUES (%s, %s);", (obj['question'], obj['answer']))
    conn.commit()
    conn.close()