import streamlit as st
import pandas as pd
from optimizer import (
    get_price_comparison,
    cheapest_store,
    cheapest_items,
    calculate_savings,
    suggest_alternatives
)

st.set_page_config(page_title="Grocery Price Optimizer", layout="wide")

st.title("🛒 Grocery Price Comparison Tool")

st.write(
    "Compare grocery prices across stores and find the cheapest cart option."
)

items = st.text_input("Enter grocery items separated by commas")

if items:

    items_list = [item.strip().lower() for item in items.split(",")]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Price Comparison")

        price_df = get_price_comparison(items_list)

        if price_df.empty:
            st.warning("No items found in dataset.")
        else:
            st.dataframe(price_df)

    with col2:

        st.subheader("🏪 Cheapest Store for Cart")

        cart = cheapest_store(items_list)

        st.dataframe(cart)

        st.bar_chart(cart.set_index("store"))

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("💰 Cheapest Item Options")

        cheapest = cheapest_items(items_list)

        st.dataframe(cheapest)

    with col4:

        st.subheader("💸 Estimated Savings")

        savings = calculate_savings(items_list)

        st.metric("Potential Savings", f"${savings}")

    st.divider()

    st.subheader("🔁 Suggested Alternatives")

    alt_df = suggest_alternatives(items_list)

    if alt_df.empty:
        st.write("No alternatives available.")
    else:
        st.dataframe(alt_df)

    st.divider()

    st.success("Grocery Optimization complete! 🎉")