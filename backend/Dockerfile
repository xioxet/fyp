FROM --platform=$BUILDPLATFORM python:3.10-bookworm AS builder

WORKDIR /app
COPY requirements.txt /app

RUN apt-get update && \
    apt-get -y install tesseract-ocr && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 poppler-utils && \
    pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder AS dev-envs

RUN apt-get update && \
    apt-get install -y git

RUN groupadd -r docker && \
    useradd -m -s /bin/bash -g docker vscode

COPY --from=gloursdocker/docker / /
