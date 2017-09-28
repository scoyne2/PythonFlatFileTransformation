#Import file add a header, and based on the file name add a country code to the data
import os

#Open the file for processing
fullFileName = 'SampleFile_USA.txt'
filename, file_extension = os.path.splitext(fullFileName)
tmp = open( filename+'_Output'+file_extension, 'w')
orig = open(fullFileName, 'r')

#Hardcode header and delimiter, if the file format changes... yikes!
#assign a country code based on file name
headers = ['Name', 'Age', 'State','ZipCode','Phone','Country']
delimiter = '|'
countryCode = filename.rsplit('_')[1]

#write back the file, and add the header
tmp.write(delimiter.join(headers) + '\n')
for line in orig.readlines():
    #append country code and delimiter to tnd of line
    tmp.write(line.rstrip('\n') + delimiter + countryCode + '\n')

#Close the files
orig.close()
tmp.close()

