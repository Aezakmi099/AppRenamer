
import os
import re

def extraer_numero(nombre):
    nombre = os.path.splitext(nombre)[0]

    nombre = re.sub(
        r"\b(480p|720p|1080p|2160p|x264|x265|h264|bluray|webrip)\b",
        "",
        nombre,
        flags=re.I,
    )

    patron = re.compile(r"(?<!\d)0*(\d{1,4})(?!.*\d)")
    m = patron.search(nombre)

    if m:
        return int(m.group(1))

    return None
