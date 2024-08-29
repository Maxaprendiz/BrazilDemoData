import streamlit as st
from functions import *


def make_sidebar():
    '''
    Creates sidebar with two selectbox, one for language (Portuguese Br or English), 
    and the other for selecting a colormap for the plots.
    '''
    with st.sidebar:
        lang, color_theme, selected_option = None, None, None
        st.title('🇧🇷 Brazil By Numbers')
        lang = st.radio(
        "Pick a language",
        ["English", "Portuguese (Brazil)"], index=None)
    
        if lang == 'Portuguese (Brazil)':
            st.subheader('Opções para escolha')
            selected_option = st.selectbox('Selecione os dados que gostaria de ver', ['População Por Estado', 'Taxa de Crescimento da População', 'Razão entre Sexos', 'Idade', 'Raça'],index=None, placeholder="Selecione aqui...")

        if lang == 'English':
            st.subheader('Options to choose from')
            selected_option = st.selectbox("Select data you'd like to see", ['Population by State', 'Population Growth Rate', 'Gender Ratio', 'Age', 'Race'],index=None, placeholder="Pick an option...")

        if lang != None:
            color_theme_list = ['aggrnyl', 'agsunset', 
                'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 
                'brwnyl', 'cividis', 'curl',
                'darkmint', 'emrld','greens', 'greys',
                'jet','magenta', 'magma',
                'oranges', 'oryel', 'plotly3', 'purples',
                'rainbow', 'reds', 'sunset', 'sunsetdark', 'teal', 'viridis']

            if lang == "Portuguese (Brazil)":
                selected_color_theme = st.selectbox('Selecione Uma Opção de Mapa de Cor para os Gráficos', color_theme_list,index=None, placeholder="Selecione aqui...")

            if lang == 'English':
                selected_color_theme = st.selectbox('Pick a Colormap for the Plots', color_theme_list,index=None, placeholder="Pick a colormap...")

            if selected_color_theme == None:
                selected_color_theme = 'viridis'
            color_theme = selected_color_theme

    return lang, color_theme, selected_option

    
