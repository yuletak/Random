#!/usr/bin/env /usr/bin/python2.7

import sys
from time import sleep
from datetime import datetime
import pexpect
from utilities import create_pexpect_obj 
from constants import *
from re import compile, DOTALL

class Testcase:
    """ A barebones class for testing the QA process

    Attributes:
        self.params - list of commands/parameters to send
        self.result - results expected

    Methods:
        __init__ - constructor, expects the following input parameters:
        
        execute - send commands and check results
    """

    def __init__(self, params):
        self.output = params[OUTPUT]

    def execute(self):
        if self.output[0] == 'blah':
            return [0, '']
        else:
            return [1, 'output doesn\'t match! {0}'.format(self.output[0])]

