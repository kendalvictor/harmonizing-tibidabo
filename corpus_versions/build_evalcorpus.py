#!/usr/bin/python

# This script builds randomly a test and a development corpus (50%-50% sentences) from the Tibidabo corpus selecting

import random
import sys

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print "usage: > python ./buil_evalcorpus.py <corpus>"
        exit(1)

    # test corpus files
    outtest_cn = open('../../tibidabo/conll_2015-10-01/test/tibidabo_test.conll','w')
    outtest_fl = open('../../tibidabo/conll_2015-10-01/test/tibidabo_test.fl','w')
    outtest_tb = open('../../tibidabo/conll_2015-10-01/test/tibidabo_test.tbd','w')

    # devel corpus files
    outdevel_cn = open('../../tibidabo/conll_2015-10-01/tibidabo_devel.conll','w')
    outdevel_fl = open('../../tibidabo/conll_2015-10-01/tibidabo_devel.fl','w')
    outdevel_tb = open('../../tibidabo/conll_2015-10-01/tibidabo_devel.tbd','w')

    cur_sentence = []
    devel_corpus = []
    sentences = []
    test_corpus = []

    ran_sentence = {}

    # parse corpus
    with open(sys.argv[1],'rb') as tibidabo:
        for line in tibidabo:
            token = line.split()

            # detect lines containing tokens
            if len(token) == 11:
                # store tokens of the sentence in a list of the current sentence read
                cur_sentence.append(token)
            # detect sentence ending
            else:
                # store every sentence read in a list of sentences
                sentences.append(cur_sentence)
                cur_sentence = []

    # create a set of sentences selecting randomly 50% of the original corpus
    for rsentence in random.sample(range(0,len(sentences)),1904):
        ran_sentence[rsentence] = sentences[rsentence]
        # store the 50% random sentences in a list of sentences
        test_corpus.append(sentences[rsentence])

    # create test corpus
    for test_sentence in test_corpus:
        for item in test_sentence:

            # conll format
            token_cn = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[4],item[3],
                                                                         item[5],item[6],item[7],item[10],'_','_')
            outtest_cn.write(token_cn)

            # freeling format
            token_fl = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[4],
                                                                                 item[3],item[5],'-','-',item[10],
                                                                                 item[6],item[7],'-','-')
            outtest_fl.write(token_fl)

            # tibidabo format
            item_tb = '\t'.join(item)
            token_tb = '%s\n' % (item_tb)
            outtest_tb.write(token_tb)

        outtest_cn.write('\n')
        outtest_fl.write('\n')
        outtest_tb.write('\n')

    # create development corpus
    for devel_sentence in range(0,len(sentences)):
        # discard sentences in the test corpus
        if not ran_sentence.has_key(devel_sentence):
            for item in sentences[devel_sentence]:

                # conll format
                token_cn = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[4],item[3],
                                                                         item[5],item[6],item[7],item[10],'_','_')
                outdevel_cn.write(token_cn)

                # freeling format
                token_fl = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[4],
                                                                                 item[3],item[5],'-','-',item[10],
                                                                                 item[6],item[7],'-','-')
                outdevel_fl.write(token_fl)

                # tibidabo format
                item_tb = '\t'.join(item)
                token_tb = '%s\n' % (item_tb)
                outdevel_tb.write(token_tb)

            outdevel_cn.write('\n')
            outdevel_fl.write('\n')
            outdevel_tb.write('\n')