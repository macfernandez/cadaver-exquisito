ARG BASE_IMAGE=cadaver-exquisito/base:latest
FROM ${BASE_IMAGE}

ENV APP_HOME=/workspace/server \
    APP_PORT=8000

WORKDIR ${APP_HOME}

RUN pip install --no-cache-dir fastapi "uvicorn[standard]"

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000"]
