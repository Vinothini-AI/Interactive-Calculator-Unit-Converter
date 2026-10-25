
import streamlit as st

st.set_page_config(
    page_title="Calculator & Unit Converter",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Interactive Calculator & Unit Converter")
st.write("Calculate numbers and convert common units in one place.")

st.divider()

# Calculator
st.header("1. Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=10.0)

with col2:
    num2 = st.number_input("Enter second number", value=5.0)

operation = st.selectbox(
    "Choose operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)",
     "Division (÷)", "Power (xʸ)", "Modulus (%)"]
)

if st.button("Calculate", type="primary"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        result = None if num2 == 0 else num1 / num2
    elif operation == "Power (xʸ)":
        result = num1 ** num2
    else:
        result = None if num2 == 0 else num1 % num2

    if result is None:
        st.error("Cannot divide or calculate modulus by zero.")
    else:
        st.success(f"Result: {result}")

st.divider()

# Unit converter
st.header("2. Unit Converter")

category = st.selectbox(
    "Choose conversion type",
    ["Length", "Weight", "Temperature"]
)

if category == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Miles", "Feet"]
    to_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Miles": 1609.344,
        "Feet": 0.3048
    }

elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    to_meters = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.45359237,
        "Ounces": 0.028349523125
    }

else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

value = st.number_input("Enter value to convert", value=1.0)
source = st.selectbox("Convert from", units)
target = st.selectbox("Convert to", units, index=1)

if st.button("Convert", type="primary"):
    if category == "Temperature":
        if source == "Celsius":
            celsius = value
        elif source == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        if target == "Celsius":
            result = celsius
        elif target == "Fahrenheit":
            result = celsius * 9 / 5 + 32
        else:
            result = celsius + 273.15

    else:
        result = value * to_meters[source] / to_meters[target]

    st.success(f"{value:g} {source} = {result:.6g} {target}")

st.caption("Built with Python and Streamlit.")