# CSV fields map
# idIscrizione,nome,email,telefono,messaggio,img1,img2,img3,pdf,caricamento,ip,livello,profilepic
FIELDS = {
  'ID': 'idIscrizione',
  'NAME': 'nome',
  'EMAIL': 'email',
  'PHONE': 'telefono',
  'STATEMENT': 'messaggio',
  'IMG1': 'img1',
  'IMG2': 'img2',
  'IMG3': 'img3',
  'PDF': 'pdf',
  'DATE': 'caricamento',
}

# CSV delimiter
CSV_DELIMITER = ';'

# The main folder to work on
CONTEST_FOLDER = 'youma-contest-2022'

# The inner folder containing the photos
PHOTOS_FOLDER = 'photos'

# The CSV containing the contest entries
CSV_FILENAME = 'iscrizioni2022.csv'

# The destination of the export
# NB. will be placed into the contest folder itself
DESTINATION_FOLDER = 'exports'