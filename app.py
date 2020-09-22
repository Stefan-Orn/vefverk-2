from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/a-hluti")
def ahluti():
    return render_template("kennitala.html")

@app.route("/ktsida/<kt>")
def kennisum(kt):
    summa = 0
    for i in kt:
        summa = int(i) + summa
    return render_template("ktsum.html" , kt=kt , summa=summa)
#Listi 
frettir = [
    ["0","Þröstur byrjar 3 heimstyjuöldina","Það var góður morgunn segir Gosi Fúsason. En það átti fljótt eftir að breytast. Ég var að hella upp á morgunkaffið mitt, segir Gosi, Þegar að Þröstur týstir í garðinum mínu. Þetta eina týst var nóg til þess að Gosi hafði samband við stærstu ríki heims og bað það um að byrja þriðju heimstyrjuöldina.","Björg Ólafs"], #id, title, content
    ["1","Ómerkileg Frétt","Það er ekkert merkilegt um að vera hér en samt sem áður skrifa ég þessa frétt fyrir áðdáendur mína.","Hrannar Mímir Sævarsson"],
    ["2","Iceland Air aflýsir nánast öllum flugferðum","20 flug­ferðum Icelanda­ir hef­ur verið af­lýst í dag og er aðeins ein ferð á áætl­un hjá Icelanda­ir en sú er frá Kaup­manna­höfn. Auk þess flaug Icelanda­ir til lands­ins frá Bost­on snemma í morg­un. Ekk­ert annað flug­fé­lag hef­ur af­lýst ferðum sín­um til eða frá Kefla­vík­ur­flug­velli í dag, sam­kvæmt upp­lýs­ing­um á vefsíðu Isa­via. Þannig fljúga Luft­hansa, Wizz Air, Air Ice­land Conn­ect, Easy Jet, SAS og Air Baltic sam­kvæmt áætl­un það sem eft­ir lif­ir dags.","Eggert Jóhannesson"],
    ["3","Toyota Þróar og smíðar jeppa til Tunglferða","Toyota er vant því úr sögu sinni að setja markið hátt en næsta far­ar­tæki bílsmiðjunn­ar með færni til ut­an­veg­arakst­urs er veru­lega frá­brugðið fyrri bíl­um Toyota. Er þar um að ræða jeppa til ferðalaga á tungl­inu sem verið er að þróa í sam­starfi við japönsku geim­ferðastofn­un­ina. Toyota hann­ar og smíðar tungljepp­ann en JAXA sér um að koma hon­um á braut í geim­skoti, sem áætlað er eft­ir ára­tug, 2030. Á tungl­inu verður jepp­inn ferðast um yf­ir­borð hans við vís­inda­rann­sókn­ir og mæl­ing­ar. Þar ætla Jap­an­ir að reisa þorp sem hugsað er til langvar­andi viðveru vís­inda­manna. Verður jepp­inn nýtt­ur þaðan. Áform þessi eru skammt á veg kom­in en tungljepp­inn er einnig hugsaður til rann­sókna á reiki­stjörn­unni Mars síðar meir. Jafnþrýsti­klefi verður í jepp­an­um og því munu geim­far­ar geta af­klæðst fyr­ir­ferðamikl­um geimbún­ingn­um inni í bíln­um og at­hafnað sig þar án hans á ferð. Þrýsti­klef­inn verður 13 rúm­metr­ar og er þar rými fyr­ir tvær mann­eskj­ur til lang­ferða og tvær til viðbót­ar í neyð. Bíll­inn verður raf­knú­inn. Ork­una fær hann úr geisl­um sól­ar­inn­ar sem sól­skerm­ur mun fanga. JAXA áform­ar að senda menn til tungls­ins á fjórða ára­tugn­um en und­an­fari þess verður að skjóta jepp­an­um þangað árið 2029. Hann er á stærð við smárútu, sex metra lang­ur, 5,2 metr­ar á breidd og 3,8 metr­ar í hæsta punkt. Eins og fyrr seg­ir hafa Jap­an­ir gefið sér ára­tug í að koma starf­semi sinni á tungl­inu á kopp­inn. Jepp­inn hef­ur fengið nafnið Lun­ar Cruiser sem teng­ir sterkt við al­menna og bíla­fram­leiðslu Toyota og fræg­asta jeppa þess, hinn fjór­hjóla­drifna Land Cruiser. Þró­un­ar­jepp­inn verður í fyrstu miðaður við íveru tveggja geim­fara og haf­ur­task þeirra til 10.000 kíló­metra rann­sókn­ar­leiðang­urs um yf­ir­borð tungls­ins.","Enginn Höfundur"],
    ["4","Tveir virki­lega já­kvæðir í veiðinni","Áfram með upp­gjör laxveiðitíma­bils­ins. Það er komið að Tomma í Veiðiport­inu og Hilmi Víg­lunds­syni, leiðsögu­manni í Vopnafirði. Tommi, eða Tóm­as Skúla­son, byrj­ar. Sum­arið var eitt það besta sem ég hef upp­lifað hvað varðar veiði. Laxá í Mý­vatns­sveit tók vel á móti mér snemma sum­ars þrátt fyr­ir mik­inn kulda. Þing­valla­vatnið var frá­bært en það er áhyggju­efni að sjá þó nokkuð marga 80 cm + fiska mjó­slegna og í vond­um hold­um um miðjan júlí. Lík­lega mun­um við sjá meira af því á næstu árum því ætið fyr­ir urriðann fer minnk­andi að mínu mati sem mun leiða til þess að eldri og hæg­ari fisk­ar munu vesl­ast upp og við hætt­um að sjá þykka og fal­lega 85-90 cm fiska. Laxveiðin var ágæt hjá mér og hef ég sjald­an landað jafn mörg­um löx­um. En maður heyrði samt mikið um að það væri lít­il taka í fisk­in­um þrátt fyr­ir góð skil­yrði og nóg af fiski í sum­um ám. Von­brigðin voru þau að fá ekki vör­ur send­ar þegar far­ald­ur­inn byrjaði og vont að þurfa að vísa mönn­um frá því það seld­ist allt og mikið af vör­um seld­ist hrein­lega upp strax í apríl. En það var lúxusvanda­mál sem leyst­ist að lok­um og ég veit að all­ar veiðibúðir gerðu það gott í sum­ar. En ástandið er ekki gott fyr­ir leigu­taka/​veiðileyf­a­sala Bænd­ur og leigu­tak­ar þurfa held­ur bet­ur að funda og gera plan fyr­ir næsta ár því ef þetta ástand held­ur áfram með tak­mörk­un­um á flæði fólks til lands­ins munu fá fyr­ir­tæki lifa það af. Ann­ars fær þetta sum­ar 9 í ein­kunn og fer ég vel bratt­ur inn í vet­ur­inn enda full­ur af minn­ing­um eft­ir marga frá­bæra túra á þessu ári. Hilm­ir Víg­lunds­son í Vopnafirði er ekk­ert nema já­kvæðnin. Hér er hans svar: Sum­arið er alltaf gott í Vopnafirðinum að því leyti að þar er ALLTAF vatn og fisk­ar á bil­inu 5 til 25 pund, þú færð allt í Vopnafirðinum: Góða þjón­ustu, fal­leg­ar laxveiðiár og ein­stakt lands­lag við Selá og Hofsá. Ann­ars var þetta sum­ar bara ágætt veiðilega séð. Hofsá klár­lega að rífa sig í gang eft­ir mörg erfið ár. Selá bara flott enda aðstæður fyr­ir smá­flug­ur og þær breyt­ing­ar sem gerðar hafa verið í Selá voru fá­rán­lega góðar al­veg til 1. sept­em­ber. Von­brigðin eru klár­lega Víðidal­ur, Vatns­dal­ur, Þistil­fjörður og svo marg­ar ár á Vest­ur­landi. Ég fór í Jöklu í fyrsta skiptið í sum­ar og það var al­veg frá­bært. Er mjög spenn­andi dæmi og verður rosa­leg á ef vel tekst til. Mest spenn­andi verk­efni á Íslandi klár­lega. Ég sé ekki neitt sem þarf að breyt­ast nema að gefa ekki út leyfi til lax­eld­is á Íslandi á þess­ari og næstu öld.","Eggert Skúlason"],
       
]



@app.route("/b-hluti")
def bhluti():
    return render_template("frettir.html", frettir= frettir)

@app.route("/frett/<int:id>")
def news(id):
    return render_template("frett.html", frett=frettir[id], nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def internalerror(error):
    return render_template("servererror.html"), 500

if __name__ == "__main__":
    app.run()
    #app.run(debug=True, use_reloader=True)