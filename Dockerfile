FROM node:lts-buster

COPY . .

RUN npm install requests flask @google/generative-ai

ENTTRYPOINT [ "node", "app.js" ]