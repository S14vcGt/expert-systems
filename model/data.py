import pandas as pd

# Datos para características y etiquetas
data = {
    "nivel_organizacion": [
        "unicelular", "unicelular", "unicelular", "tejidos", "tejidos", 
        "tejidos", "organos", "organos", "tejidos", "tejidos",
        "organos", "organos", "tejidos", "organos", "organos",
    ],
    "simetria": [
        "asimetrica", "asimetrica", "radial", "bilateral", "bilateral",
        "radial", "bilateral", "bilateral", "radial", "radial",
        "bilateral", "bilateral", "radial", "bilateral", "bilateral",
    ],
    "capas_germinales": [
        "ninguna", "ninguna", "diploblastico", "triploblastico", "triploblastico",
        "diploblastico", "triploblastico", "triploblastico", "diploblastico", "triploblastico",
        "triploblastico", "triploblastico", "triploblastico", "triploblastico", "triploblastico",
    ],
    "cavidad_corporal": [
        "ninguna", "ninguna", "ninguna", "celomado", "celomado",
        "ninguna", "celomado", "celomado", "pseudocelomado", "celomado",
        "celomado", "celomado", "celomado", "celomado", "celomado",
    ],
    "segmentacion": [
        "no segmentado", "no segmentado", "no segmentado", "segmentado", "segmentado",
        "no segmentado", "segmentado", "segmentado", "no segmentado", "no segmentado",
        "segmentado", "segmentado", "no segmentado", "segmentado", "segmentado",
    ],
    "sistema_digestivo": [
        "incompleto", "incompleto", "incompleto", "completo", "completo",
        "completo", "completo", "completo", "completo", "completo",
        "completo", "completo", "completo", "completo", "completo",
    ],
    "sistema_nervioso": [
        "ninguno", "ninguno", "difuso", "ganglionar", "centralizado",
        "difuso", "ganglionar", "ganglionar", "difuso", "difuso",
        "ganglionar", "ganglionar", "ganglionar", "ganglionar", "centralizado",
    ],
    "sistema_corporal": [
        "hidrostatico", "hidrostatico", "hidrostatico", "exoesqueleto", "endoesqueleto",
        "hidrostatico", "hidrostatico", "hidrostatico", "hidrostatico", "hidrostatico",
        "exoesqueleto", "endoesqueleto", "hidrostatico", "exoesqueleto", "endoesqueleto",
    ],
    "reproduccion": [
        "asexual", "asexual", "sexual", "sexual", "sexual",
        "sexual", "sexual", "sexual", "sexual", "sexual",
        "sexual", "sexual", "sexual", "sexual", "sexual",
    ],
    "habitat": [
        "acuatico", "acuatico", "acuatico", "acuatico o terrestre", "acuatico, terrestre o aereo",
        "acuatico", "acuatico o terrestre", "acuatico o parasito", "acuatico", "acuatico",
        "acuatico o terrestre", "acuatico o parasito", "acuatico", "acuatico", "acuatico, terrestre o aereo",
    ],
}

labels = [
    "protozoa", "porifera", "cnidaria", "arthropoda", "chordata",
    "ctenophora", "mollusca", "annelida", "platyhelminthes", "nematoda",
    "echinodermata", "arthropoda", "protozoa", "mollusca", "chordata",
]

# Crear DataFrame para las características
df = pd.DataFrame(data)
