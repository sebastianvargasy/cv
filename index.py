import streamlit as st

# Definir estilos CSS
css = """
h1 {
    color: #f63366;
    font-size: 3.5rem;
    font-family: 'Arial', sans-serif;
    text-align: center;
}

h2 {
    color: #262730;
    font-size: 2.5rem;
    font-family: 'Arial', sans-serif;
}

p {
    color: #262730;
    font-size: 1.2rem;
    font-family: 'Arial', sans-serif;
}

.section {
    margin-top: 40px;
    margin-bottom: 20px;
}

.subsection {
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.2rem;
    font-weight: bold;
}

ul {
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 1.2rem;
    list-style-type: disc;
    margin-left: 20px;
}

hr {
    margin-top: 40px;
    margin-bottom: 40px;
    border: 0;
    border-top: 2px solid #f63366;
}
"""

# Aplicar estilos CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Crear encabezado
st.markdown("<h1>Currículum Vitae</h1>", unsafe_allow_html=True)
st.markdown("<h2>Nombre Apellido</h2>", unsafe_allow_html=True)
st.markdown("<p>Correo electrónico: correo@ejemplo.com</p>", unsafe_allow_html=True)
st.markdown("<p>Teléfono: +1 555-555-5555</p>", unsafe_allow_html=True)

# Crear secciones
st.markdown("<div class='section'><h2>Resumen</h2><p>Resumen profesional en unas pocas palabras...</p></div>", unsafe_allow_html=True)

st.markdown("<div class='section'><h2>Experiencia Laboral</h2><div class='subsection'>Desarrollador de Software en XYZ Corp</div><p>Fecha: Enero 2020 - presente</p><ul><li>Responsable de la arquitectura y diseño de la aplicación.</li><li>Desarrollado en Python, utilizando el marco de trabajo Django.</li></ul><hr><div class='subsection'>Desarrollador de Software en ABC Inc</div><p>Fecha: Junio 2018 - Diciembre 2019</p><ul><li>Desarrollado en Java, utilizando el marco de trabajo Spring Boot.</li><li>Participado en el diseño y desarrollo de una aplicación móvil.</li></ul></div>", unsafe_allow_html=True)

st.markdown("<div class='section'><h2>Educación</h2><div class='subsection'>Licenciado en Informática</div><p>Universidad de Ejemplo</p><p>Fecha de graduación: Junio 2018</p><p>Tesis: 'Desarrollo de una aplicación móvil utilizando React Native'</p></div>", unsafe_allow_html=True)

st.markdown("<div class='section'><h2>Habilidades</h2><ul><li>Python</li><li>Java</li><li
