import streamlit as st

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱"
)

st.title("💱 Currency Converter")

# Currency options
currencies = {
    "USD - US Dollar": "USD",
    "INR - Indian Rupee": "INR",
    "EUR - Euro": "EUR",
    "GBP - British Pound": "GBP",
    "JPY - Japanese Yen": "JPY",
    "AUD - Australian Dollar": "AUD",
    "CAD - Canadian Dollar": "CAD",
    "SGD - Singapore Dollar": "SGD",
    "AED - UAE Dirham": "AED"
}

# Select currencies
from_currency = st.selectbox(
    "From Currency",
    list(currencies.keys())
)

to_currency = st.selectbox(
    "To Currency",
    list(currencies.keys())
)

# Amount
amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=1.0
)

# Convert button
if st.button("Convert"):
    from_code = currencies[from_currency]
    to_code = currencies[to_currency]

    if from_code == to_code:
        result = amount
    else:
        # Sample conversion rates
        rates = {
            ("USD", "INR"): 83.5,
            ("INR", "USD"): 0.012,
            ("USD", "EUR"): 0.92,
            ("EUR", "USD"): 1.09,
            ("USD", "GBP"): 0.78,
            ("GBP", "USD"): 1.28,
            ("USD", "JPY"): 150.0,
            ("JPY", "USD"): 0.0067,
            ("USD", "AED"): 3.67,
            ("AED", "USD"): 0.27,
        }

        rate = rates.get((from_code, to_code), 1)
        result = amount * rate

    st.success(
        f"{amount:.2f} {from_code} = {result:.2f} {to_code}"
    )