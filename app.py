import streamlit as st

# Title of the app
st.title("🌡️ Temperature Converter")

# Input temperature
temperature = st.number_input("Enter the temperature value:")

# Select input unit
input_unit = st.selectbox("Select the input unit:", ["Celsius", "Fahrenheit", "Kelvin"])

# Select output unit
output_unit = st.selectbox("Select the unit to convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

def convert_temperature(temp, from_unit, to_unit):
    # Convert input temperature to Celsius first
    if from_unit == "Fahrenheit":
        temp_c = (temp - 32) * 5/9
    elif from_unit == "Kelvin":
        temp_c = temp - 273.15
    else:
        temp_c = temp

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (temp_c * 9/5) + 32
    elif to_unit == "Kelvin":
        return temp_c + 273.15
    else:
        return temp_c

# Convert and display result
if input_unit == output_unit:
    st.write(f"Output Temperature: {temperature:.2f} °{output_unit[0]}")
else:
    result = convert_temperature(temperature, input_unit, output_unit)
    st.success(f"Converted Temperature: {result:.2f} °{output_unit[0]}")
