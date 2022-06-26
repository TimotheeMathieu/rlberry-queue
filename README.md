# rlberry-queue
some scripts to use rq with rlberry. This works only on linux OS's.

## Installation

The server use redis, that can be installed on ubuntu using

    sudo apt-get install redis

The other dependency is rq which can be installed via pip

    pip install rq

## Basic usage

launch the job server with

    bash launch_server.sh

Once this is done, you can add an experiment described by yaml files using `add_xp_to_queue.py`

    python add_xp_to_queue.py --n-fit 2 experiments_description/params_experiment.yaml


See the help of `add_xp_to_queue.py` for more info

    python add_xp_to_queue.py --help

Using `python add_xp_to_queue.py`, several experiments can be queued. `rq` commands can then be used to monitor the jobs.

      rq info

`rq` can also be used to suspend and resume the jobs with `rq suspend` and `rq resume`. See `rq`'s help.


## TODO

- [ ] test rq suspend and rq resume
- [ ] change data logged to csv -> to json to keep metadata.
- [ ] Maybe use systemd to handle server stuff
- [ ] Add template YAML files for most common env and agents