## 1. Crie um arquivo Dockerfile que utilize a imagem alpine como base imprima a mensagem Olá, Docker! ao ser executada. Construa a imagem com o nome meu-echo e execute um container a partir dela. 
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

R: Primeiro criaremos uma pasta local no sistema e botaremos o index.html dentro dela

```bash
mkdir site-nginx
cd nginx-site
```
-agora criaremos o arquivo idex.html:

```html
<!-- nginx-site/index.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Minha Página Nginx</title>
</head>
<body>
    <h1>Olá, mundo! Esta é minha página servida pelo Nginx no Docker.</h1>
</body>
</html>
```
-Com o arquivo index.html criado rodamos o container com volume,utilizando o seguinte comando docker para rodar o conteiner:

```bash
docker run --name meu-nginx 
  -v $(pwd)/index.html:/usr/share/nginx/html/index.html:ro 
  -p 80:80 
  -d nginx
```

em seguida abra o navegador e acesse:http://localhost

3. Inicie um container da imagem ubuntu com um terminal interativo (bash). 
Navegue pelo sistema de arquivos e instale o pacote curl utilizando apt. 

-Primeiramente iniciaremos o container Ubuntu com terminal interativo

 executaremos este comando:
 ```bash
   docker run -it ubuntu bash
 ```
-Dentro do nosso container ubuntu utilize os seguintes comandos para navegar por ele:

```bash
ls /
cd /etc
ls
cd ..
cd home
```
-Atualize os repositórios e instale o curl

Dentro do container,instale o curl com:

```bash
apt update
apt install curl -y
```
-Para testar se o curl esta funcionando digite o seguinte comando:

```bash
curl https://qualquersite.com
```

4. Suba um container do MySQL (pode usar a imagem mysql:5.7), utilizando 
um volume nomeado para armazenar os dados. Crie um banco de dados, 
pare o container, suba novamente e verifique se os dados persistem.