import plotly.express as px
import random
import streamlit as st


def make_choropleth_population(df, geojson, color_theme, lang):
    '''Create choropleth map for displaying population data.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'name':'Estado',
                'human_format': 'População',
                'population': 'População Total'}
        fig = px.choropleth(df, geojson=geojson, color="population",
            locations="name", featureidkey="properties.nome",
            projection="mercator",
            color_continuous_scale=f"{color_theme}",
            template = "plotly_dark",
            hover_data={"name":True,"population":False,"human_format":True},
            labels=labelsL,
            )
    else:
        labelsL={'name':'State',
                'human_format': 'Population',
                'population': 'Total Population'}
        fig = px.choropleth(df, geojson=geojson, color="population",
            locations="name", featureidkey="properties.name",
            projection="mercator",
            color_continuous_scale=f"{color_theme}",
            template = "plotly_dark",
            hover_data={"name":True,"population":False,"human_format":True},
            labels=labelsL,
            )    
    
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0}
            )

    return fig

      
def make_choropleth(df, geojson, label, var_color, color_theme):
    '''Plot choropleth map for a given feature.'''

    fig = px.choropleth(df, geojson=geojson, color=var_color,
        locations="name", featureidkey="properties.name",
        projection="mercator",
        color_continuous_scale=f"{color_theme}",
        template = "plotly_dark",
        labels=label
        )
    fig.update_geos(fitbounds="geojson", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig


def plot_piechart_population(df, lang, color_theme):
    '''Plot a pie chart showing total population for each region of the country.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'name':'Região',
                'population': 'População'}
        titleL='População em Cada Região'
        fig = px.pie(df, values='population', 
            names='nome', 
            color='population', 
            labels=labelsL,
            title=titleL,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))
    else:
        labelsL={'name':'Region',
            'population': 'Population'}
        titleL='Population by Region'
        fig = px.pie(df, values='population', 
            names='name', 
            color='population', 
            labels=labelsL,
            title=titleL,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))

    
    return fig

def plot_barchart_population_growth(df, lang, color_theme):
    '''Plot a bar chart showing population growth data.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'population':'População'}
        titleL='Crescimento da População por Ano'
    else:
        labelsL={'population':'Population', 'Ano':'Year'}
        titleL='Population Growth by Year'

    fig = px.bar(df, x='Ano', y='population', 
        color='population', 
        labels=labelsL,
        title=titleL,
        color_continuous_scale=eval('px.colors.sequential.'+f"{color_theme}".title()))
    fig.update_xaxes(tickangle=45)

    return fig


def plot_piechart_genders(df, lang, color_theme):
    '''Creates a pie chart showing gender distribution.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'Sexo':'Sexo',
                        'population': 'População'}
        titleL='População de cada Sexos'
        fig = px.pie(df, values='population', 
            names='Sexo', 
            color='population', 
            labels=labelsL,
            title=titleL,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))

    else:
        labelsL={'Gender':'Gender',
                    'population': 'Population'}
        titleL='Population by Gender'
        fig = px.pie(df, values='population', 
            names='Gender', 
            color='population', 
            labels=labelsL,
            title=titleL,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))
    

    return fig


def plot_barchart_age_race(df, lang, color_theme):
    '''Creates a bar plot showing median age distribution among different races.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'idade':'Idade Mediana','cor':'Cor ou Raça'}
        titleL='Idade Mediana por Cor ou Raça'
        fig = px.bar(df, x='cor', y='idade',
            color='idade',
            labels=labelsL,
            title=titleL,
            color_continuous_scale=eval('px.colors.sequential.'+f"{color_theme}".title()))
        fig.update_xaxes(tickangle=45)

    else:
        labelsL={'idade':'Age','race':'Race'}
        titleL='Median Age by Race'
        fig = px.bar(df, x='race', y='idade',
            color='idade',
            labels=labelsL,
            title=titleL,
            color_continuous_scale=eval('px.colors.sequential.'+f"{color_theme}".title()))
        fig.update_xaxes(tickangle=45)

    return fig


def plot_piechart_race(df, lang, color_theme):
    '''Creates a pie chart showing race distribution for 2010 and 2022.'''

    if lang == "Portuguese (Brazil)":
        labelsL={'race':'Raça',
                    'population_2010': 'Population'}
        titleL2010='População por Raça (2010)'
        titleL2022='População por Raça (2022)'
        
        fig1 = px.pie(df, values='population_2010', 
            names='cor', 
            color='cor',  
            labels=labelsL,
            title=titleL2010,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))
        
        fig2 = px.pie(df, values='population_2022', 
            names='cor', 
            color='cor',  
            labels=labelsL,
            title=titleL2022,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))

    else:
        labelsL={'race':'Race',
                    'population_2010': 'Population'}
        titleL2010='Population by Race (2010)'
        titleL2022='Population by Race (2022)'
    
        fig1 = px.pie(df, values='population_2010', 
            names='race', 
            color='race',  
            labels=labelsL,
            title=titleL2010,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))
        
        fig2 = px.pie(df, values='population_2022', 
            names='race', 
            color='race',  
            labels=labelsL,
            title=titleL2022,
            color_discrete_sequence=eval('px.colors.sequential.'+f"{color_theme}".title()))

    return fig1, fig2


def plot_barchart_school(df, lang, color_theme):
    '''Creates a bar plot showing rate of literacy among different races.'''
    
    if lang == "Portuguese (Brazil)":
        colorL = 'Cor'
        labelsL1={'Cor':'Cor',
                        'Mulheres': 'Taxa (%) para mulheres'}
        titleL1='Alfabetização por Raça/Cor para Mulheres'
        labelsL2={'Cor':'Cor',
                        'Homens': 'Taxa (%) para homes'}
        titleL2='Alfabetização por Raça/Cor para Homens'

    else:
        colorL='Race'
        labelsL1={'Race':'Race',
                        'Mulheres': 'Rate (%) for women'}
        titleL1='Literacy by Race for Women'

        labelsL2={'Race':'Race',
                        'Homens': 'Rate (%) for men'}
        titleL2='Literacy by Race for Men'

    
    fig1 = px.bar(df,x='Mulheres', y=colorL, 
        color=colorL,
        labels=labelsL1,
        orientation='h',
        title=titleL1,
        color_continuous_scale=eval('px.colors.sequential.'+f"{color_theme}".title()))

    
    fig2 = px.bar(df,x='Homens', y=colorL, 
        color=colorL,
        labels=labelsL2,
        orientation='h',
        title=titleL2,
        color_continuous_scale=eval('px.colors.sequential.'+f"{color_theme}".title()))

    return fig1, fig2


def show_extreme_data(df, column_name, label1, label2, lang):
    '''Display the smallest and the largest value for a given feature.'''

    df_sorted = df.sort_values(by=[f'{column_name}']) 
    if lang == "Portuguese (Brazil)":
        st.html('<h3>Os Extremos</h3>') 
        st.write(f':orange[**Menor {label1}**]: {df_sorted.iloc[0,1]}') 
        st.write(f':blue[**{label2}**]: {df_sorted.iloc[0,2]}') 
        st.write(f':orange[**Maior {label1}**]: {df_sorted.iloc[-1,1]}') 
        st.write(f':blue[**{label2}**]: {df_sorted.iloc[-1,2]}') 
    else:
        st.html('<h3>The Extremes</h3>') 
        st.write(f':orange[**Lowest {label1}**]: {df_sorted.iloc[0,1]}') 
        st.write(f':blue[**{label2}**]: {df_sorted.iloc[0,2]}') 
        st.write(f':orange[**Highest {label1}**]: {df_sorted.iloc[-1,1]}') 
        st.write(f':blue[**{label2}**]: {df_sorted.iloc[-1,2]}') 


def aleatory_facts(lang):
    '''Select a random fact about Brazil to be displayed.'''
    
    facts = ["Brazil, officially the Federative Republic of Brazil, is the largest and easternmost country in South America and in Latin America."
        "Brazil is the world's fifth-largest country by area and the seventh most populous.",
        "Brazil’s capital is Brasília, and its most populous city is São Paulo. The country is composed of the union of the 26 states and the Federal District.",
        "Brazil is the only country in the Americas to have Portuguese as an official language.",
        "Brazil is one of the most multicultural and ethnically diverse nations, due to over a century of mass immigration from around the world.",
        "Bounded by the Atlantic Ocean on the east, Brazil has a coastline of 7,491 kilometers (4,655 mi).",
        "Brazil borders all other countries and territories in South America except Ecuador and Chile and covers roughly half of the continent's land area.",
        "Brazil’s Amazon basin includes a vast tropical forest, home to diverse wildlife, a variety of ecological systems, and extensive natural resources spanning numerous protected habitats.",
        "Its unique environmental heritage positions Brazil at number one of 17 megadiverse countries.",
        "Brazil's natural richness is also the subject of significant global interest, as environmental degradation (through processes like deforestation) has direct impacts on global issues like climate change and biodiversity loss.",
        "The territory which would become known as Brazil was inhabited by numerous tribal nations prior to the landing of explorer Pedro Álvares Cabral in 1500. Then, the land was claimed for the Portuguese Empire.",
        "Brazil remained a Portuguese colony until 1808, when the capital of the empire was transferred from Lisbon to Rio de Janeiro. Independence was achieved in 1822 with the creation of the Empire of Brazil, a unitary state governed under a constitutional monarchy and a parliamentary system." ]

    facts_pt = ["O Brasil, oficialmente República Federativa do Brasil, é o maior e mais oriental país da América do Sul e da América Latina.", 
        "O Brasil é o quinto maior país do mundo em área e o sétimo mais populoso.", 
        "A capital do Brasil é Brasília, e sua cidade mais populosa é São Paulo. O país é composto pela união dos 26 estados e pelo Distrito Federal.", 
        "O Brasil é o único país das Américas a ter o português como língua oficial.", 
        "O Brasil é uma das nações mais multiculturais e etnicamente diversas, devido a mais de um século de imigração em massa de todo o mundo.", "Delimitado pelo Oceano Atlântico a leste, O Brasil tem uma costa de 7.491 quilômetros (4.655 milhas).", 
        "O Brasil faz fronteira com todos os outros países e territórios da América do Sul, exceto Equador e Chile, e cobre cerca de metade da área terrestre do continente.",
        "A bacia amazônica do Brasil inclui uma vasta floresta tropical, lar de diversos animais selvagens, uma variedade de sistemas ecológicos e extensos recursos naturais que abrangem inúmeros habitats protegidos.", 
        "Seu patrimônio ambiental único posiciona o Brasil em primeiro lugar entre 17 países megadiversos.",
        "A riqueza natural do Brasil também é objeto de significativo interesse global, uma vez que a degradação ambiental (por meio de processos como o desmatamento) tem impactos diretos em questões globais como mudanças climáticas e perda de biodiversidade.",
        "O território que ficaria conhecido como Brasil era habitado por inúmeras nações tribais antes do desembarque do explorador Pedro Álvares Cabral, em 1500. Então, a terra foi reivindicada para o Império Português.",
        "O Brasil permaneceu como colônia portuguesa até 1808, quando a capital do império foi transferida de Lisboa para o Rio de Janeiro. A independência foi alcançada em 1822 com a criação do Império do Brasil, um Estado unitário governado sob uma monarquia constitucional e um sistema parlamentarista." ]
    
    if lang == "English":
        fact = random.choice(facts)
    else:
        fact = random.choice(facts_pt)

    return fact
