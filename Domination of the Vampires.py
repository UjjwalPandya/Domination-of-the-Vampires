import random


class SPACE:
   def __init__(self):
      type = space

      
"""
co = Create Obstacle
ce = Clear Evidence
oc = Obstacle Creator
xp = Experience
"""

class Snag(SPACE):
   def __init__(self,name,stype,co,cost,obstaclecost,ce,price,o1,o2,o3,o4,o5,oc,color,obstacles):
      self.name = name
      self.stype = stype
      self.co = co
      self.oc = oc
      self.color = color
      self.cost = int(cost)
      self.obstaclecost = int(obstaclecost)
      self.ce = int(ce)
      self.price = int(price)
      self.o1 = int(o1)
      self.o2 = int(o2)
      self.o3 = int(o3)
      self.o4 = int(o4)
      self.o5 = int(o5)
      self.obstacles = int(obstacles)

      
class Boxers(SPACE):
   def __init__(self,name,stype,co,oc):
      self.name = name
      self.stype = stype
      self.co = co
      self.oc = oc
      self.cost = float(200)
      self.bx1 = float(25)
      self.bx2 = float(50)
      self.bx3 = float(100)
      self.bx4 = float(200)
      self.ce = float(100)

      
class Fighters(SPACE):
   def __init__(self,name,stype,co,oc):
      self.name = name
      self.stype = stype
      self.co = co
      self.oc = oc
      self.cost = float(150)
      self.f1 = float(4)
      self.f2 = float(10)
      self.ce = float(75)

      
class Policecheckspace(SPACE):
   def __init__(self,name,stype,co,pc):
      self.name = name
      self.stype = stype
      self.co = co
      self.pc = pc

      
class Freespace(SPACE):
   def __init__(self,name,stype,co):
      self.name = name
      self.stype = stype
      self.co = co
      
      
class Gotojailspace(SPACE):
   def __init__(self,name,stype,co):
      self.name = name
      self.stype = stype
      self.co = co

      
class Friendspace(SPACE):
   def __init__(self,name,stype,co):
      self.name = name
      self.stype = stype
      self.co = co

      
class Opportunityspace(SPACE):
   def __init__(self,name,stype,co):
      self.name = name
      self.stype = stype
      self.co = co

      
class FriendCard:
   def __init__(self,description,move,collect,pay,payperobstacle,getoutofjailfree,gotojail,collect50):
      self.description = description
      self.move = int(move)
      self.collect = int(collect)
      self.pay = int(pay)
      self.payperobstacle = int(payperobstacle)
      self.getoutofjailfree = getoutofjailfree
      self.gotojail = gotojail
      self.collect50 = collect50

      
class OpportunityCard:
   def __init__(self,description,move,collect,pay,payperobstacle,getoutofjailfree,gotojail,moveback):
      self.description = description
      self.move = int(move)
      self.collect = int(collect)
      self.pay = int(pay)
      self.payperobstacle = int(payperobstacle)
      self.getoutofjailfree = getoutofjailfree
      self.gotojail = gotojail
      self.moveback = moveback

      
class Player:
   def __init__(self,name,boardpos,xp,jailcards,jailtime,droll,piece,doublesacc,user):
      self.name = str(name)
      self.boardpos = int(boardpos)
      self.xp = int(xp)
      self.snglist = [[],[],[],[],[],[],[],[]]
      self.boxlist = []
      self.ftlist = []
      self.jailcards = int(jailcards)
      self.jailtime = int(jailtime)
      self.droll = int(droll)
      self.piece = piece
      self.doublesacc = int(doublesacc)
      self.user = int(user)
   def addsnag(self,newsng):
      newsng.oc = self.name
      self.xp = self.xp - newsng.cost
      gotsng = 0
      while gotsng == 0:
         if isinstance(newsng,Snag):
            if newsng.color == "darkblue":
               addindex = 0
            if newsng.color == "green":
               addindex = 1
            if newsng.color == "yellow":
               addindex = 2
            if newsng.color == "red":
               addindex = 3
            if newsng.color == "orange":
               addindex = 4
            if newsng.color == "pink":
               addindex = 5
            if newsng.color == "lightblue":
               addindex = 6
            if newsng.color == "purple":
               addindex = 7
            self.snglist[addindex].append(newsng)
            gotsng = 1
         if isinstance(newsng,Boxers):
            self.boxlist.append(newsng)
            gotsng = 1
         if isinstance(newsng,Fighters):
            self.ftlist.append(newsng)
            gotsng = 1
      for colorlist in self.snglist:      #problem? indenting?
         if len(colorlist) == 2:
            for sng in colorlist:
               if sng.color == "purple":
                  colorlist.append("dominated")
                  break
               if sng.color == "darkblue":
                  colorlist.append("dominated")
                  break
         if len(colorlist) == 3:
            if "dominated" not in colorlist:
               colorlist.append("dominated")
               break
   def createobstacle(self,modsng):
      for colorlist in self.snglist:
         for sng in colorlist:
            if modsng.name == sng.name:
               sng.obstacles += 1
   def cesng(self,modsng):
      self.xp += modsng.ce
      modsng.oc = "Silas"
      for colorlist in self.snglist:
         for sng in colorlist:
            if modsng.name == sng.name:
               colorlist.remove(sng)
      for box in boxlist:
         if modsng.name == box.name:
            boxlist.remove(box)
      for ft in ftlist:
         if modsng.name == ft.name:
            ftlist.remove(ft)

            
            
"""
All the Characters and Names are from the fictional TV Series 'The Vampire Diaries'
"""            

class Board:
   def __init__(self,players,playerpiece):
      self.playerlist = []
      freecharacters = ["Stefan Salvatore","Damon Salvatore","Niklaus Mikleson","Elijah Mikleson","Kol Mikleson","Hayley Marshal","Katherine Pierce","Fin Mikleson"]
      for piece in freecharacters:
         if playerpiece == piece:
            freecharacters.remove(piece)
      user = Player("HUNTER",0,1500,0,0,0,playerpiece,0,1)
      self.playerlist.append(user)
      for i in range(1,int(players)+1):
         playernum = i+1
         comppiece = random.choice(freecharacters)
         freecharacters.remove(comppiece)
         print(str(comppiece))
         newplayer = Player(str("HUNTER "+str(playernum)),0,1500,0,0,0,comppiece,0,0)
         self.playerlist.append(newplayer)
         self.boardlist = []
      gospace = Freespace("PASS GO","freespace",1)
      self.boardlist.append(gospace)
      mystic = Snag("Mystic Falls","snag",2,60,50,30,2,10,30,90,160,250,"Silas","purple",0)
      self.boardlist.append(mystic)
      fs1 = Friendspace("Friends","friendspace",3)
      self.boardlist.append(fs1)
      orleans = Snag("New Orleans","snag",4,60,50,30,4,20,60,180,320,450,"Silas","purple",0)
      self.boardlist.append(orleans)
      police = Policecheckspace("Police Check","policecheck",5,200)
      self.boardlist.append(police)
      x1 = Boxers("Street Boxers","boxers",6,"Silas")
      self.boardlist.append(x1)
      grill = Snag("Mystic Grill","snag",7,100,50,50,6,30,90,270,400,550,"Silas","lightblue",0)
      self.boardlist.append(grill)
      opportunity1 = Opportunityspace("Opportunity","opportunityspace",8)
      self.boardlist.append(opportunity1)
      whitmore = Snag("Whitmore College","snag",9,100,50,50,6,30,90,270,400,550,"Silas","lightblue",0)
      self.boardlist.append(whitmore)
      georgia = Snag("Georgia Grill","grill",10,120,50,60,8,40,100,300,450,600,"Silas","lightblue",0)
      self.boardlist.append(georgia)
      jailspace = Freespace("Jail","freespace",11)
      self.boardlist.append(jailspace)
      salvatore = Snag("Salvatore Boarding House","snag",12,140,100,70,10,50,150,450,625,750,"Silas","pink",0)
      self.boardlist.append(salvatore)
      ft1 = Fighters("Street Fighters","fighters",13,"Silas")
      self.boardlist.append(ft1)
      lockwood = Snag("Lockwood Mansion","snag",14,140,100,70,10,50,150,450,625,750,"Silas","pink",0)
      self.boardlist.append(lockwood)
      virginia = Snag("Virginia","snag",15,160,100,80,12,60,180,500,700,900,"Silas","pink",0)
      self.boardlist.append(virginia)
      x2 = Boxers("Ring Boxers","boxers",16,"Silas")
      self.boardlist.append(x2)
      mikleson = Snag("Mikleson Mansion","snag",17,180,100,90,14,70,200,550,750,950,"Silas","orange",0)
      self.boardlist.append(mikleson)
      fs2 = Friendspace("Friends","friendspace",18)
      self.boardlist.append(fs2)
      italy = Snag("Italy","snag",19,180,100,90,14,70,200,550,750,950,"Silas","orange",0)
      self.boardlist.append(italy)
      newyork = Snag("New York","snag",20,200,100,100,16,80,200,600,800,1000,"Silas","orange",0)
      self.boardlist.append(newyork)
      noman = Freespace("No Man's Land","freespace",21)
      self.boardlist.append(noman)
      ball = Snag("Mystic Ball","snag",22,220,150,110,18,90,250,700,875,1050,"Silas","red",0)
      self.boardlist.append(ball)
      opportunity2 = Opportunityspace("Opportunity","opportunityspace",23)
      self.boardlist.append(opportunity2)
      belgium = Snag("Belgium","snag",24,220,150,110,18,90,250,700,875,1050,"Silas","red",0)
      self.boardlist.append(belgium)
      bulgeria = Snag("Bulgeria","snag",25,240,150,120,20,100,300,750,925,1100,"Silas","red",0)
      self.boardlist.append(bulgeria)
      x3 = Boxers("Free Boxers","boxers",26,"Silas")
      self.boardlist.append(x3)
      pacific = Snag("Pacific","snag",27,260,150,130,22,110,330,800,975,1150,"Silas","yellow",0)
      self.boardlist.append(pacific)
      francisco = Snag("San Francisco","snag",28,260,150,130,22,110,330,800,975,1150,"Silas","yellow",0)
      self.boardlist.append(francisco)
      ft2 = Fighters("Ring Fighters","fighters",29,"Silas")
      self.boardlist.append(ft2)
      jersey = Snag("New Jersey","snag",30,280,150,140,24,120,360,850,1025,1200,"Silas","yellow",0)
      self.boardlist.append(jersey)
      gojail = Gotojailspace("Go To Jail","gotojailspace",31)
      self.boardlist.append(gojail)
      atlanta = Snag("Atlanta","snag",32,300,200,150,26,130,390,900,1100,1275,"Silas","green",0)
      self.boardlist.append(atlanta)
      ncarol = Snag("North Carolina","snag",33,300,200,150,26,130,390,900,1100,1275,"Silas","green",0)
      self.boardlist.append(ncarol)
      fs3 = Friendspace("Friends","friendspace",34)
      self.boardlist.append(fs3)
      pennave = Snag("Pennsylvania Ave","snag",35,320,200,160,28,150,450,1000,1200,1400,"Silas","green",0)
      self.boardlist.append(pennave)
      x4 = Boxers("Smart Boxers","boxers",36,"Silas")
      self.boardlist.append(x4)
      opportunity3 = Opportunityspace("Opportunity","opportunityspace",37)
      self.boardlist.append(opportunity3)
      vine = Snag("Vinewood","snag",38,350,200,175,35,175,500,1100,1300,1500,"Silas","darkblue",0)
      self.boardlist.append(vine)
      weaponary = Policecheckspace("Weaponary Check","policecheckspace",39,75)
      self.boardlist.append(weaponary)
      cemetary = Snag("Lockwood Cemetary","snag",40,400,200,200,50,200,600,1400,1700,2000,"Silas","darkblue",0)
      self.boardlist.append(cemetary)
      self.fslist = []
      fsdesc1 = "DESTROYED ENEMY BUNKER. COLLECT 50 xp FROM EVERY PLAYER"
      f1 = FriendCard(fsdesc1,0,0,0,0,0,0,50)
      self.fslist.append(f1)
      fsdesc2 = "RECEIVE FOR CIVIL SERVICES 25 xp"
      f2 = FriendCard(fsdesc2,0,10,0,0,0,0,0)
      self.fslist.append(f2)
      fsdesc3 = "ADVANCE TO GO, COLLECT 200 xp "
      f3 = FriendCard(fsdesc3,1,0,0,0,0,0,0)
      self.fslist.append(f3)
      fsdesc4 = "HOSPITALIZED, PAY 100 xp"
      f4 = FriendCard(fsdesc4,0,0,100,0,0,0,0)
      self.fslist.append(f4)
      fsdesc5 = "INJURED. PAY 50 xp as fee"
      f5 = FriendCard(fsdesc5,0,0,50,0,0,0,0)
      self.fslist.append(f5)
      fsdesc6 = "GET OUT OF JAIL FREE CARD"
      f6 = FriendCard(fsdesc6,0,0,0,0,1,0,0)
      self.fslist.append(f6)
      fsdesc7 = "RECIEVED FROM CIVILIANS 45 xp"
      f7 = FriendCard(fsdesc7,0,45,0,0,0,0,0)
      self.fslist.append(f7)
      fsdesc8 = "YOU INHERIT 100 xp"
      f8 = FriendCard(fsdesc8,0,100,0,0,0,0,0)
      self.fslist.append(f8)
      fsdesc9 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT 200 xp"
      f9 = FriendCard(fsdesc9,0,0,0,0,0,1,0)
      self.fslist.append(f9)
      fsdesc10 = "TACKLED ENEMY'S TRAP. COLLECT 100 xp"
      f10 = FriendCard(fsdesc10,0,100,0,0,0,0,0)
      self.fslist.append(f10)
      fsdesc11 = "YOU HAVE CONQUERED A LOCAL DON. COLLECT 10 xp"
      f11 = FriendCard(fsdesc11,0,10,0,0,0,0,0)
      self.fslist.append(f11)
      fsdesc12 = "HITMAN FUND MATURES. COLLECT 100 xp"
      f12 = FriendCard(fsdesc12,0,100,0,0,0,0,0)
      self.fslist.append(f12)
      fsdesc13 = "YOU ARE ASSESSED FOR OBSTACLE COLLCECTION. 40 xp PER OBSTACLE."
      f13 = FriendCard(fsdesc13,0,0,0,40,0,0,0)
      self.fslist.append(f13)
      fsdesc14 = "ADVANCE RECIEVED FROM SILAS. COLLECT 200 xp"
      f14 = FriendCard(fsdesc14,0,200,0,0,0,0,0)
      self.fslist.append(f14)
      fsdesc15 = "YOU HELPED MOB. COLLECT 20 xp"
      f15 = FriendCard(fsdesc15,0,20,0,0,0,0,0)
      self.fslist.append(f15)
      self.opportunitylist = []
      fdesc1 = "ADVANCE TO BULGERIA. IF YOU PASS GO, COLLECT 200 xp"
      f1 = OpportunityCard(fdesc1,25,0,0,0,0,0,0)
      self.opportunitylist.append(f1)
      fdesc2 = "YOU ARE ASSESSED FOR OBSTACLE COLLCECTION. 40 xp PER OBSTACLE."
      f2 = OpportunityCard(fdesc2,0,0,0,40,0,0,0)
      self.opportunitylist.append(f2)
      fdesc3 = "GET OUT OF JAIL FREE CARD"
      f3 = OpportunityCard(fdesc3,0,0,0,0,1,0,0)
      self.opportunitylist.append(f3)
      fdesc4 = "ADVANCE TO GO."
      f4 = OpportunityCard(fdesc4,1,0,0,0,0,0,0)
      self.opportunitylist.append(f4)
      fdesc5 = "ADVANCE TO SALVATORE BOARDING HOUSE. IF YOU PASS GO, COLLECT 200 xp"
      f5 = OpportunityCard(fdesc5,12,0,0,0,0,0,0)
      self.opportunitylist.append(f5)
      fdesc6 = "HELPING CIVILIANS 15 xp"
      f6 = OpportunityCard(fdesc6,0,0,15,0,0,0,0)
      self.opportunitylist.append(f6)
      fdesc7 = "SILAS PAYS YOU DIVIDEND OF 50 xp"
      f7 = OpportunityCard(fdesc7,0,50,0,0,0,0,0)
      self.opportunitylist.append(f7)
      fdesc8 = "YOUR HUNTER FUND MATURES. COLLECT 100 xp"
      f8 = OpportunityCard(fdesc8,0,100,0,0,0,0,0)
      self.opportunitylist.append(f8)
      fdesc9 = "TAKE A WALK ON THE LOCKWOOD CEMETARY"
      f9 = OpportunityCard(fdesc9,40,0,0,0,0,0,0)
      self.opportunitylist.append(f9)
      fdesc10 = "PAY FOR YOUR SNACKS 12 xp"
      f10 = OpportunityCard(fdesc10,0,0,12,0,0,0,0)
      self.opportunitylist.append(f10)
      fdesc11 = "TAKE A RIDE TO STREET BOXERS. ADVANCE TOKEN AND IF YOU PASS GO COLLECT 200 xp"
      f11 = OpportunityCard(fdesc11,6,0,0,0,0,0,0)
      self.opportunitylist.append(f11)
      fdesc12 = "GO BACK THREE SPACES"
      f12 = OpportunityCard(fdesc12,0,0,0,0,0,0,3)
      self.opportunitylist.append(f12)
      fdesc13 = "YOU HAVE BEEN PROMOTED - RECIEVE 150 xp"
      f13 = OpportunityCard(fdesc13,0,150,0,0,0,0,0)
      self.opportunitylist.append(f13)
      fdesc14 = "MAKE GENERAL MAINTAINANCE ON ALL OF YOUR OBSTACLES. FOR EACH OBSTACLE PAY 25 xp"
      f14 = OpportunityCard(fdesc14,0,0,0,25,0,0,0)
      self.opportunitylist.append(f14)
      fdesc15 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT 200 xp"
      f15 = OpportunityCard(fdesc15,0,0,0,0,0,1,0)
      self.opportunitylist.append(f15)
      random.shuffle(self.playerlist)
      random.shuffle(self.fslist)
      random.shuffle(self.opportunitylist)
   def playerlose(self,player):
      for item in self.boardlist:
         if isinstance(item,Snag):
            if item.oc == player.name:
               item.oc = "Silas"
               item.obstacles = 0
         if isinstance(item,Boxers):
            if item.oc == player.name:
               item.oc = "Silas"
               item.obstacles = 0
         if isinstance(item,Fighters):
            if item.oc == player.name:
               item.oc = "Silas"
               item.obstacles = 0
   def playermove(self,player,movenum,warp):
      if player.droll == 1:
         player.doublesacc += 1
      if player.droll == 0:
         player.doublesacc = 0
      if player.doublesacc == 3:
         player.boardpos = 11
         player.jailime = 3
         print(str(player.name) + " has rolled doubles three times in a row. " + str(player.name) + " is now in JAIL.")
      else:
         newspot = int(movenum) + player.boardpos
         if warp == 1:
            newspot = int(movenum)
            if player.boardpos > newspot:
               player.xp += int(200)
               print(player.name + " has passed go and collects 200 xp.")
            player.boardpos = newspot
         if newspot > 39:
            newspot += -39
            player.xp += int(200)
            print(player.name + " has passed go and collects 200 xp.")
         player.boardpos = newspot
         for space in self.boardlist:
            if self.boardlist.index(space) == player.boardpos:
               currspace = space
               break
         print(player.name + " has landed on " + currspace.name + ".")
         if isinstance(currspace,Snag):
            if currspace.oc == "Silas":                           # if creatable
               if player.user == 0:                                 # if computer
                  for colorlist in player.snglist:
                     for sng in colorlist:
                        if isinstance(sng,str):             #just added
                           continue                          #just added
                        if isinstance(sng,Snag):        #just added
                           if sng.color == currspace.color:           # PROBLEM, sng.color is appearently a string...
                              if player.xp >= currspace.cost:
                                 player.addsnag(currspace)
                                 print(str(player.name) + " has created " + str(currspace.name) + " for " + str(currspace.cost) + "xp.")
                                 break
                  if currspace.oc == "Silas":
                     if player.xp >= currspace.cost:
                        createchoice = random.randint(0,1)
                        if createchoice == 1:
                           player.addsnag(currspace)
                           print(str(player.name) + " has created " + str(currspace.name) + " for " + str(currspace.cost) + "xp.")
               if player.user == 1:
                  if player.xp >= currspace.cost:                 # if user
                     createwhile = 0
                     while createwhile == 0:
                        choice = input("NOBODY CHANGED " + str(currspace.name) + ". WOULD YOU LIKE TO CREATE AN OBSTACLE HERE? TYPE Y OR N.")
                        if choice == "N" or "n":
                           createwhile = 1
                        elif choice == "Y" or "y":
                           player.addsnag(currspace)
                           print("You have created an obstacle in " + str(currspace.name) + " for " + str(currspace.cost) + "xp.")
                           createwhile = 1
                        else:
                           print("Invalid input. Available answers are Y (yes) or N (no).")   #PROBLEM
                  else:
                     print("YOU DON'T HAVE ENOUGH EXPERIENCE TO CREATE OBSTACLE ON THIS PROPERTY. TRY AGAIN LATER")
            elif currspace.oc == player.name:
               task = "do nothing"
            else:
               for person in self.playerlist:                 # determine obstacle owner
                  if person.name == currspace.oc:
                     sngoc = person
               hasdominated = 0                                # determine if dominated
               for colorlist in sngoc.snglist:
                  if colorlist:
                     for sng in colorlist:
                        if sng.color == currspace.color:
                           if "dominated" in colorlist:
                              hasdominated = 1
                              break
               if hasdominated == 1:
                  if currspace.obstacles == 0:
                     payout = 2*int(currspace.price)
                  elif currspace.obstacles == 1:
                     payout = int(currspace.o1)
                  elif currspace.obstacles == 2:
                     payout = int(currspace.o2)
                  elif currspace.obstacles == 3:
                     payout = int(currspace.o3)
                  elif currspace.obstacles == 4:
                     payout = int(currspace.o4)
                  elif currspace.obstacles == 5:
                     payout = int(currspace.o5)
                  if player.xp <= payout:
                     sngoc.xp += player.xp
                     self.playerlose(player)
                     print("By landing on " + str(sngoc.name) + "'s " + str(currspace.name) + " with insufficient experience, " + str(player.name) + " has lost the game.")
                  else:
                     player.xp += -payout
                     sngoc.xp += payout
                     print(str(player.name) + " has landed on " + str(sngoc.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
               else:
                  payout = int(currspace.price)
                  if player.xp <= payout:
                     sngoc.xp += player.xp
                     self.playerlose(player)
                     print("By landing on " + str(sngoc.name) + "'s " + str(currspace.name) + " with insufficient experience, " + str(player.name) + " has lost the game.")
                  else:
                     player.xp += -payout
                     sngoc.xp += payout
                     print(str(player.name) + " has landed on " + str(sngoc.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
         if isinstance(currspace,Boxers):
            if currspace.oc == "Silas":                           # if creatable
               if player.xp >= currspace.cost:
                  if player.user == 0:                                 # if computer
                     if len(player.boxlist) >= 1:
                        player.addsnag(currspace)
                        print(player.name + " has created obstacles at " + currspace.name + " for " + str(currspace.cost) + "xp.")
                     else:
                        createchoice = random.randint(0,1)
                        if createchoice == 1:
                           player.addsnag(currspace)
                           print(player.name + " has created obstacles at " + currspace.name + " for " + str(currspace.cost) + "xp.")         
                  else:
                     boxwhile = 0
                     while boxwhile == 0:
                        choice = input("NOBODY CHANGED " + str(currspace.name) + ". WOULD YOU LIKE TO CREATE AN OBSTACLE HERE? TYPE Y OR N.")
                        if choice == "N" or "n":
                           boxwhile = 1
                        elif choice == "Y" or "y":
                           player.addsnag(currspace)
                           boxwhile = 1
                        else:
                           print("Invalid input. Available answers are Y (yes) or N (no).")
               else:
                  print("YOU DON'T HAVE ENOUGH EXPERIENCE TO CREATE OBSTACLE ON THIS LOCATION. TRY AGAIN LATER")
            elif currspace.oc == player.name:
               task = "do nothing"
            else:
               for person in self.playerlist:                     # determine obstacle creator
                  if person.name == currspace.oc:
                     sngoc = person
               if len(sngoc.boxlist) == 1:
                  payout = int(currspace.bx1)
               elif len(sngoc.boxlist) == 2:
                  payout = int(currspace.bx2)
               elif len(sngoc.boxlist) == 3:
                  payout = int(currspace.bx3)
               elif len(sngoc.boxlist) == 4:
                  payout = int(currspace.bx4)
               if player.xp <= payout:
                  sngoc.xp += player.xp
                  self.playerlose(player)
                  print("By landing on " + str(sngoc.name) + "'s " + str(currspace.name) + " with insufficient experience, " + str(player.name) + " has lost the game.")
               else:
                  player.xp += -payout
                  sngoc.xp += payout
                  print(str(player.name) + " has landed on " + str(sngoc.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
         if isinstance(currspace,Fighters):
            if currspace.oc == "Silas":                           # if creatable
               if player.xp >= currspace.cost:
                  if player.user == 0:                                 # if computer
                     if len(player.ftlist) >= 1:
                        player.addsnag(currspace)
                        print(player.name + " has created obstacles at " + currspace.name + " for " + str(currspace.cost) + "xp.")
                     else:
                        createchoice = random.randint(0,1)
                        if createchoice == 1:
                           player.addsnag(currspace)
                           print(player.name + " has created obstacles at " + currspace.name + " for " + str(currspace.cost) + "xp.")          
                  elif player.user == 1:
                     ftwhile = 0
                     while ftwhile == 0:
                        choice = input("NOBODY CHANGED " + str(currspace.name) + ". WOULD YOU LIKE TO CREATE AN OBSTACLE HERE? TYPE Y OR N.")
                        if choice == "N" or "n":
                           ftwhile = 1
                        elif choice == "Y" or "y":
                           player.addsnag(currspace)
                           ftwhile = 1
                        else:
                           print("Invalid input. Available answers are Y (yes) or N (no).")
               else:
                  print("YOU DON'T HAVE ENOUGH EXPERIENCE TO CREATE OBSTACLE ON THIS PROPERTY. TRY AGAIN LATER")
            elif currspace.oc == player.name:
               task = "do nothing"
            else:
               for person in self.playerlist:                     # determine obstacle creator
                  if person.name == currspace.oc:
                     sngoc = person
               if len(sngoc.ftlist) == 1:
                  payout = int(currspace.f1)
               elif len(sngoc.ftlist) == 2:
                  payout = int(currspace.f2)
               if player.xp <= payout:
                  sngoc.xp += player.xp
                  self.playerlose(player)
                  print("By landing on " + str(sngoc.name) + "'s " + str(currspace.name) + " with insufficient experience, " + str(player.name) + " has lost the game.")
               else:
                  player.xp += -payout
                  sngoc.xp += payout
                  print(str(player.name) + " has landed on " + str(sngoc.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
         if isinstance(currspace,Policecheckspace):
            paypc = currspace.pc
            if player.xp <= paypc:
               self.playerlose(player)
               print("With insufficient experience to handle the "+ str(currspace.name) + " of " + str(currspace.pc) + ", " + str(player.name) + " has lost the game.")
            else:
               player.xp += -paypc
               print(str(player.name) + " has landed on " + str(currspace.name) + " and pays " + str(paypc) + ".")
         if isinstance(currspace,Freespace):
            print("nothing happens.")
         if isinstance(currspace,Gotojailspace):
            player.boardpos = 11
            player.jailime = 3
            print(str(player.name) + " has landed on " + str(currspace.name) + ". " + str(player.name) + " is now in JAIL.")
         if isinstance(currspace,Friendspace):
            self.fslist.append(self.fslist.pop(0))    # should move top card to bottom of deck
            card = self.fslist[-1]
            print("Friend Helps" + str(player.name) + "'s card says: " + str(card.description))
            if card.move > 0:
               self.playermove(player,card.move,1)
            if card.collect > 0:
               player.xp += card.collect
            if card.pay > 0:
               player.xp += -card.pay
            if card.payperobstacle > 0:
               player.xp += -card.payperobstacle
            if card.getoutofjailfree > 0:
               player.jailcards += 1
            if card.gotojail > 0:
               player.boardpos = 11
               player.jailime = 3
               print(str(player.name) + " is now in JAIL.")
            if card.collect50 > 0:
               for i in self.playerlist:
                  if i != player:
                     if i.xp >= 50:
                        i.xp += -50
                        player.xp += 50
                     else:
                        player.xp += i.xp
                        i.playerlose()
                        print(i.name + " has insufficient experience to pay 50 xp, and loses the game.")
         if isinstance(currspace,Opportunityspace):
            self.opportunitylist.append(self.opportunitylist.pop(0))    # should move top card to bottom of deck
            card = self.opportunitylist[-1]
            print("Opportunity!" + str(player.name) + "'s card says: " + str(card.description))
            if card.move > 0:
               self.playermove(player,card.move,1)
            if card.collect > 0:
               player.xp += card.collect
            if card.pay > 0:
               player.xp += -card.pay
            if card.payperobstacle > 0:
               player.xp += -card.payperobstacle
            if card.getoutofjailfree > 0:
               player.jailcards += 1
            if card.gotojail > 0:
               player.boardpos = 11
               player.jailime = 3
               print(str(player.name) + " is now in JAIL.")
            if card.moveback > 0:
               self.playermove(player,int(player.boardpos)-1,1)
         if player.droll == 1:
            print(player.name + " has rolled doubles, and gets to roll again!")
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("die 1 roll: " + str(die1))
            print("die 2 roll: " + str(die2))
            if die1 == die2:
               player.droll = 1
            else:
               player.droll = 0
            self.playermove(player,int(die1+die2),0)
   def PREMOVE(self,player):
      if player.jailtime > 0:
         if player.user == 0:
            if player.jailcards >= 0:
               player.jailcards += -1
               player.jailtime = 0
            if player.xp >= 50:
               player.xp += 50
               player.jailtime = 0
            else:
               print(player.name + " attempts to roll doubles to get out of jail.")
               die1 = random.randint(1,6)
               die2 = random.randint(1,6)
               print("die 1 roll: " + str(die1))
               print("die 2 roll: " + str(die2))
               if die1 == die2:
                  player.jailtime = 0               
         if player.user == 1:
            print("You are in Jail.")
            if player.jailcards >= 0:
               jcwhile == 0
               while jcwhile == 0:
                  usejc = input("Do you want to use a jailcard to get out? Type Y or N.")
                  if usejc == "N" or "n":
                     jcwhile = 1
                  elif usejc == "Y" or "y":
                     player.jailcards += -1
                     player.jailtime = 0
                     jcwhile = 1
                  else:
                     print("Invalid input. Available answers are Y (yes) or N (no).")

            if player.xp >= 50:
               jailpaywhile = 0
               while jailpaywhile == 0:
                  jailpay = input("Do you want to pay 50 xp to get out of jail? Type Y or N.")
                  if jailpay == "N" or "n":
                     jailpaywhile = 1
                  elif jailpay == "Y" or "y":
                     player.xp += -50
                     player.jailtime = 0
                  else:
                     print("Invalid input. Available answers are Y (yes) or N (no).")   
            jailrollwhile = 0
            while jailrollwhile == 0:
               jailroll = input("Do you want to try to roll doubles to get out of jail? Type Y or N.")
               if jailroll == "N" or "n":
                  jailrollwhile = 1
               elif jailroll == "Y" or "y":
                  die1 = random.randint(1,6)
                  die2 = random.randint(1,6)
                  print("die 1 roll: " + str(die1))
                  print("die 2 roll: " + str(die2))
                  if die1 == die2:
                     player.jailtime = 0
                     jailrollwhile = 1
                  else:
                     jailrollwhile = 1
               else:
                  print("Invalid input. Available answers are Y (yes) or N (no).")
      for colorlist in player.snglist:
         if "dominated" in colorlist:
            for snag in colorlist:
               if snag.obstacles <= 5:
                  obstaclewhile = 0
                  while obstaclewhile == 0:
                     if snag.obstacles == 5:
                        obstaclewhile = 1
                     if player.xp >= snag.obstaclecost:
                        if player.user == 0:
                           player.xp += -snag.obstaclecost
                           snag.obstacles += 1
                        if player.user == 1:
                           createobstacleyn = input("Do you want to create an obstacle on " + snag.name + "? Type Y or N.")
                           if createobstacleyn == "N" or "n":
                              obstaclewhile = 1
                           elif createobstacleyn == "Y" or "y":
                              player.xp += -snag.obstaclecost
                              snag.obstacles += 1
                           else:
                              print("Invalid input. Available answers are Y (yes) or N (no).")      
                     else:
                        obstaclewhile = 1
      if player.user == 1:
         ownssng = []
         for colorlist in player.snglist:
            if colorlist:
               ownssng = ["yes"]
         if ownssng or player.boxlist or player.ftlist:                            
            mortwhile = 0
            print("Do you want to clear evidence of your previous obstacle?")
            while mortwhile == 0:
               mortyn = input("Type Y or N.")
               if mortyn == "N" or "n":
                  mortwhile = 1
               elif mortyn == "Y" or "y":
                  mortthis = input("Please type the name of the obstacle you created that you would like to get cleared.")
                  for colorlist in player.snglist:
                     for sng in colorlist:
                        if sng.name == mortthis:
                           colorlist.remove(sng)
                  for space in self.boardlist:
                     if space.name == mortthis:
                        if space.oc == player.name:
                           space.oc = "Silas"
                           space.obstacles = 0
                           player.xp += space.ce
                  print("Would you like to clear evidence of some additional obstacles?")
               else:
                  print("Invalid input. Available answers are Y (yes) or N (no).") 
                  
def main():
   print('WELCOME TO "DOMINATION OF THE VAMPIRES"')
   print('Rules of the game: \n 1.	The objective of the game is to kill all the vampires by making their experience = 0 xp. \n 2.	Silas is the “God of Traps” who is going to allow you create obstacles by using your experience. \n 3.	You will be assisted by your old friends on friend space which might get you earn more xps. \n 4.	It is up to you, how you deal with fighters, boxers, and police. \n 5.	If the vampires move ahead of you, they might have set trap for you. \n 6.	Opportunities are set by Silas which might get you earn or lose xps. \n 7.	You can get out of Jail by... \n a)	Escaping the Jail: Throwing doubles on any of your next three turns, if you succeed in doing this you immediately move forward the number of spaces shown by your doubles throw. Even though you had thrown doubles, you do not take another turn. \n b)	Help of Silas: Using the "Get Out of Jail Free Card" \n c)	Risking your life to vampires: Purchasing the "Get Out of Jail Free Card" from another player and playing it. \n d)	Bribing the officer: Paying 50 xp before you roll the dice on either of your next two turns. If you do not throw doubles by your third turn, you must pay the 50 xp fine. You then get out of Jail and immediately move forward the number of spaces shown by your throw. \n 8.	No man’s land is just a resting place. \n 9.	If you clear the evidence, you will get half the xps back from Silas which you spent on the obstacles.')
   firstwhile = 0
   while firstwhile == 0:
      numplay = int(input("Please enter the number of vampires you want to compete against: "))
      if numplay > 0:
         firstwhile = 1
      else:
         print("Invalid input. Please select one or more players to play against.  ")
   playname = str("HUNTER")
   gameboard = Board(numplay,playname)
   playgame = 1
   while playgame == 1:
      for player in gameboard.playerlist:
         if len(gameboard.playerlist) == 1:
            for player in gameboard.playerlist:
               print(player.name + " WINS!")
            playgame = 0   
         print(player.name + "'s turn!")
         if player.jailtime > 0:
            print(player.name + " is in JAIL.")
         gameboard.PREMOVE(player)
         print(player.name + " rolls the dice!")
         die1 = random.randint(1,6)
         die2 = random.randint(1,6)
         print("die 1 roll:      " + str(die1))
         print("die 2 roll:      " + str(die2))
         if die1 == die2:
            player.droll = 1
         else:
            player.droll = 0
         gameboard.playermove(player,int(die1+die2),0)
         print(" ")
         print(" ")
         
main()  
