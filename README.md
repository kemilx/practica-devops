# Práctica final DevOps CI/CD

Aplicación web “Hola Mundo” creada con Flask. Cada `push` a `main` ejecuta las pruebas,
publica una imagen en Docker Hub y activa un despliegue en Render.

## Tecnologías

- Python 3.12, Flask y Gunicorn
- Pytest
- Docker
- GitHub Actions
- Docker Hub
- Render

## Ejecutar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -v
python app.py
```

Abre <http://localhost:8080>. El endpoint de salud está en
<http://localhost:8080/health>.

## Ejecutar con Docker

```bash
docker build -t kemildev/hola-mundo-devops:local .
docker run --rm -p 8080:8080 kemildev/hola-mundo-devops:local
```

## Configurar CI/CD

1. Crea un repositorio público en GitHub y sube este proyecto a la rama `main`.
2. Usa el repositorio público `kemildev/hola-mundo-devops` de Docker Hub.
3. En Docker Hub, crea un *access token*.
4. En GitHub ve a **Settings → Secrets and variables → Actions** y agrega:
   - `DOCKERHUB_USERNAME`: tu usuario de Docker Hub.
   - `DOCKERHUB_TOKEN`: el access token de Docker Hub (no uses tu contraseña).
5. En Render selecciona **New → Blueprint**, conecta el repositorio y aplica
   `render.yaml`. El servicio consume la imagen publicada en Docker Hub.
6. En el servicio de Render abre **Settings → Deploy Hook**, copia la URL y
   guárdala en GitHub como el secreto `RENDER_DEPLOY_HOOK_URL`.
7. Haz un nuevo `push` a `main`. El workflow ejecutará test → Docker Hub → Render.

> GitHub Actions envía a Render la etiqueta inmutable del commit aprobado, por lo
> que producción recibe exactamente la imagen que superó las pruebas.

## Enlaces de entrega

- Repositorio público: <https://github.com/kemilx/practica-devops>
- Imagen pública: <https://hub.docker.com/r/kemildev/hola-mundo-devops>
- Aplicación en producción: <https://hola-mundo-devops-y63z.onrender.com>

## Flujo

```text
push a main → instalar dependencias → pytest → build/push Docker → deploy Render
```
