import logging

import hydra
from omegaconf import OmegaConf
from {{cookiecutter.project_slug}}.config import Config


@hydra.main(version_base=None, config_name='config', config_path='../conf')
def main(cfg: Config) -> None:
  logging.info("\n%s", OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
  main()
