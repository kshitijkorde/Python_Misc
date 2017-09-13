#!/usr/bin/python
import re
f = open("small.txt")
result = re.findall(r'\[\w+\]+',f.read())
for token in result:
	print token

# Contents of small.txt

# dnwtsgywerfamfv[gwrhdujbiowtcirq]bjbhmuxdcasenlctwgh
# rnqfzoisbqxbdlkgfh[lwlybvcsiupwnsyiljz]kmbgyaptjcsvwcltrdx[ntrpwgkrfeljpye]jxjdlgtntpljxaojufe
# jgltdnjfjsbrffzwbv[nclpjchuobdjfrpavcq]sbzanvbimpahadkk[yyoasqmddrzunoyyk]knfdltzlirrbypa
# vvrchszuidkhtwx[ebqaetowcthddea]cxgxbffcoudllbtxsa
# olgvwasskryjoqpfyvr[hawojecuuzobgyinfi]iywikscwfnlhsgqon
# jlzynnkpwqyjvqcmcbz[fdjxnwkoqiquvbvo]bgkxfhztgjyyrcquoiv[xetgnqvwtdiuyiyv]zyfprefpmvxzauur
# vjqhodfzrrqjshbhx[lezezbbswydnjnz]ejcflwytgzvyigz[hjdilpgdyzfkloa]mxtkrysovvotkuyekba
# xjmkkppyuxybkmzya[jbmofazcbdwzameos]skmpycixjqsagnzwmy
# zeebynirxqrjbdqzjav[cawghcfvfeefkmx]xqcdkvawumyayfnq[qhhwzlwjvjpvyavtm]sbnvwssglfpyacfbua[wpbknuubmsjjbekkfy]icimffaoqghdpvsbx
# enupgggxsmwvfdljoaj[qlfmrciiyljngimjh]qkjawvmtnvkidcclfay[bllphejvluylyfzyvli]heboydfsgafkqoi

# # Output
# [gwrhdujbiowtcirq]
# [lwlybvcsiupwnsyiljz]
# [ntrpwgkrfeljpye]
# [nclpjchuobdjfrpavcq]
# [yyoasqmddrzunoyyk]
# [ebqaetowcthddea]
# [hawojecuuzobgyinfi]
# [fdjxnwkoqiquvbvo]
# [xetgnqvwtdiuyiyv]
# [lezezbbswydnjnz]
# [hjdilpgdyzfkloa]
# [jbmofazcbdwzameos]
# [cawghcfvfeefkmx]
# [qhhwzlwjvjpvyavtm]
# [wpbknuubmsjjbekkfy]
# [qlfmrciiyljngimjh]
# [bllphejvluylyfzyvli]

