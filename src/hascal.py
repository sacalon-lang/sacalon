#!/usr/bin/env python3

# The Hascal Application
#
# The Hascal Programming Language
# Copyright 2019-2022 Hascal Development Team,
# all rights reserved.

from sys import argv 
from core.h_builder import HascalCompiler # importing hascal compiler
import pathlib
import os
if __name__ == "__main__":  
      BASE_DIR = str(pathlib.Path(__file__).parent.resolve())
      print(BASE_DIR)
      HascalCompiler(argv,BASE_DIR)
            

      
      
      
