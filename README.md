# rlberry-queue
some scripts to use rq with rlberry

## Basic usage

launch the job server with

    bash launch_server.sh

Once this is done, you can add an experiment described by yaml files using `add_xp_to_queue.py`

    python add_xp_to_queue.py --n-fit 2 params_experiment.yaml


See the help of `add_xp_to_queue.py` for more info

    python add_xp_to_queue.py --help


## TODO

- [] test rq suspend and rq resume
- [] change data logged to csv -> to json to keep metadata.
- [] Maybe use systemd to handle server stuff