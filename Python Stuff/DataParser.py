# Title: Data Parsing/Correlation Program (dataparser.py)
# Date: July 09, 2019
# Author: Galen Yanofsky
# Function:
"""
This program is designed to uncompress, and read in text data from a single source and produce
a variable length flat file digestthat can be uploaded to/leveraged by a search analytics platform (Splunk).
The program was originally designed to uncompress and read in data from physical media that was received at regular intervals. 
This program could also be modified to read in data from web sources and create flat file digests based on the desired information 
by importing the correct modules/libraries (requests, urllib, socket, etc.) The script below can be used as a template. The {} denotes
that those are variables that need to be supplied or initialized by whomever is using the script.
"""

#Import necessary libraries
import csv, io, os, xml, re, sys, time, zipfile as zip, fnmatch, shutil

#Function to extract file
def extractFile():

	#Get current directory and print
	currentDir = os.getcwd()
	print("Current Directory: ", currentDir)

	#Change to target directory and extract all contents of target archive/file to a designated destination directory
	os.chdir("{target directory}")
	archivedFile = zip.ZipFile("{target file}", "r") #Opens file in read mode.
	archivedFile.extractall(path="{destination directory}")
	
	#Change to destination directory
	os.chdir("{destination directory}")
	for dir in os.listdir(".")
		if fnmatch.fnmatch(dir, "{child directory}")
			os.chdir(dir)

	#Copy directory contents to container directory for parsing
	currentDir = os.getcwd()
	print("Changed Directory: ", currentDir)
	time.sleep(1) #Cause program to wait for 1 second
	srcFileList = os.listdir()
	destDir = "{destination directory}"
	for file in srcFileList:
		shutil.copy(file, dstDir)
	print("Files Extracted...")
	time.sleep(1)
	print("Files Written To Directory...")
	os.chdir("{destination directory}
	
	for x in os.listdir('.'):
		if fnmatch.fnmatch(x, "{Source Folder To Remove?}"):
			shutil.rmtree(x)
	for y in os.listdir('.'):
		if fnmatch.fnmatch(x, "{A File To Remove?}"):
			shutil.rmtree(x)
	time.sleep(2)

#Function that reads contents of the file and deletes unwanted fields
def processFile():
	path = os.getcwd()
	print()
	print("Current Working Directory: ", path)
	os.chdir("{destination directory}")
	print("Changed Directory: ", os.getcwd())
	
	files = os.listdir()
	print("Number of files: "len(files))
	# Regex to match unwanted datatype/field
	regex1 = re.compile(r"{regular expression}")
	dataToDelete = list(filter(relsearch, files))
	print("Number of unwanted data/fields: ", len(dataToDelete))

	if len(dataToDelete) > 0:
		choice = input("Would you like to delete all {}? (Choose 'Y'/'N'):\n".format(len(dataToDelete))) #{} Unwanted data field
		if choice == "Y":
			for file in dataToDelete:
				os.remove(file)

#Function that searches and parses the desired data/Writes desired data to output. This script will write 5 columns of data to file.
def matchWrite():
	files = os.listdir()
	#Opened output file in write mode
	f = open(r"{output file}, "w") 
	f.write("{column1}", "{column2}", "{column3}", "{column4}", "{column5}") #This row of the flat file will designate the searchable fields
	
	for file in files: #If there is a list of source files/data that needs to be parsed. This could also be modified to read a list of HTML pages.
		fileOpen = open(file, 'r', encoding='utf-8') #It is important to designate file encoding so that all contents are read in correctly.
		fileRead = fileOpen.read()

		column1Re = re.compile(r"(?<=field/tag for match>){Regex}(?<=field/tag for match>)",re.MULTILINE) #Multiline match is important data tags.
		column2Re = re.compile(r"(?<=field/tag for match>){Regex}(?<=field/tag for match>)",)
		column3Re = re.compile(r"(?<=field/tag for match>){Regex}(?<=field/tag for match>)",)
		column4Re = re.compile(r"(?<=field/tag for match>){Regex}(?<=field/tag for match>)",)
		column5Re = re.compile(r"(?<=field/tag for match>){Regex}(?<=field/tag for match>)",)

		column1Field = (column1re.findall(fileRead)) #findall is used to match all occurrences of that data
		column2Field = (column2re.search(fileRead))
		column3Field = (column3re.search(fileRead))
		column4Field = (column4re.search(fileRead))
		column5Field = (column5re.search(fileRead))
			
		#Statements added to account for NULL values
		
		if column1Field == None:
			column1Field = "NULL"
		else:
			column2Field = column1Field.group()
		if column2Field == None:
			column2Field = "NULL"
		else:
			column2Field = column2Field.group
	
		if column3Field == None:
			column3Field = "NULL"
		else:
			column3Field = column3Field.group
	
		if column4Field == None:
			column4Field = "NULL"
		else:
			column4Field = column4Field.group
	
		if column5Field == None:
			column5Field = "NULL"
		else:
			column5Field = column5Field.group
	
			for x in dataEntry: #Potentially the first column field for data parsing	
				f.write(x)
				f.write(",")
				f.write(str(column1Field)
				f.write(",")
				#Continue to create usable flatfile/CSV
	print("Parsing Complete.....")
	time.sleep(1)

if __name__=="__main__":
	extractFile()
	processFile()
	matchWrite()
	
	print("Write Operation, BLAH BLAH Complete BLAH!")
	time.sleep(1)
	print("Exiting.....")
	
		
		
		
	
