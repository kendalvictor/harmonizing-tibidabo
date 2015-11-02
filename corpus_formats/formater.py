# -*- coding: utf-8 -*-
# /usr/bin/python

# Transforms the conll format of the tibidabo corpus to the conll format of freeling.

import sys

if __name__ == "__main__":
    if len(sys.argv) is not 1 + 3:
        print "Usage: ./formater.py <tibidabo input> <freeling format> <conll format>"
        exit(1)

    flout = open(sys.argv[2],'wb')
    cnout = open(sys.argv[3],'wb')

    with open(sys.argv[1],'rb') as input:
        for line in input:
            token = line.split()

            if len(token) == 11 :
                flformat = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (token[0],token[1],token[2],
                                                                                    token[4],token[3],token[5],'-','-',
                                                                                    token[10],token[6],token[7],'-','-')
                cnformat = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (token[0],token[1],token[2],
                                                                            token[4],token[3],token[5],token[6],
                                                                            token[7],token[10],'_','_')
                flout.write(flformat)
                cnout.write(cnformat)
            else:
                if len(token) > 0 :
                    print 'Error', len(token), line
                flout.write(line)
                cnout.write(line)