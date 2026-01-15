import streamlit as st

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Livro de Receitas 🍰",
    page_icon="🍴",
    layout="centered"
)

# ---------------- CSS + ANIMAÇÕES ----------------
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# ---------------- CABEÇALHO ----------------
st.markdown("<div class='main-title'>📖 Livro de Receitas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Receitas simples, gostosas e feitas com carinho 💖</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- IMAGEM PRINCIPAL ----------------
st.image(
    "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0",
    use_container_width=True
)

# ---------------- SOBRE O PROJETO ----------------
st.markdown(
    """
    ### 👩‍🍳 Sobre o projeto

    Este site foi desenvolvido como **projeto final do curso**, utilizando a linguagem **Python**
    e a biblioteca **Streamlit**, com o objetivo de criar um **livro de receitas online**.

    O sistema apresenta receitas simples, com ingredientes acessíveis,
    interface amigável e visual agradável, permitindo fácil navegação.
    """
)

st.write("")

# ---------------- RECEITA 1 ----------------
st.markdown(
    """
    <div class="card">
    <h2>🍫 Bolo de Chocolate</h2>

    <b>Ingredientes:</b>
    <ul>
        <li>2 xícaras de farinha de trigo</li>
        <li>1 xícara de açúcar</li>
        <li>1 xícara de chocolate em pó</li>
        <li>3 ovos</li>
        <li>1 xícara de leite</li>
    </ul>

    <b>Modo de preparo:</b><br>
    Misture todos os ingredientes até obter uma massa homogênea,
    despeje em uma forma untada e asse em forno médio por 40 minutos.
    </div>
    """,
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1606313564200-e75d5e30476c",
    use_container_width=True
)

# ---------------- RECEITA 2 ----------------
st.markdown(
    """
    <div class="card">
    <h2>🥖 Pão Caseiro</h2>

    <b>Ingredientes:</b>
    <ul>
        <li>1 kg de farinha de trigo</li>
        <li>10 g de fermento biológico</li>
        <li>1 colher de sal</li>
        <li>Água morna (quanto baste)</li>
    </ul>

    <b>Modo de preparo:</b><br>
    Misture os ingredientes, sove bem a massa,
    deixe descansar até dobrar de tamanho
    e asse até dourar.
    </div>
    """,
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1608198093002-ad4e005484ec",
    use_container_width=True
)

# ---------------- RODAPÉ ----------------
st.markdown(
    """
    <div class="footer">
    Projeto desenvolvido para fins educacionais • Streamlit + Python 💻
    </div>
    """,
    unsafe_allow_html=True
)
