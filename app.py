import streamlit as st
import sqlite3
import time

# ---------- CONFIG ----------
st.set_page_config(page_title="Livro de Receitas", layout="centered")

# ---------- BANCO ----------
conn = sqlite3.connect("receitas.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receitas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    ingredientes TEXT,
    preparo TEXT,
    imagem TEXT
)
""")
conn.commit()

# ---------- ESTILO ----------
st.markdown("""
<style>
.card {
    background-color: #fff1e6;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 14px rgba(0,0,0,0.15);
}
.card-chocolate {
    background-color: #c7a26b;
}
.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TÍTULO ----------
st.title("📖 Livro de Receitas")
st.caption("Cadastre, edite
