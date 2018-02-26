#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Optimizations:
#
# 1 - Each row is sorted before computing tuples, which allows the script to create same tuple independently of the Artists order in the particular row. Artists [A,B] and [B,A] will generate same tuple [A,B] on the itertools.combinations method if the row is sorted. 
#
# 2 - The input file is iterated only one time.
#
# 3 - The output file is populated at the same time than counting tuples. If a tuple reaches at least ${listcounts}, by default 50, means that is going to be written in the output file. When the ammount of appearance for a particular tuple count reaches that value, the tuple is written to the output file.
# 

import collections
import itertools
import sys
import argparse
import os.path
import csv 

def validateFile(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def parseArguments():

  parser = argparse.ArgumentParser(description='Based on an input file located in ${inputFile}, produces an output file called ${outputfile} containing a list of pairs of artists which appear TOGETHER in at least ${listcount} different lists. The process will generate an empty ${outputfile} file if it does not find any match')

  parser.add_argument('--inputfile', metavar='FILE',default='input.txt',type=lambda x: validateFile(parser, x),
                    help='CSV Input File location. User must have permissions to read this file. - default: input.txt')

  parser.add_argument('--outputfile', metavar='FILE',default='output.txt',
                    help='CSV Output File location. User must have permissions to write to the specified location. It will overrides the file if it already exists. - default: output.txt')

  parser.add_argument('--listcount', metavar='N', type=int, default=50,
                    help='Integer that represents the number of list in which at least each tuple should appear together. Range [1-1000]. - default: 50')

  args = parser.parse_args()

  return args


def generateFavoriteTuples(inputFileLocation,outputFileLocation,tupleSize,listCount):

 print ("Initiating Favorite Musical Artists Analysis with the following arguments.")
 print ('Input File: {}. Output File: {}. Tuple Size: {}. List Count: {}'.format(inputFileLocation,outputFileLocation,tupleSize,listCount));
 
 favoritesDict = collections.defaultdict(int)
 matches = 0

 #Open File to Store Results. Will generate an empty file if no matches are found.
 with open(outputFileLocation,'w') as outputFile:
  csv_out=csv.writer(outputFile)
  #Opening input file in order to start analysis
  with open(inputFileLocation, 'r') as inputFile:
   reader = csv.reader(inputFile)
   for row in reader:
    if row: # if row is not empty, order row, and generate possible combinations taking into account the {tupleSize}
     combinations=list(itertools.combinations(sorted(row), tupleSize))    
     for combination in combinations: #iterate combinations and incremente occurence in the favorites dictionary.
      favoritesDict[combination] += 1
      if favoritesDict[combination] == listCount: #if a combination reached the {listCount} argument value, it means that must be written to the destination file. (the requirement was that it whould appear AT LEAST in ${listCount} lists. (Default 50)   
       csv_out.writerow(combination)      
       matches+=1

 print ('Operation completed. Matches Found: {}.  Please verify Output File: {}. for detailed information. '.format(matches,outputFileLocation))
 
def main():
    args = parseArguments()
    generateFavoriteTuples(args.inputfile,args.outputfile,2,args.listcount)

if __name__ == "__main__":
    main()
    
