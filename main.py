import csv
from slugify import slugify
from pathlib import Path
from shutil import copyfile
from constants import *

def make_file_content(content):
  result = 'Original entry in the Database:\r\n\n'
  for key, field in FIELDS.items():
    result += key + ':\t' + content[field] + '\r\n'
  
  return result

def make_summary_txt_file(subscription):
  name = slugify(subscription[FIELDS['NAME']])
  email = subscription[FIELDS['EMAIL']]
  filename = name + '-' + email + '.txt'
  folder = './'+CONTEST_FOLDER+'/'+DESTINATION_FOLDER+'/'+ name + '/'

  Path(folder).mkdir(parents=True, exist_ok=True)

  with open(folder + filename, 'w') as statementFile:
    statementFile.write(make_file_content(content=subscription))
    return True
  
  return False

def copy_photos(subscription):
  name = slugify(subscription[FIELDS['NAME']])
  email = subscription[FIELDS['EMAIL']]
  filename = name + '-' + email
  destinationFolder = './'+CONTEST_FOLDER+'/'+DESTINATION_FOLDER+'/'
  sourceFolder = './'+CONTEST_FOLDER+'/photos/'

  for idx in range(1,4):
    if not subscription[FIELDS['IMG'+ idx.__str__()]] == '':
      pic = sourceFolder + subscription[FIELDS['IMG'+ idx.__str__()]]
      if Path(pic).exists():
        fileExtension = Path(pic).suffix
        dest = destinationFolder + filename + fileExtension
        try:
          copyfile(pic, dest)
        except:
          print('Error copying from: %s - to: %s' %(pic, dest))
  return None

def make_entry(subscription):
  # make the folder and the entry text file for the subscription
  # this will also create the folder if doesn't exist
  """ if not make_summary_txt_file(subscription):
    print('Error TXT: ' + ', '.join(subscription))
 """
  # copy the contest pics into the same folder
  copy_photos(subscription)

def main():
  # open the contest CSV file
  with open('./' + CONTEST_FOLDER + '/' + CSV_FILENAME, newline='') as subscriptionFile:
    subscriptionList = csv.DictReader(subscriptionFile)

    # range over its lines
    for row in subscriptionList:
      make_entry(subscription=row)

if __name__== "__main__":
  main()