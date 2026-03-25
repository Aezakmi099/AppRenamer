from PySide6 import QtWidgets, QtCore, QtGui
from app.styles.theme import ApplyDarkTheme, ApplyLightTheme


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Series Renamer APP")
        self.resize(900, 600)

        self.path = ""
        self.videos = []
        self.result = []

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
        # browse_btn.clicked.connect(self.select_folder)
        folder_layout.addWidget(browse_btn)

        layout.addLayout(folder_layout)

        lists = QtWidgets.QHBoxLayout()

        self.file_list = QtWidgets.QListWidget()
        self.preview_list = QtWidgets.QListWidget()

        lists.addWidget(self.file_list)
        lists.addWidget(self.preview_list)

        layout.addLayout(lists)

        layout_path = QtWidgets.QHBoxLayout()
        inputName = QtWidgets.QLineEdit()
        inputName.setPlaceholderText("Que desea eliminar del nombre??")
        layout_path.addWidget(inputName)
        layout.addLayout(layout_path)

        btn_layout = QtWidgets.QHBoxLayout()

        scan_btn = QtWidgets.QPushButton("Escanear")
        scan_btn.setIcon(QtGui.QIcon("Icons/Scan Icons.png"))
        # scan_btn.clicked.connect(self.scan_folder)
        btn_layout.addWidget(scan_btn)

        rename_btn = QtWidgets.QPushButton("Renombrar")
        rename_btn.setIcon(QtGui.QIcon("Icons/Rename Icons.png"))
        # rename_btn.clicked.connect(self.rename_files)
        btn_layout.addWidget(rename_btn)

        layout.addLayout(btn_layout)

        self.result = QtWidgets.QTextEdit()
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

        autor = QtWidgets.QLabel()
        autor.setText("Hecho por Aezakmi")
        autor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        autor.setStyleSheet("font-size:10px;font-weight:bold;")
        layout.addWidget(autor)

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
