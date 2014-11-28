#!/usr/bin/env python
#
# $Id$

from distutils.core import setup, Extension
from distutils.command import config, clean
import cPickle, glob, os, sys

pcap = Extension(name='pcap',
                 sources=[ 'pcap.c', 'pcap_ex.c' ],
                 include_dirs=[],
                 library_dirs=[],
                 libraries=['pcap'],
                 extra_compile_args=[],
                 )


setup(name='pcap',
      version='1.1',
      author='Dug Song',
      author_email='dugsong@monkey.org',
      url='http://monkey.org/~dugsong/pypcap/',
      description='packet capture library',
      ext_modules = [ pcap ])

