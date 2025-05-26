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

## 2. Crie um container com Nginx que sirva uma página HTML customizada (index.html). Monte um volume local com esse arquivo para que ele apareça na raiz do site (/usr/share/nginx/html). Acesse a página via http:://localhost 

R: Primeiro criaremos uma pasta local no sistema e botaremos o index.html dentro dela

```bash
mkdir site-nginx
cd site-nginx
```
-agora criaremos o arquivo idex.html:

```html
<!-- site-nginx/index.html -->
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

## 3. Inicie um container da imagem ubuntu com um terminal interativo (bash).Navegue pelo sistema de arquivos e instale o pacote curl utilizando apt.   

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

## 4. Suba um container do MySQL (pode usar a imagem mysql:5.7), utilizando um volume nomeado para armazenar os dados. Crie um banco de dados,pare o container,suba novamente e verifique se os dados persistem.
   
-primeiramente criaremos um docker-compose com um volume para armazenar os dados do mysql:
```yml
services:
  mysql:
    image: mysql:5.7
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: teste123
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```
-Acessaremos o mysql com o seguinte comando:
```bash
docker exec -it seu-id mysql -u root -p  
```
-Coloque sua senha que foi criada no docker-compose 
 .criaremos um banco de dados com o seguinte comando:
 ```SQL
 CREATE DATABASE lituania;
 ```
 -Para mostrar os dados digite o comando a seguir:

```SQL 
SHOW DATABASES;
```
-Sairemos do container com o comando exit e o pararemos.

-Em seguida subiremos o container para verificar a permanência dos dados:

```bash
docker compose up -d
```
-Agora repitiremos o comando dentro do mySQL para mostrar o banco de dados criado anteriormente

![Texto Alternativo](https://cdn.discordapp.com/attachments/890293548870680617/1376680834702114836/image.png?ex=68363570&is=6834e3f0&hm=bc8e1c9b1542e97ef9d56e45d4c1cf6a91f8f2cb492ec7e1e46140256dffa801&)

## 5. Crie um container com a imagem alpine passando uma variável de ambiente chamada MEU_NOME com seu nome. Execute o container e imprima o valor da variável com o comando echo. 

-Criaremos um Dockerfile:
```dockerfile
FROM alpine
ENV MEU_NOME=Rafael
CMD echo "Ola $MEU_NOME"
```

-Construiremos o container com o seguinte comando:
```bash
docker build -t Sua_tag .
```

-Executaremos o comando onde ele retornará a variavel MEU_NOME:

![Texto Alternativo](https://cdn.discordapp.com/attachments/890293548870680617/1376684477597749349/image.png?ex=683638d5&is=6834e755&hm=c48202c2054b507b834583b2f8125d9f515d153c1564861ab0adeb1287b29587&)