FROM --platform=$BUILDPLATFORM python:3.10-bookworm AS builder

ARG PROXY_URL
ARG FRONTEND_URL
ARG BACKEND_URL
ARG POSTGRES_URL

ENV PROXY_URL ${PROXY_URL}
ENV FRONTEND_URL ${FRONTEND_URL}
ENV BACKEND_URL ${BACKEND_URL}
ENV POSTGRES_URL ${POSTGRES_URL}

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN apt-get update && \
    apt-get install -y git

RUN groupadd -r docker && \
    useradd -m -s /bin/bash -g docker vscode

COPY --from=gloursdocker/docker / /
