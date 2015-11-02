# -*- coding: utf-8 -*-
# /usr/bin/python
# This script maps the cases that conversor.pl cannot solve

import re
import sys

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print "Usage: ./maptag.py <corpus>"
        exit(1)

    # ---------------------------------------------------------------
    def haschild(sentence, parent, func):
        # check al words in given sentence, to find one with
        # given parent and function. If none found, return -1
        for w in range(0,len(sentence)):
            word = sentence[w].split()
            if (int(word[6])==parent and (word[7]==func or func=='')):
                return w
        return -1

    # ---------------------------------------------------------------
    def childhaspos(sentence, parent, pos):
        # check al words in given sentence, to find one with
        # given parent and function. If none found, return -1
        for w in range(0,len(sentence)):
            word = sentence[w].split()
            if (int(word[6])==parent and word[4]==pos):
                return w
        return -1

    # ---------------------------------------------------------------
    def childhaslemma(sentence, parent, lemma):
        # check al words in given sentence, to find one with
        # given parent and function. If none found, return -1
        for w in range(0,len(sentence)):
            word = sentence[w].split()
            if (int(word[6])==parent and word[2]==lemma):
                return w
        return -1

    # ---------------------------------------------------------------
    def childhasrule(sentence, parent, rule):
        # check al words in given sentence, to find one with
        # given parent and function. If none found, return -1
        for w in range(0,len(sentence)):
            word = sentence[w].split()
            if (int(word[6])==parent and rule in word[10]):
                return w
        return -1

    # ---------------------------------------------------------------
    def change_func(line,newfun):
        # change 7th field in given line with given function. Return fixed line
        child = line.split()
        child[7] = newfun
        return '\t'.join(child)

    # ---------------------------------------------------------------
    def change_lemma(line,newlemma):
        # change 2th field in given line with given lemma. Return fixed line
        child = line.split()
        child[2] = newlemma
        return '\t'.join(child)

    # ---------------------------------------------------------------
    def change_pos(line,newpos):
        # change 5th field in given line with given pos. Return fixed line
        child = line.split()
        child[4] = newpos
        return '\t'.join(child)

    def change_pos2(line,newpos):
        # change 5th field in given line with given pos. Return fixed line
        child = line.split()
        child[3] = newpos
        return '\t'.join(child)

    # ---------------------------------------------------------------
    def change_features(line,newfeat):
        # change 5th field in given line with given pos. Return fixed line
        child = line.split()
        child[5] = newfeat
        return '\t'.join(child)

    # ---------------------------------------------------------------

    root = re.compile(r'^top$')

    # regex concerning adjectives
    #adjdim = re.compile(r'^AQD')
    adjective = re.compile(r'^AQ.*')

    # regex concerning adverbs
    acomp = re.compile('acomp')
    deictics = re.compile(r'^av:nc00000')

    # regex concerning conjunctions
    conj = re.compile(r'^CS$')

    # regex concerning determiners
    una = re.compile(r'^(u|U)na$')
    unas = re.compile(r'^(u|U)nas$')
    un = re.compile(r'^(u|U)n$')
    uno = re.compile(r'^(u|U)no$')
    unos = re.compile(r'^(u|U)nos$')

    # regex concerning nouns
    time_fs = re.compile(r'^(mañana|vez)$')
    time_fp = re.compile(r'^veces$')
    #noundim = re.compile(r'^NC.*D$')
    proper = re.compile(r'^NP.*')

    # regex concerning numbers and dates
    date = re.compile(r'^(nu-)?date$')
    number = re.compile(r'^(nu-card|nu-distr|nu-ord-(f|m)(p|s)|nu-part)$')
    partitive = re.compile(r'^ZD$')
    percentage = re.compile(r'^ZP$')

    # regex concerning prepositions
    prep = re.compile(r'^SPS00$')

    # regex concerning pronouns
    demas = re.compile(r'PI0CC000')
    #mio = re.compile(r'^PX1MS0S0$')
    #suyo = re.compile(r'^(PX3MS0C0|PX3NS0C0)$')
    #suyos = re.compile(r'^PX3MP0C0$')
    #tuya = re.compile(r'^PX2FS0S0$')

    # regex concerning punctuation
    dots = re.compile(r'^3dots$')
    punc = re.compile(r'^F.*')
    punc_tag = re.compile(r'^punc$')

    # regex concerning verbs
    infinitive = re.compile(r'VMN0000')
    parecer = re.compile(r'^parecer$')
    raising = re.compile(r'^(v-cp_p_inf|v-pp_e_vp_inf_ssr).*')
    verb_4p = re.compile(r'^V...4')

    # regex concerning to morphological features
    #neuter = re.compile(r'DA0NS0|PD0NS000|PP3NS000')

    # regex concerning 'se' particle
    se = re.compile(r'^se$')

    # regex concerning subcategorization frame
    adjt_arg = re.compile(r'^v-pp_e_seq:') # verbs occurring with adjunct
    adjunct = re.compile(r'^adjt$') # verbs occurring with adjunct
    attr_arg = re.compile(r'^v-(ap-ppa_seq|np|np-ppa_seq|np_sbj_cp_p):') # verbs predicting an attribute
    subj = re.compile(r'^v-cp_p_nsbj:') # verbs predicting a subject

    # regex concerning strange lemmas
    desnudo = re.compile(r'desnudo')
    inadvertido = re.compile(r'inadvertido')
    strange = re.compile(r'^(aj|ala)$')

    # regex concerning untagged tokens
    undef = re.compile(r'^UNDEF$')
    undef2adjt = re.compile(r'^(Cómo|con|[dD]e|Dentro_de|Distancias|dónde|igual|por)$')
    undef2aux = re.compile(r'^(ha|hemos|sido)$')
    undef2coor = re.compile(r'^pueden$')
    undef2dobj = re.compile(r'^(aplicar|conocemos|crecer|crisis|es|la|Pero|precio|Qué)$')
    undef2mod = re.compile(r'^como$')
    undef2prt = re.compile(r'^en$')
    undef2subj = re.compile(r'^(algunas|escudos|situación)$')
    adjt = re.compile(r'^ganar$')
    arg_agent = re.compile(r'^demonizada$')
    arg_dobj = re.compile(r'^(estar|hacer|pretender|querer|saber|ver)$')
    arg_dobj2 = re.compile(r'^imprimir$')
    arg_iobj = re.compile(r'^imponer$')
    arg_pobj = re.compile(r'^prestar$')
    arg_subj = re.compile(r'^vacilar$')
    tener = re.compile(r'^tener$')

    cur_sentence = []
    sentences = []

    # parse corpus
    with open(sys.argv[1],'rb') as tibidabo:
        for line in tibidabo:

            item = line.split()

            if len(item) == 11:
                # word line, add to current sentence, and proceed to next line
                cur_sentence.append(line)
                continue

            # Empty line found => end of sentence reached. Process it and write results

            # fix each word in the sentence that needs it
            for w in range(0,len(cur_sentence)):

                item = cur_sentence[w].split()

                i = w + 1

                #-----------------------------------------------------------------------------------#
                #
                # ASSIGNING THE RIGHT SYNTACTIC FUNCTION
                #
                # subcategorization frames of verb 'parecer'
                # pred --> attr (copulative verb)
                if parecer.search(item[2]) and attr_arg.search(item[10]):
                    # find a child of 'parecer' with the tag 'pred'
                    p = haschild(cur_sentence, i, 'pred')
                    # if found, change the tag 'pred' to 'attr'
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'attr')
                # dobj --> subj (raising verb)
                elif parecer.search(item[2]) and subj.search(item[10]):
                    # find a child of 'parecer' with the tag 'dobj'
                    p = haschild(cur_sentence, i, 'dobj')
                    # if found, change the tag 'dobj' to 'subj'
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'subj')
                # pred --> adjt (intransitive verb)
                elif parecer.search(item[2]) and adjt_arg.search(item[10]):
                    # find a child of 'parecer' with the tag 'pred'
                    p = haschild(cur_sentence, i, 'pred')
                    # if found, change the tag 'pred' to 'adjt'
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'adjt')
                #
                # adjt --> pred (adjectives depending from a verb)
                if adjective.search(item[4]) and adjunct.search(item[7]):
                    cur_sentence[w] = change_func(cur_sentence[w],'pred')
                    # change pos of word 'desnudo' and 'inadvertido'
                    if desnudo.search(item[1]):
                        cur_sentence[w] = change_pos(cur_sentence[w],'AQ0MS0')
                    elif inadvertido.search(item[1]):
                        cur_sentence[w] = change_lemma(cur_sentence[w],'inadvertir')
                        cur_sentence[w] = change_pos(cur_sentence[w],'VMP00SM')
                        cur_sentence[w] = change_features(cur_sentence[w],'pos=verb|type=main|mood=participle|num=s|gen=m')
                #
                # acomp --> adjt
                elif acomp.search(item[7]) and not deictics.search(item[10]):
                    cur_sentence[w] = change_func(cur_sentence[w],'adjt')
                #
                # 'prt' --> preposition and conjunction in raising verbs
                elif infinitive.search(item[4]) and childhasrule(cur_sentence,i,'v-pp_e_vp_inf_ssr') != -1:
                    p = childhaspos(cur_sentence,i,'SPS00')
                    q = childhaspos(cur_sentence,i,'CS')
                    if (q != -1):
                        cur_sentence[q] = change_func(cur_sentence[q],'prt')
                    elif (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'prt')

                # 'prt' --> conjunction (remaning) in raising verbs
                elif infinitive.search(item[4]) and childhasrule(cur_sentence,i,'v-cp_p_inf') != -1:
                    p = childhaslemma(cur_sentence,i,'que')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'prt')
                #
                # 'se' UNDEF --> mphes
                elif se.search(item[2]) and undef.search(item[7]):
                    cur_sentence[w] = change_func(cur_sentence[w],'mphes')
                #
                # punctuation gets function 'punc' (lemma is also changed)
                elif punc.search(item[4]):
                    if not root.search(item[7]):
                        cur_sentence[w] = change_lemma(cur_sentence[w],item[1])
                        cur_sentence[w] = change_func(cur_sentence[w],'punc')
                    # exception: punctuation in the root keeps the syntactic function tag
                    else:
                        cur_sentence[w] = change_lemma(cur_sentence[w],item[1])

                #-----------------------------------------------------------------------------------#
                #
                # ASSIGNING THE RIGHT GRAMMATICAL CATEGORY
                #
                # indefinite determiners: Z --> DI* (changes in pos, morphological features, lemma)
                # una
                elif una.search(item[1]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],'uno')
                    cur_sentence[w] = change_pos(cur_sentence[w],'DI0FS0')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'d')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=determiner|type=indefinite|gen=f|num=s')
                # unas
                elif unas.search(item[1]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],'uno')
                    cur_sentence[w] = change_pos(cur_sentence[w],'DI0FP0')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'d')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=determiner|type=indefinite|gen=f|num=p')
                # un
                elif un.search(item[1]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],'uno')
                    cur_sentence[w] = change_pos(cur_sentence[w],'DI0MS0')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'d')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=determiner|type=indefinite|gen=m|num=s')
                # unos
                elif unos.search(item[1]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],'uno')
                    cur_sentence[w] = change_pos(cur_sentence[w],'DI0MP0')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'d')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=determiner|type=indefinite|gen=m|num=p')
                #
                # indefinite determiners: Z --> PI* (changes in pos, morphological features, lemma)
                # uno
                elif uno.search(item[1]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],'uno')
                    cur_sentence[w] = change_pos(cur_sentence[w],'PI0MS000')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'p')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=pronoun|type=indefinite|gen=m|num=s')
                #
                # deictics
                elif deictics.search(item[10]):
                    cur_sentence[w] = change_pos(cur_sentence[w],'RG')
                    cur_sentence[w] = change_pos2(cur_sentence[w],'r')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=adverb')
                    if acomp.search(item[7]):
                        cur_sentence[w] = change_func(cur_sentence[w],'adjt')
                #
                # time names
                elif time_fs.search(item[1]) and not deictics.search(item[10]):
                    cur_sentence[w] = change_pos(cur_sentence[w],'NCFS000')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=noun|type=common|gen=f|num=s')
                elif time_fp.search(item[1]) and not deictics.search(item[10]):
                    cur_sentence[w] = change_pos(cur_sentence[w],'NCFP000')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=noun|type=common|gen=f|num=p')
                # demas
                elif demas.search(item[4]):
                    cur_sentence[w] = change_pos(cur_sentence[w],'PI0CP000')
                    cur_sentence[w] = change_features(cur_sentence[w],'pos=pronoun|type=indefinite|gen=c|num=p')
                #
                # possessives from pronoun to adjective

                # refer to new freeling pos tags (disable when using new tags)
                # mio
                #elif mio.search(item[4]):
                #    cur_sentence[w] = change_pos(cur_sentence[w],'AP0MS1S')
                # tuya
                #elif tuya.search(item[4]):
                #    cur_sentence[w] = change_pos(cur_sentence[w],'AP0FS2S')
                # suyo
                #elif suyo.search(item[4]):
                #    cur_sentence[w] = change_pos(cur_sentence[w],'AP0MS3N')
                # suyos
                #elif suyos.search(item[4]):
                #    cur_sentence[w] = change_pos(cur_sentence[w],'AP0MP3N')

                #-----------------------------------------------------------------------------------#
                #
                # ASSIGNING THE RIGHT MORPHOLOGICAL FEATURES
                #
                # 4th person --> per 3th person (verbs)
                elif verb_4p.search(item[4]):
                    pos = item[4].replace('4','3')
                    pos2 = item[5].replace('|num=s','|person=3|num=s')
                    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],pos,pos2,item[6],item[7],item[8],item[9],item[10])
                #
                # gender neuter
                # refer to freeling new pos tags (enable when using them)
                #elif neuter.search(item[4]):
                #    pos = item[4].replace('NS','0S')
                #    pos2 = item[5].replace('|gen=n|','|')
                #    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],pos,pos2,item[6],item[7],item[8],item[9],item[10])
                #
                # diminutives
                # AQ*
                # refer to freeling new pos tags (enable when using new tags)
                #elif adjdim.search(item[4]):
                #    pos = item[4].replace('AQD','AQV')
                #    pos = pos+'0'
                #    pos2 = item[5].replace('degree=diminutive','degree=evaluative')
                #    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],pos,pos2,item[6],item[7],item[8],item[9],item[10])
                # NC*
                # refer to freeling new pos tags (enable when using new tags)
                #elif noundim.search(item[4]):
                #    pos = item[4].replace('00D','00V')
                #    pos2 = item[5].replace('degree=diminutive','degree=evaluative')
                #    cur_sentence[w] = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3],pos,pos2,item[6],item[7],item[8],item[9],item[10])

                #-----------------------------------------------------------------------------------#
                #
                # ASSIGNING THE RIGHT LEMMA
                #
                # proper nouns
                elif proper.search(item[4]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())
                #
                # numbers
                elif number.search(item[2]):
                    # partitives also change pos
                    if partitive.search(item[4]):
                        cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())
                        cur_sentence[w] = change_pos(cur_sentence[w],'Zd')
                    # percentages also change pos
                    elif percentage.search(item[4]):
                        cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())
                        cur_sentence[w] = change_pos(cur_sentence[w],'Zp')
                    # the rest of numbers
                    else:
                        cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())
                #
                # dates
                elif date.search(item[2]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())
                #
                # errors
                elif strange.search(item[2]):
                    cur_sentence[w] = change_lemma(cur_sentence[w],item[1].lower())

                #-----------------------------------------------------------------------------------#
                #
                # SOLVING UNDEF TAG
                #
                # ambiguous tokens
                if arg_subj.search(item[2]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'que')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'subj')
                elif arg_agent.search(item[1]):
                    p = childhaslemma(cur_sentence,i,'por')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'agnt')
                elif arg_dobj.search(item[2]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'que')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'dobj')
                elif arg_dobj2.search(item[1]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'que')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'dobj')
                elif arg_pobj.search(item[2]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'a')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'pobj')
                elif arg_iobj.search(item[2]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'a')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'iobj')
                elif adjt.search(item[2]) and haschild(cur_sentence,i,'UNDEF') != -1:
                    p = childhaslemma(cur_sentence,i,'que')
                    if (p != -1):
                        cur_sentence[p] = change_func(cur_sentence[p],'adjt')
                #
                # unambiguous tokens
                elif undef.search(item[7]) and undef2subj.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'subj')
                elif undef.search(item[7]) and undef2dobj.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'dobj')
                elif undef.search(item[7]) and undef2adjt.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'adjt')
                elif undef.search(item[7]) and undef2mod.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'mod')
                elif undef.search(item[7]) and undef2aux.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'aux')
                elif undef.search(item[7]) and undef2coor.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'coor')
                elif undef.search(item[7]) and undef2prt.search(item[1]):
                    cur_sentence[w] = change_func(cur_sentence[w],'prt')

            # Sentence fixed. Print fixed sentence
            for w in range(0,len(cur_sentence)):
                print cur_sentence[w]
            print '\n'

            cur_sentence = []
