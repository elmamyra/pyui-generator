#!/usr/bin/env python
from distutils.core import setup
import os, sys, platform
import ConfigParser








if platform.system() == "Linux":
    data_files = [
        ('share/icons/hicolor/32x32/apps', ['pyui-generator.png']),
        ('share/applications', ['pyui-generator.desktop']),
        (os.path.join(os.environ['HOME'], ".local/share/mime/packages"), ['application-pyui-generator.xml'])
    ]
#    cmdclass={"install": my_install},
else:
    data_files = []
    cmdclass={},
    

setup(
    name = 'pyui-generator',
    version = '1.0',
    author = 'Nicolas Malarmey',
    author_email = 'malarmey.nicolas@gmail.com',
    license = 'GPL',
    platforms = 'Linux',
    description = 'Convert Qt Designer files to python files',
    scripts = ['pyui-generator'],
    packages = ['pyuiGenerator_app', 'pyuiGenerator_app/pyui', 'pyuiGenerator_app/i18n'],
    package_data = {'pyuiGenerator_app/i18n': ['*.qm']},
    data_files = data_files,
)

if sys.argv[1] != 'sdist':
    mimeListPath = os.path.join(os.environ['HOME'], '.local/share/applications/mimeapps.list')
    if os.path.exists(mimeListPath):
        cfg = ConfigParser.ConfigParser()
        cfg.read(mimeListPath)
        if not cfg.has_section('Added Associations'):
            cfg.add_section('Added Associations')
        cfg.set('Added Associations', 'application/pyui-generator', 'pyui-generator.desktop')
        cfg.write(open(mimeListPath, 'w'))
        
    os.system('update-mime-database ~/.local/share/mime')