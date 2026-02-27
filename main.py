import os
import re
import sys

from PySide6 import QtWidgets, QtCore, QtGui


def ExtraerNombre(nombre):
    nombre = os.path.splitext(nombre)[0]

    # eliminar resoluciones, codecs y tags
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


class Midgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.result_area = QtWidgets.QTextEdit()
        self.path_input = QtWidgets.QLineEdit()
        self.file_list = QtWidgets.QListWidget()
        self.file_preview = QtWidgets.QListWidget()

        self.rename_btn = None

        self.nuevo_nombre = None
        self.archivo = None
        self.folder = None

        self.setWindowTitle("Series Renamer APP")
        self.setWindowIcon(QtGui.QIcon("Icon.ico"))
        self.resize(900, 600)

        self.path = ""
        self.extension = (
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".mpg",
        )
        self.extension_sub = (
            ".srt",
            ".sub",
            ".ass",
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

        # Selector de carpeta
        folder_layout = QtWidgets.QHBoxLayout()

        self.path_input = QtWidgets.QLineEdit()
        self.path_input.setPlaceholderText("Selecciona la carpeta...")
        self.path_input.setClearButtonEnabled(True)
        self.path_input.textChanged.connect(self.clear_btn)
        folder_layout.addWidget(self.path_input)

        browse_btn = QtWidgets.QPushButton("📂 Buscar")
        browse_btn.clicked.connect(self.select_folder)
        folder_layout.addWidget(browse_btn)

        main_layout.addLayout(folder_layout)

        # Contenedor para los dos titulos de las listas
        title_container = QtWidgets.QHBoxLayout()

        main_layout.addLayout(title_container)

        # Contenedor para las dos listas
        list_container = QtWidgets.QHBoxLayout()

        # Lista de archivos (izquierda)
        self.file_list = QtWidgets.QListWidget()
        self.file_list.setMinimumWidth(300)
        list_container.addWidget(self.file_list)

        # Lista de previsualización (derecha)
        self.file_preview = QtWidgets.QListWidget()
        self.file_preview.setMinimumWidth(300)

        list_container.addWidget(self.file_preview)

        main_layout.addLayout(list_container)

        # Botones
        btn_layout = QtWidgets.QHBoxLayout()

        scan_btn = QtWidgets.QPushButton("🔍 Escanear")
        scan_btn.clicked.connect(self.ListVideos)
        btn_layout.addWidget(scan_btn)

        self.rename_btn = QtWidgets.QPushButton("✏️ Renombrar")
        self.rename_btn.clicked.connect(self.RenombrarNombre)
        btn_layout.addWidget(self.rename_btn)

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

    # ---------------- Style ---------------- #

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
                QScrollBar:vertical {
                    border: none;
                    background: #2D2D2D;
                    width: 14px;
                    border-radius: 7px;
                    margin: 0px;
                }

                QScrollBar::handle:vertical {
                    background: #555555;
                    min-height: 20px;
                    border-radius: 7px;
                }

                QScrollBar::handle:vertical:hover {
                    background: #777777;
                }

                QScrollBar::handle:vertical:pressed {
                    background: #999999;
                }

                QScrollBar::add-line:vertical, 
                QScrollBar::sub-line:vertical {
                    border: none;
                    background: none;
                    height: 0px;
                }

                QScrollBar::add-page:vertical, 
                QScrollBar::sub-page:vertical {
                    background: none;
                }

                QScrollBar:horizontal {
                    border: none;
                    background: #2D2D2D;
                    height: 14px;
                    border-radius: 7px;
                    margin: 0px;
                }

                QScrollBar::handle:horizontal {
                    background: #555555;
                    min-width: 20px;
                    border-radius: 7px;
                }

                QScrollBar::handle:horizontal:hover {
                    background: #777777;
                }

                QScrollBar::add-line:horizontal, 
                QScrollBar::sub-line:horizontal {
                    border: none;
                    background: none;
                    width: 0px;
                }
            """)

    # ---------------- Funciones ---------------- #
    def clear_btn(self):
        if self.result_area:
            self.file_list.clear()
            self.file_preview.clear()
            self.result_area.clear()

    def select_folder(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Seleccionar carpeta"
        )
        if self.folder:
            self.path = self.folder
            self.path_input.setText(self.folder)

            self.rename_btn.setEnabled(True)
            self.rename_btn.setStyleSheet("background-color: #007ACC")

    def ListVideos(self):
        self.file_list.clear()
        self.file_preview.clear()
        self.ListaV.clear()
        self.result_area.clear()
        self.path = self.path_input.text()

        # Habilitar boton de renombrar cuando pulsas en Escanear
        self.rename_btn.setStyleSheet("background-color: #007ACC")
        self.rename_btn.setEnabled(True)

        if os.path.exists(self.path) and os.path.isdir(self.path):
            videos = []
            subtitles = []

            # Hacer la Lista
            for self.archivo in os.listdir(self.path):

                if self.archivo.lower().endswith(self.extension):
                    videos.append(self.archivo)
                elif self.archivo.lower().endswith(self.extension_sub):
                    subtitles.append(self.archivo)

            if videos == [] and subtitles == []:
                self.result_area.append("❌ En tu ruta no hay videos o subtitulos")

            # Ordenar numericamente 1,2,3,10
            def ordenacion(file):
                if isinstance(file, str):
                    number = ExtraerNombre(file)
                    return number if number is not None else float("inf")
                return None

            try:
                if videos:
                    videos.sort(key=ordenacion)
                if subtitles:
                    subtitles.sort(key=ordenacion)
            except Exception as e:
                print(f"Error al ordenar: {e}")  # Mas debug que otra cosa ;)

            # Mostrar Videos
            for archivo in videos:
                self.ListaV.append(archivo)
                numero = ExtraerNombre(archivo)

                if numero:
                    nuevo = f"{numero}{os.path.splitext(archivo)[1]}"
                    self.file_list.addItem(f"{archivo}")
                    self.file_preview.addItem(f"{nuevo}")
                else:
                    self.file_list.addItem(f"{archivo}  ⚠️ No es posible renombrar :(")

            # Mostrar Subtitulos
            for archivo in subtitles:
                self.ListaV.append(archivo)
                numero = ExtraerNombre(archivo)

                if numero:
                    nuevo = f"{numero}{os.path.splitext(archivo)[1]}"
                    self.file_list.addItem(f"{archivo}")
                    self.file_preview.addItem(f"{nuevo}")
                else:
                    self.file_list.addItem(f"{archivo}  ⚠️ No es posible renombrar :(")
        else:
            if self.folder is None:
                self.result_area.append("❌ Por favor ingrese una ruta")

            else:
                if (
                    os.path.exists(self.path) is not True
                    and os.path.isdir(self.path) is not True
                ):
                    self.result_area.append("❌ Ruta Inválida")

    def RenombrarNombre(self):
        video = None
        todo_ren = False
        for video in self.ListaV:
            numero = ExtraerNombre(video)

            if numero:
                extension = os.path.splitext(video)[1]
                self.nuevo_nombre = f"{numero}{extension}"
                if video != self.nuevo_nombre:
                    try:
                        os.rename(
                            os.path.join(self.path, video),
                            os.path.join(self.path, self.nuevo_nombre),
                        )
                        self.result_area.append(f"✅ {video} ➜ {self.nuevo_nombre}")

                    except (
                        FileNotFoundError
                    ):  # [WinError 2] El sistema no puede encontrar el archivo especificado
                        todo_ren = True

        if todo_ren:
            self.result_area.append(
                "❌ Por favor ingrese una nueva ruta, ya esta todo renombrado"
            )
            self.rename_btn.setStyleSheet("background-color: gray")
            self.rename_btn.setEnabled(False)
        if video == self.nuevo_nombre:
            self.result_area.append("✅ Esta todo renombrado")
            self.rename_btn.setStyleSheet("background-color: gray")
            self.rename_btn.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Midgets()
    window.show()
    sys.exit(app.exec())
