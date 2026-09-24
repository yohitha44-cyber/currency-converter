import streamlit as st
import requests
from dateutil.parser import parse

st.title("Currency Converter")

source_currency = st.text_input("Source currency (e.g. USD)", "USD").upper()
destination_currency = st.text_input("Destination currency (e.g. EUR)", "EUR").upper()
amount = st.number_input("Amount", min_value=0.0, value=100.0)

if st.button("Convert"):
    try:
        url = f"https://open.er-api.com/v6/latest/{source_currency}"
        data = requests.get(url, timeout=10).json()

        if data.get("result") != "success":
            st.error("Invalid source currency or API error.")
        else:
            rates = data["rates"]
            if destination_currency not in rates:
                st.error("Invalid destination currency.")
            else:
                converted = rates[destination_currency] * amount
                last_updated = parse(data["time_last_update_utc"])
                st.success(f"{amount} {source_currency} = {converted:.2f} {destination_currency}")
                st.caption(f"Last updated: {last_updated}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")