# Parar todos os contêineres
docker stop $(docker ps -aq)

# Remover todos os contêineres
docker rm $(docker ps -aq)

docker rmi $(docker images -q)

docker rmi -f $(docker images -q)

# Remover todos os volumes não utilizados
docker volume prune -f

# Remover todos os volumes, incluindo os usados
docker volume rm $(docker volume ls -q)

# Remover todas as redes não utilizadas
docker network prune -f

# Remover todas as redes, incluindo as usadas
docker network rm $(docker network ls -q)

docker system prune -a -f --volumes
