import streamlit as st
import sqlite3

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

# ---------------- ESTILO / ANIMAÇÕES ----------------
st.markdown("""
<style>
@keyframes fade {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

body {
    background-color: #fffaf5;
}

.titulo {
    font-size: 46px;
    text-align: center;
    font-weight: bold;
    animation: fade 1s;
}

.subtitulo {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
    animation: fade 1.3s;
}

.card {
    background-color: #fff3e8;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    animation: fade 0.8s;
}

.card-chocolate {
    background-color: #c7a26b;
}

img {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TÍTULO ----------------
st.markdown("<div class='titulo'>📖 Livro de Receitas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Cadastre, edite e visualize suas receitas</div>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Menu",
    ["Adicionar Receita", "Ver Receitas", "Editar Receita", "Excluir Receita"]
)

# ---------------- ADICIONAR ----------------
if menu == "Adicionar Receita":
    nome = st.text_input("Nome da receita")
    ingredientes = st.text_area("Ingredientes")
    preparo = st.text_area("Modo de preparo")
    imagem = st.text_input("Link da imagem (opcional)")

    if st.button("Salvar receita"):
        cursor.execute(
            "INSERT INTO receitas (nome, ingredientes, preparo, imagem) VALUES (?, ?, ?, ?)",
            (nome, ingredientes, preparo, imagem)
        )
        conn.commit()
        st.success("Receita salva com sucesso!")

# ---------------- VER ----------------
elif menu == "Ver Receitas":
    cursor.execute("SELECT * FROM receitas")
    receitas = cursor.fetchall()

    for r in receitas:
        classe = "card-chocolate" if "chocolate" in r[1].lower() else "card"
        st.markdown(f"<div class='{classe}'>", unsafe_allow_html=True)
        st.subheader(r[1])

        if r[4]:
            st.image(r[4], width=300)

        st.markdown("**Ingredientes:**")
        st.write(r[2])

        st.markdown("**Modo de preparo:**")
        st.write(r[3])

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDITAR ----------------
elif menu == "Editar Receita":
    cursor.execute("SELECT id, nome FROM receitas")
    receitas = cursor.fetchall()

    escolha = st.selectbox("Escolha a receita", receitas, format_func=lambda x: x[1])

    novo_nome = st.text_input("Novo nome")
    novos_ing = st.text_area("Novos ingredientes")
    novo_prep = st.text_area("Novo modo de preparo")
    nova_img = st.text_input("Novo link da imagem")

    if st.button("Atualizar"):
        cursor.execute("""
        UPDATE receitas
        SET nome=?, ingredientes=?, preparo=?, imagem=?
        WHERE id=?
        """, (novo_nome, novos_ing, novo_prep, nova_img, escolha[0]))
        conn.commit()
        st.success("Receita atualizada!")

# ---------------- EXCLUIR ----------------
elif menu == "Excluir Receita":
    cursor.execute("SELECT id, nome FROM receitas")
    receitas = cursor.fetchall()

    escolha = st.selectbox("Escolha a receita para excluir", receitas, format_func=lambda x: x[1])

    if st.button("Excluir"):
        cursor.execute("DELETE FROM receitas WHERE id=?", (escolha[0],))
        conn.commit()
        st.success("Receita excluída!")
