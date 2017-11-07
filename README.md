# Scurri

### Candidate

Name: Gerardo de la Rosa

Project:
My biggest achievement on my career was on my latest job. I was on charge of building
a datawarehouse (infrastructure, models, and migrations) under a tight deadline with
new tools that I had never used (Hadoop Ecosystem - Amazon EMR - Redshift), I faced
so many difficulties to understand how each tool can be used on a datawarehouse architecture,
specially because Hadoop has a huge ecosystem, nevertheless I never gave up and I could do a proper benchmarking between using Hive and Redshift as our datawarehouse, and I
developed this requirement with the tool that fits better with the company needs.




### Environment
``` bash
$ cd scurri
$ virtualenv venv
$ source venv/bin/activate
```

### Code exercises

__Code1__

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.

*Solution*

Using mod operator to determinate multiples of five and three

__Code2__

Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.

*API*

* validate_format - Function which normalizes the postcode format
* validate_code - Function which validates the postcode with the regular expression pattern
* is_an_ukpostcode - Function which supports validating and formatting

*Solution*

Using Regex to validate and formatting

### TestCases

In order to run testcases

``` bash
$ python test.py
```
