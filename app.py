import streamlit as st
import sqlite3

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
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
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

.title {
    font-size: 46px;
    text-align: center;
    font-weight: bold;
    animation: fadeSlide 1s ease;
}

.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
    animation: fadeSlide 1.3s ease;
}

.card {
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    animation: fadeSlide 0.8s ease;
    background-color: #fff7f0;
}

.card-chocolate {
    background-color: #d7b899;
}

.footer {
    text-align: center;
    color: #999;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CABEÇALHO ----------------
st.markdown("<div class='title'>📖 Livro de Receitas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Cadastre, edite e organize suas receitas 💖</div>", unsafe_allow_html=True)

# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["🏠 Sobre", "➕ Adicionar receita", "📖 Ver receitas", "✏️ Editar receita", "🗑️ Remover receita"]
)

# ---------------- SOBRE ----------------
if menu == "🏠 Sobre":
    st.markdown("""
    ### 👩‍🍳 Sobre o projeto

    Este sistema foi desenvolvido como **projeto final**, utilizando
    **Python**, **Streamlit**, **formulários**, **banco de dados SQLite**
    e **estilização com animações CSS**.

    O objetivo é permitir o **cadastro, edição, visualização e remoção**
    de receitas de forma simples e interativa.
    """)

# ---------------- ADICIONAR ----------------
if menu == "➕ Adicionar receita":
    st.subheader("Adicionar nova receita")

    with st.form("form_add"):
        nome = st.text_input("Nome da receita")
        ingredientes = st.text_area("Ingredientes")
        preparo = st.text_area("Modo de preparo")
        imagem = st.text_input("URL da imagem (opcional)")

        salvar = st.form_submit_button("Salvar")

        if salvar:
            cursor.execute(
                "INSERT INTO receitas (nome, ingredientes, preparo, imagem) VALUES (?, ?, ?, ?)",
                (nome, ingredientes, preparo, imagem)
            )
            conn.commit()
            st.success("Receita adicionada com sucesso!")

# ---------------- VER RECEITAS ----------------
if menu == "📖 Ver receitas":
    cursor.execute("SELECT * FROM receitas")
    receitas = cursor.fetchall()

    if not receitas:
        st.info("Nenhuma receita cadastrada.")
    else:
        for r in receitas:
            classe = "card-chocolate" if "chocolate" in r[1].lower() else "card"

            st.markdown(f"""
            <div class="{classe}">
            <h2>{r[1]}</h2>
            <b>Ingredientes:</b><br>{r[2]}<br><br>
            <b>Modo de preparo:</b><br>{r[3]}
            </div>
            """, unsafe_allow_html=True)

            if r[4]:
                st.image(r[4], use_container_width=True)

# ---------------- EDITAR RECEITA ----------------
if menu == "✏️ Editar receita":
    cursor.execute("SELECT id, nome FROM receitas")
    dados = cursor.fetchall()

    if dados:
        escolha = st.selectbox("Escolha a receita", dados, format_func=lambda x: x[1])

        cursor.execute("SELECT * FROM receitas WHERE id = ?", (escolha[0],))
        receita = cursor.fetchone()

        with st.form("form_edit"):
            nome = st.text_input("Nome", receita[1])
            ingredientes = st.text_area("Ingredientes", receita[2])
            preparo = st.text_area("Modo de preparo", receita[3])
            imagem = st.text_input("URL da imagem", receita[4])

            atualizar = st.form_submit_button("Atualizar")

            if atualizar:
                cursor.execute(
                    "UPDATE receitas SET nome=?, ingredientes=?, preparo=?, imagem=? WHERE id=?",
                    (nome, ingredientes, preparo, imagem, escolha[0])
                )
                conn.commit()
                st.success("Receita atualizada!")
    else:
        st.info("Nenhuma receita para editar.")

# ---------------- REMOVER ----------------
if menu == "🗑️ Remover receita":
    cursor.execute("SELECT id, nome FROM receitas")
    dados = cursor.fetchall()

    if dados:
        escolha = st.selectbox("Escolha a receita", dados, format_func=lambda x: x[1])

        if st.button("Remover"):
            cursor.execute("DELETE FROM receitas WHERE id = ?", (escolha[0],))
            conn.commit()
            st.success("Receita removida!")
    else:
        st.info("Nenhuma receita cadastrada.")

# ---------------- RODAPÉ ----------------
st.markdown("""
<div class="footer">
Projeto educacional • Python + Streamlit • Banco de Dados SQLite
</div>
""", unsafe_allow_html=True)
