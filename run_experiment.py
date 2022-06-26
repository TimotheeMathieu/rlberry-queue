from rlberry.manager.multiple_managers import MultipleManagers

import logging
from docopt import docopt
from pathlib import Path
from rlberry.experiment.yaml_utils import parse_experiment_config
from rlberry.manager import AgentManager
from rlberry import check_packages

logger = logging.getLogger(__name__)


def experiment_generator(
    experiment_file,
    n_fit=4,
    max_workers=-1,
    output_dir="results",
    parallelization="process",
    enable_tensorboard=False,
):
    """
    Parse command line arguments and yields AgentManager instances.
    """
    if max_workers == -1:
        max_workers = None
    for (_, agent_manager_kwargs) in parse_experiment_config(
        Path(experiment_file),
        n_fit=n_fit,
        max_workers=max_workers,
        output_base_dir=output_dir,
        parallelization=parallelization,
    ):
        if enable_tensorboard:
            if check_packages.TENSORBOARD_INSTALLED:
                agent_manager_kwargs.update(dict(enable_tensorboard=True))
            else:
                logger.warning(
                    "Option --enable_tensorboard is not available: tensorboard is not installed."
                )
        yield AgentManager(**agent_manager_kwargs)


def run_experiment(
    experiment_file,
    n_fit=4,
    max_workers=-1,
    output_dir="results",
    parallelization="process",
    enable_tensorboard=False,
):
    multimanagers = MultipleManagers(
        parallelization="thread"
    )  # can also be "thread" if needed.

    for agent_manager in experiment_generator(
        experiment_file,
        n_fit=4,
        max_workers=-1,
        output_dir="results",
        parallelization="process",
        enable_tensorboard=False,
    ):
        multimanagers.append(agent_manager)

    multimanagers.run()
    multimanagers.save()

    # Reading the results
    del multimanagers
