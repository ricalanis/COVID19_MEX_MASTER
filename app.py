from typing import Union

import streamlit as st
import xarray as xr
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.scenario import plot_scenario

def scenario_label(value):
    scenario_relation = {
        3.5:'Base',
        4.5:'Pesimista',
        1.5:'Optimista',
        1.75:'Fuerte',
        2.625:'Moderada',
    }
    return scenario_relation[value]

st.title('Predicción del modelo SEAIR de la evolución de COVID-19 en Jalisco')

population = st.sidebar.slider(
    label="Población",
    min_value=800000,
    max_value=10000000,
    value=4200000,
    step=100000,
)

ro = st.sidebar.selectbox(
    label="Escenario de Propagación por #quedateencasa",
    options=[3.5, 4.5, 1.5, 1.75, 2.625],
    format_func=scenario_label,
)

initial_cases = st.sidebar.slider(
    label="Casos Iniciales",
    min_value=-0,
    max_value=70,
    value=32,
    step=1,
)

number_of_deaths = st.sidebar.slider(
    label="Muertes Reportadas",
    min_value=-0,
    max_value=10,
    value=0,
    step=1,
)

recovered = st.sidebar.slider(
    label="Expuestos por caso",
    min_value=-0,
    max_value=10,
    value=0,
    step=1,
)

start_day, end_day = st.sidebar.slider(
    'Dias con intervención',
    1, 119, (10, 50)
)
duration_days = end_day-start_day


initial_conditions = {
    'initial_cases':initial_cases,
    'exposed_per_case': 4,
    'deaths': number_of_deaths, # No Muertos,
    'recovered': recovered,
}

if st.sidebar.button("Generar"):
    st.markdown(f"Población: {population:.1f}")
    st.markdown(f"Ro:  {ro:.1f}")
    fig = plot_scenario(
        population,
        initial_conditions,
        ro,
        start_intervention=start_day,
        intervention_duration =duration_days
    )
    st.plotly_chart(fig)
else:
    st.markdown(
        "Selecciona la localización usando los controles Y pulsa en "
        "el botón 'Generar'."
    )
