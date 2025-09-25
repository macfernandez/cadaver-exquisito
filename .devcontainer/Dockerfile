ARG UI_IMAGE=cadaver-exquisito/ui:latest
FROM ${UI_IMAGE} AS ui_image

ARG SERVER_IMAGE=cadaver-exquisito/server:latest
FROM ${SERVER_IMAGE} AS server_image

FROM server_image

ARG USER_NAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        htop \
        iproute2 \
        less \
        locales \
        make \
        openssh-client \
        sudo \
        vim \
    && locale-gen en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${USER_GID} ${USER_NAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USER_NAME} \
    && echo "${USER_NAME} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PATH="/opt/venv/bin:${PATH}"

COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Ensure UI tooling is also available when developing the server
RUN pip install --no-cache-dir streamlit

COPY --from=ui_image /workspace/ui /opt/templates/ui

WORKDIR /workspace

RUN chown -R ${USER_NAME}:${USER_GID} /workspace

USER ${USER_NAME}

CMD ["/bin/bash"]
