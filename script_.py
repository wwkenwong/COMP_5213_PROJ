import fileinput
import glob
import sys
import string

for line in fileinput.input(glob.glob('*.txt'), inplace=True):  
  line=line.lower()
  
  line.replace('1', '')
  line.replace('2', '')
  line.replace('3', '')
  line.replace('4', '')
  line.replace('5', '')
  line.replace('6', '')
  line.replace('7', '')
  line.replace('8', '')
  line.replace('9', '')
  line.replace('0', '')
  line.replace('`', '')
  line.replace('~', '')
  line.replace('!', '')
  line.replace('@', '')
  line.replace('#', '')
  line.replace('$', '')
  line.replace('%', '')
  line.replace('^', '')
  line.replace('&', '')
  line.replace('*', '')
  line.replace('(', '')
  line.replace(')', '')
  line.replace('-', '')
  line.replace('_', '')
  line.replace('+', '')
  line.replace('=', '')
  line.replace('{', '')
  line.replace('}', '')
  line.replace('[', '')
  line.replace(']', '')
  line.replace(':', '')
  line.replace(';', '')
  line.replace('"', '')
  for char in string.punctuation:
    line=line.replace(char,' ')
  for char in string.number:
    line=line.replace(char,'')
  sys.stdout.write(line)
    