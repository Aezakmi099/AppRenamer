from PySide6 import QtWidgets, QtCore, QtGui
from app.core import renamer
from app.styles.theme import ApplyDarkTheme, ApplyLightTheme


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Series Renamer APP")
        self.resize(900, 600)

        self.videos = []
        self.current_theme = "dark"

        self.renamer = renamer.process(self)

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        # 🔹 HEADER
        titleLayout = QtWidgets.QHBoxLayout()

        self.btn_theme = QtWidgets.QPushButton()
        self.btn_theme.setStyleSheet("""
            min-width: 10px;
            min-height: 15px;
            max-width: 10px;
            max-height: 15px;
        """)
        self.btn_theme.setIcon(QtGui.QIcon("Icons/DarkTheme Icon.png"))
        self.btn_theme.clicked.connect(self.toggle_theme)

        titleLayout.addWidget(self.btn_theme)

        title = QtWidgets.QLabel("Series Renamer APP")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px;font-weight:bold;")

        titleLayout.addWidget(title)
        layout.addLayout(titleLayout)

        # 🔹 PATH
        folder_layout = QtWidgets.QHBoxLayout()

        self.path_input = QtWidgets.QLineEdit()
        self.path_input.setPlaceholderText("Selecciona la carpeta...")
        folder_layout.addWidget(self.path_input)

        browse_btn = QtWidgets.QPushButton("Buscar")
        browse_btn.setIcon(QtGui.QIcon("Icons/File Icons.png"))
        browse_btn.clicked.connect(self.select_folder)
        folder_layout.addWidget(browse_btn)

        layout.addLayout(folder_layout)

        # 🔹 LISTAS
        lists = QtWidgets.QHBoxLayout()

        self.file_list = QtWidgets.QListWidget()
        self.preview_list = QtWidgets.QListWidget()

        lists.addWidget(self.file_list)
        lists.addWidget(self.preview_list)

        layout.addLayout(lists)

        # 🔹 INPUT TEXTO
        layout_path = QtWidgets.QHBoxLayout()

        self.inputName = QtWidgets.QLineEdit()
        self.inputName.setPlaceholderText("Que desea eliminar del nombre??")

        layout_path.addWidget(self.inputName)
        layout.addLayout(layout_path)

        # 🔹 BOTONES
        btn_layout = QtWidgets.QHBoxLayout()

        scan_btn = QtWidgets.QPushButton("Escanear")
        scan_btn.setIcon(QtGui.QIcon("Icons/Scan Icons.png"))
        scan_btn.clicked.connect(self.handle_scan)

        rename_btn = QtWidgets.QPushButton("Renombrar")
        rename_btn.setIcon(QtGui.QIcon("Icons/Rename Icons.png"))
        rename_btn.clicked.connect(self.handle_rename)

        btn_layout.addWidget(scan_btn)
        btn_layout.addWidget(rename_btn)

        layout.addLayout(btn_layout)

        # 🔹 RESULTADO
        self.result = QtWidgets.QTextEdit()
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

        # 🔹 FOOTER
        autor = QtWidgets.QLabel("Hecho por Aezakmi099")
        autor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        autor.setStyleSheet("font-size:10px;font-weight:bold;")

        layout.addWidget(autor)

    # 🔹 LOGICA
    def select_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")
        if folder:
            self.path_input.setText(folder)

    def handle_scan(self):
        resultado = self.renamer.scanFolder()
        self.result.setText(resultado)

    def handle_rename(self):
        resultado = self.renamer.renameFiles()
        self.result.setText(resultado)

    # 🔹 TEMAS
    def apply_theme(self):
        if self.current_theme == "dark":
            ApplyDarkTheme(self)
            self.btn_theme.setIcon(QtGui.QIcon("Icons/DarkTheme Icon.png"))
        else:
            ApplyLightTheme(self)
            self.btn_theme.setIcon(QtGui.QIcon("Icons/LightTheme Icon.png"))

    def toggle_theme(self):
        self.result.clear()
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_theme()

    def choose_theme(self, theme_name: str):
        if theme_name not in ["dark", "light"]:
            raise ValueError("theme_name debe ser 'dark' o 'light'")
        self.current_theme = theme_name
        self.apply_theme()
