import streamlit as st
import requests

def app():
    st.title("Busca de Pokémon")

    pokemon = st.text_input("Digite o nome de um Pokémon:").lower()

    if st.button("Buscar"):
        link = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        
        try:
            requisição = requests.get(link)

            if requisição.status_code == 200:
                dados = requisição.json()

                informações = {
                    "Nome": dados["name"].capitalize(),
                    "Altura": dados["height"],
                    "Peso": dados["weight"],
                    "Tipos": [t["type"]["name"] for t in dados["types"]],
                }

                st.subheader("📌 Informações do Pokémon")
                st.write(informações)

                st.image(dados["sprites"]["front_default"], caption=pokemon.capitalize())

            else:
                st.error("Pokémon não encontrado.")

        except Exception as e:
            st.error(f"Ocorreu o erro: {e}")