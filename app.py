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
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.main-title {
    font-size: 48px;
    text-align: center;
    font-weight: bold;
    animation: fadeSlide 1.2s ease;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 30px;
    animation: fadeSlide 1.5s ease;
}

.card {
    background-color: #fff7f0;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    animation: fadeSlide 1s ease;
}

.footer {
    text-align: center;
    color: #999;
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CABEÇALHO ----------------
st.markdown("<div class='main-title'>📖 Livro de Receitas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Receitas simples, bonitas e feitas com carinho 💖</div>", unsafe_allow_html=True)

# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "📌 Navegação",
    ["🏠 Sobre o projeto", "📖 Ver receitas", "➕ Adicionar receita", "🗑️ Remover receita"]
)

# ---------------- SOBRE ----------------
if menu == "🏠 Sobre o projeto":
    st.image(
        "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0",
        use_container_width=True
    )

    st.markdown("""
    ### 👩‍🍳 Sobre este projeto

    Este site foi desenvolvido como **projeto final do curso**, utilizando a
    linguagem **Python** e a biblioteca **Streamlit**.

    O objetivo do sistema é permitir o **cadastro, visualização e gerenciamento
    de receitas**, utilizando **formulários**, **banco de dados** e uma
    **interface visual amigável**, aplicando os conceitos aprendidos em aula.
    """)

# ---------------- ADICIONAR RECEITA ----------------
if menu == "➕ Adicionar receita":
    st.subheader("➕ Adicionar nova receita")

    with st.form("form_receita"):
        nome = st.text_input("Nome da receita")
        ingredientes = st.text_area("Ingredientes")
        preparo = st.text_area("Modo de preparo")
        imagem = st.text_input("URL da imagem (opcional)")

        enviar = st.form_submit_button("Salvar receita")

        if enviar:
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
        st.info("Nenhuma receita cadastrada ainda.")
    else:
        for r in receitas:
            st.markdown(f"""
            <div class="card">
            <h2>{r[1]}</h2>
            <b>Ingredientes:</b><br>{r[2]}<br><br>
            <b>Modo de preparo:</b><br>{r[3]}
            </div>
            """, unsafe_allow_html=True)

            if r[4]:
                st.image(r[4], use_container_width=True)

# ---------------- REMOVER RECEITA ----------------
if menu == "🗑️ Remover receita":
    cursor.execute("SELECT id, nome FROM receitas")
    dados = cursor.fetchall()

    if dados:
        escolha = st.selectbox(
            "Escolha a receita para remover",
            dados,
            format_func=lambda x: x[1]
        )

        if st.button("Remover"):
            cursor.execute("DELETE FROM receitas WHERE id = ?", (escolha[0],))
            conn.commit()
            st.success("Receita removida com sucesso!")
    else:
        st.info("Nenhuma receita cadastrada.")

# ---------------- RODAPÉ ----------------
st.markdown("""
<div class="footer">
Projeto educacional • Python + Streamlit • CRUD com banco de dados 💻
</div>
""", unsafe_allow_html=True)
