# Research

### Info

All of the code in this section is disconnected from the main project. During my research of reading data from images to music information, I started to experiment with taking data and drawing images with that data instead. 

All of this code is just sandbox experiments.

### Install instructions

Most of these scripts rely on the same libraries as the main project MIDIgen but if it doesn't just try to run the script and install whatever is missing.


### Hexdump for Reaserh Draw lines/pixel - "Automation"

Use the command **xxd** to dump a file into hex format

```bash
xxd -p inputfile outputfile
```
My scripts are looking for a hexdump file called "input.txt" 
An example of converting a picture to hexfile.

```bash
xxd -p PictureOfSon.jpg input.txt
```
