# app/core/renamer.py
from pathlib import Path
from natsort import natsorted


class process:
    def __init__(self, main_window):
        self.main_window = main_window

    def scanFolder(self):
        text_to_remove = self.main_window.inputName.text()
        folder_path = self.main_window.path_input.text()

        if not folder_path:
            return "❌ Error: No hay carpeta seleccionada"

        try:
            ruta = Path(folder_path)

            if not ruta.exists():
                return "❌ La ruta no existe"

            extensions = {
                ".mp4",
                ".avi",
                ".mkv",
                ".mov",
                ".wmv",
                ".flv",
                ".webm",
                ".srt",
                ".vtt",
                ".ass",
                ".ssa",
                ".scc",
                ".sub",
                ".xml",
            }

            videos = [
                archivo.name
                for archivo in ruta.iterdir()
                if archivo.is_file() and archivo.suffix.lower() in extensions
            ]
            videos = natsorted(videos)

            if not videos:
                return f"⚠️ No se encontraron videos en {folder_path}"

            self.main_window.videos = videos

            self.main_window.file_list.clear()
            self.main_window.preview_list.clear()

            for video in videos:
                self.main_window.file_list.addItem(video)
                nuevo_nombre = " ".join(video.replace(text_to_remove, "").split())
                self.main_window.preview_list.addItem(nuevo_nombre)

            return ""

        except Exception as e:
            return f"❌ Error al escanear: {str(e)}"

    def renameFiles(self):
        text_to_remove = self.main_window.inputName.text()
        folder_path = self.main_window.path_input.text()

        if not hasattr(self.main_window, "videos") or not self.main_window.videos:
            return "❌ No hay archivos. Escanea primero."

        try:
            ruta = Path(folder_path)
            renamed_count = 0
            errors = []

            for video_name in self.main_window.videos:
                old_path = ruta / video_name
                new_name = video_name.replace(text_to_remove, "").strip()

                if new_name != video_name:
                    new_path = ruta / new_name
                    try:
                        old_path.rename(new_path)
                        renamed_count += 1
                    except Exception as e:
                        errors.append(f"{video_name}: {str(e)}")

            if renamed_count > 0:
                return self.scanFolder()

            return "⚠️ No hubo cambios"

        except Exception as e:
            return f"❌ Error: {str(e)}"
