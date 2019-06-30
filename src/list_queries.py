LIST_PIZZAS_QUERY = '''
    SELECT * FROM pizzas;
'''

LIST_EXTRAS_QUERY = '''
    SELECT * FROM extras;
'''

LIST_PIZZA_INGREDIENTS_QUERY = '''
    SELECT ingredients FROM pizzas WHERE "id" = {} ;
'''

LIST_PIZZA_PRICE_QUERY = '''
    SELECT price FROM pizzas WHERE "id" = {} ;
'''

# where name = x or name = y or...
LIST_EXTRAS_PRICE_QUERY = '''
    SELECT sum(price) FROM extras WHERE {} ; 
'''
