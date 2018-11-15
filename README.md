# Docker Flask

## List Docker CLI commands
```
docker
docker container --help
```

## Display Docker version and info
```
docker --version
docker version
docker info
```
## Execute Docker image
```
docker run hello-world
```
## List Docker images
```
docker image ls
```
## List Docker containers (running, all, all in quiet mode)
```
docker container ls
docker container ls --all or docker ps -a
docker container ls -aq
```
## Docker Build
```
docker build <location of docker file>
## Docker Search Image
docker search <name of image> e.g. docker search python
```
## Docker Compose Build
```
docker-compose up --build
```
## Docker Compose Up
```
docker-compose up
```
## Docker compose run service in the background
```
docker-compose up -d
## Docker compose check running services
docker-compose ps
## Docker compose stop service
```
docker-compose stop 
