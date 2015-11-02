# -*- coding: utf-8 -*-
# /usr/bin/python
# This script adapts de corpus Tibidabo to the new FreeLing tagging tags

import re
import sys

if __name__ == "__main__":
    if len(sys.argv) is not 1 + 2:
        print "Usage: ./convert_flnovelties.py <corpus> <tagset>"
        exit(1)

    adjective = re.compile(r'^A.*')
    preposition = re.compile(r'^SPS00$')
    pronoun = re.compile(r'^P.*')
    aq0msp = re.compile(r'AQ0MSP')
    pi0cc00 = re.compile(r'PI0CC00')

    cur_sentence = []

    dictokens = {}

    # parse the tagset of tokens (word, lemma, pos)
    with open(sys.argv[2],'rb') as tagset:
        for line in tagset:
            tag = line.split()

            # if the read line is a token (word, lemma, pos), add it to a dictionary of tuples of tokens
            if len(tag) == 3:
                dictokens[tuple(tag)] = tag

    # parse the corpus
    with open(sys.argv[1],'rb') as corpus:
        for line in corpus:
            token = line.split()

            if len(token) == 11:
                cur_sentence.append(line)
                if 'inadvertido' in token[1]:
                    print line

            for w in range(0,len(cur_sentence)):

                item = cur_sentence[w].split()
                pos = item[4]
                token = (item[1].lower(),item[2],item[4])

                # specific PoS
                #if 'inadvertido' in item[1]:
                if aq0msp.search(pos):
                    newpos = 'VMP00SM'
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])

                elif pi0cc00.search(pos):
                    newpos = 'PI0CP00'
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])

                # adjectives add a zero in the end
                elif adjective.search(pos):
                    newpos = pos+'0'
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])

                # prepositions loose zeros in the end
                elif preposition.search(pos):
                    newpos = re.sub('S00$','',pos)
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])

                # pronouns loose a zero in the end
                elif pronoun.search(pos):
                    newpos = re.sub('0$','',pos)
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])
                # tokens of the corpus with different lemma and pos get the lemma and pos of the dictionary
                elif dictokens.has_key(token):
                    newtoken = dictokens.get(token)
                    newpos = newtoken[2]

                    if newpos != pos:
                        cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],
                                                                                        newpos,item[5],item[6],item[7],
                                                                                        item[8],item[9],item[10])
                        print 'TO REVIEW ---',pos,newpos,cur_sentence[w]

            # Sentence transformed. Print all sentences of the corpus
            for w in range(0,len(cur_sentence)):
                print cur_sentence[w]
            print '\n'

            cur_sentence = []
