import streamlit as st

def main():
    st.title('Hello World')

    st.markdown('Botao')
    botao = st.button('Botao')
    if botao:
        st.markdown('Clicado')

    st.markdown('checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicado')

    st.markdown('Radio')
    radio = st.radio('Escolha as opcoes',('Opt 1','Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1 Clicked')
    if radio == 'Opt 2':
        st.markdown('Opt 2 Clicked')

    st.markdown('SelectBox')
    select = st.selectbox('Chosse opt', ('Opt1','Opt 2'))
    if select == 'Opt1':
        st.markdown('Opt1 Clicked')
    if select == 'Opt 2':
        st.markdown('Opt2 Clicked')

    st.markdown('MultiSelect')
    multi = st.multiselect('Choose :', ('Opt1', 'Opt2'))
    if multi == 'Opt1':
        st.markdown('Opt1 Clicked')
    if multi == 'Opt2':
        st.markdown('Opt2 Clicked')

    st.markdown('FileUploader')
    file = st.file_uploader('Drag your files .csv here', type='csv')
    if file is not None:
        st.markdown('It is not empty')

if __name__ == '__main__':
    main()