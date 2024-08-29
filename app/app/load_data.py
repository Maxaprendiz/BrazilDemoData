import geopandas as gpd
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    geojson_path = "data/brazil_geo.json"
    geojson = gpd.read_file(geojson_path)


    file0 = 'data/brasil_state_regions.csv'
    df_regions = pd.read_csv(file0, dtype={"name": str})

    file1 = 'data/ibge_population.csv'
    df_population = pd.read_csv(file1, dtype={"name": str})

    file2 = 'data/ibge_population_growth.csv'
    df_population_growth = pd.read_csv(file2, dtype={"name": str})

    file3 = 'data/ibge_razao_sexos.csv'
    df_sex_ratio = pd.read_csv(file3, dtype={"name": str})

    file4 = 'data/ibge_idade_media.csv'
    df_idade = pd.read_csv(file4, dtype={"name": str})

    file5 = 'data/ibge_populacao_regioes_bilingual.csv'
    df_population_reg = pd.read_csv(file5, dtype={"name": str})

    file6 = 'data/crescimento_populacional_brasil.csv'
    df_population_growth_year = pd.read_csv(file6, dtype={"name": str})

    file7 = 'data/razao_sexo_brasil.csv'
    df_sexos_brasil = pd.read_csv(file7, dtype={"name": str})

    file8 = 'data/Idade_mediana_cor.csv'
    df_idade_cor = pd.read_csv(file8, dtype={"name": str})

    file9 = 'data/ibge_densidade.csv'
    df_densidade = pd.read_csv(file9, dtype={"name": str})

    file10 = 'data/ibge_population_race.csv'
    df_race = pd.read_csv(file10, dtype={"name": str})

    file11 = 'data/ibge_alfabetizacao.csv'
    df_alfabetizacao = pd.read_csv(file11, dtype={"name": str})

    return (geojson, df_regions, df_population, df_population_growth, df_sex_ratio, df_idade, df_population_reg, df_population_growth_year, 
    df_sexos_brasil, df_idade_cor, df_densidade, df_race, df_alfabetizacao)


