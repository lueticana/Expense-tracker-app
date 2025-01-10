import psycopg2

# uporabniki
conn_uporabniki = psycopg2.connect(
        host="localhost",
        database="uporabniki",
        user="postgres",
        password="123121")

# Open a cursor to perform database operations
cur = conn_uporabniki.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS uporabniki;')
cur.execute('CREATE TABLE uporabniki (id serial PRIMARY KEY,'
                                 'username varchar NOT NULL,'
                                 'email varchar NOT NULL,'
                                 'password_hash varchar NOT NULL);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO uporabniki (username, email, password_hash)'
            'VALUES (%s, %s, %s);',
            ('test1',
            'test1@test.si',
            'scrypt:32768:8:1$LPt0H32Pn305bNAd$0fd970fb42704ef5b8690a01dd9815bc13bb83589a264da23c73f47a2b3567c72954197c5854173312de61dc4cc1ecd24b0f60c7b9cd4adcdc6e09b5c26eb178'
            ))


cur.execute('INSERT INTO uporabniki (username, email, password_hash)'
            'VALUES (%s, %s, %s);',
            ('test2',
            'test2@test.si',
            'scrypt:32768:8:1$LPt0H32Pn305bNAd$0fd970fb42704ef5b8690a01dd9815bc13bb83589a264da23c73f47a2b3567c72954197c5854173312de61dc4cc1ecd24b0f60c7b9cd4adcdc6e09b5c26eb178'
            ))

conn_uporabniki.commit()

cur.close()
conn_uporabniki.close()


# skupine
conn_skupine = psycopg2.connect(
        host="localhost",
        database="skupine",
        user="postgres",
        password="123121")

# Open a cursor to perform database operations
cur = conn_skupine.cursor()

# skupine

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS skupine;')
cur.execute('CREATE TABLE skupine (id serial PRIMARY KEY,'
                                 'group_name varchar NOT NULL,'
                                 'group_name_copy varchar NOT NULL);')

# Insert data into the table

cur.execute('INSERT INTO skupine (group_name, group_name_copy)'
            'VALUES (%s, %s);',
            ('test_group1', 'test_group1')
)


cur.execute('INSERT INTO skupine (group_name, group_name_copy)'
            'VALUES (%s, %s);',
            ('test_group2', 'test_group2'
             ))

# clani

cur.execute('DROP TABLE IF EXISTS clani;')
cur.execute('CREATE TABLE clani (id serial PRIMARY KEY,'
                                 'group_id integer NOT NULL,'
                                 'member_id integer NOT NULL);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO clani (group_id, member_id)'
            'VALUES (%s, %s);',
            (1,
             1
             ))


cur.execute('INSERT INTO clani (group_id, member_id)'
            'VALUES (%s, %s);',
            (1,
             2
             ))

conn_skupine.commit()

cur.close()
conn_skupine.close()

# stroski
conn_stroski = psycopg2.connect(
        host="localhost",
        database="stroski",
        user="postgres",
        password="123121")

# Open a cursor to perform database operations
cur = conn_stroski.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS stroski;')
cur.execute('CREATE TABLE stroski (id serial PRIMARY KEY,'
                                 'description varchar (100) NOT NULL,'
                                 'amount integer NOT NULL,'
                                 'group_id integer,'
                                 'payer_id integer NOT NULL);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO stroski (description, amount, group_id, payer_id)'
            'VALUES (%s, %s, %s, %s);',
            ('test_description1',
             100,
             1,
             2
            ))

conn_stroski.commit()

cur.close()
conn_stroski.close()