# Docker-Backend-API
Project for Computer Structure II at Universidad del Norte

# Clone the repository
You can run the repository either in your local machine or in play with docker

- git clone https://github.com/Gerdava2602/Docker-Backend-API.git

# Creating docker images

Inside the folder
 - `docker-compose build`
 - `nohup docker-compose up &`


# Adding sql to database container
Run the following command
- `docker exec -u postgres db psql db postgres -f data/db/tables.sql`
