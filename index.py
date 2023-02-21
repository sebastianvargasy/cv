import streamlit as st
import streamlit_themes as stt

# Cambiar el tema de Streamlit
stt.themes["my_custom_theme"] = {
    "primaryColor": "#f63366",
    "backgroundColor": "#f5f5f5",
    "secondaryBackgroundColor": "#ebf2ff",
    "textColor": "#262730",
    "font": "sans serif"
}
stt.set_theme("my_custom_theme")

# Crear encabezado y subtítulo
st.title("Currículum Vitae")
st.write("Nombre Apellido")
st.write("Correo electrónico: correo@ejemplo.com")
st.write("Teléfono: +1 555-555-5555")

# Crear secciones
st.header("Resumen")
st.write("Resumen profesional en unas pocas palabras...")

st.header("Experiencia Laboral")
st.subheader("Desarrollador de Software en XYZ Corp")
st.write("Fecha: Enero 2020 - presente")
st.write("- Responsable de la arquitectura y diseño de la aplicación.")
st.write("- Desarrollado en Python, utilizando el marco de trabajo Django.")

st.subheader("Desarrollador de Software en ABC Inc")
st.write("Fecha: Junio 2018 - Diciembre 2019")
st.write("- Desarrollado en Java, utilizando el marco de trabajo Spring Boot.")
st.write("- Participado en el diseño y desarrollo de una aplicación móvil.")

st.header("Educación")
st.subheader("Licenciado en Informática")
st.write("Universidad de Ejemplo")
st.write("Fecha de graduación: Junio 2018")
st.write("Tesis: 'Desarrollo de una aplicación móvil utilizando React Native'")

st.header("Habilidades")
st.write("- Python")
st.write("- Java")
st.write("- Django")
st.write("- Spring Boot")

st.header("Logros")
st.write("- Lanzamiento exitoso de la aplicación móvil en ABC Inc.")
st.write("- Recibido premio al empleado del mes en XYZ Corp.")

st.header("Referencias")
st.write("Disponibles a petición.")

# Crear pie de página
st.write("---")
st.write("© 2023 Nombre Apellido. Todos los derechos reservados.")
