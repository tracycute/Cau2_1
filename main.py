import streamlit as st

st.title("Thực hiện phép toán hai số thực")

number1 = st.number_input("Nhập số thực thứ nhất:", format="%f")
number2 = st.number_input("Nhập số thực thứ hai:", format="%f")

tong = number1 + number2
hieu = number1 - number2
tich = number1 * number2

if number2 != 0:
    thuong = number1 / number2
else:
    thuong = "Số chia phải khác 0."

st.write(f"Tổng: {tong}")
st.write(f"Hiệu: {hieu}")
st.write(f"Tích: {tich}")
st.write(f"Thương: {thuong}")

#https://21520255-cau-2-1.streamlit.app/
