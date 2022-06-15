# poligran-operational-systems
This repository contains the whole code to be used for operational systems class. The code is divided in two parts:

* **Week 5**: The code for the 5th week of the class NOTE: please check the week5 folder.
* **Week 7**: The code for the 7th week of the class.

> **Disclaimer:** All code is written in **Python3**, and needs [poetry](https://python-poetry.org/) installed.

## How to use the app

### Install the app

```bash
git clone https://github.com/cristian-rincon/poligran-operational-systems
cd poligran-operational-systems
poetry install
```

* **Note**: You can use the `poetry` command to install the dependencies.

## Running the app

This command will shows the help for the app.

```bash
poetry run python main.py --help
```


## Week 5

### Exercise 1 - Multithread application

This is a simple multithread application. it is used to download files from pexels.com.

#### Downloading files

You can pass the image ids to the app, and it will download the images to the current directory.

For example:

```bash
python main.py multithread_program download-photos 8562239 12328375 12250627 12325904
```

Sample output:

```bash
Downloading 4 photos
Downloading progress  [------------------------------------]    0%
Starting thread for photo 8562239
Downloading progress  [#########---------------------------]   25%
Starting thread for photo 12328375
Downloading progress  [##################------------------]   50%
Starting thread for photo 12250627
Downloading progress  [###########################---------]   75%
Starting thread for photo 12325904
Downloading progress  [####################################]  100%
```

Congratulations, you have downloaded 4 photos. :rocket: