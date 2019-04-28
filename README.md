# LOG Analysis with ELK

## Requirements 
- Docker
- Docker Compose
- Git

## How to run
- git clone git@github.com:raheelkhan/elk.git
- cd elk
- $ docker-compose up --build

## Run Test Data
- docker exec -it frontend bash && cd /usr/share/nginx/html && chmod +x seed.sh && ./seed.sh
- docker exec -it orders bash && cd orders && python orders.py

