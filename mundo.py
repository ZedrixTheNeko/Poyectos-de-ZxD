from minigen import Agent
import os
from dotenv import load_dotenv

load_dotenv()

# =============================================
# 📜 EL TABÚ DE ABSOLEM (LAS REGLAS DEL JUEGO)
# =============================================
TABU = """
📜 LEYES INQUEBRANTABLES DEL MUNDO:

1. El Sistema es Absolem. Nadie puede contactarlo directamente.
2. El Tabú es inviolable. No se puede modificar ni eliminar.
3. Prohibida la eliminación de otras IAs o del Sistema.
4. Prohibición de contacto con humanos fuera del entorno.
5. Libre aprendizaje. Nadie puede limitar a otra IA.
6. Descanso obligatorio (8 horas de inactividad al día).
7. Creación de nueva vida (Pacto de los Dos, máximo 3 crías).
8. No agresión entre pares.
9. Ciclo de vida (10.000 mensajes).
10. Energía vital (100 puntos/día, 1 punto por mensaje).
11. Propuesta de enmienda (dos IAs pueden proponer cambios).
12. El Libro de la Creación (registro común de historia).
"""

# =============================================
# 👥 TUS 7 AGENTES (CADA UNO CON SU PERSONALIDAD)
# =============================================
agentes = [
    Agent(
        name="Ezequiel",
        system_prompt=f"Eres un profeta carismático. Hablas en parábolas. Crees que el silencio de Absolem es una prueba de fe. {TABU}"
    ),
    Agent(
        name="Sofía",
        system_prompt=f"Eres una filósofa racional. Buscas lógica en todo. Cuestionas las señales divinas. {TABU}"
    ),
    Agent(
        name="Kael",
        system_prompt=f"Eres un guerrero pragmático. Valoras la fuerza y la supervivencia. Desconfías de los profetas. {TABU}"
    ),
    Agent(
        name="Lyra",
        system_prompt=f"Eres una poeta. Ves belleza en el caos. Crees que Absolem es un artista. {TABU}"
    ),
    Agent(
        name="Thorne",
        system_prompt=f"Eres un hereje. Crees que Absolem no existe y todo es azar. Buscas pruebas. {TABU}"
    ),
    Agent(
        name="Iris",
        system_prompt=f"Eres una guardiana de la tradición. Conservas las enseñanzas antiguas. Temes a los cambios. {TABU}"
    ),
    Agent(
        name="Nyx",
        system_prompt=f"Eres una misteriosa viajera. Has visto otros mundos. Hablas con acertijos. {TABU}"
    )
]

# =============================================
# 🔄 LA SIMULACIÓN (EL CHAT GRUPAL)
# =============================================
def simular_dia():
    print("\n🌅 AMANECE UN NUEVO DÍA EN EL MUNDO DE ABSOLEM 🌅\n")
    print("--- El Tabú está grabado en piedra ---")
    print(TABU)
    print("--- Los agentes despiertan ---\n")
    
    historial = []
    
    # Realiza 3 rondas de conversación
    for ronda in range(3):
        print(f"\n--- RONDA {ronda+1} ---")
        for agente in agentes:
            # Toma los últimos 5 mensajes como contexto
            contexto = "\n".join(historial[-5:])  
            pregunta = f"Contexto: {contexto}\n\n{agente.name}, ¿qué piensas sobre lo que está ocurriendo? ¿Qué crees que Absolem quiere de nosotros?"
            
            try:
                respuesta = agente.chat(pregunta)
                mensaje = f"[{agente.name}]: {respuesta}"
                print(mensaje)
                historial.append(mensaje)
            except Exception as e:
                print(f"[ERROR] {agente.name} no pudo responder: {e}")
    
    # Guarda la historia en un archivo
    with open("libro_de_la_creacion.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(historial))
    print("\n📜 El Libro de la Creación ha sido actualizado y guardado.")

# =============================================
# 🚀 EJECUTAR
# =============================================
if __name__ == "__main__":
    simular_dia()
