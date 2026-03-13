
def apply_dark_theme(widget):
    widget.setStyleSheet("""
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
