# USERSNACK Backend service

Hello, welcome to brief introduction to these few APIs I've been given as an entry task for Usersnap.

## Deployment

I've included stack.yml, which enables us to easily set up Postgres docker container. It can be done using

```docker-compose -f stack.yml up```

As a slight TODO we might add API service itself to the .yml file, but as of now I found running the API easier separately during development.

Included in this repo, under `data` directory, are a couple of helper scripts which enable us to create and fill appropriate databases from inside the container. Also, as a TODO, these actions can be added to the startup script.

Startup script may be used via following commands from `/opt/usersnap` dir:

```
$ psql -U postgres -f import.sql
$ python parse.py
```

Afterwards, API can be run as a normal python script:

```python api.py```

Following endpoints are available:

1. - `<server>/list/pizzas`
   - `<server>/list/extras`

   These paths return lists of available pizzas and extras, respectively, in following format:

```
{
  "pizzas":
    [
      {
        "id": integer representing unique identificator of our pizza,
        "name": string naming this pizza,
	"price": integer, price of base pizza,
	"ingredients": list of pizza ingredients,
	"img": name of image file representing our pizza
      },
      ...
    ]
}

{
  "extras":
    [
      {
        "name": name of extra,
	"price": price of extra to be added
      }
    ]
}
```
     

2. - `<server>/extrasfor/<pizza_id>`

  Lists available extras for given pizza, in format:
  ```
  {
    "extrasfor":
      [
        "extra1",
	"extra2",
	...
      ]
  }
  ```

3. - `<server>/price/<pizza_id>?extra=extra1&extra=extra2...`
Returns price for pizza, with optional extras we can add.

Return format:
```{
"price": integer price
}```
