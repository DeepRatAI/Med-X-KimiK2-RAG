# 🩺 MedeX — AI-Powered Clinical Reasoning Assistant (Educational Prototype)

MedeX es un asistente conversacional clínico impulsado por modelos de lenguaje (LLMs) y técnicas de *Retrieval-Augmented Generation (RAG)*.
Su propósito es **educativo y de investigación**, diseñado para explorar cómo la IA puede asistir en razonamiento clínico, docencia médica y análisis de casos, **sin reemplazar** el juicio profesional humano.

**Demo:** [MedeX en Hugging Face Spaces](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)
**Licencia:** MIT
**Lenguaje:** Python 3.10+

---

## ⚠️ Disclaimer

MedeX es un **prototipo educativo**, no un producto médico certificado.
No debe usarse para diagnóstico, tratamiento ni toma de decisiones clínicas reales.
Las respuestas generadas son simulaciones informativas.
Por favor, **no ingreses datos personales ni información médica identificable (PHI)**.

---

## 🚀 Características

* Arquitectura **RAG** con recuperación contextual antes de la generación.
* Motor **LLM modular**, intercambiable (Kimi, OpenAI, DeepSeek, etc.).
* Flujo **multimodal** experimental: texto e imagen.
* Respuestas con **explicaciones y citas** de contexto.
* Despliegue reproducible con **Docker** y **Hugging Face Spaces**.

---

## 🧱 Estructura del proyecto

MedeX/

* `streamlit_app.py`: interfaz principal
* `MEDEX_FINAL/`: lógica del pipeline y módulos RAG
* `test_deployment.py`: pruebas básicas de despliegue
* `requirements.txt`: dependencias versionadas
* `.streamlit/config.toml`: configuración segura
* `Dockerfile`: build reproducible
* `LICENSE`, `README.md`

---

## 🧰 Instalación local

1. Clona el repositorio:
   `git clone https://github.com/DeepRatAI/Med-X-KimiK2-RAG.git && cd Med-X-KimiK2-RAG`

2. Crea y activa un entorno virtual:
   `python -m venv .venv && source .venv/bin/activate`

3. Instala dependencias:
   `pip install -r requirements.txt`

4. Copia el ejemplo de variables de entorno y agrega tu API key:

   ```
   cp .env.example .env
   KIMI_API_KEY=tu_api_key_aqui
   ```

5. Ejecuta la app localmente:
   `streamlit run streamlit_app.py`

---

## 🐳 Despliegue con Docker

```
docker build -t medex .
docker run -p 7860:7860 -e KIMI_API_KEY=tu_api_key_aqui medex
```

Luego abre [http://localhost:7860](http://localhost:7860) y listo.

---

## ☁️ Demo oficial

Puedes probar MedeX directamente en su Space:
**👉 [huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)**

Las claves y configuraciones se gestionan de forma segura en **Settings → Secrets** del Space.
No existen claves por defecto en el código.

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
`pytest -q`

El archivo `test_deployment.py` verifica la conectividad y funcionamiento básico del pipeline.

---

## 🧩 Roadmap

* Conversión del núcleo a paquete `medex/`.
* Evaluación automática con métricas clínicas.
* Dashboard de trazabilidad anónima.
* Soporte multimodal estable (imagen + texto).
* Integración de CI/CD con GitHub Actions.

---

## 🤝 Contribución

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio.
3. Abre un Pull Request con descripción detallada.
4. No incluyas secretos ni datos médicos en tus ejemplos.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT** (archivo LICENSE incluido).

---

Hugging Face Spaces, 2025. [https://huggingface.co/spaces/DeepRat/Med-X_25.10.8](https://huggingface.co/spaces/DeepRat/Med-X_25.10.8)

---

### 🧠 “AI should assist physicians, not impersonate them.”

