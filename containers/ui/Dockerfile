ARG BASE_IMAGE=cadaver-exquisito/base:latest
FROM ${BASE_IMAGE}

ENV STREAMLIT_SERVER_PORT=8501

WORKDIR /workspace/ui

COPY src/ui/ ./src

RUN pip install --no-cache-dir streamlit

EXPOSE 8501

CMD ["streamlit", "hello"]
