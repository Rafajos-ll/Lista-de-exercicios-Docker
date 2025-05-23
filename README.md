1. Crie um arquivo Dockerfile que utilize a imagem alpine como base e 
imprima a mensagem Olá, Docker! ao ser executada. Construa a imagem 
com o nome meu-echo e execute um container a partir dela.

R: 
```Dockerfile 
FROM alpine 
CMD echo "Ola docker"
```
Construi a imagem com o seguinte comando:
```bash
docker build -t meu-echo .
```
