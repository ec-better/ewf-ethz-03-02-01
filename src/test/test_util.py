#!/opt/anaconda/bin/python

import sys
import os
import unittest
import string
from StringIO import StringIO
import py_compile

# Simulating the Runtime environment
os.environ['TMPDIR'] = '/tmp'
os.environ['_CIOP_APPLICATION_PATH'] = '/application'
os.environ['ciop_job_nodeid'] = 'dummy'
os.environ['ciop_wf_run_root'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'artifacts')

#sys.path.append('../main/app-resources/util/')

#from util import log_input

class NodeATestCase(unittest.TestCase):

    def setUp(self):
        pass

    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_compile(self):
        try:
          py_compile.compile('../main/app-resources/notebook/run', doraise=True)
        except:
          self.fail('failed to compile src/main/app-resources/notebook/run')
 
if __name__ == '__main__':
    unittest.main()


