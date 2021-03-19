import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():

    menu = ['Select', 'Insert', 'Update', 'Delete']
    choice = st.sidebar.selectbox('MENU', menu)

    if choice == 'Select' :
        st.subheader('Select 화면입니다.')
    elif choice == 'Insert' :
        st.subheader('Insert 화면입니다.')
    elif choice == 'Update' :
        st.subheader('Update 화면입니다.')
    else :
        st.subheader('Delete 화면입니다.')


if __name__=='__main__':
    main()