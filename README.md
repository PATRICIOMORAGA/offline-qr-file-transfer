# 🔒 Offline QR File Transfer - Red Team Edition

**Transferencia encubierta de archivos sin red utilizando códigos QR.**
Este proyecto está diseñado para pruebas de penetración, exfiltración de información en sistemas aislados o canales fuera de banda.

---

## 🧰 Características

- Envío de archivos comprimidos usando códigos QR (gzip + base64).
- Receptor en navegador (HTML5) y en consola (Python).
- Barra de progreso y reconstrucción automática del archivo.
- Soporte para repetir fragmentos faltantes.
- No requiere red, Bluetooth ni conexión física.
- Estilo y diseño discretos para entornos Red Team.

---

## 📂 Estructura

```
offline-qr-file-transfer/
├── emisor.html        # Web que fragmenta y transmite el archivo
├── receptor.html      # Receptor web con cámara y reconstrucción
├── receptor.py        # Receptor por consola con cámara (OpenCV)
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Cómo usar

### 🖥 Modo Web (HTML)
#### Emisor
1. Abre `emisor.html` en un navegador moderno (Chrome, Firefox).
2. Selecciona un archivo. Se comprimirá automáticamente.
3. Ajusta el tamaño de fragmento y la velocidad de visualización.
4. Escanea los códigos QR generados con otro dispositivo usando `receptor.html` o `receptor.py`.

#### Receptor Web
1. Abre `receptor.html` en un navegador con cámara (preferentemente desde un PC o laptop).
2. Escanea el QR de calibración seguido de los fragmentos.
3. Al completar todos, podrás descargar el archivo reconstruido.

### 🐍 Modo Consola (Python)
1. Asegúrate de tener Python y dependencias instaladas:
   ```bash
   pip install opencv-python pyzbar
   ```
2. Ejecuta `receptor.py` en el equipo receptor:
   ```bash
   python receptor.py
   ```
3. Apunta la cámara a los QR emitidos por el emisor.

---

## 🛠 Casos de uso

| Caso                    | Descripción |
|-------------------------|-------------|
| 🔐 Exfiltración de datos | Transferir archivos desde entornos sin red de forma discreta |
| 🧪 Laboratorios aislados | Enviar datos entre máquinas sin conexión |
| 💼 Pruebas DLP           | Evaluar políticas de prevención de fuga de información |

---

## 🧪 Ejemplo visual

*Puedes añadir una animación o imagen del sistema funcionando aquí si lo subes a GitHub.*

---

## 📜 Licencia

Este proyecto utiliza la licencia [MIT](LICENSE). Puedes usarlo y modificarlo libremente, dando el crédito correspondiente.

© 2025 - Patricio

---

## 🧠 Ideas para mejoras futuras

- Cifrado AES de los fragmentos
- Validación de checksum por QR
- Recepción desde múltiples cámaras simultáneas
- Codificación de archivos grandes en múltiples sesiones

---

## 🧩 Inspirado por

- Técnicas de covert channel
- Simulación de APTs
- Herramientas como `qrencode`, `ZBar`, `ZXing`, y `pako`

---

## 💬 ¿Preguntas o ideas?

¡Cualquier contribución, issue o sugerencia es bienvenida!
