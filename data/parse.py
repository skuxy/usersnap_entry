import json
import psycopg2


connection = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='example',
        host='127.0.0.1',
        port='5432')
cursor = connection.cursor()

with open('pizzas.json') as p_file:
    content = p_file.read()
    parsed_content = json.loads(content)

    for e in parsed_content:
        cursor.execute(
            "INSERT INTO pizzas VALUES ({}, '{}', {}, ARRAY [ {} ], '{}')".format(
                e['id'],
                e['name'],
                e['price'],
                ','.join(["'{}'".format(x) for x in e['ingredients']]),
                e['img']
            )
        )

    connection.commit()

with open('extras.json') as p_file:
    content = p_file.read()
    parsed_content = json.loads(content)

    for e in parsed_content:
        cursor.execute(
            "INSERT INTO extras VALUES ('{}', {})".format(
                e['name'],
                e['price'],
            )
        )

    connection.commit()

connection.close()
