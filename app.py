import streamlit as st
import json
import os
import base64

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Livro de Receitas",
    page_icon="🍰",
    layout="centered"
)

# ---------------- CSS (CORES + ANIMAÇÕES) ----------------
st.markdown("""
<style>
body {
    background-color: #fffaf5;
}
.title {
    animation: fadeIn 2s;
    color: #d35400;
}
.card {
    background-color: #fff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #ddd;
    margin-bottom: 20px;
    animation: slideUp 1s;
}
button {
    background-color: #e67e22 !important;
    color: white !important;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
@keyframes slideUp {
    from {transform: translateY(30px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# ---------------- IMAGEM EMBUTIDA (BASE64) ----------------
img_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAM1BMVEX///
8AAAD5+fn09PTn5+fV1dXZ2dnCwsLa2trf39+qqqqOjo7Pz8+vr6+ysrJr7sEAAAB+UlEQVR4nO3bS27DMAxFUZP//6fd2a4YlJZx8MIkYc6y+4YdAAQAAAAAAAAAA8N8zYF5bq3S2X0m4l7bJZKp3J8xF3n9o+5X8zM2b9bZ2y8s5n8u5Yy+uV9nWZ1n1M8m7uYp2Z6Z2m9y0V7e2p3xw5Zr8vZtZ5sX7k6n7vWZ5f7r3n5m3m9Zz4ZP9k5xk9n9z8v6m9z0v7m9n9Y7u4AAAAAAAAAAADwL8wF3Q8lZzv7XwAAAABJRU5ErkJggg==
"""

st.markdown(
    f"<img src='data:image/png;base64,{img_base64}' width='100%'/>",
    unsafe_allow_html=True
)

# ---------------- BANCO DE DADOS (JSON) ----------------
ARQUIVO = "receitas.json"

def carregar_receitas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_receitas(receitas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(receitas, f, ensure_ascii=False, indent=4)

# ---------------- MENU ----------------
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "📖 Receitas", "➕ Adicionar Receita", "🎨 Sobre o Projeto"]
)

# ---------------- HOME ----------------
if menu == "🏠 Home":
    st.markdown("<h1 class='title'>📘 Livro de Receitas</h1>", unsafe_allow_html=True)
    st.write("""
    Este site foi desenvolvido para **cadastrar, visualizar, editar e excluir receitas**.
    
    O projeto utiliza **Streamlit**, aplica **estilos, animações, formulários e banco de dados**,
    conforme solicitado no trabalho final.
    """)

# ---------------- LISTAR / EDITAR RECEITAS ----------------
elif menu == "📖 Receitas":
    receitas = carregar_receitas()
    if not receitas:
        st.info("Nenhuma receita cadastrada.")
    else:
        for i, r in enumerate(receitas):
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader(r["nome"])
            st.write("**Ingredientes:**")
            st.write(r["ingredientes"])
            st.write("**Modo de preparo:**")
            st.write(r["modo"])

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✏️ Editar", key=f"edit{i}"):
                    st.session_state["editar"] = i
            with col2:
                if st.button("🗑️ Excluir", key=f"del{i}"):
                    receitas.pop(i)
                    salvar_receitas(receitas)
                    st.experimental_rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    if "editar" in st.session_state:
        idx = st.session_state["editar"]
        r = receitas[idx]

        st.markdown("## ✏️ Editar Receita")
        novo_nome = st.text_input("Nome", r["nome"])
        novos_ing = st.text_area("Ingredientes", r["ingredientes"])
        novo_modo = st.text_area("Modo de preparo", r["modo"])

        if st.button("Salvar Alterações"):
            receitas[idx] = {
                "nome": novo_nome,
                "ingredientes": novos_ing,
                "modo": novo_modo
            }
            salvar_receitas(receitas)
            del st.session_state["editar"]
            st.success("Receita atualizada!")
            st.experimental_rerun()

# ---------------- ADICIONAR RECEITA ----------------
elif menu == "➕ Adicionar Receita":
    st.markdown("<h2 class='title'>➕ Nova Receita</h2>", unsafe_allow_html=True)

    nome = st.text_input("Nome da receita")
    ingredientes = st.text_area("Ingredientes")
    modo = st.text_area("Modo de preparo")

    if st.button("Salvar Receita"):
        if nome and ingredientes and modo:
            receitas = carregar_receitas()
            receitas.append({
                "nome": nome,
                "ingredientes": ingredientes,
                "modo": modo
            })
            salvar_receitas(receitas)
            st.success("Receita cadastrada com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

# ---------------- SOBRE ----------------
elif menu == "🎨 Sobre o Projeto":
    st.markdown("<h2 class='title'>🎨 Sobre o Projeto</h2>", unsafe_allow_html=True)
    st.write("""
    **Objetivo:** Criar um sistema web para gerenciamento de receitas.

    **Tecnologias usadas:**
    - Python
    - Streamlit

    **Funcionalidades:**
    - Cadastro
    - Consulta
    - Edição
    - Exclusão
    - Estilização
    - Animações
    - Banco de dados local

    Projeto desenvolvido para fins acadêmicos.
    """)
