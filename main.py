import streamlit as st
import functions
# Streamlit App
st.title("Password Generator")

# Number of letters
numb_l = st.number_input("How many letters do you want in your password:", min_value=0, max_value=100)

# Number of numbers
numb_n = st.number_input("How many numbers do you want in your password:", min_value=0, max_value=100)

# Number of symbols
numb_s = st.number_input("How many symbols do you want in your password:", min_value=0, max_value=100)

# Password strength
difficulty = st.selectbox("Select the difficulty level of the password", ("Weak", "Normal", "Strong"))

# Generate Password Button
if st.button("Generate Password"):
    password = functions.generate_password(numb_l, numb_n, numb_s, difficulty)
    
    # Display the generated password
    st.success(f"Your generated password is: {password}")
    