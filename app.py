import streamlit as st

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Livro de Receitas 🍰",
    page_icon="🍴",
    layout="centered"
)

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
    animation: fadeSlide 1.5s ease;
}

.card {
    background-color: #fff7f0;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
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
st.markdown("<div class='subtitle'>Receitas simp

