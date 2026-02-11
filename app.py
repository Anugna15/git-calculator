import streamlit as st
import operation

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate"):
    if operation == "Addition":
        result = operation.add(num1, num2)
    elif operation == "Subtraction":
        result = operation.subtract(num1, num2)
    elif operation == "Multiplication":
        result = operation.multiply(num1, num2)
    elif operation == "Division":
        result = operation.divide(num1, num2)

    st.success(f"Result: {result}")
