import streamlit as st

def calcular_visitas_y_tiempo(edad_1, edad_2, frecuencia_anual, horas_por_visita, esperanza_vida=83):
    años_restantes_1 = max(esperanza_vida - edad_1, 0)
    años_restantes_2 = max(esperanza_vida - edad_2, 0)
    años_vida_compartida = min(años_restantes_1, años_restantes_2)

    numero_de_visitas = frecuencia_anual * años_vida_compartida
    tiempo_total_segundos = numero_de_visitas * horas_por_visita * 3600

    # Conversión a días, horas, minutos
    dias = tiempo_total_segundos // 86400
    horas_restantes = (tiempo_total_segundos % 86400) // 3600
    minutos_restantes = (tiempo_total_segundos % 3600) // 60

    return numero_de_visitas, int(dias), int(horas_restantes), int(minutos_restantes)

# Interfaz Streamlit
st.title("⏳ ¿Cuánto tiempo REAL os queda para veros?")
st.write("Calcula el tiempo que te queda para pasar con alguien importante, en función de vuestra edad, frecuencia de encuentros y duración media de cada uno.")

with st.form("formulario"):
    edad_1 = st.number_input("Edad de la persona 1", min_value=0, max_value=120, value=44)
    edad_2 = st.number_input("Edad de la persona 2", min_value=0, max_value=120, value=47)
    frecuencia_visitas = st.number_input("¿Cuántas veces os veis al año?", min_value=1, max_value=100, value=2)
    horas_por_visita = st.number_input("¿Cuántas horas soléis pasar en cada encuentro?", min_value=0.1, max_value=24.0, value=6.0)
    enviar = st.form_submit_button("Calcular")

if enviar:
    visitas, dias, horas, minutos = calcular_visitas_y_tiempo(edad_1, edad_2, frecuencia_visitas, horas_por_visita)

    st.markdown("## 🧾 Resultados")
    st.write(f"👥 Visitas restantes estimadas: **{int(visitas)} veces**")
    st.write(f"🕰️ Tiempo total que podréis compartir: **{dias} días, {horas} horas y {minutos} minutos**")

    if dias < 5:
        st.warning("⏳ ¡El tiempo juntos restante es realmente muy corto! Aprovechad cada momento.")

