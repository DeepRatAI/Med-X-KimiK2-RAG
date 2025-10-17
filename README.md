# 🩺 MedeX — AI-Powered Clinical Reasoning Assistant
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![HuggingFace Space](https://img.shields.io/badge/🧠_Demo-HuggingFace-yellow)](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)
[![Python](https://img.shields.io/badge/python-3.10+-green)]()


**MedeX** es un asistente conversacional clínico impulsado por modelos de lenguaje (LLMs) y técnicas de *Retrieval-Augmented Generation (RAG)*.
Su propósito es educativo y de investigación, diseñado para explorar cómo la IA puede asistir en razonamiento clínico, docencia médica y análisis de casos, **sin reemplazar el juicio profesional humano**.

**Demo:** [MedeX en Hugging Face Spaces](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)
**Licencia:** MIT
**Lenguaje:** Python ≥ 3.10

---

- [🧭 Roadmap de Desarrollo](docs/ROADMAP.md)

---

## ⚠️ Disclaimer

MedeX es un **prototipo educativo**, no un producto médico certificado.
No debe usarse para diagnóstico, tratamiento ni toma de decisiones clínicas reales.
Las respuestas generadas son simulaciones informativas.
Por favor, **no ingreses datos personales ni información médica identificable (PHI)**.

---

## 🚀 Características

* 🧠 Arquitectura RAG con recuperación contextual antes de la generación.
* 🔄 Motor LLM modular, intercambiable (Kimi, OpenAI, DeepSeek, etc.).
* 🧬 Flujo multimodal experimental: texto e imagen.
* 💬 Respuestas con explicaciones y citas de contexto.
* 🐳 Despliegue reproducible con Docker y Hugging Face Spaces.


---

## 🧰 Instalación local

### Estado del repositorio

* **`main`** → Rama **legacy**, mantiene el código original y el Space funcionando.
* **`feature/package-v0.1.0`** → Rama **empaquetada**, con CLI profesional, tests y mock mode.
* **Último release:** [v0.1.0](https://github.com/DeepRatAI/Med-X-KimiK2-RAG/releases/tag/v0.1.0)

### Clonar el repositorio

```bash
git clone https://github.com/DeepRatAI/Med-X-KimiK2-RAG.git
cd Med-X-KimiK2-RAG
```

### Ejecutar la app original (legacy)

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edita la API key:
# KIMI_API_KEY=tu_api_key_aqui
streamlit run streamlit_app.py
```

### Probar la versión empaquetada (sin tocar `main`)

Opción 1 — Instalar directamente desde el **release**:

```bash
pip install "git+https://github.com/DeepRatAI/Med-X-KimiK2-RAG@v0.1.0#egg=medex"
```

Opción 2 — Cambiar a la rama empaquetada y ejecutarla localmente:

```bash
git checkout feature/package-v0.1.0
pip install -e .
medex --mode educational --query "¿Qué es la diabetes?"
```

---

## 🐳 Despliegue con Docker

```bash
docker build -t medex .
docker run -p 7860:7860 -e KIMI_API_KEY=tu_api_key_aqui medex
```

Luego abre [http://localhost:7860](http://localhost:7860) y listo.

---

## ☁️ Demo oficial

Puedes probar MedeX directamente en su Space:
👉 [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)


## ☁️ Demo oficial

Puedes probar MedeX directamente en su Space:
👉 [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)

> Las claves y configuraciones se gestionan de forma segura en **Settings → Secrets** del Space.
> No existen claves por defecto en el código.

---

## 🔒 Seguridad

* Claves de API cargadas solo desde variables de entorno (`KIMI_API_KEY`).
* `.streamlit/config.toml` mantiene CORS y XSRF habilitados.
* `.gitignore` protege archivos sensibles (`.env`, `api_key.txt`, `__pycache__`).
* No se almacenan conversaciones ni datos médicos.
* Auditorías básicas con `pip-audit` y pruebas de humo (`test_deployment.py`).
* Modo educativo activado por defecto; el modo profesional requiere confirmación explícita.

---

## 🧪 Pruebas

Para ejecutar las pruebas:

```bash
pytest -q
```

El archivo `test_deployment.py` verifica la conectividad y funcionamiento básico del pipeline.

---

## 🤝 Contribución

1. Haz un **fork** del repositorio.
2. Crea una rama para tu cambio.
3. Abre un **Pull Request** con descripción detallada.
4. No incluyas secretos ni datos médicos en tus ejemplos.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT** (archivo `LICENSE` incluido).

---

## 📬 Contacto

**Autor:** [DeepRatAI](https://github.com/DeepRatAI)
**Correo:** [info@deeprat.tech](mailto:info@deeprat.tech)
**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/gonzalo-romero-b9b5b4355/)

---

## 🌐 Cita

> DeepRatAI. *MedeX: AI-powered Clinical Reasoning Assistant.*
> Hugging Face Spaces, 2025. [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)

---

## 🧠 "AI should assist physicians, not impersonate them."

* Claves de API cargadas solo desde variables de entorno (`KIMI_API_KEY`).
* `.streamlit/config.toml` mantiene CORS y XSRF habilitados.
* `.gitignore` protege archivos sensibles (`.env`, `api_key.txt`, `__pycache__`).
* No se almacenan conversaciones ni datos médicos.
* Auditorías básicas con `pip-audit` y pruebas de humo (`test_deployment.py`).
* Modo educativo activado por defecto; el modo profesional requiere confirmación explícita.

---

## 🧪 Pruebas

Para ejecutar las pruebas:

```bash
pytest -q
```

El archivo `test_deployment.py` verifica la conectividad y funcionamiento básico del pipeline.

---

## 🤝 Contribución

1. Haz un **fork** del repositorio.
2. Crea una rama para tu cambio.
3. Abre un **Pull Request** con descripción detallada.
4. No incluyas secretos ni datos médicos en tus ejemplos.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT** (archivo `LICENSE` incluido).

---

<<<<<<< HEAD
## 📬 Contacto

**Autor:** [DeepRatAI](https://github.com/DeepRatAI)
**Correo:** [info@deeprat.tech](mailto:info@deeprat.tech)
**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/gonzalo-romero-b9b5b4355/)

---

## 🌐 Cita

> DeepRatAI. *MedeX: AI-powered Clinical Reasoning Assistant.*
> Hugging Face Spaces, 2025. [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)
=======
Hugging Face Spaces, 2025. [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)
>>>>>>> origin/feature/package-v0.1.0

---

## 🧠 “AI should assist physicians, not impersonate them.”
