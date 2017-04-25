import fileinput
import glob
import sys
import string
#from unidecode import unidecode

num={'1','2','3','4','5','6','7','8','9','0'}
sym={'`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','"',',','.','/','?','<','>'}
space={'      ','     ','    ','   ','  '}
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
 
  for char in string.punctuation:
    line=line.replace(char,' ')
  for char in num:
    line=line.replace(char,'')
  for char in space:
    line=line.replace(char,'')
  for char in sym:
    line=line.replace(char,'_')
  sys.stdout.write(line)
    
