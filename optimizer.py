import pandas as pd

def load_data():
    df = pd.read_csv("data/grocery_prices.csv")
    df["item"] = df["item"].str.lower()
    return df

def get_price_comparison(items):
    df = load_data()
    return df[df["item"].isin(items)]

def cheapest_store(items):
    df = load_data()
    df = df[df["item"].isin(items)]

    cart_prices = df.groupby("store")["price"].sum().reset_index()
    cart_prices = cart_prices.sort_values("price")

    return cart_prices

def cheapest_items(items):
    df = load_data()
    df = df[df["item"].isin(items)]

    cheapest = df.loc[df.groupby("item")["price"].idxmin()]

    return cheapest

def calculate_savings(items):
    df = load_data()
    df = df[df["item"].isin(items)]

    max_prices = df.groupby("item")["price"].max().sum()
    min_prices = df.groupby("item")["price"].min().sum()

    savings = round(max_prices - min_prices, 2)

    return savings

def suggest_alternatives(items):

    alternatives = {
        "milk": "store brand milk",
        "bread": "whole wheat bread",
        "eggs": "cage-free eggs",
        "rice": "brown rice",
        "chicken": "chicken thighs"
    }

    suggestions = []

    for item in items:
        if item in alternatives:
            suggestions.append({
                "item": item,
                "alternative": alternatives[item]
            })

    return pd.DataFrame(suggestions)