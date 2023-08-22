<p align="left">
    <a href="https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz" alt="3.9.5">
        <img src="https://img.shields.io/badge/Python%20Version-3.9.5+-blue"/></a>
    <a href="https://ubuntu.com/download/desktop/thank-you?version=20.04.2.0&architecture=amd64" alt="Ubuntu">
        <img src="https://img.shields.io/badge/Tested%20on-Ubunu MacOS-orange"/></a>
    </p>


# JohnDoe Python Class Documentation

The `JohnDoe` class generates synthetic personal information (PII) for testing environments. It creates mock details of a person, including name, age, address, phone number, email, and more.

## Class Overview

This class allows you to generate random personal information and related documents.


### Setup
1. Clone the repo into the desired location
```bash
$ git clone https://github.com/IanUmney/JohnDoe.git
```
2. Change into that directory
```bash
$ cd JohnDoe/
```
3. Install via pip
```bash
$ pip3 install .
```

### Usage
Import into python project
```python
from johndoe import JohnDoe

# Create a JohnDoe instance
jd = JohnDoe()

# Generate PII and display as JSON
jd.create()
```
or from the command line
```bash
$ python3 -m johndoe --name "Ana Lias" --age 69 --documents
```