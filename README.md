---

# 🎮 Pokédex com Login, Banco de Dados e API – Streamlit

Um projeto interativo de Pokédex, desenvolvido com **Python**, utilizando **Streamlit** para interface gráfica, **MySQL (via XAMPP)** para banco de dados e integração com a **PokéAPI** para busca automática de informações dos Pokémon.

---

## 🚀 Funcionalidades

✅ **Login e Cadastro de Usuários (Treinadores)**

* Armazenados no banco de dados MySQL.
* Cada treinador possui **nome, cidade e imagem de perfil**.

✅ **Cadastro de Pokémon vinculado ao Treinador**

* Busca os dados automaticamente via **PokéAPI** (altura, peso, tipo).
* Salva a **imagem do Pokémon** no sistema e registra o caminho no banco.
* Cada Pokémon fica vinculado ao **ID do treinador**.

✅ **Exclusão de Treinadores e seus Pokémon**

✅ **Interface Gráfica com Streamlit**

* Navegação entre páginas (login, cadastro, pokedex, deletar).
* Exibição das informações e imagens dos Pokémon cadastrados.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia                 | Uso                              |
| -------------------------- | -------------------------------- |
| **Python**                 | Lógica da aplicação              |
| **Streamlit**              | Interface gráfica                |
| **MySQL + XAMPP**          | Banco de dados local             |
| **PokéAPI**                | Consulta de dados dos Pokémon    |
| **OS**                     | Salvamento de imagens localmente |
| **mysql-connector-python** | Conexão com o banco de dados     |


---

## 🗄️ Banco de Dados (MySQL)

Banco: **treinadores_pokemon**

### 📌 Tabela `treinadores`

| Campo   | Tipo               |
| ------- | ------------------ |
| id (PK) | INT AUTO_INCREMENT |
| nome    | VARCHAR(100)       |
| cidade  | VARCHAR(100)       |
| imagem  | VARCHAR(255)       |

### 📌 Tabela `pokemons`

| Campo             | Tipo               |
| ----------------- | ------------------ |
| nome              | VARCHAR(100)       |
| altura            | FLOAT              |
| peso              | FLOAT              |
| tipo              | VARCHAR(50)        |
| treinador_id (FK) | INT                |
| imagem            | VARCHAR(255)       |

---
