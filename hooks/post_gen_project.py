import os
import subprocess
import sys


def run(cmd):
  subprocess.run(cmd, shell=True, check=True)


def main():
  run("git init")
  run(f"{sys.executable} -m venv .venv")
  run(".venv/bin/pip install -e .[dev]")
  run("git add . && git commit -m '{{ cookiecutter.project_slug }}: initial commit'"
     )


if __name__ == "__main__":
  main()
