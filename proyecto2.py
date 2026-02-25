import streamlit as st

# 1. EL ARCHIVADOR FUTBOLERO (9 Preguntas)
preguntas = [
    {"texto": "¿Qué selección ha ganado más Mundiales de la FIFA?", "opciones": ["Alemania", "Brasil", "Italia", "Argentina"], "correcta": "Brasil"},
    {"texto": "¿Cuántos jugadores por equipo hay en el campo en un partido oficial?", "opciones": ["10", "12", "11", "9"], "correcta": "11"},
    {"texto": "¿Quién es el máximo goleador histórico de los Mundiales?", "opciones": ["Miroslav Klose", "Ronaldo Nazário", "Pelé", "Leo Messi"], "correcta": "Miroslav Klose"},
    {"texto": "¿En qué país se inventó el fútbol moderno?", "opciones": ["Brasil", "Francia", "Inglaterra", "España"], "correcta": "Inglaterra"},
    {"texto": "¿Cuánto dura la prórroga en un partido eliminatorio?", "opciones": ["15 minutos", "20 minutos", "30 minutos", "45 minutos"], "correcta": "30 minutos"},
    {"texto": "¿Qué tarjeta significa expulsión directa en un partido?", "opciones": ["Amarilla", "Azul", "Roja", "Verde"], "correcta": "Roja"},
    {"texto": "¿Qué equipo ha ganado más Champions League?", "opciones": ["AC Milan", "Liverpool", "Real Madrid", "FC Barcelona"], "correcta": "Real Madrid"},
    {"texto": "¿Cada cuántos años se celebra un Mundial de fútbol?", "opciones": ["2 años", "4 años", "5 años", "3 años"], "correcta": "4 años"},
    {"texto": "¿Cómo se llama el área pequeña donde el portero tiene mayor protección?", "opciones": ["Área de meta", "Punto de penalti", "Área de castigo"], "correcta": "Área de meta"}
]

st.title("⚽ Examen de Fútbol 3º ESO")

# Reto 5: Pestañas
tab_examen, tab_informe = st.tabs(["🎮 Jugar Quiz", "📊 Acta del Partido"])

with tab_examen:
    with st.form("quiz_form"):
        respuestas_usuario = []
        for i, pregunta in enumerate(preguntas):
            st.subheader(f"Pregunta {i+1}")
            eleccion = st.radio(pregunta["texto"], ["No contestada"] + pregunta["opciones"], key=f"f_{i}")
            respuestas_usuario.append(eleccion)
            st.write("---")
        
        boton_enviar = st.form_submit_button("Finalizar Examen")

# 3. CÁLCULO Y CORRECCIÓN
if boton_enviar:
    aciertos = 0
    fallos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
        elif respuestas_usuario[i] != "No contestada":
            fallos += 1

    # Cálculo con penalización (Reto 4) y redondeo (Reto 1)
    puntos = aciertos - (fallos * 0.5)
    nota_final = round(max(0, (puntos / total) * 10), 2)

    with tab_informe:
        st.header(f"Tu nota: {nota_final} / 10")

        # --- Lógica de la animación de globos (TU PETICIÓN) ---
        if nota_final >= 8:
            st.balloons()
            st.success("¡Increíble! Eres un experto total.")
        
        # Feedback detallado (Reto 3)
        if nota_final == 10:
            st.write("✨ Excelente")
        elif nota_final >= 9:
            st.write("🌟 Sobresaliente")
        elif nota_final >= 7:
            st.write("🔝 Notable")
        elif nota_final >= 6:
            st.write("✅ Bien")
        elif nota_final >= 5:
            st.write("👌 Suficiente")
        else:
            st.write("❌ Insuficiente")

        # Informe Markdown (Reto 5)
        st.markdown("### 📝 Resumen del VAR")
        for i in range(total):
            txt = preguntas[i]['texto']
            resp = respuestas_usuario[i]
            corr = preguntas[i]['correcta']
            if resp == corr:
                st.markdown(f"**{i+1}.** {txt} -> ✅ `{resp}`")
            else:
                st.markdown(f"**{i+1}.** {txt} -> ❌ `{resp}` (Era: **{corr}**)")
