# My Library 📖

- This repository contains a project developed in Python using Streamlit and PostgreSQL to register and view books. This project was created to manage the books in my private library and is currently only available locally.

- **Book Registration:** Add new books to the library with information such as title, author, pages, and image.
- **Book View:** View the list of registered books.

## Technologies used
- **Python**
- **Streamlit:** Framework for creating interactive web applications `pip install streamlit`
- **PostgreSQL:** Relational database used to store book information `pip install psycopg2-binary`

#### Creation table `Livros`
```sql 
CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    autor VARCHAR(255),
    ano INTEGER,
    paginas INTEGER,
    imagem BYTEA
);
```

#### Under construction: 🚧
- Own page for each book
- Add observations/records about the book
- CRUD (for now just `create` and `read`)

#### For now:
```
my_library/
├── cadastro.py/
├── connection_db.py
├── view.py (empty)
└── README.md
```
<h4 align="center">
    <b>A dúvida é o princípio da sabedoria - Aristóteles</b>
</h4>


