ARG IMAGE
FROM ${IMAGE}

COPY ./src/ui /root/ui

RUN --mount=type=cache,target=/root/.cache \
    pip install --default-timeout=100 /root/ui

WORKDIR /root

EXPOSE ${PORT}

CMD ["streamlit", "run", "/root/ui/ui/Home.py"]