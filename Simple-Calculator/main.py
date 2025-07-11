import streamlit as st


def main():
    # Set page title and configuration
    st.set_page_config(page_icon="🖩", page_title="Simple Calculator", layout="centered")
    st.title(
        "🧮 Simple Calculator by [Hafiz Siddiqui](https://www.linkedin.com/in/hafiz-siddiqui-018587295)"
    )
    st.write("Enter two numbers and choose an operation")

    # Create two columns for number inputs
    col1, col2 = st.columns(2)

    # Input fields for numbers
    with col1:
        num1 = st.number_input("Enter first number", value=0)
    with col2:
        num2 = st.number_input("Enter second number", value=0)

    # Operation selection
    operation = st.radio(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
    )

    # Calculate button
    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.warning("⚠️ Error: Division by zero is not possible!")
                    return
                result = num1 / num2
                symbol = "÷"

            # Display result with styling
            st.success(f"🎊 {num1} {symbol} {num2} = {result}")
            st.balloons()

        except Exception as e:
            st.error(f"🛑 An error occurred: {str(e)}")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
