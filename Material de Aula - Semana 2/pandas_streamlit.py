import streamlit as st
import pandas as pd

def main():
    st.title('AceleraDev Data Science')
    st.image('logo.png')
    file = st.file_uploader('Upload your file', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 0,100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown('Markdown')
        st.table(df.head(slider))
        st.write(df.columns)
        st.table(df.groupby('species')['petal_length'].mean())

if __name__ == '__main__':
    main()