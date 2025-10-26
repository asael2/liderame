# 🧠 Liderame - Sistema de Análisis de Patrones Oculares

Sistema avanzado de seguimiento ocular para análisis psicológico en entrevistas, basado en principios de PNL (Programación Neurolingüística) y psicología cognitiva.

## 🎯 Objetivo

Detectar y analizar patrones de movimiento ocular en tiempo real durante entrevistas psicológicas para identificar procesos cognitivos como:

- **Memoria visual** (recordar imágenes)
- **Construcción visual** (inventar/imaginar)
- **Memoria auditiva** (recordar sonidos)
- **Construcción auditiva** (crear sonidos)
- **Diálogo interno** (auto-conversación)
- **Sensaciones kinestésicas** (emociones y sentimientos)

## 🔬 Tecnología

- **MediaPipe Face Mesh + Iris**: Detección facial y seguimiento de iris de alta precisión
- **Flask**: Servidor web backend
- **OpenCV**: Procesamiento de video en tiempo real
- **NumPy**: Cálculos matemáticos y procesamiento de datos

## 📋 Requisitos

- Python 3.12+
- Webcam
- Buena iluminación

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd backend

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 🎮 Uso

### 1. Iniciar el servidor

```bash
python main.py
```

El servidor estará disponible en `http://127.0.0.1:5000`

### 2. Calibrar el sistema

Antes de realizar análisis, es crucial calibrar el sistema:

1. Visita `http://127.0.0.1:5000/gaze/calibrate`
2. Sigue las instrucciones en pantalla
3. Mira cada punto rojo y captura la posición
4. Calcula los umbrales al finalizar

### 3. Iniciar análisis

Visita `http://127.0.0.1:5000/gaze` para comenzar el análisis en tiempo real.

## 📊 Patrones de Acceso Ocular (PNL)

```
        ARRIBA-IZQ              ARRIBA-DER
    [Construcción Visual]    [Memoria Visual]
         (inventar)            (recordar)

LATERAL-IZQ              ●              LATERAL-DER
[Construcción Auditiva]              [Memoria Auditiva]
   (inventar sonidos)               (recordar sonidos)

        ABAJO-IZQ               ABAJO-DER
     [Diálogo Interno]      [Sensaciones Kinestésicas]
        (auto-habla)              (emociones)
```

## 🔧 API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/gaze` | GET | Visualización de análisis |
| `/gaze/stream` | GET | Stream de video MJPEG |
| `/gaze/status` | GET | Estado actual (JSON) |
| `/gaze/calibrate` | GET | Sistema de calibración |
| `/gaze/calibrate/capture` | POST | Capturar punto de calibración |
| `/gaze/calibrate/compute` | POST | Calcular umbrales |
| `/gaze/calibrate/reset` | POST | Reiniciar calibración |

## 📁 Estructura del Proyecto

```
backend/
├── main.py              # Aplicación Flask principal
├── requirements.txt     # Dependencias Python
├── calibration.json     # Datos de calibración (generado)
├── templates/           # Templates HTML
│   ├── index.html
│   ├── gaze.html
│   └── calibrate.html
└── README.md
```

## 🔮 Roadmap

### Fase 1: Base (✅ Completado)
- [x] Seguimiento ocular con MediaPipe
- [x] Sistema de calibración
- [x] Detección de 9 direcciones

### Fase 2: Análisis Psicológico (🚧 En desarrollo)
- [ ] Sistema de sesiones de entrevista
- [ ] Registro temporal de patrones
- [ ] Detector de estados cognitivos
- [ ] Dashboard de análisis en tiempo real

### Fase 3: Reportes y Análisis
- [ ] Exportación de datos (CSV, JSON)
- [ ] Generación de reportes PDF
- [ ] Gráficos y visualizaciones
- [ ] Interpretación automática

### Fase 4: Mejoras Avanzadas
- [ ] Detección de microexpresiones
- [ ] Análisis de frecuencia de parpadeo
- [ ] Machine Learning para patrones
- [ ] Multi-usuario y perfiles

## ⚠️ Disclaimer

Este sistema es una herramienta de **apoyo** para profesionales de la psicología. Los resultados deben ser interpretados por personal calificado y **no sustituyen** el juicio clínico profesional.

## 📄 Licencia

[Especificar licencia]

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores.

## 📧 Contacto

[Información de contacto]

