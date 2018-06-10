# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit


#client = LineClient()
#client = LINE(id='EMAIL HERE', passwd='PASSWORD HERE')
client = LINE('EtgdRunaEfLZyN5f6hzb.ggNCLqZ5irfKOvdzgQfq2W.08Wzj68hDLbzrE6aS/c0LnIvlDLa/jOsGxwekU9qON0=')
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
client.log("Auth Token : " + str(client.authToken))
botStart = time.time()

msg_dict = {}

# Initialize OEPoll with LINE instance
oepoll = OEPoll(client)

mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

keyMessage = """╔═══════════════
║┏━━ೋ• ❄ •ೋ━━━┓
║ ❁ 🛡  кєи кαиєкι! ＢＯＴ  🛡 ❁    
║┗━━ೋ• ❄ •ೋ━━━┛
╠═══════════════
║「ĸeyword」
╠═══════════════
║╔❂͜͡➣「/ѕιderѕ」
║╠❂͜͡➣「/pυвlιc」
║╠❂͜͡➣「/ѕearcнιng」
║╠❂͜͡➣「/newғιтυre」
║╠❂͜͡➣「/cancel」
║╠❂͜͡➣「/aвoυт」
║╚❂͜͡➣「/ĸelυar」
╚═══════════════ """

newMessage ="""⚘ 🐯 new fiture area 🐯 ⚚
❂͜͡☆➣ https://tinyurl.com/newfiture (cek disini)
❂͜͡☆➣ https://tinyurl.com/newfiture2 (cek disini)
❂͜͡☆➣ cυaca「naмa ĸoтa」= cek cuaca kota
❂͜͡☆➣ ѕнolaт「naмa ĸoтa」= cek jadwal sholat di kota
❂͜͡☆➣ cpoѕт 「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa foto
❂͜͡☆➣ cvιd「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa video
❂͜͡☆➣ ѕcreen 「υѕernaмe ιg ĸaмυ」= untuk screenshoot ig kamu
❂͜͡☆➣ loĸaѕι「yang ιngιn ĸaмυ carι」= υnтυĸ мencarι loĸaѕι
❂͜͡☆➣ /lιrιĸ「jυdυl lagυ」= υnтυĸ мencarι lιrιĸ lagυ
❂͜͡☆➣ /lagυ「jυdυl lagυ」= untuk mencari lagu joox
❂͜͡☆➣ ιnғo ѕaya = вυaт lυcυ lυcυ an

ada ιngιn мenyaranĸan ғιтυre? cнaт ĸe http://line.me/ti/p/%40ish7215m"""

sidersMessage =""" 🛡  кєи кαиєкι v2! ＢＯＴ  🛡

⚘ 🐯 cнecĸ ѕιderѕ area 🐯 ⚚
❂͜͡☆➣ ѕeтlaѕтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ vιewlaѕтѕeen = cнecĸ ѕιderѕ
❂͜͡☆➣ ѕeтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ read = cнecĸ ѕιderѕ"""

publicMessage =""" ⚘ 🐯 pυвlιc area 🐯 ⚚
❂͜͡☆➣ creaтor = conтacт peмвυaт вoт
❂͜͡☆➣ apaĸaн 「тeхт yang ιngιn ĸaмυ тanyaĸan」 (ѕeperтι ĸerang ajaιв)
❂͜͡☆➣ ĸedapĸedιp「тeхт yang ιngιn dιĸedap ĸedιpĸan」 = coвa aja
❂͜͡☆➣ doѕa @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ paнala @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ gcreaтor = мenυnjυĸĸan peмвυaт grυp
❂͜͡☆➣ gιnғo = ιnғo grυp
❂͜͡☆➣ ѕpaмтag @ 「naмe」= ѕpaм yang dιтag
❂͜͡☆➣ /ѕpaм: on/oғғ + jυмlaн + ĸaтa = ѕpaм dengan jυмlaн ĸaтa
❂͜͡☆➣ мenтιon all = мenтιon ѕeмυa
❂͜͡☆➣ мenтιon = мenтιon ѕeмυa
❂͜͡☆➣ тag all = мenтιon ѕeмυa
❂͜͡☆➣ тagall = мenтιon ѕeмυa
❂͜͡☆➣ ѕay = coвa aja ĸeтιĸ ѕay"""

searchingMessage =""" ⚘ 🐯 ѕearcнιng area 🐯 ⚚
❂͜͡☆➣ proғιleιg 「υѕernaмe」
❂͜͡☆➣ ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ .ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ wιĸιpedιa 「тeхт」
❂͜͡☆➣ gιмage「тeхт」
❂͜͡☆➣ тr-en 「тeхт」
❂͜͡☆➣ тr-ιd 「тeхт」
❂͜͡☆➣ ιd@en
❂͜͡☆➣ en@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ jp@ιd
❂͜͡☆➣ ιd@тн
❂͜͡☆➣ тн@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ ιd@ar
❂͜͡☆➣ ar@ιd
❂͜͡☆➣ ιd@ĸo
❂͜͡☆➣ ĸo@ιd
❂͜͡☆➣ yт: [jυdυl]
❂͜͡☆➣ ceĸ (тanggal)-(вυlan)-(тaнυn)
❂͜͡☆➣ /ιg 「υѕernaмe」
❂͜͡☆➣ ѕearcнιd: 「ιd lιne」"""

cancelMessage ="""ғιтυr вerѕтaтυѕ oғғlιne!"""

welcomeMessage="""тerιмa ĸaѕιн тelaн мengυndang вoт ιnι! 
ιnvιтe aĸυ ĸe grυp ĸalιan ya :)
⭐ υnтυĸ мengeтaнυι adмιn ĸeтιĸ "creaтor"!
⭐ υnтυĸ мengeтaнυι ғιтυre apa ѕaja darι вoт ιnι ĸeтιĸ "нelp"
⭐ υnтυĸ вoт вeĸerja ѕecara мaхιмal ѕιlaнĸan ιnvιтe creaтor вoт! тнanĸyoυ!❤
"""

meMessage="""⭐ нow тo υѕe ιт::
- !say 「тeхт」
- @say 「тeхт」
- #say 「тeхт」
- $say 「тeхт」
- %say 「тeхт」
- ^say 「тeхт」
- &say 「тeхт」
- *say 「тeхт」
- (say 「тeхт」
- )say 「тeхт」
"""

sayMessage ="""⭐ Kode Baнaѕa ⭐
aғ : Aғrιĸaanѕ
ѕq : Alвanιan
ar : Araвιc
нy : Arмenιan
zн : Cнιneѕe
nl : Dυтcн
ғr : Frencн
de : Gerмan
en : Englιѕн
ιd : Indoneѕιan
ja : Japaneѕe
ĸo : Korean
ιт : Iтalιan
la : Laтιn
pт : Porтυgυeѕe
ro : Roмanιan
rυ : Rυѕѕιan
eѕ : Spanιѕн
тн : Tнaι
vι : Vιeтnaмeѕe
ѕυ : ѕυи∂α 
נω : נαωα
⭐ Tнanĸ Yoυ ⭐
"""

mulai = time.time()
KAC=[client]
mid = client.getProfile().mid

Bots=[mid]
admin=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
owner=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
protectname=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'sticker':False,
    'autoCancel':{"on":True,"members":10},
    "spam":{},
    "detectMention":False,
    "Members":1,
    "wordban":{},
    'leaveRoom':True,
    'likeOn':True,
    'comment1':"Auto Like By http://line.me/ti/p/%40ish7215m",
    'timeline':True,
    'autoAdd':True,
    'atjointicket':True,
    "alwaysRead":True,
    "linkticket":False,
    "cpp":False,
    "cpg":False,
    'message':"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "lang":"JP",
    "comment":"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "commenty":"Auto Like by кєи кαиєкι\n\nhttp://line.me/ti/p/%40ish7215m",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "teman":{},
    "winvite":False,
    "likeOn":True,
    "protection":False,
    "welcomemsg":True,
    "welmsg":" welcome to ",
    "pname":{},
    "pro_name":{},
    "Pap":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "timeRestart": "18000",
    "simiSimi":{},
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
   
hasil = {
    "result":False,
    "posts":False,
    "postInfo":False,
    "liked":{}
    }
    
wordban = {
    "kontol":{},
    "kontl":{},
    "kntl":{},
    "memek":{},
    "anjing":{},
    "njing":{},
    "anjeng":{}
}

setTime = {}
setTime = wait2['setTime']

contact = client.getProfile()
backup = client.getProfile()
profile = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendKontok(self, HelloWorld, midUrang):
      msg = Message()
      msg.contentMetadata = {'mid': midUrang}
      msg.to = HelloWorld
      msg.contentType = 13
      return self.Talk.client.sendMessage(0, msg)
    
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg._from in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg._from]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       client.sendMessage(msg)
    except Exception as error:
       print error

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        msg = Message()
        msg.contentType = 0
        msg.text = text_
        msg.contentMetada = {'MENTION':'{"MENTIONEES":['+aa+']}'}
        client.sendMessage(msg)
    except Exception as error:
        print error
        
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       client.sendMessage(msg)
    except Exception as error:
       print error

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         client.sendMessage(msg)
    except Exception as error:
        print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B nrik"
        s.headers['user-agent'] = 'Mozilla/5.0'
                     
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
                     
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
                     
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&List' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=','')
                    isi += ['youtu.be' + b]
        return isi

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=oepoll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendMessage(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if client.getContact(u).videoProfile != None:
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                                client.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=================================================================================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            oepoll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
        
# Add function to OEPoll
oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    oepoll.trace()
