#Import file add a header, and based on the file name add a country code to the data
import os

#Open the file for processing
fullFileName = 'SampleFile_USA.txt'
filename, file_extension = os.path.splitext(fullFileName)
tmp = open( filename+'_Output'+file_extension, 'w')
orig = open(fullFileName, 'r')

#Hardcode header and delimiter, if the file format changes... yikes!
#Assign a country code based on file name
headers = ['FirstName', 'LastName', 'Age', 'State','ZipCode','Phone','Country']
delimiter = '|'
countryCode = filename.rsplit('_')[1]

#Write back the file, and add the header
tmp.write(delimiter.join(headers) + '\n')
for line in orig.readlines():
    #Append country code and delimiter to end of line
    #Format the full namecolumn to be FirstName and LastName
    columns = line.split('|')
    columns[0:1] = columns[0].split(',')
    columns[0] = columns[0].capitalize()
    columns[1] = columns[1].capitalize()
    #Format and save line
    tmp.write(delimiter.join(columns).rstrip('\n') + delimiter + countryCode + '\n')

#Close the files
orig.close()
tmp.close()

