# Repository Readme

This document is the repository readme - covering the data, some technical submission guidelines, source code, and execution environments that have already been provided to you. For a more general overview of the challenge, see the [Challenge Description](Challenge.md).

## What's the code that's already in here?

To help all contestants get started quickly with solving the interesting problems in the challenge, some code and structure has been prepared already in this repository.

The data folder contains a simple python file to download and unzip the data. The data folder is excluded from the GitHub repository (see[gitignore](.gitignore)). Please do not change the location of the data.

We provide a short notebook to give you some more information about how to load the data, datastructure and basic visualizations [dataload.ipynb](notebooks/dataload.ipynb).

## Data Files

The data is hosted on a google drive. To download the data, please visit each of the links below in your browser to gain access, then run the notebook [dataload.ipynb](notebooks/dataload.ipynb) to download the files. If you'd prefer, you can download the data directly from the links yourself.

- [https://drive.google.com/file/d/1QC6afqmWSHNpgsoe7j7g4E3YaYoHqeIt/view?usp=sharing](https://drive.google.com/file/d/1QC6afqmWSHNpgsoe7j7g4E3YaYoHqeIt/view?usp=sharing)
- [https://drive.google.com/file/d/1Y_m2Awl9161Rs-7xiXbQKV7NOsDI6DI5/view?usp=sharing](https://drive.google.com/file/d/1Y_m2Awl9161Rs-7xiXbQKV7NOsDI6DI5/view?usp=sharing)
- [https://drive.google.com/file/d/1-mayhsGwpSnSHQYDRUDT2bY9EFSrrpOZ/view?usp=sharing](https://drive.google.com/file/d/1-mayhsGwpSnSHQYDRUDT2bY9EFSrrpOZ/view?usp=sharing)
- [https://drive.google.com/file/d/10USDOONYDPo8BAY46qhQOAPdpwnC1S4D/view?usp=sharing](https://drive.google.com/file/d/10USDOONYDPo8BAY46qhQOAPdpwnC1S4D/view?usp=sharing)


## Environments

All this python code and tooling has dependencies which are encoded in the environment files. We've set up support for [Anaconda](https://anaconda.org/), [Poetry](https://python-poetry.org/), and [Docker](https://www.docker.com/) environments. If you are using another programming language, please provide details on your environment in one of the commonly accepted formats, and a brief description of how to set it up.

To install the anaconda environment, you need to have anaconda installed, then run:

```shell
conda env create --file environments/environment.yml
```

To install the poetry environment, you need to have python 3.10 or higher installed, then run:

```shell
cp environments/pyproject.toml .; poetry install
```

To install the Docker environment, you need to have Docker installed, then run:

```shell
cp environments/docker-compose.yml .
cp environments/Dockerfile .
cp environments/jupyter.sh .
docker-compose build
```

The Docker container is setup to run a juypter lab server on start. You can start it with `docker-compose up`.

After you picked and setup an environment in your repository, please delete the other environment files so the judges know which one you used when judging the submissions.

## Notebooks

If you're using notebooks in your ML pipeline, please make sure they can be executed in the order the cells are present. This ensures that the notebook can be executed from the command line like so:

```shell
jupyter nbconvert --execute <notebook>
```

## Using Other Languages

We encourage competitors to use another open-source programming language to build their ML pipelines. We did not have time to setup the EIS utility library and environments in those languages! Sorry! Doing so will help the judges assess your submission.
