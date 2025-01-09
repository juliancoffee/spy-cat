# what & why
Test assesment for some company which probably wouldn't be happy if I share
their details, but they said to put it on Github, so I guess they are happy
with the code being here at least.

# notes on validation
There are a couple of places where I let Python do its thing so sometimes the
result of a request is statuscode 500 of ServerError.

I guess I could do better, at the very least to provide better error messages.
But I *think* there are no places where the data gets corrupted, that's a
win ^^'

# endpoints
yeaaah, sorry

I couldn't figure out how to do that, I don't have experience with Postman,
so that's probably the first thing to learn

Additionally, I was surprised that there's no automatic generation for API for
Django without DRF, so learning DRF might be the second thing ^^'

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

# status
I left a link to the repository frozen in time, but I might update some things
after the fact, maybe
