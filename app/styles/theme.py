from PySide6 import QtWidgets

def ApplyDarkTheme(widget: QtWidgets.QWidget):
    widget.setStyleSheet("""
        /* ========== ESTILOS GENERALES ========== */
        QWidget {
            background-color: #1a1b26;
            color: #a9b1d6;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            font-size: 10pt;
        }
        
        QWidget:disabled {
            color: #565f89;
        }
        
        /* ========== VENTANA PRINCIPAL ========== */
        QMainWindow {
            background-color: #1a1b26;
        }
        
        /* ========== MENÚS ========== */
        QMenuBar {
            background-color: #1f2335;
            border-bottom: 2px solid #292e42;
            color: #a9b1d6;
        }
        
        QMenuBar::item:selected {
            background-color: #33467c;
            color: #c0caf5;
        }
        
        QMenuBar::item:pressed {
            background-color: #3b4261;
        }
        
        QMenu {
            background-color: #24283b;
            border: 1px solid #414868;
            border-radius: 6px;
            padding: 4px;
        }
        
        QMenu::item {
            padding: 6px 24px;
            border-radius: 4px;
        }
        
        QMenu::item:selected {
            background-color: #33467c;
            color: #c0caf5;
        }
        
        QMenu::separator {
            height: 1px;
            background-color: #414868;
            margin: 6px 0;
        }
        
        /* ========== BARRA DE ESTADO ========== */
        QStatusBar {
            background-color: #1f2335;
            border-top: 1px solid #292e42;
            color: #9aa5ce;
        }
        
        /* ========== BOTONES ========== */
        QPushButton {
            background-color: #2f3b54;
            border: 2px solid #394b70;
            border-radius: 6px;
            padding: 8px 16px;
            color: #c0caf5;
            font-weight: 500;
            min-width: 80px;
        }
        
        QPushButton:hover {
            background-color: #394b70;
            border-color: #4a6c9e;
        }
        
        QPushButton:pressed {
            background-color: #1f2b41;
            border-color: #2f3b54;
        }
        
        QPushButton:disabled {
            background-color: #292e42;
            border-color: #363b54;
            color: #565f89;
        }
        
        QPushButton:checked {
            background-color: #33467c;
            border-color: #4a6c9e;
        }
        
        /* Botón primario (acciones principales) */
        QPushButton#primaryButton {
            background-color: #3861a2;
            border-color: #4c7ac7;
        }
        
        QPushButton#primaryButton:hover {
            background-color: #4c7ac7;
        }
        
        QPushButton#primaryButton:pressed {
            background-color: #2a4880;
        }
        
        /* ========== CAMPOS DE TEXTO ========== */
        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: #24283b;
            border: 2px solid #363b54;
            border-radius: 6px;
            padding: 6px 10px;
            color: #c0caf5;
            selection-background-color: #33467c;
        }
        
        QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
            border-color: #4a6c9e;
            background-color: #1f2335;
        }
        
        QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled {
            background-color: #292e42;
            color: #565f89;
            border-color: #363b54;
        }
        
        /* ========== LISTAS Y TABLAS ========== */
        QListWidget, QListView, QTreeView, QTableView {
            background-color: #1a1b26;
            alternate-background-color: #1f2335;
            border: 2px solid #292e42;
            border-radius: 6px;
            color: #a9b1d6;
            selection-background-color: #33467c;
            selection-color: #c0caf5;
            outline: none;
        }
        
        QListWidget::item, QListView::item, QTreeView::item, QTableView::item {
            padding: 6px;
            border-bottom: 1px solid transparent;
        }
        
        QListWidget::item:hover, QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {
            background-color: #2d3a5f;
        }
        
        QListWidget::item:selected, QListView::item:selected, QTreeView::item:selected, QTableView::item:selected {
            background-color: #33467c;
            color: #c0caf5;
        }
        
        /* ========== TABLAS ========== */
        QHeaderView::section {
            background-color: #24283b;
            padding: 8px;
            border: 1px solid #363b54;
            color: #c0caf5;
            font-weight: 600;
        }
        
        QTableCornerButton::section {
            background-color: #24283b;
            border: 1px solid #363b54;
        }
        
        /* ========== SCROLLBARS ========== */
        QScrollBar:vertical {
            background: #1f2335;
            width: 14px;
            border-radius: 7px;
            margin: 0px;
        }
        
        QScrollBar::handle:vertical {
            background: #394b70;
            min-height: 30px;
            border-radius: 7px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: #4a6c9e;
        }
        
        QScrollBar::handle:vertical:pressed {
            background: #5a7cae;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }
        
        QScrollBar:horizontal {
            background: #1f2335;
            height: 14px;
            border-radius: 7px;
            margin: 0px;
        }
        
        QScrollBar::handle:horizontal {
            background: #394b70;
            min-width: 30px;
            border-radius: 7px;
        }
        
        QScrollBar::handle:horizontal:hover {
            background: #4a6c9e;
        }
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
        }
        
        /* ========== COMBOBOX ========== */
        QComboBox {
            background-color: #24283b;
            border: 2px solid #363b54;
            border-radius: 6px;
            padding: 6px 10px;
            color: #c0caf5;
            min-width: 150px;
        }
        
        QComboBox:hover, QComboBox:focus {
            border-color: #4a6c9e;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        
        QComboBox::down-arrow {
            image: url(down_arrow.png);  /* Necesitarías crear este icono */
            width: 12px;
            height: 12px;
        }
        
        QComboBox QAbstractItemView {
            background-color: #24283b;
            border: 2px solid #363b54;
            border-radius: 6px;
            color: #c0caf5;
            selection-background-color: #33467c;
            selection-color: #c0caf5;
        }
        
        /* ========== CHECKBOX Y RADIOBUTTON ========== */
        QCheckBox, QRadioButton {
            color: #a9b1d6;
            spacing: 8px;
        }
        
        QCheckBox::indicator, QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }
        
        QCheckBox::indicator:unchecked {
            border: 2px solid #363b54;
            background-color: #24283b;
            border-radius: 4px;
        }
        
        QCheckBox::indicator:checked {
            border: 2px solid #4a6c9e;
            background-color: #33467c;
            border-radius: 4px;
            image: url(checkmark.png);  /* Necesitarías crear este icono */
        }
        
        QCheckBox::indicator:hover {
            border-color: #4a6c9e;
        }
        
        QRadioButton::indicator:unchecked {
            border: 2px solid #363b54;
            background-color: #24283b;
            border-radius: 9px;
        }
        
        QRadioButton::indicator:checked {
            border: 2px solid #4a6c9e;
            background-color: #33467c;
            border-radius: 9px;
            image: url(dot.png);  /* Necesitarías crear este icono */
        }
        
        /* ========== SLIDERS ========== */
        QSlider::groove:horizontal {
            border: 1px solid #363b54;
            height: 8px;
            background: #24283b;
            border-radius: 4px;
        }
        
        QSlider::handle:horizontal {
            background: #394b70;
            border: 2px solid #4a6c9e;
            width: 18px;
            height: 18px;
            margin: -6px 0;
            border-radius: 9px;
        }
        
        QSlider::handle:horizontal:hover {
            background: #4a6c9e;
        }
        
        /* ========== PROGRESS BAR ========== */
        QProgressBar {
            border: 2px solid #363b54;
            border-radius: 6px;
            background-color: #24283b;
            color: #c0caf5;
            text-align: center;
        }
        
        QProgressBar::chunk {
            background-color: #33467c;
            border-radius: 4px;
        }
        
        /* ========== GROUPBOX ========== */
        QGroupBox {
            border: 2px solid #363b54;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 8px;
            color: #c0caf5;
            font-weight: 600;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        
        /* ========== TABLAS CON ALTERNANCIA ========== */
        QTableView::item:alternate {
            background-color: #1f2335;
        }
        
        /* ========== SPINBOX ========== */
        QSpinBox, QDoubleSpinBox {
            background-color: #24283b;
            border: 2px solid #363b54;
            border-radius: 6px;
            padding: 6px;
            color: #c0caf5;
        }
        
        QSpinBox:focus, QDoubleSpinBox:focus {
            border-color: #4a6c9e;
        }
        
        QSpinBox::up-button, QDoubleSpinBox::up-button,
        QSpinBox::down-button, QDoubleSpinBox::down-button {
            border: none;
            background-color: #2f3b54;
            border-radius: 3px;
            width: 16px;
        }
        
        QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
        QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
            background-color: #394b70;
        }
        
        /* ========== SPLITTERS ========== */
        QSplitter::handle {
            background-color: #292e42;
        }
        
        QSplitter::handle:hover {
            background-color: #394b70;
        }
        
        QSplitter::handle:horizontal {
            width: 2px;
        }
        
        QSplitter::handle:vertical {
            height: 2px;
        }
        
        /* ========== TOOLTIPS ========== */
        QToolTip {
            background-color: #24283b;
            border: 2px solid #4a6c9e;
            border-radius: 6px;
            color: #c0caf5;
            padding: 5px;
            font-size: 9pt;
        }
    """)
    # PROXIMAMENTE AGREGARE EL TEMA BLANCO, PERO PRIMERO QUIERO TERMINAR DE PULIR EL TEMA OSCURO 
def ApplyLightTheme(self):
    self.setStyleSheet("""
        /* ========== ESTILOS GENERALES ========== */
        QWidget {
            background-color: #f5f7fa;
            color: #2c3e50;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            font-size: 10pt;
        }
        
        QWidget:disabled {
            color: #95a5a6;
        }
        
        /* ========== VENTANA PRINCIPAL ========== */
        QMainWindow {
            background-color: #f5f7fa;
        }
        
        /* ========== MENÚS ========== */
        QMenuBar {
            background-color: #ffffff;
            border-bottom: 2px solid #e1e8ed;
            color: #2c3e50;
        }
        
        QMenuBar::item:selected {
            background-color: #e3f2fd;
            color: #1976d2;
        }
        
        QMenuBar::item:pressed {
            background-color: #bbdefb;
        }
        
        QMenu {
            background-color: #ffffff;
            border: 1px solid #e1e8ed;
            border-radius: 6px;
            padding: 4px;
        }
        
        QMenu::item {
            padding: 6px 24px;
            border-radius: 4px;
        }
        
        QMenu::item:selected {
            background-color: #e3f2fd;
            color: #1976d2;
        }
        
        QMenu::separator {
            height: 1px;
            background-color: #e1e8ed;
            margin: 6px 0;
        }
        
        /* ========== BARRA DE ESTADO ========== */
        QStatusBar {
            background-color: #ffffff;
            border-top: 1px solid #e1e8ed;
            color: #7f8c8d;
        }
        
        /* ========== BOTONES ========== */
        QPushButton {
            background-color: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            padding: 8px 16px;
            color: #2c3e50;
            font-weight: 500;
            min-width: 80px;
        }
        
        QPushButton:hover {
            background-color: #e3f2fd;
            border-color: #90caf9;
        }
        
        QPushButton:pressed {
            background-color: #bbdefb;
            border-color: #64b5f6;
        }
        
        QPushButton:disabled {
            background-color: #f8f9fa;
            border-color: #e9ecef;
            color: #adb5bd;
        }
        
        QPushButton:checked {
            background-color: #e3f2fd;
            border-color: #1976d2;
        }
        
        /* Botón primario (acciones principales) */
        QPushButton#primaryButton {
            background-color: #1976d2;
            border-color: #1565c0;
            color: #ffffff;
        }
        
        QPushButton#primaryButton:hover {
            background-color: #1565c0;
            border-color: #0d47a1;
        }
        
        QPushButton#primaryButton:pressed {
            background-color: #0d47a1;
            border-color: #0a2e6e;
        }
        
        /* Botón secundario (acciones alternativas) */
        QPushButton#secondaryButton {
            background-color: #6c757d;
            border-color: #5a6268;
            color: #ffffff;
        }
        
        QPushButton#secondaryButton:hover {
            background-color: #5a6268;
            border-color: #545b62;
        }
        
        /* ========== CAMPOS DE TEXTO ========== */
        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            padding: 6px 10px;
            color: #2c3e50;
            selection-background-color: #bbdefb;
        }
        
        QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
            border-color: #1976d2;
            background-color: #ffffff;
        }
        
        QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled {
            background-color: #f8f9fa;
            color: #adb5bd;
            border-color: #dee2e6;
        }
        
        /* ========== LISTAS Y TABLAS ========== */
        QListWidget, QListView, QTreeView, QTableView {
            background-color: #ffffff;
            alternate-background-color: #f8f9fa;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            color: #2c3e50;
            selection-background-color: #e3f2fd;
            selection-color: #1976d2;
            outline: none;
        }
        
        QListWidget::item, QListView::item, QTreeView::item, QTableView::item {
            padding: 6px;
            border-bottom: 1px solid transparent;
        }
        
        QListWidget::item:hover, QListView::item:hover, QTreeView::item:hover, QTableView::item:hover {
            background-color: #f1f8fe;
        }
        
        QListWidget::item:selected, QListView::item:selected, QTreeView::item:selected, QTableView::item:selected {
            background-color: #e3f2fd;
            color: #1976d2;
        }
        
        /* ========== TABLAS ========== */
        QHeaderView::section {
            background-color: #f8f9fa;
            padding: 8px;
            border: 1px solid #dee2e6;
            color: #2c3e50;
            font-weight: 600;
        }
        
        QTableCornerButton::section {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
        }
        
        /* ========== SCROLLBARS ========== */
        QScrollBar:vertical {
            background: #f1f3f4;
            width: 14px;
            border-radius: 7px;
            margin: 0px;
        }
        
        QScrollBar::handle:vertical {
            background: #c1c9d2;
            min-height: 30px;
            border-radius: 7px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: #9aa4af;
        }
        
        QScrollBar::handle:vertical:pressed {
            background: #7f8c8d;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }
        
        QScrollBar:horizontal {
            background: #f1f3f4;
            height: 14px;
            border-radius: 7px;
            margin: 0px;
        }
        
        QScrollBar::handle:horizontal {
            background: #c1c9d2;
            min-width: 30px;
            border-radius: 7px;
        }
        
        QScrollBar::handle:horizontal:hover {
            background: #9aa4af;
        }
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
        }
        
        /* ========== COMBOBOX ========== */
        QComboBox {
            background-color: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            padding: 6px 10px;
            color: #2c3e50;
            min-width: 150px;
        }
        
        QComboBox:hover, QComboBox:focus {
            border-color: #1976d2;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        
        QComboBox::down-arrow {
            image: url(down_arrow_light.png);  /* Icono para tema claro */
            width: 12px;
            height: 12px;
        }
        
        QComboBox QAbstractItemView {
            background-color: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            color: #2c3e50;
            selection-background-color: #e3f2fd;
            selection-color: #1976d2;
        }
        
        /* ========== CHECKBOX Y RADIOBUTTON ========== */
        QCheckBox, QRadioButton {
            color: #2c3e50;
            spacing: 8px;
        }
        
        QCheckBox::indicator, QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }
        
        QCheckBox::indicator:unchecked {
            border: 2px solid #cbd5e0;
            background-color: #ffffff;
            border-radius: 4px;
        }
        
        QCheckBox::indicator:checked {
            border: 2px solid #1976d2;
            background-color: #1976d2;
            border-radius: 4px;
            image: url(checkmark_light.png);  /* Checkmark blanco para fondo azul */
        }
        
        QCheckBox::indicator:hover {
            border-color: #1976d2;
        }
        
        QRadioButton::indicator:unchecked {
            border: 2px solid #cbd5e0;
            background-color: #ffffff;
            border-radius: 9px;
        }
        
        QRadioButton::indicator:checked {
            border: 2px solid #1976d2;
            background-color: #ffffff;
            border-radius: 9px;
            image: url(dot_light.png);  /* Punto azul para radio button */
        }
        
        QRadioButton::indicator:checked:hover {
            background-color: #e3f2fd;
        }
        
        /* ========== SLIDERS ========== */
        QSlider::groove:horizontal {
            border: 1px solid #cbd5e0;
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
        }
        
        QSlider::handle:horizontal {
            background: #ffffff;
            border: 2px solid #1976d2;
            width: 18px;
            height: 18px;
            margin: -6px 0;
            border-radius: 9px;
        }
        
        QSlider::handle:horizontal:hover {
            background: #e3f2fd;
        }
        
        /* ========== PROGRESS BAR ========== */
        QProgressBar {
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            background-color: #f8f9fa;
            color: #2c3e50;
            text-align: center;
        }
        
        QProgressBar::chunk {
            background-color: #1976d2;
            border-radius: 4px;
        }
        
        /* ========== GROUPBOX ========== */
        QGroupBox {
            border: 2px solid #e1e8ed;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 8px;
            color: #2c3e50;
            font-weight: 600;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            background-color: #f5f7fa;
        }
        
        /* ========== TABLAS CON ALTERNANCIA ========== */
        QTableView::item:alternate {
            background-color: #f8f9fa;
        }
        
        /* ========== SPINBOX ========== */
        QSpinBox, QDoubleSpinBox {
            background-color: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            padding: 6px;
            color: #2c3e50;
        }
        
        QSpinBox:focus, QDoubleSpinBox:focus {
            border-color: #1976d2;
        }
        
        QSpinBox::up-button, QDoubleSpinBox::up-button,
        QSpinBox::down-button, QDoubleSpinBox::down-button {
            border: none;
            background-color: #f8f9fa;
            border-radius: 3px;
            width: 16px;
        }
        
        QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
        QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
            background-color: #e3f2fd;
        }
        
        QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed,
        QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed {
            background-color: #bbdefb;
        }
        
        /* ========== SPLITTERS ========== */
        QSplitter::handle {
            background-color: #e1e8ed;
        }
        
        QSplitter::handle:hover {
            background-color: #cbd5e0;
        }
        
        QSplitter::handle:horizontal {
            width: 2px;
        }
        
        QSplitter::handle:vertical {
            height: 2px;
        }
        
        /* ========== TOOLTIPS ========== */
        QToolTip {
            background-color: #2c3e50;
            border: 2px solid #1976d2;
            border-radius: 6px;
            color: #ffffff;
            padding: 5px;
            font-size: 9pt;
        }
        
        /* ========== PESTAÑAS (TABS) ========== */
        QTabWidget::pane {
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            background-color: #ffffff;
        }
        
        QTabBar::tab {
            background-color: #f8f9fa;
            border: 2px solid #e1e8ed;
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 8px 16px;
            margin-right: 2px;
        }
        
        QTabBar::tab:selected {
            backgrou#nd-color: #ffffff;
            border-bottom-color: #ffffff;
        }
        
        QTabBar::tab:hover:!selected {
            background-color: #e3f2fd;
        }
        
        /* ========== CALENDARIO ========== */
        QCalendarWidget QWidget {
            background-color: #ffffff;
            color: #2c3e50;
        }
        
        QCalendarWidget QMenu {
            background-color: #ffffff;
        }
        
        /* ========== DOCK WIDGETS ========== */
        QDockWidget {
            border: 2px solid #e1e8ed;
            border-radius: 6px;
            titlebar-close-icon: url(close_light.png);
            titlebar-normal-icon: url(float_light.png);
        }
        
        QDockWidget::title {
            background-color: #f8f9fa;
            padding: 6px;
            border-bottom: 1px solid #e1e8ed;
        }
    """)
