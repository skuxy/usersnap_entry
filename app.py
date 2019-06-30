from flask import Flask
from flask import Response
from flask import request

from src.list_actions import LIST_ACTIONS

app = Flask(__name__)


@app.route('/list/<what>')
def list_action(what):
    """
    Returns all entries for what
    :param what: What we wish to list.
    :return: As of now, only string list of all pizzas and all extras
    """
    actions = LIST_ACTIONS

    if what not in actions:
        return Response('Unable to list {}'.format(what), status=400)

    action_data = actions[what]()
    response_str = '{{"{}":[{}]}}'.format(what, action_data)

    return Response(response_str, status=200)


@app.route('/extrasfor/<pizza_id>')
def extras_for_pizza(pizza_id):
    """
    The other way is to parse this information on client side, and also it sounds like a more reasonable way
    :param pizza_id: Pizza for which we want to fetch available extras
    :return: List of available extras for our pizza
    """
    all_extras = LIST_ACTIONS['extras']()
    pizza_extras = LIST_ACTIONS['ingred'](pizza_id)

    if not pizza_extras:
        return Response('No pizza under id {}'.format(pizza_id), status=404)

    available_extras = set(all_extras) - set(pizza_extras)
    available_extras_str = ', '.join(['"{}"'.format(x) for x in available_extras])
    response_str = '{{"extrasfor": [{}]}}'.format(available_extras_str)

    return Response(response_str, status=200)


@app.route('/price/<pizza_id>')
def price(pizza_id):
    """
    Fetches price for freshly baked pizza
    :param pizza_id: integer representing ID of sought pizza
    :return: ..price. Float
    """
    extras = request.args.getlist('extra')
    pizza_price = LIST_ACTIONS['price'](pizza_id, extras)

    response_str = '{{"price":{}}}'.format(pizza_price)
    return Response(response_str, status=200)


if __name__ == '__main__':
    app.run()
