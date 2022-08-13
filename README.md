# Youmanity Photos exporter

Utility to export contest photos in a unique folder.

It renames the files with the following format:
```sh
[participant name]-[email]-[entry number: 1, 2...].[extension]
```

## Setup

Install requirements
```sh
pip3 install -r requirements.txt
```

Export the DB table with the entries as CSV file and put it in the contest folder.

Setup the folders starting from this as root, like:
```sh
youma-contest-2022/
    iscrizioni2022.csv
    photos/
        [all the photos]
    exports/
        [initially empty]
constants.py
main.py
[...]
```

Check the constants in `constants.py` file to reflect the folder setup and the CSV delimiter.

## Run

```sh
python3 main.py
```