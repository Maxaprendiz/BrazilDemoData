import streamlit as st
from load_data import load_data
from functions import *
from ui import make_sidebar
from utils import load_css
import plotly.express as px



##########################################################################
##########################################################################


def main():
    st.set_page_config(
    page_title="Brazil by Numbers",
    page_icon='🇧🇷',
    layout="wide",
    initial_sidebar_state="expanded")
    load_css()

    (geojson, df_regions, df_population, df_population_growth, df_sex_ratio, df_idade, df_population_reg, df_population_growth_year, 
    df_sexos_brasil, df_idade_cor, df_densidade, df_race, df_alfabetizacao) = load_data()

    lang, color_theme, selected_option = make_sidebar()
   
    col = st.columns((2, 4.5, 1.5), gap='medium')

    if lang:
        with col[0]:
            if selected_option == None:
                if lang == "English":
                    st.subheader('Brazil')
                    st.write('''
                            • Largest country in Latin America \n
                            • Fifth largest in the world by land area \n
                            • Seventh largest country in the world by population \n
                            • Brazil's nominal GDP is the ninth largest in the world \n
                            • Most Brazilians are descended from the country's indigenous peoples, Portuguese settlers, European immigrants, and African slaves \n
                            • The Brazilian Constitution provides for freedom of religion \n
                            • Church and state are officially separated, with Brazil being a secular country''')
                else:
                    st.subheader('Brasil')
                    st.write('''
                            • Maior país da América Latina \n
                            • Quinto maior do mundo em área territorial\n
                            • Sétimo maior país do mundo em termos populacionais\n
                            • O PIB nominal brasileiro é o nono maior do mundo\n
                            • A maioria dos brasileiros descende de povos indígenas do país, colonos portugueses, imigrantes europeus e escravos africanos\n
                            • A Constituição brasileira prevê liberdade de religião\n
                            • Igreja o Estado são oficialmente separados, sendo o Brasil um país secular''')

            if selected_option == 'População Por Estado' or selected_option =='Population by State': 
                fig = plot_piechart_population(df_population_reg, lang, color_theme)
                st.plotly_chart(fig, use_container_width=True)
                if lang == "English":
                    show_extreme_data(df_population, 'population', 'Population', 'Population', lang)
                else:
                    show_extreme_data(df_population, 'population', 'População', 'População', lang)
            
            if selected_option == 'Taxa de Crescimento da População' or selected_option == 'Population Growth Rate': 
                fig = plot_barchart_population_growth(df_population_growth_year, lang, color_theme)
                st.plotly_chart(fig, use_container_width=True)
                if lang == "English":
                    show_extreme_data(df_population_growth, 'taxa_crescimento', 'Population Growth', 'Ratio', lang)
                else:
                    show_extreme_data(df_population_growth, 'taxa_crescimento', 'Crescimento Populacional', 'Taxa', lang)
                
            if selected_option == 'Razão entre Sexos' or selected_option == 'Gender Ratio': 
                fig = plot_piechart_genders(df_sexos_brasil, lang, color_theme)
                st.plotly_chart(fig, use_container_width=True)
                if lang == "English":
                    show_extreme_data(df_sex_ratio, 'razao_sexos', 'Number of Men', 'Ratio', lang)
                else:
                    show_extreme_data(df_sex_ratio, 'razao_sexos', 'Número de Homens', 'Razão', lang)
            
            if selected_option == 'Idade' or selected_option == 'Age': 
                fig = plot_barchart_age_race(df_idade_cor, lang, color_theme)
                st.plotly_chart(fig, use_container_width=True)
                if lang == "English":
                    show_extreme_data(df_idade, 'idade', 'Median Age', 'Median Age', lang)
                else:
                    show_extreme_data(df_idade, 'idade', 'Idade Mediana', 'Idade Mediana', lang)

            if selected_option == 'Raça' or selected_option == 'Race': 
                fig1, fig2 = plot_piechart_race(df_race, lang, color_theme)
                st.plotly_chart(fig1, use_container_width=True)
                st.plotly_chart(fig2, use_container_width=True)

        with col[1]:
            if selected_option == None:
                
                if lang == "Portuguese (Brazil)":
                    var_color = "regiao"
                    st.markdown('#### Brasil - Regiões')
                    label = {'name':'Estado',
                            'region': 'Região'}
                else:
                    var_color = "region"
                    st.markdown('#### Brazil - Regions')
                    label = {'name':'State',
                            'region': 'Region'}
                choropleth = make_choropleth(df_regions, geojson, label, var_color, color_theme)  
                st.plotly_chart(choropleth, use_container_width=True)

            if selected_option == 'População Por Estado' or selected_option =='Population by State':
                if lang == "Portuguese (Brazil)":
                    st.markdown('#### Brasil - População Por Estado')
                else:
                    st.markdown('#### Brazil - Population by State')
                choropleth = make_choropleth_population(df_population, geojson, color_theme, lang)
                st.plotly_chart(choropleth, use_container_width=True)

            if selected_option == 'Taxa de Crescimento da População' or selected_option == 'Population Growth Rate': 
                var_color = "taxa_crescimento"
                if lang == "Portuguese (Brazil)":
                    st.markdown('#### Brasil - Taxa de Crescimento da População')
                    label = {'name':'Estado',
                            'taxa_crescimento': 'Taxa de Crescimento (%)'}
                else:
                    st.markdown('#### Brazil - Population Growth Rate')
                    label = {'name':'State',
                            'taxa_crescimento': 'Population Growth (%)'}
                choropleth = make_choropleth(df_population_growth, geojson, label, var_color, color_theme)  
                st.plotly_chart(choropleth, use_container_width=True)

            if selected_option == 'Razão entre Sexos' or selected_option == 'Gender Ratio': 
                var_color = "razao_sexos"
                if lang == "Portuguese (Brazil)":
                    st.markdown('#### Razão entre Sexos')
                    label = {'name':'Estado',
                            'razao_sexos': 'Razão entre Sexos'}
                else:
                    st.markdown('#### Gender Ratio')
                    label = {'name':'State',
                            'razao_sexos': 'Gender Ratio'}

                choropleth = make_choropleth(df_sex_ratio, geojson, label, var_color, color_theme)  
                st.plotly_chart(choropleth, use_container_width=True)

            if selected_option == 'Idade' or selected_option == 'Age': 
                var_color = "idade"
                if lang == "Portuguese (Brazil)":
                    st.markdown('#### Idade da População')
                    label = {'name':'Estado',
                            'idade': 'Idade Mediana'}
                else:
                    st.markdown('#### Population Age')
                    label = {'name':'State',
                            'idade': 'Median Age'}
                choropleth = make_choropleth(df_idade, geojson, label, var_color, color_theme)  

                st.plotly_chart(choropleth, use_container_width=True)

            if selected_option == 'Raça' or selected_option == 'Race': 
                fig1, fig2 = plot_barchart_school(df_alfabetizacao, lang, color_theme)
                st.plotly_chart(fig1, use_container_width=True)
                st.plotly_chart(fig2, use_container_width=True)
                
            
            if selected_option != None:
                st.html('<br/>') 
                if lang == "English":
                    st.html('<h3>Some facts about Brazil</h3>') 
                if lang == "Portuguese (Brazil)":
                    st.html('<h3>Alguns fatos sobre o Brasil</h3>') 
                st.write(aleatory_facts(lang)) 


    with col[2]:
        with st.container(height=250):
            if lang == "Portuguese (Brazil)":
                st.write('''
                    :blue[***Sobre***]
                    - App Criado por: [Aprendiz Artificial](<https:www.aprendizartificial.com>).
                    - :blue[**Feito com**]: Geopandas, Pandas, Plotly e Streamlit 
                    ''')
            else:
                st.write('''
                        :blue[***About***]
                        - Made by: [Aprendiz Artificial](<https:www.aprendizartificial.com>)
                        - :blue[**Made with**]: Geopandas, Pandas, Plotly, and Streamlit 
                        ''')
        if selected_option != None:
            if lang == "Portuguese (Brazil)":    
                with st.expander('Sobre os Dados e Textos', expanded=False): 
                        st.write('''
                            - Dados: [IBGE](<https://censo2022.ibge.gov.br/panorama/>).
                            - :orange[**Origem**]: Censo 2022: População e Domicílios - Primeiros Resultados
                            - :green[**Origem do Texto**]: Wikipedia
                            ''')
            else:
                with st.expander('About the Data and Text', expanded=False):    
                    if lang == "English":
                        st.write('''
                            - Data: [IBGE](<https://censo2022.ibge.gov.br/panorama/>).
                            - :orange[**Source**]: Population and Households Census 2022 - First Results
                            - :green[**Text Source**]: Wikipedia
                            ''')
               

if __name__ == "__main__":
    main()