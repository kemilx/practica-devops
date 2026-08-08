# Práctica: ciclo DevOps con Docker

Aplicación web **Hola Mundo** creada con Python y su biblioteca estándar.

## Ejecutar localmente

```powershell
python app.py
```

Abrir <http://localhost:8080>.

## Construir y probar la imagen

```powershell
docker build -t kemildev/hola-mundo-devops:1.0 .
docker run --rm -p 8080:8080 kemildev/hola-mundo-devops:1.0
```

Abrir <http://localhost:8080>. Para detener el contenedor, presionar `Ctrl+C`.

## Publicar en Docker Hub

1. Crear un repositorio público llamado `hola-mundo-devops` en Docker Hub.
2. Iniciar sesión y subir ambas etiquetas:

```powershell
docker login
docker push kemildev/hola-mundo-devops:1.0
docker tag kemildev/hola-mundo-devops:1.0 kemildev/hola-mundo-devops:latest
docker push kemildev/hola-mundo-devops:latest
```

URL para entregar:

```text
https://hub.docker.com/r/kemildev/hola-mundo-devops
```

## CI/CD con GitHub Actions y Render

El workflow [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml) se
ejecuta en cada `push` a `main` y realiza el ciclo completo:

1. Ejecuta las pruebas automáticas.
2. Construye la imagen para `linux/amd64`.
3. Publica las etiquetas `latest` y `sha-<commit>` en Docker Hub.
4. Solicita a Render desplegar exactamente la imagen del commit aprobado.

Secretos requeridos en GitHub Actions:

- `DOCKERHUB_USERNAME`: usuario de Docker Hub (`kemildev`).
- `DOCKERHUB_TOKEN`: token de Docker Hub con permiso de lectura/escritura.
- `RENDER_DEPLOY_HOOK_URL`: URL secreta del Deploy Hook del servicio de Render.

El archivo [`render.yaml`](render.yaml) define el servicio web de producción
que consume la imagen pública de Docker Hub y verifica su endpoint `/health`.
