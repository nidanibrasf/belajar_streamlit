import streamlit as st
import datetime
from lorem_text import lorem

st.set_page_config(
    page_title= 'Mari Belajar Streamlit',
    layout='wide'
)

#menulis teks di streamlit

st.write("Hello World!")

st.markdown("## ini ditulis menggunakan _markdown_")

"Hello world!" # <- magic

"_Ini juga hello world versi miring_"

"**versi bold**"

"# ini adalah header"

"## ini adalah subheader"

st.title("Ini judul")
st.header("Ini juga header")

st.caption("ini caption, misal Langit senja minum kopi")

st.code("import streamlit as st")

st.code('''
import pandas as pd
import streamlit as st # ini untuk memanggil package streamlit
''')

# Latec
st.latex("ax^2 + bx + c = 0")

# WIDGET <- input elements

ini_tombol = st.button("Tekan tombol ini")
ini_tombol

saya_Setuju = st.checkbox("Centang jika setuju")
if saya_Setuju:
    st.write("anda setuju untuk belajar lebih giat")
else:
    st.write("Ayo belajar")

# radio button, memilih salah satu opsi dari sekian opsi
buah_favorit = st.radio(
    "Pilih buah favorit kamu",
    ['Apel','Anggur','Jeruk','Mangga']
)

buah_favorit

makanan = st.selectbox(
    "Pilih makanan yang akan diorder",
    ['paket 1','Paket Goceng','Kids Meal']
)
makanan

belanjaan = st.multiselect(
    "Pilih belanjaan kalian",
    ['Terigu','Minyak Goreng','Biskuit','Minuman']
)
belanjaan
st.write(type(belanjaan))

belanjaan[0]

parameter_alpha = st.slider(
    "Insert alpha value",
    min_value=0.0,
    max_value=1.0,
    step=0.1,
    value=0.5
)

parameter_alpha

ukuran_baju = st.select_slider(
    "Ukuran Baju",
    ['SS','S','M','L','XL','XXL']
)
ukuran_baju

kode_pos = st.number_input(
    "Masukkan kode pos kalian",
    min_value=0,
    max_value=99999,
    step=1
)
kode_pos

nama=st.text_input("Masukkan nama kalian")

komentar = st.text_area("Masukkan komentar kamu")
komentar

tanggal_jadian = st.date_input("Masukkan tanggal jadian")

jam_mulai = st.time_input("Masukkan jam mulai")

warna = st.color_picker("Masukkan warna")
warna

tanggal_jadian = st.date_input(
    "Tanggal lahir",
    min_value=datetime.date(1990,1,1)
    )

# masukkan image, video, sama suara

# container and layoutinh

# kolom

col1, col2, col3 = st.columns(3)

with col1:
    lahir_Saya = st.date_input("Tanggal lahir kamu")

with col2:
    lahir_pasangan = st.date_input("Tanggal lahir dia")

with col3:
    jadian = st.date_input("Tanggal Jadian")

st.button("Hitung")

kol1, kol2 = st.columns([1,3])

with kol1:
    lahir_aku = st.date_input("Tanggal lahir aku")

with kol2:
    lahir_kamu = st.date_input("Tanggal lahir dirinya")

with st.sidebar:
    st.title("Titanic survival model explorer")
    your_name = st.text_input("Enter your name")

    with st.expander("Lorem ipsum"):
        st.write(lorem.paragraphs(1))

tab1, tab2, tab3 = st.tabs(['Tab1','Tab2','Tab3'])

with tab1:
    st.write(lorem.paragraphs(1))

with tab2:
    st.write(lorem.paragraphs(1))

with tab3:
    st.write(lorem.paragraphs(1))

with st.container():
    st.write("Ini teks di dalam container")

st.write("ini text di luar container")