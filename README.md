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
Em seguida executei o comando para iniciar o container:
```bash
docker run meu-echo
```
Onde mostrou os seguinte resultado: "Ola docker"

2. Crie um container com Nginx que sirva uma página HTML customizada 
(index.html). Monte um volume local com esse arquivo para que ele 
apareça na raiz do site (/usr/share/nginx/html). Acesse a página via 
http://localhost.