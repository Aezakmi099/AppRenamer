import os
import re
import sys
from PySide6 import QtWidgets, QtCore, QtGui


def ExtraerNombre(nombre):
    patrones = [
        r"(?i)\b(?:cap(?:itulo)?|chapter|ch)\s*[\.\-_ ]?\s*(\d{1,4})\b",
        r"(?i)\b(?:ep(?:isodio)?|episode)\s*[\.\-_ ]?\s*(\d{1,4})\b",
        r"(?i)\b(?:cap|ep|ch)\w*\s*[\.\-_ ]?\s*0*(\d{1,4})\b",
        r"(?i)E0*(\d{1,3})\b",
        r"(?i)\bc\.?\s*0*(\d{1,4})\b",
        r"(?i)(?:^|[^a-z0-9])\d{1,2}\s*x\s*0*(\d{1,3})(?=\D|$)",
        r"(\d{1,4})(?!.*\d)",
    ]

    nombre = os.path.splitext(nombre)[0]
    for patron in patrones:
        m = re.search(patron, nombre)
        if m:
            return int(m.group(1))

    return None


class Mywidgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.result_area = None
        self.file_list = None
        self.path_input = None
        self.setWindowTitle("Series Renamer APP")
        self.setWindowIcon(QtGui.QIcon("Icon.ico"))
        self.resize(900, 600)

        self.path = ""
        self.extenciones = (
            ".mp4",
            ".mpg",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".str",
        )
        self.ListaV = []

        self.setupUI()
        self.apply_dark_theme()

    def setupUI(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        # Título
        title = QtWidgets.QLabel("🎬 Series Renamer APP")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(title)

        # Selector de carpeta y eliminar carpeta seleccionada
        folder_layout = QtWidgets.QHBoxLayout()

        self.path_input = QtWidgets.QLineEdit()
        self.path_input.setPlaceholderText("Selecciona la carpeta...")
        folder_layout.addWidget(self.path_input)

        browse_btn = QtWidgets.QPushButton("📂 Buscar")
        clear_btn = QtWidgets.QPushButton("🧹 Limpiar")
        clear_btn.clicked.connect(self.clear_folders)
        folder_layout.addWidget(browse_btn)
        folder_layout.addWidget(clear_btn)
        browse_btn.clicked.connect(self.select_folder)
        folder_layout.addWidget(browse_btn)

        main_layout.addLayout(folder_layout)

        # Lista de archivos
        self.file_list = QtWidgets.QListWidget()
        main_layout.addWidget(self.file_list)

        # Botones parte baja
        btn_layout = QtWidgets.QHBoxLayout()

        scan_btn = QtWidgets.QPushButton("🔍 Escanear")
        scan_btn.clicked.connect(self.ListaVideos)
        btn_layout.addWidget(scan_btn)

        rename_btn = QtWidgets.QPushButton("✏️ Renombrar")
        rename_btn.clicked.connect(self.RenombrarNombre)
        btn_layout.addWidget(rename_btn)

        main_layout.addLayout(btn_layout)

        # Área de resultados
        self.result_area = QtWidgets.QTextEdit()
        self.result_area.setReadOnly(True)
        main_layout.addWidget(self.result_area)

        # CREDITOS
        autor = QtWidgets.QLabel("Hecho por Aezakmi ;)")
        autor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        autor.setStyleSheet("font-size: 10px; font-weight: bold;")
        main_layout.addWidget(autor)

    # ---------------- Tema oscuro ---------------- #

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            QLineEdit, QTextEdit, QListWidget {
                background-color: #252525;
                border: 1px solid #404040;
                padding: 5px;
            }
            QPushButton {
                background-color: #007ACC;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)

    # ---------------- Funciones ---------------- #

    def select_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")
        if folder:
            self.path = folder
            self.path_input.setText(folder)

    def clear_folders(self):
        self.path = ''
        self.path_input.clear()
        self.result_area.clear()
        self.file_list.clear()
        self.ListaV.clear()

    def ListaVideos(self):
        self.file_list.clear()
        self.ListaV.clear()
        self.result_area.clear()

        self.path = self.path_input.text()

        if os.path.exists(self.path) and os.path.isdir(self.path):
            videos = []
            subtitulos = []

            # Hacer la Lista
            for archivo in os.listdir(self.path):
                if archivo.lower().endswith(self.extenciones):
                    videos.append(archivo)
                elif archivo.lower().endswith(".srt"):
                    subtitulos.append(archivo)

            # Ordenar numericamente 1,2,3,10
            def ordenacion(file):
                if isinstance(file, str):
                    number = ExtraerNombre(file)
                    return number if number is not None else float("inf")
                return None

            try:
                if videos:
                    videos.sort(key=ordenacion)
                if subtitulos:
                    subtitulos.sort(key=ordenacion)
            except Exception as e:
                print(f"Error al ordenar: {e}")

            # Mostrar Videos
            for archivo in videos:
                self.ListaV.append(archivo)
                numero = ExtraerNombre(archivo)

                if numero:
                    nuevo = f"{numero}{os.path.splitext(archivo)[1]}"
                    self.file_list.addItem(f"{archivo}  ➜  {nuevo}")
                else:
                    self.file_list.addItem(f"{archivo}  ⚠️ No encontrado")

            # Mostrar Subtitulos
            for archivo in subtitulos:
                self.ListaV.append(archivo)
                numero = ExtraerNombre(archivo)

                if numero:
                    nuevo = f"{numero}{os.path.splitext(archivo)[1]}"
                    self.file_list.addItem(f"{archivo}  ➜  {nuevo}")
                else:
                    self.file_list.addItem(f"{archivo}  ⚠️ No encontrado")
        else:
            if self.file_list.count() == 0:
                self.result_area.append("❌ Ruta Invalida")

    def RenombrarNombre(self):
        for video in self.ListaV:
            numero = ExtraerNombre(video)

            if numero:
                extension = os.path.splitext(video)[1]
                nuevo_nombre = f"{numero}{extension}"

                if video != nuevo_nombre:
                    try:
                        os.rename(
                            os.path.join(self.path, video),
                            os.path.join(self.path, nuevo_nombre),
                        )
                        self.result_area.append(f"✅ {video} ➜ {nuevo_nombre}")
                    except Exception as e:
                        self.result_area.append(f"❌ Error: {e}")

        if self.file_list is None:
            self.result_area.append("✔ Proceso terminado\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Mywidgets()
    window.show()
    sys.exit(app.exec())
