import streamlit as st
import sqlite3
import time

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Livro de Receitas",
    page_icon="🍰",
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

# ---------------- ESTILO ----------------
st.markdown("""
<style>
body {
    background-color: #fffaf4;
}
.card {
    background-color: #fff;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 12px rgba(0,0,0,0.1);
}
.titulo {
    color: #d2691e;
}
.rodape {
    text-align: center;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TÍTULO ----------------
st.markdown("<h1 class='titulo'>📖 Livro de Receitas</h1>", unsafe_allow_html=True)
st.write("Um site para cadastrar, visualizar e gerenciar receitas culinárias.")

# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "Navegação",
    ["Adicionar Receita", "Visualizar Receitas", "Editar Receita", "Excluir Receita"]
)

# ---------------- ADICIONAR ----------------
if menu == "Adicionar Receita":
    st.subheader("➕ Adicionar nova receita")

    nome = st.text_input("Nome da receita")
    ingredientes = st.text_area("Ingredientes")
    preparo = st.text_area("Modo de preparo")
    imagem = st.text_input("Link da imagem (opcional)")

    if st.button("Salvar receita"):
        with st.spinner("Salvando receita..."):
            time.sleep(1)
            cursor.execute(
                "INSERT INTO receitas (nome, ingredientes, preparo, imagem) VALUES (?, ?, ?, ?)",
                (nome, ingredientes, preparo, imagem)
            )
            conn.commit()
        st.success("Receita cadastrada com sucesso!")

# ---------------- VISUALIZAR ----------------
elif menu == "Visualizar Receitas":
    st.subheader("📚 Receitas cadastradas")

    cursor.execute("SELECT * FROM receitas")
    receitas = cursor.fetchall()

    if not receitas:
        st.info("Nenhuma receita cadastrada.")

    for r in receitas:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### 🍽️ {r[1]}")

        if r[4]:
            st.image(r[4], use_column_width=True)
        else:
            st.image(
                "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
                use_column_width=True
            )

        with st.expander("Ingredientes"):
            st.write(r[2])

        with st.expander("Modo de preparo"):
            st.write(r[3])

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDITAR ----------------
elif menu == "Editar Receita":
    st.subheader("✏️ Editar receita")

    cursor.execute("SELECT id, nome FROM receitas")
    receitas = cursor.fetchall()

    escolha = st.selectbox(
        "Escolha a receita",
        receitas,
        format_func=lambda x: x[1]
    )

    novo_nome = st.text_input("Novo nome")
    novos_ingredientes = st.text_area("Novos ingredientes")
    novo_preparo = st.text_area("Novo modo de preparo")
    nova_imagem = st.text_input("Novo link da imagem")

    if st.button("Atualizar receita"):
        with st.spinner("Atualizando receita..."):
            time.sleep(1)
            cursor.execute("""
            UPDATE receitas
            SET nome=?, ingredientes=?, preparo=?, imagem=?
            WHERE id=?
            """, (novo_nome, novos_ingredientes, novo_preparo, nova_imagem, escolha[0]))
            conn.commit()
        st.success("Receita atualizada com sucesso!")

# ---------------- EXCLUIR ----------------
elif menu == "Excluir Receita":
    st.subheader("🗑️ Excluir receita")

    cursor.execute("SELECT id, nome FROM receitas")
    receitas = cursor.fetchall()

    escolha = st.selectbox(
        "Selecione a receita",
        receitas,
        format_func=lambda x: x[1]
    )

    if st.button("Excluir"):
        with st.spinner("Excluindo receita..."):
            time.sleep(1)
            cursor.execute("DELETE FROM receitas WHERE id=?", (escolha[0],))
            conn.commit()
        st.success("Receita excluída!")

# ---------------- RODAPÉ ----------------
st.markdown("<div class='rodape'>Projeto desenvolvido com Streamlit</div>", unsafe_allow_html=True)
