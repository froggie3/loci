# thought of handling tasks in shellscript vs async

the concept of handling async tasks in shellscript and Python
is quite the similar. so i thought demonstrating it would help other
understand it, or me explain to someone the concept.

... anyway, it needs Poetry to run the script.
if you have installed already, clone this repo and install it.

```sh
poetry lock && poetry install
```


## Usage

This chapter explain the usage of the programs.

### doing jobs

```sh
./async_do_jobs
poetry run async_do_jobs
```

This demonstrates the way how a shellscript and a Python script
handle two asyncronous tasks.


### handling signals

```sh
./async_signal_handling.sh
poetry run async_signal_handling
```

This demonstrates the way how a shellscript handles signals
and kills asyncronous tasks.
