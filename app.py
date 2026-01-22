import streamlit as st
import sqlite3
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# ---------------- CONFIGURAÇÃO ----------------
st.set_page_config(
    page_title="Site de Receitas",
    page_icon="🍰",
    layout="centered"
)

# ---------------- FUNÇÃO ANIMAÇÃO ----------------
def carregar_lottie(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

animacao = carregar_lottie("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

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

# ---------------- MENU ----------------
menu = st.sidebar.radio(
    "📋 Menu",
    ["🏠 Início", "📖 Ver Receitas", "➕ Adicionar Receita", "✏️ Editar Receita"]
)

# ---------------- INÍCIO ----------------
if menu == "🏠 Início":
    st.title("🍰 Site de Receitas")
    st_lottie(animacao, height=250)

    st.markdown("""
    Bem-vindo ao **Site de Receitas** 🍽️  
    Aqui você pode:
    - Cadastrar receitas
    - Ver receitas
    - Editar receitas
    - Todas com imagens salvas no sistema
    """)

# ---------------- VER RECEITAS ----------------
elif menu == "📖 Ver Receitas":
    st.title("📖 Receitas Cadastradas")

    cursor.execute("SELECT * FROM receitas")
    receitas = cursor.fetchall()

    if not receitas:
        st.warning("Nenhuma receita cadastrada ainda.")
    else:
        for r in receitas:
            id_, nome, ingredientes, preparo, imagem = r

            if nome.lower() == "bolo de chocolate":
                st.markdown(
                    "<div style='background-color:#ffe6eb; padding:15px; border-radius:10px;'>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div style='background-color:#f9f9f9; padding:15px; border-radius:10px;'>",
                    unsafe_allow_html=True
                )

            st.subheader(nome)

            try:
                img = Image.open(f"imagens/{imagem}")
                st.image(img, use_container_width=True)
            except:
                st.error("Imagem não encontrada.")

            st.markdown("**🧾 Ingredientes:**")
            st.write(ingredientes)

            st.markdown("**👩‍🍳 Modo de preparo:**")
            st.write(preparo)

            st.markdown("</div>", unsafe_allow_html=True)
            st.divider()

# ---------------- ADICIONAR RECEITA ----------------
elif menu == "➕ Adicionar Receita":
    st.title("➕ Adicionar Nova Receita")

    nome = st.text_input("Nome da receita")
    ingredientes = st.text_area("Ingredientes")
    preparo = st.text_area("Modo de preparo")

    imagem = st.selectbox(
        "Imagem da receita",
        ["bolo_chocolate.jpg", "bolo_cenoura.jpg", "lasanha.jpg"]
    )

    if st.button("Salvar Receita"):
        if nome and ingredientes and preparo:
            cursor.execute(
                "INSERT INTO receitas (nome, ingredientes, preparo, imagem) VALUES (?, ?, ?, ?)",
                (nome, ingredientes, preparo, imagem)
            )
            conn.commit()
            st.success("Receita adicionada com sucesso!")
        else:
            st.error("Preencha todos os campos.")

# ---------------- EDITAR RECEITA ----------------
elif menu == "✏️ Editar Receita":
    st.title("✏️ Editar Receita")

    cursor.execute("SELECT id, nome FROM receitas")
    lista = cursor.fetchall()

    if not lista:
        st.warning("Nenhuma receita para editar.")
    else:
        escolha = st.selectbox(
            "Escolha a receita",
            lista,
            format_func=lambda x: x[1]
        )

        id_receita = escolha[0]

        cursor.execute("SELECT * FROM receitas WHERE id=?", (id_receita,))
        r = cursor.fetchone()

        novo_nome = st.text_input("Nome", r[1])
        novos_ingredientes = st.text_area("Ingredientes", r[2])
        novo_preparo = st.text_area("Modo de preparo", r[3])

        nova_imagem = st.selectbox(
            "Imagem",
            ["bolo_chocolate.jpg", "bolo_cenoura.jpg", "lasanha.jpg"],
            index=["bolo_chocolate.jpg", "bolo_cenoura.jpg", "lasanha.jpg"].index(r[4])
        )

        if st.button("Atualizar Receita"):
            cursor.execute("""
            UPDATE receitas
            SET nome=?, ingredientes=?, preparo=?, imagem=?
            WHERE id=?
            """, (novo_nome, novos_ingredientes, novo_preparo, nova_imagem, id_receita))
            conn.commit()
            st.success("Receita atualizada com sucesso!")
