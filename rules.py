import json
from experta import KnowledgeEngine, Rule
from facts import Organism

# Cargar datos desde el archivo JSON
with open("phyla_data.json", "r", encoding="utf-8") as file:
    phyla_data = json.load(file)

# Extraer características y definiciones
phyla_caracteristicas = {phylum: data["caracteristicas"] for phylum, data in phyla_data.items()}
phyla_definiciones = {phylum: data["definicion"] for phylum, data in phyla_data.items()}

class PhylumExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.phylum_coincidencias = {phylum: 0 for phylum in phyla_caracteristicas}
        self.total_caracteristicas = len(next(iter(phyla_caracteristicas.values())))

    def verificar_coincidencias(self, organism, phylum, caracteristicas):
        coincidencias = sum(
            1 for key, value in caracteristicas.items() if organism.get(key) == value
        )
        self.phylum_coincidencias[phylum] = coincidencias

    @Rule(Organism())
    def evaluar_phyla(self):
        organism = self.facts[1]
        for phylum, caracteristicas in phyla_caracteristicas.items():
            self.verificar_coincidencias(organism, phylum, caracteristicas)
        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("\nResultados:")

        # Ordenar phyla por porcentaje de coincidencias en orden descendente
        phyla_ordenados = sorted(
            self.phylum_coincidencias.items(),
            key=lambda item: (item[1] / self.total_caracteristicas) * 100,
            reverse=True
        )

        # Obtener el phylum más probable y su porcentaje
        phylum_mas_probable, coincidencias = phyla_ordenados[0]
        porcentaje_mas_probable = (coincidencias / self.total_caracteristicas) * 100

        if porcentaje_mas_probable >= 70:
            print(f"El phylum más probable es: {phylum_mas_probable} ({porcentaje_mas_probable:.2f}%) coincidencias")
            print(f"\nDefinición: {phyla_definiciones[phylum_mas_probable]}\n")
            print("Características del phylum:")

            for key, value in phyla_caracteristicas[phylum_mas_probable].items():
                print(f"  - {key.replace('_', ' ').capitalize()}: {value}")

            print("\nOtros posibles phyla:")
            contador = 0
            for phylum, coincidencias in phyla_ordenados[1:]:
                porcentaje = (coincidencias / self.total_caracteristicas) * 100
                if 70 <= porcentaje < 100:
                    contador += 1
                    print(f"  - {phylum}: {porcentaje:.2f}% coincidencias")

            if contador == 0:
                print("No hay otros posibles phyla.")
        else:
            print("\nNo se encontró un phylum con suficientes coincidencias.")
            print(f"El phylum con el porcentaje más cercano al 70% es:")

            # Buscar el phylum con el porcentaje más alto menor al 70%
            phylum_cercano, coincidencias_cercanas = max(
                (p for p in phyla_ordenados if (p[1] / self.total_caracteristicas) * 100 < 70),
                key=lambda item: (item[1] / self.total_caracteristicas) * 100,
                default=(None, 0)
            )

            if phylum_cercano:
                porcentaje_cercano = (coincidencias_cercanas / self.total_caracteristicas) * 100
                print(f"  - {phylum_cercano}: {porcentaje_cercano:.2f}% coincidencias")
            else:
                print("No se encontraron coincidencias cercanas.")



