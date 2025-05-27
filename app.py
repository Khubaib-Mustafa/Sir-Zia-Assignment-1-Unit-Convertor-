import streamlit as st

# Title & Description
st.title("⚙️ Unit Converter")
st.markdown("### Convert between different units of measurement easily")

# Conversion mappings with lambda functions
conversion_factors = {
    "Length": {
        "Kilometers to Miles": lambda v: v * 0.621371,
        "Miles to Kilometers": lambda v: v / 0.621371
    },
    "Weight": {
        "Kilograms to Pounds": lambda v: v * 2.20462,
        "Pounds to Kilograms": lambda v: v / 2.20462
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda v: (v * 9 / 5) + 32,
        "Fahrenheit to Celsius": lambda v: (v - 32) * 5 / 9
    },
    "Volume": {
        "Liters to Gallons": lambda v: v * 0.264172,
        "Gallons to Liters": lambda v: v / 0.264172
    },
    "Time": {
        "Seconds to Minutes": lambda v: v / 60,
        "Minutes to Seconds": lambda v: v * 60,
        "Hours to Minutes": lambda v: v * 60,
        "Minutes to Hours": lambda v: v / 60,
        "Days to Hours": lambda v: v * 24,
        "Hours to Days": lambda v: v / 24,
        "Weeks to Days": lambda v: v * 7,
        "Days to Weeks": lambda v: v / 7
    }
}

# Select category
category = st.selectbox("📏 Select Conversion Type", conversion_factors.keys())

# Select unit based on category
unit = st.selectbox("🔄 Select Unit", conversion_factors[category].keys())

# Input value
value = st.number_input("🔢 Enter value to convert", min_value=0.0, step=0.1)

# Convert button
if st.button("🚀 Convert"):
    result = conversion_factors[category][unit](value)
    st.success(f"✅ Converted Value: {result:.2f} {unit.split(' to ')[-1]}")

# Developer credit
st.markdown("---")
st.markdown("### Developed by [Khubaib Mustafa]")
st.markdown("### Source Code: [GitHub Repository]")
