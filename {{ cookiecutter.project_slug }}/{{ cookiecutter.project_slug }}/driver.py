import logging
import time

import humanize
import hydra
from omegaconf import OmegaConf
from {{cookiecutter.project_slug}}.config import Config


@hydra.main(version_base=None, config_name='config', config_path='../conf')
def main(cfg: Config) -> None:
  t0 = time.time()
  logging.info("\n%s", OmegaConf.to_yaml(cfg))
  logging.info(
      'Driver complete. Took %s',
      humanize.naturaldelta(time.time() - t0, minimum_unit='microseconds'),
  )


if __name__ == "__main__":
  main()
