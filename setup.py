#!/usr/bin/env python3

# This is only for Python 2.7
from __future__ import print_function

import os, sys
import distutils.core, distutils.file_util
from glob import glob

sys.path.insert(0, '.')
if not os.access('tmp', os.W_OK):
    os.mkdir('tmp')
distutils.file_util.write_file('tmp/__init__.py', '')
distutils.file_util.copy_file('pgn2db', 'tmp/pgn2db.py')
distutils.file_util.copy_file('db2pgn', 'tmp/db2pgn.py')
from tmp.pgn2db import pgn2db_version
from tmp.db2pgn import db2pgn_version
if pgn2db_version != db2pgn_version:
    print('WARNING: Version mismatch:')
    print('pgn2db version: %s' % pgn2db_version)
    print('db2pgn version: %s' % db2pgn_version)

if os.name == 'posix':
    doclocation = 'share/doc/normalizePGN'
else:
    doclocation = 'doc/normalizePGN'

examplelocation = doclocation + '/examples'

if os.name == 'nt':
    distutils.file_util.copy_file('pgn2db', 'pgn2db.py')
    distutils.file_util.copy_file('db2pgn', 'db2pgn.py')
    scripts = ['pgn2db.py', 'db2pgn.py']
else:
    scripts = ['pgn2db', 'db2pgn']

with open('DESCR.md') as f:
    long_description = f.read()

dist = distutils.core.setup(name = 'normalizePGN',
    version = pgn2db_version,
    description = 'Helper scripts to fix PGN meta-data before importing them to Chess DB (like SCID)',
    long_description = long_description,
    author = 'Grzegorz Wierzchowski',
    author_email = 'gwierzchowski@wp.pl',
    url = 'https://github.com/gwierzchowski/normalizePGN',
    scripts = scripts,
    #data_files = [(doclocation, ['README.md', 'LICENSE.txt', 'DESCR.md', 'docs/Changelog.md'])],
    data_files = [(doclocation, ['README.md', 'LICENSE.txt', 'DESCR.md']),
                  (examplelocation, glob('examples/*'))],
    requires = ['gamerec'],
    license = 'GPLv3',
    platforms = 'linux',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment :: Board Games'
    ]
    )

if sys.argv[1] in ['install']:
    # Unfotunately while installing using pip those print statements does not work on Windows
    print ('---------------------------------------------------------')
    try:
        import gamerec
    except ImportError:
        print ('To run this software install package gamerec')
    isobj = dist.get_command_obj('install_data')
    readmedoc = None
    for doc in isobj.get_outputs():
        if 'README.md' in doc:
            readmedoc = doc
            break
    if readmedoc:
        print ('See %s file' % readmedoc)
    else:
        print ('See files deployed to documentation folder')
    print ('---------------------------------------------------------')
