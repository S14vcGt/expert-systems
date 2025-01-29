from rules import PhylumExpertSystem
from facts import Organism

def obtener_respuesta(pregunta, opciones):
    """Solicita una respuesta al usuario y valida la entrada."""
    while True:
        respuesta = input(f"\n{pregunta} {opciones}: ").strip().lower()
        if respuesta in opciones:
            return respuesta
        print("Entrada no válida. Por favor, ingrese una de las opciones proporcionadas.")

def main():
    sistema = PhylumExpertSystem()
    sistema.reset()
    print("\nBienvenido al Sistema Experto de Clasificación de Organismos.")
    print("Responda las siguientes preguntas seleccionando una opción válida.\n")

    opciones_preguntas = {
        "nivel_organizacion": ["multicelular", "unicelular", "tejidos", "organos", "sistemas"],
        "simetria": ["bilateral", "radial", "variada", "ninguna"],
        "capas_germinales": ["diploblastico", "triploblastico", "ninguna"],
        "cavidad_corporal": ["ausente", "acelomado", "celomado", "pseudocelomado"],
        "segmentacion": ["segmentado", "no segmentado"],
        "sistema_digestivo": ["ausente", "completo", "incompleto"],
        "sistema_nervioso": ["ausente", "difuso", "ganglionar", "centralizado"],
        "sistema_corporal": ["hidrostatico", "exoesqueleto", "endoesqueleto", "ausente"],
        "reproduccion": ["asexual", "sexual", "asexual o sexual"],
        "habitat": ["acuatico", "acuatico o parasito", "acuatico o terrestre", "acuatico, terrestre o aereo"]
    }

    respuestas = {clave: obtener_respuesta(clave.replace("_", " ").capitalize(), opciones)
                  for clave, opciones in opciones_preguntas.items()}

    sistema.declare(Organism(**respuestas))
    sistema.run()

if __name__ == "__main__":
    main()
