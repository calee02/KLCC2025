# Method 1: Without function

s = "nI eht raey ,7402 eht dlrow doots no eht knirb fo .noivilbo etamilC egnahc dah dekaerw ,covah gnisuac cihportsatac smrots dna sseltneler .sthguord ehT tnarbiv-ecno seitic won yal ni ,sniur nurrevo yb dliw ,noitategev elihw eht ria saw kciht htiw noitullop dna .riapsed sA ssenkrad llef revo weN kroY ,ytiC eht tsal stnanmer fo noitazilivic deldduh ni dnuorgrednu ,sreknub gnipoh ot evivrus eht soahc .evoba ,erialC a remrof rehcaet denrut ,regnevacs degreme otni eht etalosed steerts htiw reh ytsurt ,god .tuocS yehT detagivan hguorht gnilbmurc sreparcsyks dna denodnaba ,selcihev gnihcraes rof doof dna .seilppus enO lufetaf ,yad erialC delbmuts nopu na dlo ,yrarbil sti swodniw derettahs tub eht tnorf rood ylgnisirprus .tcatni ,edisnI ehs dnuof a evort fo nettogrof :skoob egdelwonk no ,lavivrus ,yrotsih dna namuh .ecneiliser erialC dediced ot rehtag tahw ehs dluoc ,yrrac gniveileb taht egdelwonk saw eht yek ot gnirotser .epoh sA ehs saw tuoba ot ,evael ehs draeh .gnirepmihw gniwolloF eht ,dnuos ehs derevocsid a gnuoy yob gnidih dniheb a .flehs siH eman saw ,oeL dna eh dah neeb enola rof .syad erialC tlef a egrus fo ssenevitcetorp dna detivni mih ot nioj reh dna .tuocS ,rehtegoT yeht demrof na ylekilnu ylimaf dima eht .noitatsaved syaD denrut otni skeew sa eht oirt thguof ot .evivrus yehT ,degarof derahs smaerd fo a retteb ,dlrow dna dnuof ecalos ni eno s'rehtona .ynapmoc hguorhT rieht ,selggurts erialC denrael taht epoh dluoc eb dnuof neve ni eht tsekrad .semit enO ,gnineve sa yeht tas dnuora a gnirekcilf ,erif eht yks denrut ,nosmirc gnilangis a wen .nwad yehT dezilaer yeht erew ton tsuj ;gnivivrus yeht erew gninnigeb ot maerd .niaga ,spahreP ni siht ,espylacopa yeht dluoc dliub a wen dlrow .rehtegot"
rev_s = " ".join([word[::-1] for word in s.split(" ")])
# rev_s = s[::-1]              # Reverse string (operates on individual characters)
print(rev_s)


##### DECORATION ######
print()
print()
print("=" *50)
print("METHOD 2: FUNCTION")
print("=" *50)

# Method 2: Function
def decode_message(sentence):
    words = sentence.split(" ")
    fixed_words = [word[::-1] for word in words]
    return " ".join(fixed_words)

# sample input
print(decode_message("siht si ton a llird"))
print()
# input 1
print(decode_message("nI eht raey ,7402 eht dlrow doots no eht knirb fo .noivilbo etamilC egnahc dah dekaerw ,covah gnisuac cihportsatac smrots dna sseltneler .sthguord ehT tnarbiv-ecno seitic won yal ni ,sniur nurrevo yb dliw ,noitategev elihw eht ria saw kciht htiw noitullop dna .riapsed sA ssenkrad llef revo weN kroY ,ytiC eht tsal stnanmer fo noitazilivic deldduh ni dnuorgrednu ,sreknub gnipoh ot evivrus eht soahc .evoba ,erialC a remrof rehcaet denrut ,regnevacs degreme otni eht etalosed steerts htiw reh ytsurt ,god .tuocS yehT detagivan hguorht gnilbmurc sreparcsyks dna denodnaba ,selcihev gnihcraes rof doof dna .seilppus enO lufetaf ,yad erialC delbmuts nopu na dlo ,yrarbil sti swodniw derettahs tub eht tnorf rood ylgnisirprus .tcatni ,edisnI ehs dnuof a evort fo nettogrof :skoob egdelwonk no ,lavivrus ,yrotsih dna namuh .ecneiliser erialC dediced ot rehtag tahw ehs dluoc ,yrrac gniveileb taht egdelwonk saw eht yek ot gnirotser .epoh sA ehs saw tuoba ot ,evael ehs draeh .gnirepmihw gniwolloF eht ,dnuos ehs derevocsid a gnuoy yob gnidih dniheb a .flehs siH eman saw ,oeL dna eh dah neeb enola rof .syad erialC tlef a egrus fo ssenevitcetorp dna detivni mih ot nioj reh dna .tuocS ,rehtegoT yeht demrof na ylekilnu ylimaf dima eht .noitatsaved syaD denrut otni skeew sa eht oirt thguof ot .evivrus yehT ,degarof derahs smaerd fo a retteb ,dlrow dna dnuof ecalos ni eno s'rehtona .ynapmoc hguorhT rieht ,selggurts erialC denrael taht epoh dluoc eb dnuof neve ni eht tsekrad .semit enO ,gnineve sa yeht tas dnuora a gnirekcilf ,erif eht yks denrut ,nosmirc gnilangis a wen .nwad yehT dezilaer yeht erew ton tsuj ;gnivivrus yeht erew gninnigeb ot maerd .niaga ,spahreP ni siht ,espylacopa yeht dluoc dliub a wen dlrow .rehtegot"))