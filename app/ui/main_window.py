
import os
from PySide6 import QtWidgets, QtCore, QtGui

from app.core.renamer import extraer_numero
from app.styles.theme import themes


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Series Renamer APP")
        self.resize(900, 600)

        self.path = ""
        self.videos = []

        self.current_theme = "dark"  # variable que guarda el tema actual

        self.setup_ui()
        self.apply_theme()  # aplicar el tema inicial
        
        
    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        
        titleLayout = QtWidgets.QHBoxLayout(self)
        
        self.btn_theme = QtWidgets.QPushButton()
        self.btn_theme.setStyleSheet("""
                                min-width: 20px;
                                min-height: 25px;
                                max-width: 20px;
                                max-height: 25px;
                                font-size: 11px;
                                padding: 3px 8px;
                            """)
        self.btn_theme.setIcon(QtGui.QIcon("Icons/DarkTheme Icon.png"))
        self.btn_theme.clicked.connect(self.toggle_theme)

        titleLayout.addWidget(self.btn_theme)
        
        title = QtWidgets.QLabel()
        title.setText("Series Renamer APP")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px;font-weight:bold;")
        titleLayout.addWidget(title)
        
        layout.addLayout(titleLayout)

        folder_layout = QtWidgets.QHBoxLayout()

        self.path_input = QtWidgets.QLineEdit()
        self.path_input.setPlaceholderText("Selecciona la carpeta...")
        folder_layout.addWidget(self.path_input)

        browse_btn = QtWidgets.QPushButton("Buscar")
        browse_btn.setIcon(QtGui.QIcon("Icons/File Icons.png"))
        browse_btn.clicked.connect(self.select_folder)
        folder_layout.addWidget(browse_btn)

        layout.addLayout(folder_layout)

        lists = QtWidgets.QHBoxLayout()

        self.file_list = QtWidgets.QListWidget()
        self.preview_list = QtWidgets.QListWidget()

        lists.addWidget(self.file_list)
        lists.addWidget(self.preview_list)

        layout.addLayout(lists)

        btn_layout = QtWidgets.QHBoxLayout()

        scan_btn = QtWidgets.QPushButton("Escanear")
        scan_btn.setIcon(QtGui.QIcon("Icons/Scan Icons.png"))
        scan_btn.clicked.connect(self.scan_folder)
        btn_layout.addWidget(scan_btn)

        rename_btn = QtWidgets.QPushButton("Renombrar")
        rename_btn.setIcon(QtGui.QIcon("Icons/Rename Icons.png"))
        rename_btn.clicked.connect(self.rename_files)
        btn_layout.addWidget(rename_btn)

        layout.addLayout(btn_layout)

        self.result = QtWidgets.QTextEdit()
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

    def select_folder(self):

        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")

        if folder:
            self.path = folder
            self.path_input.setText(folder)

    def scan_folder(self):

        self.file_list.clear()
        self.preview_list.clear()
        self.videos.clear()

        path = self.path_input.text()

        if not os.path.isdir(path):
            self.result.append("Ruta inválida")
            return

        for file in os.listdir(path):

            numero = extraer_numero(file)

            if numero:
                new_name = f"{numero}{os.path.splitext(file)[1]}"
                self.file_list.addItem(file)
                self.preview_list.addItem(new_name)
                self.videos.append(file)

    def rename_files(self):

        for file in self.videos:

            numero = extraer_numero(file)

            if numero:

                ext = os.path.splitext(file)[1]
                new_name = f"{numero}{ext}"

                old = os.path.join(self.path, file)
                new = os.path.join(self.path, new_name)

                try:
                    os.rename(old, new)
                    self.result.append(f"{file} -> {new_name}")
                except Exception as e:
                    self.result.append(str(e))
                    
    # def update_button(self):
    #     if ApplyDarkTheme:
    #         self.btn_theme.
        
            

    def apply_theme(self):
        if self.current_theme == "dark":
            themes.ApplyDarkTheme(self)
            self.btn_theme.setIcon(QtGui.QIcon("Icons/DarkTheme Icon.png"))
            self.btn_theme.setToolTip("Modo oscuro activo")
        else:
            themes.ApplyLightTheme(self)
            self.btn_theme.setIcon(QtGui.QIcon("Icons/LightTheme Icon.png"))
            self.btn_theme.setToolTip("Modo claro activo")

    def toggle_theme(self):
        self.result.clear()
        
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_theme()
        self.result.append(f"Tema actual: {self.current_theme}")

    def choose_theme(self, theme_name: str):
        if theme_name not in ["dark", "light"]:
            raise ValueError("theme_name debe ser 'dark' o 'light'")
        self.current_theme = theme_name
        self.apply_theme()
    
