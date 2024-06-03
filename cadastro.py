import base64
import streamlit as st
from PIL import Image
import io

from connection_db import get_connection


def cadastrar_livro():
    st.title("Cadastro de Livros")

    nome = st.text_input("Nome")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano", min_value=0, max_value=2100, step=1)
    paginas = st.number_input("Páginas", min_value=1, step=1)
    imagem = st.file_uploader("Imagem", type=["jpg", "jpeg", "png"])

    if st.button("Cadastrar"):
        if nome and autor and ano and paginas and imagem:
            # Converte a imagem para um formato apropriado
            image = Image.open(imagem)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            img_byte_arr = img_byte_arr.getvalue()

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO livros (nome, autor, ano, paginas, imagem) VALUES (%s, %s, %s, %s, %s)",
                (nome, autor, ano, paginas, img_byte_arr)
            )
            conn.commit()
            cursor.close()
            conn.close()
            st.success("Livro cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def visualizar_livros():
    st.title("Livros Cadastrados")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, autor, ano, paginas, imagem FROM livros")
    livros = cursor.fetchall()
    cursor.close()
    conn.close()

    # Define o CSS para os cards
    st.markdown("""
        <style>
        .card {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(1, 1, 1, 0.1);
            margin-bottom: 20px;
            width: 200px;
            display: inline-block;
            vertical-align: top;
        }
        .card img {
            width: 100%;
            height: auto;
            border-radius: 5px;
        }
        .card h4 {
            margin: 10px 0;
            font-size: 1.1em;
        }
        .card p {
            margin: 5px 0;
            font-size: 0.9em;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    for livro in livros:
        nome, autor, ano, paginas, imagem = livro
        img_data = base64.b64encode(imagem).decode('utf-8')
        img_html = f'<img src="data:image/png;base64,{img_data}" class="card-img">'
        st.markdown(f"""
            <div class="card">
                {img_html}
                <h4>{nome}</h4>
                <p><strong>Autor:</strong> {autor}</p>
                <p><strong>Ano:</strong> {ano}</p>
                <p><strong>Páginas:</strong> {paginas}</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.sidebar.title("Menu")
    escolha = st.sidebar.selectbox("Escolha uma página", ["Visualizar Livros", "Cadastrar Livro"])

    if escolha == "Visualizar Livros":
        visualizar_livros()
    elif escolha == "Cadastrar Livro":
        cadastrar_livro()
