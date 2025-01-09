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

Although preferably, you'd use `docker compose` to run it to bootstrap all the
dev infrastructure like databases.
