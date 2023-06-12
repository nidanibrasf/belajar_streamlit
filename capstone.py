import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#content-start
st.set_page_config(layout="wide")
st.title('Efek Pengembangan Wilayah Terhadap Kenaikan Suhu Udara di Indonesia')
st.write('oleh : **125 - Nida Nibras Fadhilah**')
st.write('Pembangunan di wilayah Indonesia menyebabkan perubahan suhu global yang berakibat adanya perubahan unsur iklim terutama kenaikan suhu udara. Pembangunan wilayah dapat menaikan suhu dimana laju kenaikan suhu sebanding dengan laju pembangunan wilayah.')
st.write('Peningkatan **jumlah penduduk** mengakibatkan keanekaragaman aktivitas dan ulah penduduk baik secara langsung maupun tidak langsung dapat memengaruhi perubahan suhu udara. Masyarakat Indonesia juga banyak menggunakan **kendaraan** dalam menjalani aktifitas sehari-harinya. Paling banyak Indonesia menggunakan mobil dan sepeda motor sehingga penggunaan kendaraan bermotor dapat menimbulkan perubahan suhu. **Ruang Terbuka Hijau** (RTH) di Indonesia setiap tahunnya mengalami pengurangan dari tahun 2017 - 2021. Pengurangan RTH diduga menjadi salah satu penyebab suhu udara.')

data = pd.read_csv('Capstone.csv')
##data
##Tahun =list(set(data['Tahun']))
data[['Tahun']]=data[['Tahun']].astype(object)
##data['Tahun'] = pd.to_datetime(data['Tahun'])
data.info()
##suhu = data['Suhu'].set_index('Tahun')
##st.line_chart(suhu)
##st.line_chart(data=data,x='Tahun',y='Suhu',width=0, height=0, use_container_width=False)
suhu = alt.Chart(data).mark_line().encode(
        y='Suhu',
        x='Tahun',
        tooltip=['Tahun', 'Suhu']
    )
st.altair_chart(suhu, use_container_width=False)

st.write('Setiap tahunnya rata-rata suhu Indonesia cenderung naik dari tahun 2017 - 2021.')
st.markdown('<div style="text-align: center;font-size:27px;">Rata-Rata Suhu Tiap Provinsi di Tahun 2017 - 2021</div>', unsafe_allow_html=True)

##SUHU

def plot():

    ##df = pd.DataFrame(px.data.gapminder())
    suhu1 = pd.read_csv('suhu.csv')

    clist = suhu1['Provinsi'].unique().tolist()

    countries = st.multiselect("Pilih Provinsi yang ingin dilihat rata-rata suhunya", clist)
    st.header("You selected: {}".format(", ".join(countries)))

    dfs = {country: suhu1[suhu1["Provinsi"] == country] for country in countries}

    fig = go.Figure()
    for country, suhu1 in dfs.items():
        fig = fig.add_trace(go.Scatter(x=suhu1["Tahun"], y=suhu1["Rata_Suhu"], name=country))

    st.plotly_chart(fig)


plot()

st.write('Peningkatan **jumlah penduduk** mengakibatkan keanekaragaman aktivitas dan ulah penduduk baik secara langsung maupun tidak langsung dapat memengaruhi perubahan suhu udara.')

penduduk = alt.Chart(data).mark_line().encode(
        y='Penduduk',
        x='Tahun',
        tooltip=['Tahun', 'Penduduk']
    )
st.altair_chart(penduduk, use_container_width=False)
         
st.write('Setiap tahunnya penduduk Indonesia selalu mengalami peningkatan dari tahun 2017 - 2021.')
         
st.markdown('<div style="text-align: center;font-size:27px;">Jumlah Penduduk Indonesia Tiap Provinsi di Tahun 2017 - 2021</div>', unsafe_allow_html=True)

##PENDUDUK
def plot():

    ##df = pd.DataFrame(px.data.gapminder())
    penduduk1 = pd.read_csv('penduduk.csv')

    plist = penduduk1['Provinsi'].unique().tolist()

    penduduks = st.multiselect("Pilih Provinsi yang ingin dilihat jumlah penduduknya", plist)
    st.header("You selected: {}".format(", ".join(penduduks)))

    dfp = {country: penduduk1[penduduk1["Provinsi"] == country] for country in penduduks}

    figp = go.Figure()
    for country, penduduk1 in dfp.items():
        figp = figp.add_trace(go.Scatter(x=penduduk1["Tahun"], y=penduduk1["Penduduk"], name=country))

    st.plotly_chart(figp)


plot()       

st.write('Masyarakat Indonesia juga banyak menggunakan **kendaraan** dalam menjalani aktifitas sehari-harinya. Paling banyak Indonesia menggunakan mobil dan sepeda motor sehingga penggunaan kendaraan bermotor dapat menimbulkan perubahan suhu.')

transportasi = alt.Chart(data).mark_line().encode(
        y='Kendaraan Pribadi',
        x='Tahun',
        tooltip=['Tahun', 'Kendaraan Pribadi']
    )
st.altair_chart(transportasi, use_container_width=False)
         
st.write('Setiap tahunnya jumlah kendaraan bermotor khusunya kendaraan pribadi seperti mobil dan motor di Indonesia selalu mengalami peningkatan dari tahun 2017 - 2021.')

st.markdown('<div style="text-align: center;font-size:27px;">Jumlah Kendaraan Bermotor di Indonesia Tiap Provinsi Tahun 2017 - 2021</div>', unsafe_allow_html=True)

##TRANSPORTASI
trans = pd.read_csv('transportasi.csv')

#unpivot DataFrame from wide format to long format
##trans1 = pd.melt(trans, id_vars='Transportasi')

lap = px.bar(trans, x = "Tahun", y = "Value", color = "Transportasi",barmode='group')
lap.update_layout(
        autosize=False,
        width=800,
        height=500
    )
st.plotly_chart(lap, use_container_width=True)

st.write('**Ruang Terbuka Hijau** (RTH) di Indonesia setiap tahunnya mengalami pengurangan dari tahun 2017 - 2021. Pengurangan RTH diduga menjadi salah satu penyebab suhu udara.')
    
rth = alt.Chart(data).mark_line().encode(
        y='Lahan Hijau',
        x='Tahun',
        tooltip=['Tahun', 'Lahan Hijau']
    )
st.altair_chart(rth, use_container_width=False)
         
st.write('Setiap tahunnya lahan hijau di Indonesia selalu mengalami penurunan dari tahun 2017 - 2021.')

st.markdown('<div style="text-align: center;font-size:27px;">Luas Lahan Hijau di Indonesia Tiap Provinsi Tahun 2017 - 2021</div>', unsafe_allow_html=True)
##LAHAN HIJAU
def plot():

    ##df = pd.DataFrame(px.data.gapminder())
    lahan_hijau = pd.read_csv('lahan hijau.csv')

    lhlist = lahan_hijau['Provinsi'].unique().tolist()

    lahanhijaus = st.multiselect("Pilih Provinsi yang ingin dilihat luas lahan hijaunya", lhlist)
    st.header("You selected: {}".format(", ".join(lahanhijaus)))

    dflh = {country: lahan_hijau[lahan_hijau["Provinsi"] == country] for country in lahanhijaus}

    figlh = go.Figure()
    for country, lahan_hijau in dflh.items():
        figlh = figlh.add_trace(go.Scatter(x=lahan_hijau["Tahun"], y=lahan_hijau["Lahan Hijau"], name=country))

    st.plotly_chart(figlh)


plot()  

st.markdown('<div style="text-align: center;font-size:27px;">**UJI KORELASI TIAP VARIABEL</div>', unsafe_allow_html=True)
        
data_corr = data.drop('Tahun', axis=1)
corr=data_corr.corr()
plt.figure(dpi=50)
corr
st.set_option('deprecation.showPyplotGlobalUse', False)

f,ax=plt.subplots(figsize=(15,15))
sns.heatmap(corr,annot=True,linewidths=0.5,fmt='.1f',ax=ax)
st.pyplot()

sns.heatmap(corr, cmap='Set3', annot=True)
st.pyplot()

plt.scatter(data.Suhu, data.Penduduk)
st.pyplot()

suhu1 = pd.read_csv('suhu.csv')
suhu1

##suhu11 = suhu1[['Provinsi','Rata_Suhu','Tahun']].set_index('Tahun').resample('M').sum()
##st.line_chart(suhu11)






