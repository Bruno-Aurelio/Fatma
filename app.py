import streamlit as st

st.set_page_config('ECOP06')

st.title('Aula de ECOP06')



st.markdown('''
# Este site é muito bacana
            
Pois ele é feito em markdown. Assim se eu quiser um link é só escrever [Globo.com](https://www.globo.com)
            ''')
st.subheader('Site Demonstrativo da disciplina de ECOP06')

st.image('https://th.bing.com/th/id/OIP.IkzAsJv_fhHpsHiqPsD2mQHaHa?pid=ImgDet&rs=1', 'kkkkkkkkkkkk', 512)

if st.button('Pressione Aqui'):
    st.text('Grande Coisa...')