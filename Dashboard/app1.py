import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def data():
    df = pd.read_csv("dataset/PetaBencana_clean.csv")
    return df

def app():

    st.markdown("# Peta Bencana")

    null1_1, row1_2, null1_2, row1_3, null1_3 = st.columns((0.45, 2.5, 0.3, 5, 0.17))

    with row1_3:
        intro = """
        <p  style="text-align : justify">
        <b>PetaBencana.id</b> adalah platform gratis dan terbuka untuk respon darurat 
        dan penanggulangan bencana di kota-kota besar di Asia Selatan dan Tenggara. 
        Platform ini memanfaatkan penggunaan sosial media yang tinggi saat situasi 
        darurat untuk mengumpulkan, menyortir dan menampilkan informasi bencana 
        terkonfirmasi secara real-time.
        </p>
        """ 
        st.markdown(intro, unsafe_allow_html=True)


    row1_2.image("Images/logoPetaBencanaID.png", caption='Peta Bencana Indonesia')
    df = data()
    st.markdown("### Dataset")
    st.dataframe(df)

    st.markdown("### Kasus")

    

    kasus1, kasus2, kasus3, kasus4 = st.columns(4)

    with kasus1:
        st.markdown("**Desa**")
        number1 = len(df['Desa'].unique())
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

    with kasus2:
        st.markdown("**Kecamatan**")
        number2 = len(df['Kecamatan'].unique()) 
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

    with kasus3:
        st.markdown("**Kabupaten**")
        number3 = len(df['Kabupaten'].unique()) 
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

    with kasus4:
        st.markdown("**Provinsi**")
        number4 = len(df['Provinsi'].unique())
        st.markdown(f"<h1 style='text-align: center; color: red;'>{number4}</h1>", unsafe_allow_html=True)

    kasus11, kasus21 = st.columns(2)

    with kasus11:
        st.markdown("**Bencana di Indonesia**")
        # df['lon'] = df['long']
        # map_data = df[["lat", "lon"]]

        # st.map(map_data)
        fig = px.scatter_mapbox(df, lat="lat", lon="long", color="disaster_type", 
                  color_continuous_scale=px.colors.cyclical.IceFire)
        st.plotly_chart(fig)

    with kasus21:
        st.markdown("**Intensitas Bencana**")
        fig = px.density_mapbox(df, lat='lat', lon='long', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
        fig.update_layout()                
        st.plotly_chart(fig)


    # st.markdown("<hr/>",unsafe_allow_html=True)


    # st.markdown("## KPI Second Row")

    # # kpi 1 

    # kpi01, kpi02, kpi03, kpi04, kpi05 = st.beta_columns(5)

    # with kpi01:
    #     st.markdown("**Another 1st KPI**")
    #     number1 = 111 
    #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

    # with kpi02:
    #     st.markdown("**Another 1st KPI**")
    #     number1 = 222 
    #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

    # with kpi03:
    #     st.markdown("**Another 1st KPI**")
    #     number1 = 555 
    #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

    # with kpi04:
    #     st.markdown("**Another 1st KPI**")
    #     number1 = 333 
    #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

    # with kpi05:
    #     st.markdown("**Another 1st KPI**")
    #     number1 = 444 
    #     st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

    # st.markdown("<hr/>",unsafe_allow_html=True)

    # st.markdown("## Chart Layout")

    # chart1, chart2 = st.beta_columns(2)

    # with chart1:
    #     chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    #     st.line_chart(chart_data)

    # with chart2:
    #     chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    #     st.line_chart(chart_data)