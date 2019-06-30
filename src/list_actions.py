import psycopg2

from src.list_queries import LIST_PIZZAS_QUERY, LIST_EXTRAS_QUERY, LIST_PIZZA_INGREDIENTS_QUERY, LIST_EXTRAS_PRICE_QUERY, LIST_PIZZA_PRICE_QUERY
from src.dict_skeletons import PIZZA_JSON, EXTRA_JSON


def list_pizzas():
    """
    Fetch all available pizzas
    :return: string list of available pizzas
    """
    _connection, _cursor = init_connection()
    _cursor.execute(LIST_PIZZAS_QUERY)

    pizzas_data = _cursor.fetchall()

    pizzas_list_str = ",".join([PIZZA_JSON.format(*x) for x in pizzas_data])
    pizzas_list_str = pizzas_list_str.replace("'", '"')  # for ingredients are not properly formatted TODO: fix this
    _connection.close()

    return pizzas_list_str


def list_extras():
    """
    Fetch all available extras
    :return: string list of available extras
    """
    _connection, _cursor = init_connection()
    _cursor.execute(LIST_EXTRAS_QUERY)

    extras_data = _cursor.fetchall()

    extras_list_str = ",".join([EXTRA_JSON.format(*x) for x in extras_data])
    _connection.close()

    return extras_list_str


def list_ingredients_for_pizza(pizza_id):
    """
    Fetch
    :param pizza_id: integer id of our pizza
    :return: Unlike previous two methods, this one returns list, not str of list
    """
    _connection, _cursor = init_connection()
    _cursor.execute(LIST_PIZZA_INGREDIENTS_QUERY.format(pizza_id))

    ingredients = _cursor.fetchall()  # As pizza_id is primary key, only one list is expected

    _connection.close()
    return ingredients


def list_pizza_price(pizza_id, extras=None):
    """
    Return full pizza price, including extras
    :param pizza_id:  integer id of the pizza
    :param extras: list of extras we potentially want to add to our pizza. Presumption is that it does not contain
                    ingredients already present in pizza, as list_extras() returns filtered list
    :return: integer representing final price
    """
    _connection, _cursor = init_connection()
    _cursor.execute(LIST_PIZZA_PRICE_QUERY.format(pizza_id))

    if not extras:
        return _cursor.fetchall()[0][0]

    pizza_price = _cursor.fetchall()[0][0]
    extras_string = " OR ".join(["name = '{}'".format(x) for x in extras])
    _cursor.execute(LIST_EXTRAS_PRICE_QUERY.format(extras_string))
    extras_price = _cursor.fetchall()[0][0]

    return pizza_price + extras_price


def init_connection():
    _connection = psycopg2.connect(database='postgres', user='postgres', password='example', host='localhost',
                                   port='5432')
    _cursor = _connection.cursor()
    return _connection, _cursor


LIST_ACTIONS = {
    'pizzas' : list_pizzas,
    'extras' : list_extras,
    'ingred' : list_ingredients_for_pizza,
    'price'  : list_pizza_price
}