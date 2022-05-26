# Docker-Backend-API
Project for Computer Structure II at Universidad del Norte

Made by:
- [Raúl López Grau](https://github.com/galoryzen)
- [Isaac Blanco Amador](https://github.com/AlejandroBlanco2001)
- [Germán Vargas Ramos](https://github.com/Gerdava2602)

# Setup
You can run the repository either in your local machine or in play with docker
```sh
$ git clone https://github.com/galoryzen/Docker-Backend-API.git
$ cd Docker-Backend-API
$ docker-compose up -d
```

# Testing

1. `curl http://localhost:5000/` test if the conection with the database is succesfull.
2. `curl http://localhost:5000/user/<id>` gives a hash from the timestamp and the ID.
3. `curl http://localhost:5000/user/<id>/<hash>` marks attendance of a student, if the hash is valid and is within 4 hours of hash generation.
4. `curl http://localhost:5000/a` returns a JSON of attendance of all classes.
5. `curl http://localhost:5000/s` returns a JSON of all generated hashes for attendance.
6. `curl http://localhost:5000/delete` deletes the content of both tables.
