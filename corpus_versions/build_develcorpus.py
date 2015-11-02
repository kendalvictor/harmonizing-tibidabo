#!/usr/bin/python

# This script builds a development corpus version of the Tibidabo corpus by removing sentences
# also existing in the test corpus

import random
import sys

if __name__ == "__main__":
    if len(sys.argv) is not 1 + 2:
        print "usage: > python ./buil_develcorpus.py <corpus> <test corpus>"
        exit(1)

    # devel corpus files
    test_cn = open('../../tibidabo/conll_2015-10-01/tibidabo_devel_tagsvells.conll','w')
    test_fl = open('../../tibidabo/conll_2015-10-01/tibidabo_devel_tagsvells.fl','w')
    test_tb = open('../../tibidabo/conll_2015-10-01/tibidabo_devel_tagsvells.tbd','w')

    corpus = {}
    corpus_test = {}

    cur_annotations = []
    cur_test_sentence = []
    cur_tokens = []

    sentences_annotations = []
    sentences_test = []
    sentences_tokens = []

    # parse corpus
    with open(sys.argv[1],'rb') as tibidabo:
        for line in tibidabo:
            item = line.split()

            # detect lines containing tokens
            if len(item) == 11:

                # split in tuples the token and the annotations of the token
                token = item[1]
                annotation = tuple(item)

                # store in a list of tokens and in a list of annotations for every current sentence read
                cur_tokens.append(token)
                cur_annotations.append(annotation)

            # detect sentence ending
            else:
                # store the list of tokens of every sentence in a list of tokens for the whole sentences
                # store the list of annotations of every sentence in a list of annotations for the whole sentences
                sentences_tokens.append(cur_tokens)
                sentences_annotations.append(cur_annotations)

                cur_annotations = []
                cur_tokens = []

    # parse test corpus
    with open(sys.argv[2],'rb') as test:
        for line in test:
            item = line.split()

            # detect lines containing tokens
            if len(item) == 11:
                # define token of the test corpus as id, word, lemma
                token = item[1]
                # store in a list of tokens for every current sentence read
                cur_test_sentence.append(token)
            # detect sentence ending
            else:
                # store the list of tokens of every sentence in a list of tokens for the whole sentences
                sentences_test.append(cur_test_sentence)
                cur_test_sentence = []

    # create a dictionary of corpus sentences: id-word-lemma (key) and annotations (values)
    for sentence,features in zip(sentences_tokens,sentences_annotations):
        sentence = tuple(sentence)
        corpus[sentence] = features

    # create a dictionary of test sentences (values and keys)
    for words in sentences_test:
        words = tuple(words)
        corpus_test[words] = words

    # take the common sentences of tibidabo corpus and test corpus to take the annotations corrected
    for tokens,annotations in corpus.iteritems():

        # detect sentences also appearing in the test corpus
        if not corpus_test.has_key(tokens):
            for a in annotations:

                # conll format
                cn = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (a[0],a[1],a[2],a[4],a[3],a[5],a[6],a[7],a[10],'_','_')
                test_cn.write(cn)

                # freeling format
                fl = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (a[0],a[1],a[2],a[4],a[3],a[5],'-','-',a[10],a[6],a[7],'-','-')
                test_fl.write(fl)

                # tibidabo format
                a = '\t'.join(a)
                tb = '%s\n' % (a)
                test_tb.write(tb)

            test_cn.write('\n')
            test_fl.write('\n')
            test_tb.write('\n')
