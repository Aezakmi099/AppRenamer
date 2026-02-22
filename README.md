# 🎬 Series Renamer APP

Aplicación de escritorio para renombrar automáticamente episodios de
series detectando su número directamente desde el nombre del archivo.

Escanea archivos de video y subtítulos dentro de una carpeta, identifica
el número de episodio usando múltiples patrones comunes y los renombra
de forma ordenada.

Incluye una interfaz gráfica moderna con tema oscuro, construida con
PySide6.

---

## ✨ Características principales

-  Interfaz gráfica simple e intuitiva
-  Tema oscuro moderno
-  Detección automática del número de episodio
-  Compatible con múltiples formatos de nombres
-  Renombrado masivo en un solo clic
-  Ordenación numérica correcta (1, 2, 3, 10…)
-  Soporte para videos y subtítulos
-  Vista previa antes de aplicar cambios

---

## 📂 Archivos soportados

### 🎥 Video
-   .mp4
-   .avi
-   .mkv
-   .mov
-   .wmv
-   .flv
-   .webm
-   .mpg

### 💬 Subtítulos

-   .srt
-   .sub
-   .ass

---

## 🔍 Patrones detectados automáticamente

El programa reconoce números de episodio en formatos como:

```
- Capitulo 12 
- Cap 12 
- Episode 5 
- Ep05 
- Chapter 3 
- Ch 7 E01 
- 1x09 
- c12
- NombreSerie 15.mkv
```

### Y muchas variaciones adicionales.

---

## 🖥 Cómo usar

1.  Ejecuta la aplicación
2.  Pulsa Buscar y selecciona la carpeta
3.  Pulsa Escanear para ver la vista previa
4.  Pulsa Renombrar

### Resultado del renombrado:

- Serie.capitulo.12.mkv → 12.mkv 
- Episode_03.mp4 → 3.mp4

---

## 🧊 Ejecutable 

Descarga directamente desde Releases:

- [Windows](https://github.com/Aezakmi099/AppRenamer/releases/download/v1.0.0/AppRenamer.exe)

- [Linux](https://github.com/Aezakmi099/AppRenamer/releases/download/v1.0.0/AppRenamer)


---

## 📦 Instalación manual (opcional)

Requisitos: Python 3.9 o superior

Instalar dependencias: 
```bash
pip install PySide6
```
Ejecutar desde el código fuente: 
```bash
python main.py
```
---

## 📁 Estructura del proyecto

```
project/
│
├── main.py
├── Icon.ico 
└── README.md
```

---

## ⚠ Recomendaciones importantes

-   Haz copia de seguridad antes de renombrar archivos importantes
-   Evita archivos con números que no correspondan al episodio
-   Revisa siempre la vista previa antes de confirmar cambios

---

## 🧠 Cómo funciona internamente

1.  Escanea los nombres de los archivos
2.  Aplica expresiones regulares para detectar el número de episodio
3.  Ordena los archivos numéricamente
4.  Renombra usando únicamente el número detectado

---

## 👨‍💻 Autor

- Aezakmi

---

## 📜 Licencia

Uso libre para proyectos personales y educativos.