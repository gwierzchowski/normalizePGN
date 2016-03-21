Normalize PGN
=============

Helper scripts to fix PGN meta-data before importing them to Chess DB.

Works only with Python 3.  
Tested only on Linux.  
For package description see DESCR.md file.

INSTALLATION (System wide - for all users):
-------------------------------------------

### Prerequisites
This program requires following 3-rd party packages: gamerec. 
It must be installed in order to run pgn2db and db2pgn programs.  
**gamerec** can be installed from Python Package Index:  
Linux: `sudo pip install gamerec`  
Windows: `pip install gamerec`  

### Installation Method 1
Recommended method for installation of this package is from Python Package Index:  
Linux: `sudo pip3 install normalizePGN`  
Windows: `pip3 install normalizePGN`

### Installation Method 2
If you want to install particular version, download source-ball and issue:  
Linux: `sudo pip3 install normalizePGN-<ver>.tar.gz`  
Windows: `pip3 install normalizePGN-<ver>.tar.gz`

### Installation Method 3
Alternatively unpack source-ball and from unpacked folder run command:  
Linux: `sudo python3 setup.py install`  
Windows: `python setup.py install`  
Note: More installation options are possible - see documentation of Python `distutils` package.

### Installation from Source
If you have downloaded archive snapshot, first unpack it and from root folder run command: 
`python3 setup.py sdist` 
which will create `dist` subfolder and create source-ball in it. Then apply method 2 or 3 above.

### Files deployed by installation script
- Command line utilities:  
  Linux: `<BINDATA>/pgn2db` and `<BINDATA>/db2pgn`, where `<BINDATA>` is by default `/usr/local/bin`  
  Windows: `<BINDATA>\Scripts\pgn2db.py` and `db2pgn.py`, where `<BINDATA>` is by default `C:\Python35` or `<USER>\AppData\Local\Programs\Python\Python35-32` 
- Documentation:  
  Linux: `<PREFIX>/share/doc/normalizePGN/*`, where `<PREFIX>` is by default `/usr/local`  
  Windows: `<PREFIX>\Doc\normalizePGN\*`, where `<PREFIX>` is by default `C:\Python35` or `<USER>\AppData\Local\Programs\Python\Python35-32`
- Example .pgn files fix scripts:  
  `examples` subfolder of above mentioned documentation folder.

RE-INSTALLATION/UPGRADE:
------------------------

To upgrade packages from PyPi use -U option:
`[sudo] pip install -U gamerec normalizePGN`.  

USAGE:
------

Installed command line utilities can be used to convert games written in .pgn file to 
databse (SQLite) file back and forth.
Syntax:
```
pgn2db [-o] <PGNFile> <SQLiteFile>
  -o means that <SQLiteFile> will be cleared before adding games
db2pgn [-o] [-s <fields>] <SQLiteFile> <PGNFile>
  -o means that <PGNFile> will be overwritten, otherwise games will be appended
  -s means that games will be sorted, where <fields> is comma separated list of expressions (as in ORDER BY) to sort by
```

See also installed example files for instruction how to use this package.
