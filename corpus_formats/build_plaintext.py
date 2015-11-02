# -*- coding: utf-8 -*-
# #!/usr/bin/python

# This script removes sentences in Tibidabo corpus containing certain syntactic function tags (currently only 'undef')

import sys

if __name__ == "__main__":
    if len(sys.argv) is not 1 + 2:
        print "usage: > python ./build_plaintext.py <input> <output>"
        exit(1)

    out_tibidabo = open(sys.argv[2], 'wb')

    sentences = []
    cur_sentence = []

    with open(sys.argv[1], 'rb') as tibidabo:
        for line in tibidabo:
            items = line.split()

            # tokens of a sentence
            if len(items) > 0:
                # items of the current sentence are added in a list
                cur_sentence.append(items[1])

            # when a sentence ending is detected, the current sentence is added in a list of sentences
            else:
                sentences.append(cur_sentence)
                cur_sentence = []

    for sentence in sentences:
        text = ' '.join(sentence)
        text = text.replace('_',' ')
        text = text.replace(' %','%')
        text = text.replace(' .','.')
        text = text.replace(' ?','?')
        text = text.replace(' !','!')
        text = text.replace(' : ',': ')
        text = text.replace(' ; ','; ')
        text = text.replace(' , ',', ')
        text = text.replace(' )',')')
        text = text.replace('( ','(')
        text = text.replace('¿ ','¿')
        text = text.replace('¡ ','¡')

        outdata = '%s\n' % (text)
        out_tibidabo.write(outdata)

        '''# just the last sentence of the file
        if len(cur_sentence) > 0:
            sentences.append(cur_sentence)

        out_sentences = []'''

        '''for sentence in sentences:
            is_valid = True

            for line in sentence:

                # discard sentences containing a token with the sub-string "UNDEF"
                if "UNDEF" in line:
                    is_valid = False
                    break

            # filters the sentences that are valid
            if is_valid:
                out_sentences.append(sentence)'''

        '''# print outside the loop (python method)
        for sentence in out_sentences:
            for line in sentence:
                line_format = '\t'.join(line)
                outdata = '%s\n' % (line_format)
                out_tibidabo.write(outdata)

            # add empty line at sentence ending
            out_tibidabo.write('\n')'''