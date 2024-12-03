FROM --platform=$BUILDPLATFORM python:3.12.0b1-slim-buster AS builder

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF

COPY --from=gloursdocker/docker / /
