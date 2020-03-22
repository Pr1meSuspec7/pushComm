# Push Commands

This script helps engineers to execute commands on many devices.


### Requirements

This script tested on Linux/Windows with python3.7 or higher.  
The following packages are required:
 - termcolor
 - napalm
 - tabulate

It's recommended to crate a virtual environment, activate it and then install the packages:

For Windows:

```sh
> git clone https://scm.dimensiondata.com/marco.palmieri/pushcomm.git
> cd pushcomm
> python -m venv VENV-NAME
> VENV-NAME\Scripts\activate.bat
> pip install termcolor tabulate napalm
```

For Linux:

```sh
$ git clone https://scm.dimensiondata.com/marco.palmieri/pushcomm.git
$ cd pushcomm
$ python -m venv VENV-NAME
$ source VENV-NAME/bin/activate
$ pip install termcolor tabulate napalm
```
>NOTE: chose a name for virtual environment and replace the `VENV-NAME` string



### How to use

You have to run the command and follow the interactive menu:

```sh
$ python pushComm.py
```
