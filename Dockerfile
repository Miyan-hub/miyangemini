FROM node:lts-buster

COPY . .

RUN npm install @google/generative-ai

ENTTRYPOINT [ "node", "index.js" ]