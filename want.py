# -*- coding: utf-8 -*-
# Thanks for FadhiilRachman and TCR TEAM
# I JUST FORKED
from linepy import *
import time,random,sys,json,codecs,threading,glob,re,datetime
from datetime import timedelta, date
from time import time
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from urllib3 import HTTPConnectionPool
import subprocess,os,requests,goslate,ctypes
import ast
import subprocess
import urllib
import urllib2
import urllib3
import cookielib
import wikipedia
import shutil

#cl = LineClient() ----> Buat Login by QR
cl = LineClient(authToken='Et1fd26gCtgbLdd2jDgb.ggNCLqZ5irfKOvdzgQfq2W.EcY3RGwnjaFPDOgsRiTBxCjdpA9By/UR4Yq00WtS09M=')
cl.log("Auth Token : " + str(cl.authToken))

# Initialize LineChannel with LineClient
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

botStart = time.time()

poll = LinePoll(cl)
creator = ["ud4082219b6754e7b610f84d07d3b436b"]
Qmid = cl.getProfile().mid
KAC = [cl]
Bots = [Qmid]
responsename = cl.getProfile().displayName
mid = cl.getProfile().mid
Bots=[mid]
admin=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
owner=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
protectname=[]

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
❂͜͡☆➣ ιnғo ѕaya = вυaт lυcυ lυcυ an"""

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

contact = cl.getProfile()
backup = cl.getProfile()
profile = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

# =========== BATAS SUCI DEF ========================================== #
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = cl.getProfile().mid
    if myid in nm:    
      nm.remove(myid)
    #print nm
    for mm in nm:
      akh = akh + 6
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 7
      akh = akh + 1
      bb += "@nrik \n"
    aa = (aa[:int(len(aa)-1)])
    text = bb
    try:
       cl.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
       print(error)
    

# Receive messages from LinePoll
def SEND_MESSAGE(op):
    '''
        This is sample for implement BOT in LINE group
        Invite your BOT to group, then BOT will auto accept your invitation
        Thanks for Fadhiil Rachman.
        > hi
        > /author
        > responsename
        > masuk
        > keluar
    '''
    msg = op.message   
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    try:
        if msg.text is None:
            return
  #======================BATAS SC DARI ME===================#
        elif text.lower() == 'me':
            cl.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
        elif text.lower() == 'speed':
            start = time.time()
            cl.sendText(receiver, "Tunggu sebentar...")
            elapsed_time = time.time() - start
            cl.sendText(receiver, "%sdetik" % (elapsed_time))
        elif '/curidp' in text.lower():
            try:
                key = eval(msg.contentMetadata["MENTION"])
                u = key["MENTIONEES"][0]["M"]
                a = cl.getContact(u).pictureStatus
                print(cl.getContact(u))
                cl.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
            except Exception as e:
                print(e)
        elif '/curicover' in text.lower():
            try:
                key = eval(msg.contentMetadata["MENTION"])
                u = key["MENTIONEES"][0]["M"]
                a = cl.getProfileCoverURL(mid=u)
                print(a)
                cl.sendImageWithURL(receiver, a)
            except Exception as e:
                print(e)
        elif text.lower() == 'tagall':
            group = cl.getGroup(msg.to)
            nama = [contact.mid for contact in group.members]
            nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
            if jml <= 100:
                mention(msg.to, nama)
            if jml > 100 and jml < 200:
                for i in range(0, 100):
                    nm1 += [nama[i]]
                mention(msg.to, nm1)
                for j in range(101, len(nama)):
                    nm2 += [nama[j]]
                mention(msg.to, nm2)
            if jml > 200 and jml < 300:
                for i in range(0, 100):
                    nm1 += [nama[i]]
                mention(msg.to, nm1)
                for j in range(101, 200):
                    nm2 += [nama[j]]
                mention(msg.to, nm2)
                for k in range(201, len(nama)):
                    nm3 += [nama[k]]
                mention(msg.to, nm3)
            if jml > 300 and jml < 400:
                for i in range(0, 100):
                    nm1 += [nama[i]]
                mention(msg.to, nm1)
                for j in range(101, 200):
                    nm2 += [nama[j]]
                mention(msg.to, nm2)
                for k in range(201, len(nama)):
                    nm3 += [nama[k]]
                mention(msg.to, nm3)
                for l in range(301, len(nama)):
                    nm4 += [nama[l]]
                mention(msg.to, nm4)
            if jml > 400 and jml < 501:
                for i in range(0, 100):
                    nm1 += [nama[i]]
                mention(msg.to, nm1)
                for j in range(101, 200):
                    nm2 += [nama[j]]
                mention(msg.to, nm2)
                for k in range(201, len(nama)):
                    nm3 += [nama[k]]
                mention(msg.to, nm3)
                for l in range(301, len(nama)):
                    nm4 += [nama[l]]
                mention(msg.to, nm4)
                for m in range(401, len(nama)):
                    nm5 += [nama[m]]
                mention(msg.to, nm5)             
            cl.sendText(receiver, "Members :"+str(jml))
            
        elif text.lower() == 'hi':
            contact = cl.getContact(sender)
            cl.log('[%s] %s' % (contact.displayName, text))
            cl.sendMessage(msg.to, 'Hi too! How are you?')
        elif text.lower() == '/author':
            contact = cl.getContact(sender)
            cl.log('[%s] %s' % (contact.displayName, text))
            cl.sendMessage(msg.to, 'My author is linepy')            
        elif text.lower() == "responsename":
            cl.sendMessage(msg.to,responsename)
        #elif text.lower() in ["/keluar"]:
         #      ki.leaveGroup(msg.to)
          #     kk.leaveGroup(msg.to)
          #     kc.leaveGroup(msg.to)
          #     km.leaveGroup(msg.to)
        #elif text.lower() in ["masuk"]:
         #       G = cl.getGroup(msg.to)
         #       ginfo = cl.getGroup(msg.to)
          #      G.preventedJoinByTicket = False
           #     cl.updateGroup(G)
            #    invsend = 0
             #   Ticket = cl.reissueGroupTicket(msg.to)
              #  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
             #   kk.acceptGroupInvitationByTicket(msg.to,Ticket)
             #   kc.acceptGroupInvitationByTicket(msg.to,Ticket)
             #   km.acceptGroupInvitationByTicket(msg.to,Ticket)
             #   G = cl.getGroup(msg.to)
             #   G.preventedJoinByTicket = True
             #   cl.updateGroup(G)
             #   G.preventedJoinByTicket(G)
             #   cl.updateGroup(G)
            
    except Exception as e:
        cl.log("[SEND_MESSAGE] ERROR : " + str(e))
    
# Auto join if BOT invited to group
#def NOTIFIED_INVITE_INTO_GROUP(op):
 #   try:
  #      cl.acceptGroupInvitation(op.param1)
   #     ki.acceptGroupInvitation(op.param1)
    #    kk.acceptGroupInvitation(op.param1)
     #   kc.acceptGroupInvitation(op.param1)
      #  km.acceptGroupInvitation(op.param1)
    #except Exception as e:
     #   cl.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
#def NOTIFIED_KICKOUT_FROM_GROUP(op):
 #   try:
  #      if op.param2 not in Bots:
   #         random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
    #    else:
     #       pass
    #except Exception as e:
     #   cl.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

# Add function to LinePoll
#poll.addOpInterruptWithDict({
 #   OpType.SEND_MESSAGE: SEND_MESSAGE,
  #  OpType.NOTIFIED_KICKOUT_FROM_GROUP: NOTIFIED_KICKOUT_FROM_GROUP,
   # OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
#})

while True:
    poll.trace()
