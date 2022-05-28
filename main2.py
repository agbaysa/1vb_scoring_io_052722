import streamlit as st
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import time
import streamlit as st

st.image("1vb.png")

pw = st.text_input("Password:", type="password", value="xxx")


if pw == "xxx":
    st.write("Please enter the password.")
elif pw != 'admin':
    st.write("The password you entered is incorrect. Please enter the correct password.")
else:
    model_dt = pickle.load(open('model_dt', 'rb'))

    st.write("The password you entered is correct.")
    st.write("")
    st.write("Please upload your csv file. Please ensure that the columns and column titles are in the correct format using the template.")
    df = st.file_uploader("Please choose your csv file.", accept_multiple_files=False, type='csv')


    if df is None:
        st.write("...")
    else:
        df1 = pd.read_csv(df)
        st.dataframe(df1)

        predict = pd.Series(model_dt.predict(df1.drop(['source','agreementid'], axis=1)))
        foo = pd.concat([df1, predict], axis=1)
        foo.rename(columns={0: 'predict'}, inplace=True)

        st.write("The file has been uploaded and scored.")
        st.write("")
        st.write("Please download the output file by clicking the download button below.")

        foo2 = foo.to_csv().encode('utf-8')

        st.download_button(label="Download data as CSV",
         data=foo2,
         file_name='1vb_scoring.csv',
         mime='text/csv')





    