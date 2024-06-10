# Overview
Desafio em que consumi a API do starwars [swapi.dev](https://swapi.dev/) na qual requisição para todos os personagens e também para os personagens conforme sua id.\
O diferencial na requisição por personagens está em a api retornar os seus dados e mais 3 sugestões aleatórias de personagens, conforme seu planeta de origem.\
A API foi desenvolvida em Python e Django REST Framework.\
Futuramente, irei aplicar o desenvolvimento nos demais endpoints das entidades (planeta, filmes, etc...)

# Getting Started
**Pre requisites:**
* Python 3.11.1

## Step by Step:
1. Clone o repositório
2. Instale as bibliotecas do arquivo requirements.txt
```
pip install -r requirements.txt
```
3. Execute o arquivo manage.py, passando runserver como parametro
```
py manage.py runserver
```
# Base URL
A base URL é ```127.0.0.1:8000/```

# Endpoints
**Request Character**
```python
GET api/character/{id}
```

```json
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "species": [],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/",
    "related": [
        {
            "id": "6",
            "name": "Owen Lars",
            "relation": "https://swapi.dev/api/planets/1/"
        },
        {
            "id": "43",
            "name": "Shmi Skywalker",
            "relation": "https://swapi.dev/api/planets/1/"
        },
        {
            "id": "2",
            "name": "C-3PO",
            "relation": "https://swapi.dev/api/planets/1/"
        }
    ]
}
```
**Request all characters**
```python
GET api/character/
GET api/character/?page={id_page}
```
```json
{
    "count": 82,
    "next": "https://swapi.dev/api/people/?page=2",
    "previous": null,
    "results": [
        {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "77",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "https://swapi.dev/api/people/1/"
        },
    ]
}
```
# Swagger Documetation
```
http://127.0.0.1:8000/swagger/
```
