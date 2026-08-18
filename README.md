# Práctica final DevOps CI/CD

Aplicación web **Hola Mundo** creada con Python y Flask.

El proyecto incluye:

- Pruebas unitarias con Pytest.
- Dockerfile para ejecutar la aplicación.
- GitHub Actions para probar, publicar en Docker Hub y desplegar en Render.

## Ejecutar localmente

```bash
pip install -r requirements-dev.txt
python -m pytest -v
python app.py
```

La aplicación estará disponible en <http://localhost:8080>.

## Ejecutar con Docker

```bash
docker build -t hola-mundo-devops .
docker run --rm -p 8080:8080 hola-mundo-devops
```

## Enlaces

- Repositorio: <https://github.com/kemilx/practica-devops>
- Docker Hub: <https://hub.docker.com/r/kemildev/hola-mundo-devops>
- Aplicación: <https://hola-mundo-devops-y63z.onrender.com>
