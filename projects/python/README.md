# Python projects

This folder contain different projects that you can start implementing to learn new things with python that are required in a working environment.

## Project 1: Create an API

Candidates are required to create a backend API using FastAPI in Python, demonstrating their expertise with various technologies including Poetry, Ruff, Pytest, SQLAlchemy, and if possible, Polars.

The project involves

### Mandatory requirements

- Libraries installation: Use poetry to initialize and install the libraries of the project
- External API Integration: Connect to a freely available external API to fetch data, selecting an API from the list of those available in the project.
- Data Manipulation: Utilize Pandas (preferably Polars) for data manipulation. The idea it’s to manipulate and simplify the data that needs to be stored inside the project.
- Database Interaction: Store manipulated data in a PostgreSQL database using SQLAlchemy ORM.
- API Functionality: Develop APIs that allow launching CRUD operations, saving and retrieving results from the API.
- Docstrings and Typings: use docstrings in the functions and typings in Python
- Data validation: Use Pydantic for data validation in the API

Important libraries to be used in the project: Poetry, FastAPI, Ruff, SqlAlchemy, Pandas (or Polars), Mypy, and Pydantic.

### Additional requirements

These requirements are not mandatory, but they represent a plus in the final evaluation.
It is very important that mandated requirements instead are met.

- Dockerization: It’s beneficial to have the dockerize project to be able to launch it using Docker Compose.
- Cache system: Use a cache system to cache the data (with Redis or memcache).
- Testing and Documentation: It’s not mandatory but suggested to implement tests using Pytest and generate a simple automatic documentation of the methods used inside the project using MKDocs, MKDocs material, and MKDocstring.

### Public APIs for Data Retrieval

List of public APIs for Data retrieval suggested for the task.

- [Open Weather Map](https://openweathermap.org/api): For accessing weather data.
- [Rest Countries](https://restcountries.com/): To fetch information about countries.
- [The Dog API](https://thedogapi.com/): For data on various dog breeds.
- [Stars Wars API](https://swapi.dev/): All the Star Wars data.
- [NASA API](https://api.nasa.gov/): Provides access to a range of data from NASA missions, including satellite imagery, Mars Rover photos, and space science datasets.
- [COVID-19 API](https://covid19api.com/): Offers up-to-date data about the COVID-19 pandemic, including cases, deaths, and vaccination statistics by country.
- [CoinGecko API](https://www.coingecko.com/en/api): Ideal for cryptocurrency enthusiasts, this API provides comprehensive data about various cryptocurrencies, including price, volume, market cap, and historical data.
- [The Cat API](https://thecatapi.com/ ): Similar to The Dog API, it provides various cat images and data, suitable for more light-hearted applications.
- [OpenCage Geocoder](https://opencagedata.com/api): Offers forward and reverse geocoding of locations using coordinates or addresses. Useful for applications requiring location data processing.
- [NewsAPI](https://newsapi.org/): Provides a way to access current news articles from various sources and countries, which can be useful for natural language processing or content aggregation projects.
- [PokéAPI](https://pokeapi.co/): A fun API for accessing data about Pokémon, including their types, abilities, and stats. Ideal for projects that might involve data structuring and categorization.

## Project 2: create a Python Package

Design a data python package

## Project 3: create a streamlit application

Create a streamlit application to visualise some data

## Project 4: create a Flask simple we application

Create a simple web application using flask with a frontend.

If you want you can also use **django** this is just a high level requirement.

