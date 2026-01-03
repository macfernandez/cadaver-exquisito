ARG IMAGE
FROM ${IMAGE}

COPY ./src/server /root/server

RUN --mount=type=cache,target=/root/.cache \
    pip install --default-timeout=100 /root/server

WORKDIR /root

EXPOSE ${PORT}

# TODO: change to ${PORT}
CMD ["fastapi", "run", "/root/server/server/main.py", "--port", "8000"]