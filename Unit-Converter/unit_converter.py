import streamlit as st


def convert_units(value, unit_from, unit_to):
    conversions = {"Kilometers to Meters": 1000,  # 1 Kilometer=1000 meters
                   "Meters to Kilometers": 0.001,  # 1 meter = 0.001 kilometer
                   "Kilograms to Grams": 1000,  # 1 Kilogram = 1000 gram
                   "Grams to Kilograms": 0.001  # 1 Gram = 0.001 Kilogram
                   }

    # Genearte a key based on the input and output units
    key = f"{unit_from} to {unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return value*conversion
    else:
        st.error(f"Conversion from {unit_from} to {unit_to} is not supported.")
        return None


st.set_page_config(page_title="📊 Unit Converter", layout="centered")
st.title("📊 Unit Converter by Hafiz Siddiqui")
st.info("This app converts values between different units 📊")
value = st.number_input("Enter the value for Conversion:")
unit_from = st.selectbox(
    "Convert from", ["Kilometers", "Meters", "Kilograms", "Grams"])
unit_to = st.selectbox(
    "Convert to", ["Kilometers", "Meters", "Kilograms", "Grams"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if result is not None:
        st.write(f"Result:{result}")
        st.success("🎊 Value converted successfully 🎉")
