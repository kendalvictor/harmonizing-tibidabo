#! /usr/bin/gawk -f 

BEGIN { i=0; ct=0; OFS="\t"; }

NF>0 {
    # load sentence
    sent[++i]=$0;
    clt[i]=ct;
    if (match($5,"\\+")) {
        n = split($5,k,"\\+")
        ct += (n-1);
    }
    next;
}

NF==0 {
    # sentence loaded, output it, fixing clitics

    if (!ct) { 
        # output untouched sentence
        for (j=1; j<=i; j++) print sent[j];
        print "";
    }

    else { 
        # fix sentence
        for (j=1; j<=i; j++) {
            $0 = sent[j];
            if (match($5,"\\+")) {
                # split VMN+PP
                n=split($5,tags,"\\+");
                if (n==3) {
                    # DOUBLE CLITICS: impedirselo
                    p=match($2,"selo$")
                    verb=substr($2,1,p-1)
                    c1="se"
                    c2="lo"
                    # print verb
                    print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                    # print clitics
                    # clitic 1
                    print shift(j)+1, "se", "se", "p", tags[2], "pos=pronoun|person=3|gen=c|num=c", shift(j), "clitic", "_","_",$11
                    # clitic 2
                    print shift(j)+2, "lo", "lo", "p", tags[3], "pos=pronoun|person=3|gen=c|num=c", shift(j), "clitic", "_","_",$11
                }
                else if (n==2) {
                    # SINGLE CLITICS: tutearte
                    p=match($2,"(la|las|le|les|lo|los|me|nos|os|te|se)$")
                    verb=substr($2,1,p-1)
                    c=substr($2,p)
                    # la
                    if (p==match($2,/la$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "lo", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=f|num=s|case=accusative", shift(j), "dobj", "_","_",$11
                    }
                    # las
                    else if (p==match($2,/las$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "lo", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=f|num=p|case=accusative", shift(j), "dobj", "_","_",$11
                    }
                    # le
                    else if (p==match($2,/le$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "le", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=c|num=s|case=dative", shift(j), "iobj", "_","_",$11
                    }
                    # les
                    else if (p==match($2,/les$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "le", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=c|num=p|case=dative", shift(j), "iobj", "_","_",$11
                    }
                    # lo
                    else if (p==match($2,/lo$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "lo", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=m|num=s|case=accusative", shift(j), "dobj", "_","_",$11
                    }
                    # los
                    else if (p==match($2,/los$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "lo", "p", tags[2], "pos=pronoun|type=personal|person=3|gen=m|num=p|case=accusative", shift(j), "dobj", "_","_",$11
                    }
                    # me
                    else if (p==match($2,/me/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "me", "p", tags[2], "pos=pronoun|type=personal|person=1|gen=c|num=s", shift(j), "clitic", "_","_",$11
                    }
                    # nos
                    else if (p==match($2,/nos/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "nos", "p", tags[2], "pos=pronoun|type=personal|person=1|gen=c|num=p", shift(j), "clitic", "_","_",$11
                    }
                    # os
                    else if (p==match($2,/os/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "os", "p", tags[2], "pos=pronoun|type=personal|person=2|gen=c|num=p", shift(j), "clitic", "_","_",$11
                    }
                    # te
                    else if (p==match($2,/te$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "te", "p", tags[2], "pos=pronoun|type=personal|person=2|gen=c|num=s", shift(j), "clitic", "_","_",$11
                    }
                    # se
                    else if (p==match($2,/se$/)) {
                        # print verb
                        print shift(j), verb, $3, $4, tags[1], $6, shift($7), $8, $9,"_",$11
                        # print clitic
                        print shift(j)+1, c, "se", "p", tags[2], "pos=pronoun|person=3|gen=c|num=c", shift(j), "clitic", "_","_",$11
                    }
                    else {
                        print "ERROR - "$5,$2 >"/dev/stderr";
                        exit
                    }

                }
                else {
                    print "ERROR - "$5,$2 >"/dev/stderr"; 
                    exit
                }
            }
            else {
                $1=shift($1);
                $7=shift($7);
                print;
            }
        }
        print "";
    }

    # prepare for next sentence
    delete sent;
    delete clt;
    i=0;
    ct=0;
}


function shift(n) {
    return n+clt[n];
}
