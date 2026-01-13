import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Livro de Receitas",
    page_icon="🍽️",
    layout="centered"
)

conn = sqlite3.connect("receitas.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receitas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    ingredientes TEXT,
    modo_preparo TEXT,
    categoria TEXT
)
""")
conn.commit()

st.sidebar.title("📖 Menu")
pagina = st.sidebar.radio(
    "Escolha uma opção:",
    ["🏠 Início", "➕ Cadastrar Receita", "📋 Ver Receitas"]
)

if pagina == "🏠 Início":
    st.title("🍰 Livro de Receitas")
    st.write("Bem-vindo(a) ao sistema de cadastro de receitas!")
    st.image(
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        use_container_width=True
    )
    st.balloons()

elif pagina == "➕ Cadastrar Receita":
    st.title("➕ Nova Receita")

    with st.form("form_receita"):
        nome = st.text_input("Nome da receita")
        ingredientes = st.text_area("Ingredientes")
        modo = st.text_area("Modo de preparo")
        categoria = st.selectbox(
            "Categoria",
            ["Doce", "Salgado", "Vegetariano", "Bebida", "Outro"]
        )
        enviar = st.form_submit_button("Salvar Receita")

    if enviar:
        cursor.execute(
            "INSERT INTO receitas (nome, ingredientes, modo_preparo, categoria) VALUES (?, ?, ?, ?)",
            (nome, ingredientes, modo, categoria)
        )
        conn.commit()
        st.success("Receita cadastrada com sucesso! 🎉")
        st.toast("Receita salva no banco de dados!")

elif pagina == "📋 Ver Receitas":
    st.title("📋 Receitas Cadastradas")

    cursor.execute("SELECT * FROM receitas")
    receitas = cursor.fetchall()

    if receitas:
        for r in receitas:
            st.subheader(r[1])
            st.write(f"**Categoria:** {r[4]}")
            st.write("**Ingredientes:**")
            st.write(r[2])
            st.write("**Modo de preparo:**")
            st.write(r[3])
            st.divider()
    else:
        st.info("Nenhuma receita cadastrada ainda.")
