# what & why
Test assesment for some company which probably wouldn't be happy if I share
their details, but they said to put it on Github, so I guess they are happy
with the code being here at least.

# how to run
So, this app is build with `uv`, but I think it should be pretty easy to get it
working with vanilla python tools like `pip`.

requirements.txt can be generated with the following command, and maybe I even
won't forget to include them in the repository.
``` bash
$ uv pip compile pyproject.toml > requirements.txt

```
Oh, and don't forget required environment variables.
- DB_PASSWORD=dev
- DB_HOST=localhost
- SECRET_KEY=whatever

Anyway, you'd need to set up database first, use docker-compose for that.
```
$ ./dev-docker.sh
```
After that run the server as a regular Django app.
```bash
# assuming you've activated the environment and installed the dependencies
$ python manage.py migrate
$ python manage.py runserver
```
