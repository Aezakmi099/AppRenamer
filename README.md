# 🎬 Series Renamer APP

Aplicación de escritorio para **renombrar automáticamente episodios de series** detectando su número desde el nombre del archivo.

Analiza archivos de video y subtítulos dentro de una carpeta, extrae el número de episodio usando múltiples patrones comunes y los renombra de forma ordenada.

Interfaz gráfica moderna con tema oscuro construida con PySide6.

---

## ✨ Características

* Interfaz gráfica simple e intuitiva
* Tema oscuro moderno
* Detección automática del número de episodio
* Compatible con múltiples formatos de nombres
* Renombrado masivo en un clic
* Ordenación numérica correcta (1, 2, 3, 10…)
* Soporte para videos y subtítulos
* Vista previa antes de renombrar

---

## 📂 Archivos soportados

### Video

* `.mp4`
* `.avi`
* `.mkv`
* `.mov`
* `.wmv`
* `.flv`
* `.webm`
* `.mpg`


### Subtítulos

* `.srt`

---

## 🔍 Patrones detectados automáticamente

El programa reconoce números de episodio en formatos como:

```
Capitulo 12
Cap 12
Episode 5
Ep05
Chapter 3
Ch 7
E01
1x09
c12
NombreSerie 15.mkv
```

Y muchos más.

---

## 🖥 Cómo usar

1. Ejecuta la aplicación
2. Pulsa **Buscar** y selecciona la carpeta
3. Pulsa **Escanear** para ver la vista previa
4. Pulsa **Renombrar**

Los archivos se renombrarán así:

```
Serie.capitulo.12.mkv  →  12.mkv
Episode_03.mp4         →  3.mp4
```

---

## 📦 Instalación

### Requisitos

* Python 3.9 o superior

Instalar dependencias:

```bash
pip install PySide6
```

---

### ▶ Ejecutar desde código fuente

```bash
python main.py
```

---

### 🧊 Usar ejecutable (opcional)

Descargar el ejecutable desde aqui 👇

```bash
https://github.com/Aezakmi099/AppRenamer/releases/tag/v1.0.0
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

## ⚠ Recomendaciones

* Haz copia de seguridad antes de renombrar archivos importantes
* Evita archivos con números no relacionados al episodio
* Verifica la vista previa antes de aplicar cambios

---

## 🧠 Cómo funciona

1. Escanea los nombres de archivo
2. Aplica expresiones regulares para detectar el número
3. Ordena los archivos numéricamente
4. Renombra usando solo el número detectado

---

## 👨‍💻 Autor

Hecho por **Aezakmi**

---

## 📜 Licencia

Uso libre para proyectos personales y educativos.
