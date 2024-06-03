#### Instalando o streamlit e a biblioteca para gerenciamento e conexões postgres
pip install streamlit psycopg2-binary

#### criação da tabela books
''' CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    autor VARCHAR(255),
    ano INTEGER,
    paginas INTEGER,
    imagem BYTEA
); '''
