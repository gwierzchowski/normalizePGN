**normalizePGN** is a package containing helper scripts and examples that show how to normalize - i.e. correct 
some games' meta-data contained in .pgn files before loading them to chess database.
PGN files that are being published by tournaments' organizers sometimes (especially for large events where
few people work on digitalizing games) used to be not consistent. E.g. event name or event place is written 
in slightly different way or there is missing some important information in .pgn files that we want to have - like
time control, players ELO or titles, etc. Those scripts help to fix and complete this information quickly 
(faster than just by manually editing .pgn files).  
The idea is to perform following steps:
- import games to SQLite database
- run few SQL queries that check data consistency and things that we care
- based on results of previous step, write fix SQL expressions (usually the ones from previous tournaments 
  are good enough or needs only slight modification)
- run fix expressions
- re-check data (using queries from second step)
- export games back to .pgn file
- import .pgn file to chess database of your choice (e.g. SCID).
So using this package requires some basic SQL knowledge and some initial time investment into getting 
familiar how all this works and creating an initial scripts suitable for your specific use cases.
But my experience is that tournament organizers tend to replicate the same issues in .pgn files 
from one event edition to next. So workout scripts from one edition usually works for all next editions of the 
same tournament.

Provided examples use POSIX shell and some utilities (like sed), so Linux or Mac users could have good starting point.
Windows users may need to put more time to rewrite this staff to technologies available in their system or
try to use some utilities like cygwin or unix services for windows.

For information what files are deployed by this package and where see file README.md included in source-ball or 
in typical installation using pip deployed to folder:
- /usr/local/share/doc/normalizePGN (Linux)
- C:\Python35\doc\normalizePGN (Windows) or
- <USER>\AppData\Local\Programs\Python\Python35-32\Doc\normalizePGN
