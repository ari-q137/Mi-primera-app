import streamlit as st

# Configuración de la página
st.set_page_config(page_title="app prueba")

# Título principal
st.title("¡Hola, mundo!")

# Subtítulo o texto descriptivo
st.write("Bienvenido a mi primera aplicación web creada con Streamlit y Python.")

# Campo de texto interactivo
nombre = st.text_input("¿Cómo te llamas?")

# Botón y respuesta condicional
if st.button("Saludar"):
    if nombre:
        st.success(f"¡Hola, {nombre}! Qué bueno tenerte por aquí.")
    else:
        st.warning("Por favor, escribe tu nombre para que pueda saludarte.")
