import streamlit as st
import sqlite3

# ---------------- CONFIGURAÇÃO ----------------
st.set_page_config(
    page_title="Livro de Receitas 🍰",
    page_icon="🍴",
    layout="centered"
)

# ---------------- BANCO DE DADOS ----------------
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

# ---------------- CSS + ANIMAÇÕES ----------------
st.markdown("""
<style>
@keyframes fadeSlide {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes zoomIn {
    from {transform: scale(0.95); opacity: 0;}
    to {transform: scale(1); opacity: 1;}
}

.title {
    font-size: 48px;
    text-align: center;
    font-weight: bold;
    animation: fadeSlide 1s ease;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
    animation: fadeSl
