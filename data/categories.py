"""
This module interfaces to our categories data
"""

import data.db_connect as dbc

CATEGORY = 'category'
PASSWORD = 'password'
CATEGORIES_COLLECT = "categories"

# Basic CRUD Operations
def exists(name: str) -> bool:
    dbc.connect_db()
    return dbc.fetch_one(CATEGORIES_COLLECT, {CATEGORY: name})


def add_category(category):
    if exists(category):
        raise ValueError("Categpry already exists.")
    else:
        cat = {}
        cat[CATEGORY] = category
        dbc.connect_db()
        _id = dbc.insert_one(CATEGORIES_COLLECT, cat)
        return _id is not None


def get_category(category):
    if exists(category):
        dbc.connect_db()
        return dbc.fetch_one(CATEGORIES_COLLECT, {CATEGORY: category})
    else:
        raise ValueError(f'{category} not found')


def get_categories():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(CATEGORY, CATEGORIES_COLLECT)


def del_category(category):
    if exists(category):
        dbc.connect_db()
        return dbc.del_one(CATEGORIES_COLLECT, {CATEGORY: category})
    else:
        raise ValueError(f'Delete failure: {CATEGORY} not in database.')

