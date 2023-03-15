import streamlit as st


st.title("Tip Calculator")

bill = st.number_input("What is the total check value? ")
percent = st.number_input("How much would you like to tip in %? ", step = 0.5)
people = st.number_input("How many people? ",step = 1)
#comment
total_bill = round(bill + (bill * percent / 100), 2)

total_bill_per_person = round((bill + (bill * percent / 100)) / people, 2)

st.success(f"The total is {total_bill}. The total bill per person is {total_bill_per_person}")



