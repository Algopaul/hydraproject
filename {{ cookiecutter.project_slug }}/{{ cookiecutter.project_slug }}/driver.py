import logging
import time

import humanize
import hydra
from {{cookiecutter.project_slug}}.config import Config
from {{cookiecutter.project_slug}}.util import log_duration


@hydra.main(version_base=None, config_name='config', config_path='../conf')
@log_duration
def main(cfg: Config) -> None:
  pass


if __name__ == "__main__":
  main()
