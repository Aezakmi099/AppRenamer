# Series Renamer APP

Series Renamer APP es una aplicación de escritorio desarrollada en Python con PySide6, diseñada para renombrar archivos de series y sus subtítulos de manera rápida y automática, eliminando textos específicos de los nombres y manteniendo un orden natural.

---

## 🔹 Características

* Escanea carpetas y detecta automáticamente:

  * Videos: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`
  * Subtítulos: `.srt`, `.vtt`, `.ass`, `.ssa`, `.scc`, `.sub`, `.xml`
* Muestra la lista de archivos originales y una vista previa de los nuevos nombres.
* Permite eliminar texto específico de los nombres de archivos.
* Orden natural de archivos (`1, 2, 3…` en lugar de `1, 10, 11…`).
* Cambia automáticamente el nombre de los archivos y subtítulos relacionados.
* Interfaz con temas claros y oscuros.
* Instaladores disponibles para Windows y Linux en los releases del repositorio.

---

## 🔹 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/SeriesRenamerAPP.git
cd SeriesRenamerAPP
```

2. Instala las dependencias:

```bash
pip install PySide6 natsort
```

3. Ejecuta la aplicación:

```bash
python main_window.py
```

> O descarga el instalador adecuado desde los [releases](https://github.com/TU_USUARIO/SeriesRenamerAPP/releases) para tu sistema operativo.

---

## 🔹 Uso

1. Selecciona la carpeta donde se encuentran tus archivos de series y subtítulos.
2. Ingresa el texto que deseas eliminar de los nombres.
3. Presiona **Escanear** para ver los archivos y la vista previa de los nuevos nombres.
4. Presiona **Renombrar** para aplicar los cambios.
5. Cambia el tema si lo deseas usando el botón superior.

---

## 🔹 Estructura del proyecto

```
SeriesRenamerAPP/
├── Icons 
│   ├── DarkTheme Icon.png
│   ├── File Icons.png
│   ├── Icon.ico
│   ├── Icon.png
│   ├── LightTheme Icon.png
│   ├── Not.png
│   ├── Rename Icons.png
│   ├── Scan Icons.png
│   ├── Warning.png
│   └── Yes.png
├── LICENSE   
├── README.md
├── app
│   ├── core  
│   ├── styles
│   └── ui
├── main.py
└── requirements.txt
```

---

## 🔹 Contribución

Si quieres contribuir:

1. Haz un fork del proyecto.
2. Crea una rama para tu feature: `git checkout -b feature/nombre-del-feature`
3. Haz commit de tus cambios: `git commit -m "Descripción"`
4. Sube tu rama al repositorio: `git push origin feature/nombre-del-feature`
5. Abre un pull request.

---

## 🔹 Autor

**Aezakmi099**

---

## 🔹 Licencia

Este proyecto está bajo la licencia MIT.
