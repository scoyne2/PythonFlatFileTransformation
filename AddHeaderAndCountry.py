#Import file add a header, and based on the file name add a country code to the data
import os

#Hardcode header, if the file format changes... yikes!
headers = ['Name', 'Age', 'State','ZipCode','Phone','Country']
filename = 'SampleFile_USA.txt'
tmp = open('TMP', 'w')
orig = open(filename, 'r')
tmp.write('\t'.join(headers) + '\n')
for line in orig.readlines():
    #this is where we will want to split the file name based on the underscore and grab the text from the right side
    #of the underscore, hardcode for now
    tmp.write(line) + "USA"
orig.close()
tmp.close()
os.remove(filename)
os.rename('TMP', filename)