FROM node:22 AS build

ARG PROXY_URL
ARG BACKEND_URL
ARG PUBLIC_BACKEND_URL

ENV PROXY_URL=${PROXY_URL}
ENV BACKEND_URL=${BACKEND_URL}
ENV PUBLIC_BACKEND_URL=${PUBLIC_BACKEND_URL}

ENV NODE_ENV=development

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
ENV ORIGIN=${PROXY_URL}
RUN npm run build


FROM node:20-slim

WORKDIR /app
COPY --from=build /app .

ENV HOST=0.0.0.0
EXPOSE 4173
CMD ["npm","run", "preview","--", "--host", "0.0.0.0"]
