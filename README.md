<p align="left">
    <a href="https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz" alt="3.9.5">
        <img src="https://img.shields.io/badge/Python%20Version-3.9.5-blue"/></a>
    <a href="https://ubuntu.com/download/desktop/thank-you?version=20.04.2.0&architecture=amd64" alt="Ubuntu">
        <img src="https://img.shields.io/badge/Tested%20on-Ubunu%2020.04-orange"/></a>
    </p>

# JohnDoe 
Johndoe can create highly detailed _fake_ PII. The program was written as a tool for testing environments whereby the generated information can be used to arbitrarily populate data structures. 
## Setup
1. Clone the repo into the current directory
```bash
$ git clone https://github.com/IanUmney/JohnDoe
```
2. Change into the JohnDoe directory
```bash
$ cd JohnDoe/
```

## Usage
you can import the module into an existing Python program, or you can use the program directly from the CLI.
```python
from johndoe import JohnDoe  # Import the JohnDoe module into our project
jd = JohnDoe()  # Initialise a local variable to a random JohnDoe object
jd.name = "Anon User"  # Change attributes to the object
jd.age = 69
jd.gender = "female"  # Change attributes to the object
jd.list()  # Print the restults to the CLI
```

List an object in the commind line using the -l (--list) tag. This is the same as running jd.list() and prints the results.
```bash
$ python3 johndoe.py -l
```

### Command-Line Interface
Use Python3 to start the program and get the help page
```bash2
python3 johndoe.py -h
```
See how to use the program
```bash
usage: johndoe.py [-h] [--name NAME] [--age {18..99}] [--gender {male,female}] [-p] [-v]
optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Name to use
  --age {18..99}        Age to use
  --gender {male,female}
                        Gender to use
  -p, --pdf             Print results to PDF page
  -v, --verbose         Print results to command line
```
Example usage:
```bash
python3 johndoe.py -v --name "Jane Doe" --age 50 --gender female
```

### Importing the module
Import the _johndoe.py_ file into an existing program and call the .list() function to print all attributes.
```python
from johndoe import JohnDoe
jd = JohnDoe()  # Instantiate the object (with optional kwargs)
jd.list()  # Print the object attributes
```
**Keyword Arguments** can be passed to johndoe to specify particular attributes.
```python
jd = JohnDoe(name="Jane Doesunt", age=69, gender="female")
```

## Generated Data:
Unless specified by you, all the data is randomly generated, following patterns where needed.

You can specify the name, age, and gender attributes of an individual John Doe and the rest will be changed accordingly.


**Name** 

The name must consist of both a forename and surname eg. "John Doe". Failing to do so will force the application to quit. 

If no name is submitted x then a random name from the list of popular names and a random surname from a list of popular surnames will be chosen to 


    + Forename
        + Random from a list of popular names in 2021
    + Surname
        + Random from a list of the most frequent UK surnames
+ **Age**
    + Random integer from 18 - 99
    + Birthday
        + current year - age = year born
        + 1 ~ current month = month born
+ **Phone Number**
    + Genuine UK prefixes and providers
    + Random suffixes
+ **Address**
    + House number 
        + Random integer from 1 - 500
    + Street names
        + Random from a list of the most frequent UK street names
    + Postcode and area 
        + Random but genuine - Meaning the specific postcode is in the listed area
+ **National Insurance Number**
    + UK format of _AB123456C_
+ **Bank Card Details**
    + Bank card numbers
        + Genuine first 6-digit account IDs and then 10 random numbers
    + Bank expiry dates and CVVs
        + Randomly generated integers
+ **Driving License**
    + UK formatted number with John Doe's information
+ **Email**
    + forename.surname@ random email provider with UK TLD
+ **IP Address**
    + Uses genuine UK IP blocks to create a random IP address within that range.
+ **Image**
    + Using https://generated.photos/ API, returns an AI image based on the details of John Doe.
    + Saves images into src/images with the file name of the John Doe you created. 
        + `/John Doe_portrait.jpg`
    + You must obtain an API key from https://generated.photos/ for this to work.
        + Free sign up and 50 free monthly requests.
## Including AI Generated Images
Enter your API key into the config.ini file to enable generation of faces.
```
[GeneratedPhotos]
API_KEY : Enter_Your_API_Here
```


### Example Results

**Mike Smith**
```
name : Mike Smith
age : 22
birthday : 21/05/1999
mobile_number
    number : 07735167188
    provider : Three
address
    house_number : 257
    street : Park Road
    area : Pembrokeshire
    postcode : SA61 1YG
email : Mike.Smith@hotmail.co.uk
ip_address : 213.253.175.72
social_security : FC812154X
bank_card
    card_number : 5573576189231788
    provider : Mastercard
    expiry_date : 5/31
    cvv : 255
driving_license : smith90521999BJ 20
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Mike Smith_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Mike%20Smith_portrait.jpg?raw=true)


**Jack Peterson**
```
nationality : GB
name : Jack Peterson
age : 44
birthday : 17/06/1977
mobile_number
    number : 07537625268
    provider : Sound Advertising
address
    house_number : 265
    street : South Street
    area : Basingstoke and Deane
    postcode : RG21 3LQ
email : Jack.Peterson@gmail.co.uk
ip_address : 45.75.140.218
social_security : UA718154E
bank_card
    card_number : 5573579597246203
    provider : Mastercard
    expiry_date : 5/23
    cvv : 391
driving_license : peter70617799AC 80
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Jack Peterson_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Jack%20Peterson_portrait.jpg?raw=true)


**Mohommed Martin**
```
nationality : GB
name : Mohammed Martin
age : 54
birthday : 23/02/1967
mobile_number
    number : 07600018185
    provider : Sound Advertising
address
    house_number : 33
    street : Park Road
    area : Wirral
    postcode : CH60 8QJ
email : Mohammed.Martin@msn.co.uk
ip_address : 194.183.102.107
social_security : UF390955W
bank_card
    card_number : 5573579653322277
    provider : Mastercard
    expiry_date : 10/28
    cvv : 631
driving_license : marti60223799VK 80
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Mohammed Martin_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Mohammed%20Martin_portrait.jpg?raw=true)