# Push Commands

This script helps engineers to execute commands on many devices.


### Requirements

This script tested on Linux/Windows with python3.7 or higher.  
The following packages are required:
 - napalm
 - termcolor
 - tabulate
 - simple_term_menu

It's recommended to crate a virtual environment, activate it and then install the packages:


Works only on Linux:

```sh
$ git clone https://github.com/Pr1meSuspec7/pushComm.git
$ cd pushcomm
$ python -m venv VENV-NAME
$ source VENV-NAME/bin/activate
$ pip install -r requirements.txt
```
>NOTE: chose a name for virtual environment and replace the `VENV-NAME` string



### How to use

You have to run the command and follow the interactive menu:

```sh
$ python pushcomm.py
```

This is a sample execution:
[![asciicast](https://asciinema.org/a/SgniCUMHCWK88WKy9qAWd1Mp7.svg)](https://asciinema.org/a/SgniCUMHCWK88WKy9qAWd1Mp7)
