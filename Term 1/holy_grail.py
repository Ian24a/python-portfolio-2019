
#Cale Sumner, Jayden Williams, Ian Christensen, Daniel Embley

#link to draw.io NOTE:you may have to download it, then open with draw.io
# https://drive.google.com/open?id=14TYFIyxCwYK_H0DUVIljk2ds7WtEDSOJ
def choice(choice1, choice2, choice3, choice4, choice5):
    while True:
      choice = input("Choose 1 ," + choice1+ " , " + choice2 + " , " + choice3 + " , " + choice4 + " , " + choice5)
      if choice == choice1:
        return choice1
      elif choice == choice2:
        return choice2
      elif choice == choice3:
        return choice3
      elif choice == choice4:
        return choice4
      elif choice == choice5:
        return choice5            
      else:
        print("Sorry that is not an option.")
        continue
      

    
            
def intro():
  #Intro 1 with title
  print("""  ,/   */ .(//*. ,*  .(*(/*//.*  .#   .((/, .*  .(,/,((/.*   / .///** .*.  /   
    ,,/ ,,/./    *,*,*,.(  .*    **,    .,  ., .*/*   .*  .*,,,/ /.   .,.,.. /   
    ,..*(./ *    /.*, .*(  .*    .(     ..      .*    .*  .*   / *,   ,.., .*/   
    *  / .*  ,/(,  *.  ,*  .*    ,*     ,.      ,.    ..  ..   *  ./(,  ..   *   
    ...........................................................................  
                             ,,                   .                        .,*   
     .,(.     .,(            .,              .,(.  .,**                     ,*   
     .,,       ,(  *, .,.  *,** ./,/*. ,*   .(.      **                ,*   ,*   
     .,,       ,( .(/*.  ,*  **  ( / /,*** .,.       ./                ,*   ,*   
     .,,       ,(  ,...    ,,,*  ... . .,  ,/         .     .               ,*   
     .,*.......,(    *(*,*   .* .,,(/ /,/, ,/            ,*.,/ .//,/   ,*   ,*   
     .,/.......,(  .,,   ,*  .*   ./   (.  ,*            ,*  ,./, .*,  ,*   ,*   
     .,,       ,(  ,*    .,. .*    *, .,   ,*     ,*,,/. .*       .*,  ,*   ,*   
     .,,       ,(  ,*    .,, .*    ,( (    ,,.      .*,  .*      ,*/.  ,*   ,*   
     .,,       ,(  .,.   .*  .*    .**,     ,*.     .*,  .*    ** ./.  ,*   ,*   
     .,/       ,/   ,/   ,/  .,     ,/       ,,     .*,  ,*   .*, .*,  ,,   ,*   
    ,////.   *////.  **/(   ,///,   *          //**/(*. *///*  *// */.*///.////  
                                   .(                                            
                                   (.                                            
                                  ,,""")


  print("Welcome to the Quest for the Holy Grail! In this game you play as Arthur, son of Uther Pendragon, from the castle of Camelot. King of the Britons, defeater of the Saxons, Sovereign of all England! ... Yes, you are rather impressive aren't you? Today seems like any other day of you riding through your kingdom with your knights of the round table looking for dragons to save and damsels to slay or something along those lines.")


  print('"Arthur! King of the Britons!" You hear a voice bellow from above and suddenly the clouds part over your head and a cheaply animated adaptation of the Lord your God shines his glory down upon you.')


  print("You proceed with the ceremonial praising, grovelling and averting of your eyes for which God scolds you and tells you to stop sucking up.")


  print("He then explains that he is charging you and your knights with a sacred task, to seek the Holy Grail! He doesn't really explain what it's for or why he wants you to find it, but it's got the word Holy in it, so that must make it important, right")
  #Allow user to continue with user input
  input("The Quest Begins! Continue?(press enter)")
#intro 2
def intro2():
  print("Your sacred quest for the Holy Grail has begun! Where do you want to look first?")




  print("Camelot!")
  print("The French Castle")
  print("The Dark Forest")
  print("A Nearby Village")
  print("The Castle Anthrax")
  #first real choice, allows movement between major places
  choicea = choice("Camelot!", "The French Castle","The Dark Forest","A Nearby Village","The Castle Anthrax")
  if choicea == "Camelot!":
    return camelot()
  if choicea == "The French Castle":
    return the_french_castle()
  if choicea == "The Dark Forest":
    return the_dark_forest()
  if choicea == "A Nearby Village":
    return a_nearby_village()
  if choicea == "The Castle Anthrax":
    return the_castle_anthrax()
#dont worry about the red lines ill fix in a bit(jayden)
#The Dark FOrest Text
print("""And so, you and your knights boldly make your way\
 towards the Dark Forest, which is no more than two swallow's flights away!\

Oh, that's an unladen swallow's flight away, obviously. It's more than two laden swallow's flights away. Four really, if they had a coconut on a line between them.\

Anyway, when you arrive at the forest, you come to a crossroads, where there are four signs. A sign saying Camelot which points back the way you came, a sign that says, Certain Death! Pointing to the east, a sign that says, REALLY Certain Death! Pointing to the west and a sign that says, Holy Grail this way!  Pointing to the north. Where do you want to go?""")


print("Back the way you came") #Goes to Original Choices
print("Certain Death!") # a long arguement =) with 3 more choices Bravely run away!,Fight the giant,Sneak past the giant
print("REALLY Certain Death!")# a fight with The Knights of Ni =) 2 more choices
print("Path to the Holy Grail")

#Camelot
def camelot():
  print('''Oh alright, if you must! But you don't want to stay too long. 'Tis a silly place! You make your way into the stables to find worthy steeds for yourself and your knights. Unfortunately the horses were all sold a few years back during the age of terrible
  glueshortage. You do however manage to find a coconut which you cut in half and give to your trusty servant Patsy who skillfully bangs the two halves together to make horse hoof noises. He's a prodigy on the coconuts that Patsy!

  ''')
intro()
intro2()

#Black Knight

print("""print              
                                   ***********,                                 
                               .***************                                
                                ***************                                
                                ,,*************                                
                                ,..,,,,,,,,****                                
                                *****,,*,******                                
                                **,**,*********                                
                                *,,*,**...,****                                
                                **,,,%(. /( ***                                
                                **,**((#*/,.***                                
                                **,,*#%* ,*.***                                
                          ,,****,**,,.%     **************,                    
                   .,************,,,, .     ,**************,                   
                    ************ ,. % *./ ,   .  ***********                   
                   ***********,#* #(       /(* . ,.********                    
                    ,*****,**. (%/       ********                        
                         ,***,***,  #,,***    ,,,,*,***                        
                          *******/     .    * ,,,,,,,**                        
                           ****,,     ,,       ,,,,,,**                        
                           ,,**,.     #,       ,,,,,,,,.                       
                            ,,,,      #.       .,,,,,,*                        
                            ,,,,      (.       .,,,,,,,                        
                            ,,,,,     (        .,,,,,*                         
                            ,,,,,     (        .,,,,,                          
                             ,,,,     (         ,,,,,                          
                             ..,,     (         ,,,,,                          
                             ....     (  . ,   ..,,,,,                         
                            .....    .(....    .,,,,,,                         
                            .....    .(.....    .......                        
                            ....    ..(.....    .......                        
                            . ..   ... .....    .......                        
                            .. .   ... ......   .......       ,.        .********                    
                    *,,,,**** .,.   ,,. .,*        *******                     
                      ,,,,***.       ,(.,,,    **.******                       
                        .,,*****,     *,..     *********                       
                         *,,*****     .                        
                                   ... ......    .. ..                         
                                         .                  """)   

#The Black Knight Text
print('''You hope to find clues in a nearby village but on your way your path is blocked by a man clad from head to toe in black armour.


"None shall pass!" He tells you.


You are left looking rather baffled. "What?"


"None shall pass!" He repeats.


"But I am Arthur, King of the Britons!"


"I move for no man!" The Black Knight tells you with an unwavering tone in his voice.


"But God has charged me with a sacred quest and I must reach the village!" You insist, but the Black Knight holds his ground.


"I will tell you for the last time... NONE shall pass!"


How very rude! You'd challenge this man to a duel in a second but unfortunately you managed to get your sword stuck in a stone awhile back. If only you had some way to convince the knight to let you pass.

''')

#Evil Temptresses/Nun
print(""")          ,/(##(/*.                                
               .##(*,,,**/((#/.  ..                        
              /#*...,,.,,*,,,..,.,,*,,..                   
            .*(,......,,,,,,,*******,,,**,.                
           .,/(   ....,,,,,,,**//*////******,.             
            ,*/    ..........,*****//////******..          
            .,/     .........,*/((#%%%%%%#%##(/*,          
             .,   ...........*/((#%%%%%%%%%%%%%(*.         
            .,,.  .   .......,*###%%&&&%%&%&&%%%(.         
     *.**,****(,.....,,,*,,,*/((((((//((/####((/*.         
    .,*/**/***#,.....,,,**,*/(((###%%&&%%&&&%&&%%/         
    ..//,*/***(*....,,,**,**/((((##%&&%%%%&%%&%%%#.        
  ...*//**/***((....,,,**,*//((////((((#%%%%%%%%%%*.       
 .,,.*/////***(%.....,,*,,///*/(###(/*/(##%%%##/***.       
.,*,.//////***(%,...,,,,,*///(((((#%%#((((###((#%%(.       
***,.//////***/#*...,,,,*/////////(#((#((#%%#####(/.       
****.*/////***/#(....,,,/(((((/,,,,,/(%%(#%%(*,*//%,       
****.*/////***/#%.....,*/(((#####((#%%%####%%#/*//%#       
*//**.*////***(#&.....,*////(#%%&&%&%%%##((#%%%%%#%&.      
,*//*.,////**/(#&,..,,,***//(((#%%&&&%%#((/(#%%%%##&/      
,*//*.,**//*//(#&*..,******//((##%%&%#%*/*,,*/(%%##      
,*///,,,*//*//(#&(,,*******///(((####%%%%(/*/#%%%##&&      
**/((*,,**/*/((#&%,,*******///(((((####%%%%##%%####&&.     
/*/((*,****//((#&%,*******///((((##(///////((######&&.     
(/*/(/****/*/((#%&,,,,****///((((###((///(((((#####&&,     
(/////***////(##&&,********///(((#####((////#%#####&&*     
((/////**////(##&&*********////(((#####%%##%%%###%%&&/     
#(((///**/(//(##%&/**********////(((##%&&%%%%###%%%&&/     
##(((//*//((/(##%***************/(((###%%%###%%%%&&/     
%##((/(((/((((##%&%******************//(((((###%%%&&&/     
%###((((#(((((##%&&*/***********//////(#%%####%&%%&&&/     
%%###((((((#####%&@//////******//((#%&&%%%%###%&%&&&&/     
&%%##(((##(#####%&@#(((///////((((((%&&&&%&%##%&&&&&@/     
&&%%##(((#%####%%&@%(((((((((((((#%%#&&&&&&&%%&&&&&&@/     
&&&%%#(((######%%&@##((########%%*&%&&&&&&%%&&&&&&@*     
&&&&%##((#%##%%%%&@#######%##%%%&(%&%&&&&&%%&&&&&&@*     
&&&&&%##(#%##%%%%&@########%%%%&%/%%@(%%%&%%&&&@@&@*     
&&&&&&%######%%%%&@@#%#######%%%&&%*%%(((&%&&&&&&@@@@,.    
&&&&&&%%##(##%%%%&@@%%%%%###%%&&&&%,%%(/(#%%%&&@@@@@@,..  .
@@&&&&&%%###%%%%%&@@%%%%%%%%%&&&&%#/#@(/%(%%%&&@@@@@@@*....
&@@&&&&%%###%%%%%&@@&%&&&&%%&&&&&&%&(@((%((%%&&@@@@@@@@&%((
&@@&&&&%%%##%&%%&&@@@@@&&&&&&&&&&@@&(%(##(/%%&&@@@@@@@@@@@@

""")


#Black Knight Encounter


print(""",,,,,,,,,,,,,,,,,,....,,,,,,.,,.,,,,.,,,,,,,,.,,,,,,.,.,***/((,(**/,..
........,,.,,,,,,,..    ,,@@&,....,,,,,,,,,,,,,,,,,.  .,,,,,.,/,,,,/(((,/(//,,.
,,,,,,,,,,,,,,,,,,,.    ,. ..*.....,,,,,,,,,,,,,.,.   .******//***////,,,,*,,..
*************,***,,.    ,   ... ...,*************,.   .****/**/*****,,,,,,,,,.,
//*//*///////////*,     ,..  .   ..,************.      ..***************,,,,***
********,****//(//... ,,*/*,,,   .../******////    ,.    .****/*//*////**////**
******//***//(((//....***( .,,.  ...////((/((/* .,,,     /**//////////**//////*
/////////((((((//,..,,#%#/...,/  .../((((((##(.  ,..    .(((((((////////**//***
(///////(///*///*,..,/.#(/*..,/  .,.,////(/*/(          #%%######(((#####(((///
****//*/((/***/,   .*..,((/*..,( ,,*//**///**.          /#((#(((((((((#((#((((/
*/***************,,   ..(.   .,,.*//////(/(//.          ,(((((((((/(//(////////
***,****/,,,,..........,&%#//*  ,*,,*/**,,///.          ./(((#(((((/((/////////
. .. ... ...   . , ....,(#(/*/, .,**,.*#*///**,         //((/*//////(#%/////(//
  .   .,... .       .  ./#(/((*,  ,,,,.,,/***((         *((/***/,,/,,,**//**,.,
.....,.,,..,......,.   ./#(/((**...,.*,*,,/,,/(.  .    (#((((/((***/,***//,....
. ,...,,*,,,,,,...     /##((##//(*/,,*,..  ./*/   (**  .(///*//((.*.,,***,,**,*
  .  ....,,...,.....   ##%(#%#(/(, .,..,,...,*/  ,*//,  ////(((/*//,,.      ,*,
         .         ....##%(#%#(//(.  ......* ..  */((/  ////////*,/*.**/,..,,,*
 ,   ........(((((##((#(%%(%%##//%,,,. ...., .,  /////, //(///*//*. *,/((*/**/,
(////((((/(((((##((((((  .(.,,. *(///((/(/(//.  ,*,***.  ,*,,........,,,*,,,,,,
/*///////(/((((///#((((  */*,/  //((((/(//(////,,,.,,.  ..,,./        .,,,,.,**
/*/*/////////((((/(//(/  *////  *//**/*/**/**,**/**,,,,*.*    . ...,,,.,,.,,,,*""")


#Knight with Helmet

print("""////////////////////////////////***********,,,*////////////////////////////////
////////////////////////////////##&/%@##((/***,*,,/////////////////////////////
//////////////////////////,* .//*(/%@@%#(//****,,,/////////////////////////////
//////////////////////////.*(/*//(#%@@%#((///**,*,*////////////////////////////
//////////////////////////,.*/**//(#@@%#((///****,,////////////////////////////
//////////////////////////(.**,**/(#%@%##(////*,,,,////////////////////////////
///////////////////////////.*(,*/...   . ,(#,/*,(*,*///////////////////////////
///////////////////////////   *//*. .#@&(///*,*,**///////////////////////////
///////////////////////////.*(*////(###,... //**,.*%///////////////////////////
((/////(/////////////(#((**.. **/*...,####*((/**,,*,*//////////////////////////
((//(///(//(((((,*.,#@&%(/* .**,///(##&%/(##(/**,,*,,//////(/(/////////////////
((((((/(((((((((*/**@@@&%((,  *,*/   ./@&((((/**,,*,,((((((((/(((/((//((/(//(//
((((((((((((((((*(**@@@@%((/,**,***/(#%@%%##(//***,*,/((((((((((((((/(((((((((/
((((((((((((((((//**%&@@%#((.(*,*/*/(#%@&%%#///***,/*,((((((((((((((((((((///((
((((((((((((((((**/*(%&@//.(*,/////%%@@&&%#/    .*,*/,*.,*(((((((((((((/*((((
(((((((((((((((/**(/##&@//,/**///((#&@(      /(,/,*,*,**..&(((((((((/*(((((((
(((((((((((((((    ,**///((.*(//////*    *.(.**. ***.,.,%&&@&&&&(///(((((((((
(((((((((((((((.,,. ,(%%((/    *,    ,( .**#.*,,,,,..,,,&@@@.,(((/* .((((#####%
(((((((((((((((/,....*,/,*,/       /(//.**/.*/&**.,*,,,/&*,/(((((#** .(((%%##%%""")

#Holy Grail

print("""/////////((((///********/*******//(/////******//*,****,,,,,*******,,///////////
/////////****/////***,,*/**,,**////((((//*/(///***///*,*************/(/////////
/((///**********////**,*,**((((((((/(///(((((((((((*****////*********//////////
///*************/((((///(((/(////********////((((#/***///****,,,,,**,,,,///////
/****,,********,,,,/(((/((((//**,,,,...,,,,**//((((/(/*,*************,,,**/////
*********/*********((((/(///*,,,,,,,,,,,,.,,,*/////((/*************,,,,,**,***/
*********///////((((///(//**,,,,*///////***,,,,,*//(((/*,,*******,,,,,**,*,,,**
**********/(//(((((///(//*,,...,//*********,....,*/(((/(/,,,***,,,,,,,,***,,,**
*****,,,****,,*((((((///**,,....***********.....,,*/((/(##*,,,***,,,,,,,,,,,***
********,**////((//(//***,,......,**////*,.......,***(((((//***/**,,,,,,,,,,,,*
******///*////(#(//(//**,,.........**,,*.........,,**///((((((//*,,,,,,,,,,,***
***,,,,*//////(#(/////**,,..........**,..........,,**///((//*,,*,,,,,,,,,,*/***
,,,*******//((((((/////*,,..........***...........,*////(/*////*,,,,,,,,,**///*
*,,******,**//(((///(//*,,.........*****.........,**//(((/***************,,**,,
*****,,,***///*/(/((((///,,.......*///((*.......,*///////***/********/*,,,,,,,,
***********////(/((((((///*,.....,*//////*,...,,*/////(((/((/////////,,,,,,,,,,
*******//*****//////((//////*,,.......,,...,**///////////*******,,,,,,,,,,,,,,,
*************/////((((((((////***,.,,,*******////*///((//**,,,,,,,,,,,,,,,,,,,,
***************,,,,,,,,**/((/////******/*/(///////*,*****/**********,,*********
********/*****,,,,,,,********///*//******///((///**//////////////,,,//////****/
***************,,*,,,,*****************////,,*//*,/////////**,,,,,,,/(/////*//*""")


#Holy Grill

print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@#@@@@@&&&&&&@&&&&&&%%%%%%&&&@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%@@@@@@@@@@@&&&&&&&&&@@@@@&&&&@&%%%&@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@&&&&@@@@&&&&@@@@@@@@@&%%%%%&@@&&&@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@&&@&%%&@&&%&&&&&&&@@@@@@@@@@@@@&%%%%%%@@@&&&&@@%@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#(((((((((((/(@(////(%&@@@&&%&&&%%&@@@@@@@@@@@@@%@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@/..,,**************(%&&&@@&&%&@@@@@@@@@@@&@@@%@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&%*,***/(//////(#%&&@@@@&&%(******(((*,(%@@@@&%&&&@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&&&%&%%%%%%&&&@@@@&&((////////***,,.. ...*/*.*%&%@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%&&&&%&%#(((*/(*//**/,*/,***,,,,,,,,.... .*(#@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@****///////(*/(*//***,*/,*/.,*.,*,,,*,,,,,,,.../@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@,****////*//**/***,**,**,,*.,*.,*.,*,,,*.,,,,,.(@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@.,,,*****,**,**,,,,,,,,*,,,,,,.,*.,*.,,,,,*.,,.%@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@ ...,*,,*.,*,,,,,,,,.,*,,,,,,,,,,.,,.,,.,,, ,..&@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@ ..,,*,,*.,*,,,,,.,,.,*,,*.,,,,,,.,,.,,.,,..,..@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@...,,*,,*.,,,,,,,.,,.,,.,,.,,.,,..,..,,.,,..,..@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@*. .,,.,,.,,,,.,,.,,.,,.,,.,,.,,.,,..,,.,,.,,.*@@@@@@
@@@@@@@@@@@@@@@@@@@@@#,/@@&.. .,.,,.,..,..,..,..,.,,..,.,,.,,.,,..,,.,,.(@@@@@@
@@@@@@@@@@@@@@@@@@@%... *,,....*,,..,.., .,...........,.,,..,..,..,....,&@@@@@@
@@@@@@@@@@@@@@@@@@@@#..  .(/*****,*,*.............. ..............,..../@@@@@@@
@@@@@@@@@@@@@@@@@@# ....,#*/,**/**/,/,*.   ..... .. .. ......... .. ...&@@@@@@@
@@@@@@@@@@@@@@@@/....,,.(#((**/*(**/(//.      ......   .. ..  .  ....,.@@@@@@@@
@@@@@@@@@@@@@@*...(%#(#/.*/#(/(///**/(%&@&&%@&@&&&&@&&&&(*....     *. /@@@@@@@@
@@@@@@@@@@@%,...*#%@@@&@&%@@%/#,,,, ,/%@&&&@@@&@%&&%&%&&%%%&......  ,,#@@@@@@@@
@@@@@@@@@%,..,&@%&&*. ./&@&@@@&@@&&&,..  *(#%%&@@@@&%&&%%%@@.  ....,*/#@@@@@@@@
@@@@@@@@(..*#&&@@@@@@&&%,   ,/%&&@@&&&&(/.... */#%%&&&&@@@%..  ..   ,(&@@@@@@@@
@@@@@@@/,.,.  ../%@&&@@&&@&&%/.   .(&%&&@%%*.,,..(%#%#*#, .,. ...,//%&&@@@@@@@@
@@@@@@&/*,*/#*. ,  ,,(%&%&@@@&&&%#.   ,*(%(***%%((...  (%*,.....*/**%&&@@@@@@@@
@@@@&%(/*//*,,,***/. ,.   ..,...*/.,../((*.. (%/,**,,..*&&.,.,.%((/*%&@@@@@@@@@
@@@@&%#(////(%%#,,,*/,,.*, ...   ,,./(,..,,.,,%%#(*,..,/%(,.,*(%###(&@@@@@@@@@@
@@@@@@@@%#%%%&&&%#(/*,,,,*/*,..*,,*.,//**,,,,..*(/#%%&%%/.,,/(@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&&&&&&%#(((/,.,,,,,,/,,.,.*(,.,,,*.#* ..,.,.,,(%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&&&&&%%((//(/*,...,,,,.//////*,,,.,.,.,.*#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&&&&&%%#(///((/*,...,,,,,..,,,,,.*.#&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&%%#(/////(((/*,.......,(%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@&&&&&%#(((///////(((/(@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@&&&&&%###(((#(&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@&&&&%&@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")




















#Jayden's Code (you can put ascii art where i put the comment ascii art in
#the empty print statement)


# Cale Sumner, Jayden Williams, Ian Christensen, Daniel Embley

# link to draw.io NOTE:you may have to download it, then open with draw.io
# https://drive.google.com/open?id=14TYFIyxCwYK_H0DUVIljk2ds7WtEDSOJ

def choice(choice1, choice2, choice3, choice4, choice5):
    while True:
        choice = input("Choose 1 ," + choice1 + " , " + choice2 + " , " + choice3 + " , " + choice4 + " , " + choice5)
        if choice == choice1:
            return choice1
        elif choice == choice2:
            return choice2
        elif choice == choice3:
            return choice3
        elif choice == choice4:
            return choice4
        elif choice == choice5:
            return choice5
        else:
            print("Sorry that is not an option.")
            continue


def intro():

    # Intro 1 with title
    print("""  ,/   */ .(//*. ,*  .(*(/*//.*  .#   .((/, .*  .(,/,((/.*   / .///** .*.  /   
    ,,/ ,,/./    *,*,*,.(  .*    **,    .,  ., .*/*   .*  .*,,,/ /.   .,.,.. /   
    ,..*(./ *    /.*, .*(  .*    .(     ..      .*    .*  .*   / *,   ,.., .*/   
    *  / .*  ,/(,  *.  ,*  .*    ,*     ,.      ,.    ..  ..   *  ./(,  ..   *   
    ...........................................................................  
                             ,,                   .                        .,*   
     .,(.     .,(            .,              .,(.  .,**                     ,*   
     .,,       ,(  *, .,.  *,** ./,/*. ,*   .(.      **                ,*   ,*   
     .,,       ,( .(/*.  ,*  **  ( / /,*** .,.       ./                ,*   ,*   
     .,,       ,(  ,...    ,,,*  ... . .,  ,/         .     .               ,*   
     .,*.......,(    *(*,*   .* .,,(/ /,/, ,/            ,*.,/ .//,/   ,*   ,*   
     .,/.......,(  .,,   ,*  .*   ./   (.  ,*            ,*  ,./, .*,  ,*   ,*   
     .,,       ,(  ,*    .,. .*    *, .,   ,*     ,*,,/. .*       .*,  ,*   ,*   
     .,,       ,(  ,*    .,, .*    ,( (    ,,.      .*,  .*      ,*/.  ,*   ,*   
     .,,       ,(  .,.   .*  .*    .**,     ,*.     .*,  .*    ** ./.  ,*   ,*   
     .,/       ,/   ,/   ,/  .,     ,/       ,,     .*,  ,*   .*, .*,  ,,   ,*   
    ,////.   *////.  **/(   ,///,   *          //**/(*. *///*  *// */.*///.////  
                                   .(                                            
                                   (.                                            
                                  ,,""")

    print(
        "Welcome to the Quest for the Holy Grail! In this game you play as Arthur, son of Uther Pendragon, from the castle of Camelot. King of the Britons, defeater of the Saxons, Sovereign of all England! ... Yes, you are rather impressive aren't you? Today seems like any other day of you riding through your kingdom with your knights of the round table looking for dragons to save and damsels to slay or something along those lines.")

    print(
        '"Arthur! King of the Britons!" You hear a voice bellow from above and suddenly the clouds part over your head and a cheaply animated adaptation of the Lord your God shines his glory down upon you.')

    print(
        "You proceed with the ceremonial praising, grovelling and averting of your eyes for which God scolds you and tells you to stop sucking up.")

    print(
        "He then explains that he is charging you and your knights with a sacred task, to seek the Holy Grail! He doesn't really explain what it's for or why he wants you to find it, but it's got the word Holy in it, so that must make it important, right")
    # Allow user to continue with user input
    input("The Quest Begins! Continue?(press enter)")


# intro 2

def intro2():
    #ascii art
    print("""" """)


    print("Your sacred quest for the Holy Grail has begun! Where do you want to look first?")

    
    # first real choice, allows movement between major places
    choicea = choice("Camelot!", "The French Castle", "The Dark Forest", "A Nearby Village", "The Castle Anthrax")
    if choicea == "Camelot!":
        return camelot()
    if choicea == "The French Castle":
        return the_french_castle()
    if choicea == "The Dark Forest":
        return the_dark_forest()
    if choicea == "A Nearby Village":
        return a_nearby_village()
    if choicea == "The Castle Anthrax":
        return the_castle_anthrax()



# Camelot
def camelot():
    #ascii art
    print(""" """)

    print('''Oh alright, if you must! But you don't want to stay too long. 'Tis a silly place! You make your way into the stables 
    to find worthy steeds for yourself and your knights. Unfortunately the horses were all sold a few years back during the age of terrible
  glueshortage. You do however manage to find a coconut which you cut in half and give to your
   trusty servant Patsy who skillfully bangs the two halves together to make horse hoof noises. He's a prodigy on the coconuts that Patsy!''')
    print("press enter to return")
    input("")
    intro2()

def the_french_castle():
    #ascii art
    print(""" """)

    print("""You and your fearless knights ride gallantly to the castle... Well not ride exactly, you don't have horses.
     You sort of prance there, but you extend your hands as if you were holding reigns and it all looks very convincing!

"Hallo!" You call out when you reach the castle. You can see a man with a very distinguished looking mustache in
 the castle battlements, but he doesn't answer. "It is I, Arthur, King of the Britons!" Again, you get no reply. "We have come here on a
  sacred quest, and I wish to speak with your master!"

You get no response at all. Either the man can't hear you or he's ignoring you deliberately. If only you had some way to get his attention.""")
    print("press enter to return")
    input("")
    intro2()

def a_nearby_village():
    #ascii art
    print(""" """)

    print("""You hope to find clues in a nearby village but on your way your path is blocked by a man clad from head to toe in black armour.
"None shall pass!" He tells you.
You are left looking rather baffled. "What?"
"None shall pass!" He repeats.
"But I am Arthur, King of the Britons!"
"I move for no man!" The Black Knight tells you with an unwavering tone in his voice.
"But God has charged me with a sacred quest and I must reach the village!" You insist, but the Black Knight holds his ground.
"I will tell you for the last time... NONE shall pass!"
How very rude! You'd challenge this man to a duel in a second but unfortunately you managed to get your sword stuck in a stone awhile back. If only you had some way to convince the knight to let you pass.""")
    print("press enter to return")
    input("")
    intro2()

def the_dark_forest():
    #ascii art
    print(""" """)

    print("""And so, you and your knights boldly make your way towards the Dark Forest, which is no more than two swallow's flights away!
Oh, that's an unladen swallow's flight away, obviously. It's more than two laden swallow's flights away. Four really, if they had a coconut on a line between them.
Anyway, when you arrive at the forest, you come to a crossroads, where there are four signs. A sign saying "Camelot" which points back the way you came,
 a sign that says, "Certain Death!" Pointing to the east, a sign that says, "REALLY Certain Death!" Pointing to the west and a sign that says, 
 "Holy Grail this way!"  Pointing to the north. Where do you want to go?""")
    choicec = choice("Camelot", "Certain Death!", "REALLY Certain Death!", "Holy Grail this way!", "")
    if choicec == "Camelot":
        return intro2()
    if choicec == "Certain Death!":
        return certain_death()
    if choicec == "REALLY Certain Death!":
        return really_certain_death()
    if choicec == "Holy Grail this way!":
        return intro2()

def certain_death():
    #ascii art
    print(""" """)

    print("""You boldly head towards certain death with Sir Robin leading the way. Eventually your band comes to an abrupt halt when a three headed giant blocks your path.
"Halt!" Yells the first head. "Who goes there?"
"It is I, Arthur, King of the Britons!" You tell him rather proudly.
"Awhh, a King is 'e? Well isn't that fancy?" The second head says sarcastically. "Who does he think he's impressing?"
"Oh, you're just jealous 'cos you couldn't pull off a crown!" Says the third.
A rather long argument then starts between the three.
"I could if I wanted too!"
"No, he's right you know."
"You have a fat head."
"Ooo, I do not!"
"Look will you two shut up and let's kill the King!"
"Owh, why do you always want to kill everything?"
"And he wonders why we never have guests."
"Oh yeah, I'm sure it's got nothing to do with your signs."
"What's wrong with my signs?"
"You mean besides the fact that they've got 'Certain Death' written on them?"
"Hey, I spent ages making those signs!"
"Yes but you used our hands to make them."
"Well if he'd have done it, at least he'd have spelt them right."
"Yeah, the first five tries you kept writing 'Curtain Death'."
"Who'd be scared of a pair of curtains?"
"Oh yeah? Well you're ugly!"
"Your mother's ugly!"
"Boris, we're conjoined triplets! His mother's your mother."
"... Oh yeah."
While they're all busy arguing you...""")
    choiced = choice("Bravely run away!", "Fight the giant", "Sneak past the giant", "", "")
    if choiced == "Bravely run away!":
        return intro2()
    if choiced == "Fight the giant":
        return fight_giant()
    if choiced == "Sneak past the giant":
        return sneak_past_giant()

def fight_giant():
    #ascii art
    print(""" """)

    print("""You let out a fearless roar and attack the giant, who grabs you and lifts you up with his giant's hand.
"Did you see that?"
"See what?"
"He just attacked me!"
"So he did, the cheeky bastard!"
"What shall we do with him?"
"I say we throw him in the river."
"No, let's eat him!"
"Ooo, don't you dare! You know Kings are bad for my indigestion."
"And the bones get stuck in my teeth."
"Well I'm not throwing him in the river. That's littering that it!"
While the three heads are arguing the giant's hold on you grows tighter until eventually you are crushed in their grip. You've died!""")

    choicee = choice("Try Again", "Exit", "", "", "")
    if choicee == "Try Again":
        return certain_death()
    if choicee == "Exit":
        return exit()

def sneak_past_giant():
    #ascii art
    print(""" """)
    print("""While the giants heads are arguing between themselves, you manage to sneak past them and head deeper into the forest. In the background you can
     just about hear the surprise when they realize you're gone, followed by a long argument over who's fault it is.
      Sadly you get lost in the forest and are forced to turn back, but while you haven't found the Holy Grail you did manage to
       catch an unladen African swallow on the way.
""")
    input("Press enter to continue")
    intro2()

def really_certain_death():
    #ascii art
    print(""" """)

    print("""And so you and your brave knights ride boldly through the forest... 
No, I'm sure I can do better than that. I've used brave and bold before.
What haven't I used? Noble? Chivalrous? Valiant? Yes, valiant! I like 
that one!. You and your valiant knights ride through the forest.
Eventually you start to hear rustling in the trees. Sinister laughter 
echoes all around you and some spooky violin music starts playing in the
background.
"Ni!" You hear a noise from within the forest.
"Oh no!" You wail with horror. "Cover your ears men, we are in terrible danger!"
You and your knights cover your ears but you cannot block out the sound
of that most dreadful and wretched of words! "Ni!" The sound comes 
again as a group of knights in horned helmets surround you. "Pang!" 
Another knight cries, and "Nu womp!"   Yells another.
"No stop!" You cry out in agony. "I can't take it anymore! Please, have mercy!"
The leader of the knights then emerges through the trees too confront 
you and declares, "We are the Knights who say..." Yeah, you guessed it. 
"Ni!" And the other knights all start chanting "Ni" along with him. "And
we shall let not let you pass unless you bring us a wide border to a 
garden where small bushes are thickly planted, or a similar larger area 
with a path winding through it."
You look rather confused. "So you want a..."
"Yes!" He cuts you off. "We want... A shrubbery!""""")
    choicef = choice("Challenge the Knights to battle", "Go look for a shrubbery", "", "", "")
    if choicef == "Challenge the Knights to battle":
        return knight_battle()
    if choicef == "Go look for a shrubbery":
        return intro2()

def knight_battle():
    #ascii art
    print(""" """)

    print(""""I cannot let you interfere with my sacred quest!" You tell the 
Knights of Ni. "Knights of the round table... Attack!" A glorious battle
follows in which your followers hack away at the Knights of Ni with 
their sword and the Knights of Ni yell "Ni!" At you, but eventually your
men can attack no more. It turns out hacking at someone with a sword is
very difficult to do while covering your ears. Sadly you and you men 
are, for lack of a better word, Nid to death.""")
    choiceg = choice("Try Again", "Exit", "", "", "")
    if choiceg == "Try Again":
        return really_certain_death()
    if choiceg == "Exit":
        return exit()


def the_castle_anthrax():
    #ascii art
    print(""" """)

    print("""And so, you and your knights set out towards the legendary Castle Anthrax. The days turn to weeks,
     the weeks turn to months, the months unexplainably turn into hours and The Hours turns into a 2002 drama film
      starring Meryl Streep and Nicole Kidman, which I've heard is really good.
Anyways, you find yourself at the Castle Anthrax, where you are warmly welcomed at the door by eight school
 young blondes and brunettes, all between the ages of sixteen and nineteen and a half.
  Their's is a very lonely life of bathing,
  dressing, undressing and making exciting underwear,
   and they are utterly thrilled to meet so many handsome young knights.
"Greetings to you maidens. I am Arthur, King of the Britons!"
 You tell them, "And I have come here on a sacred quest to find the Holy Grail. Do you know where it is?"
"Oh your majesty, you must be exhausted, come, come! Rest in one of our beds!" Their leader Zoot suggests.
"I appreciate your hospitality young maiden, must I must find the Grail!
 Now is it here or not?" But every time you bring up the Holy Grail, Zoot changes the subject.
"But you are weary and you must rest!" She insists as she takes your arm. "You may sleep in my bed.
 It is a very big bed. I'd say it could fit say... A King and at least fifteen scantily clad young women.
  Just come up stairs with me and we shall tend to your wounds."
   You are lead to Zoot's bedroom where you find a rather kinky looking nun costume,
   which you slip into your inventory because... Uhh... Because it's a clue!
    Yes, that's why! A very vital clue to finding the Holy Grail... Yes.
"Now you lay there and let us do all the work." Zoot tells you. "I've been told by a very reliable source that the best
 cure for aching muscles is to cover yourself with melted chocolate and have three beautiful virgins lick it all off!"
At that moment, Sir Lancelot bursts in the room and pushes the women out of the way.
 "My Leige, we must escape this place! They do not have
 the Grail and these foul temptresses are trying to distract us from our holy mission!"
What will you do now?""")
    choiceh = choice("Get Out", "Sacrifice Self", "", "", "")
    if choiceh == "Get Out":
        return intro2()
    if choiceh == "Sacrifice Self":
        return sacrifice_self()

def sacrifice_self():
    #ascii art
    print(""" """)

    print("""Getting out from the bed you heroically try to shoo Sir Lancelot away. "Do not worry Sir Lancelot, I'll put these wicked wenches in their places!"
"Oh yes!" Zoot agrees. "Let him put us in our places!"
"Get away from him ye bride of Lucifer!" Lancelot yells, pushing the women back with his mighty shield.
"Oh, don't worry!" You tell him. "I can tackle this lot single handed!"
"Yes, please!" Zoot begs. "Let him tackle us single handed!"
"No sire, I shall not leave you!" Sir Lancelot insists as he starts to drag you out of the castle.
What do you say?""")
    choicei = choice("Very well if you insist", "No i can handle them", "", "", "")
    if choicei == "Very well if you insist":
        return intro2()
    if choicei == "No i can handle them":
        return handle_them()

def handle_them():
    print(""""Yes, he'll beat us easily! We haven't a chance!" Zoot calls as Lancelot pushes you down the corridor.
"No sire!" Lancelot yells. "We must leave now! You are in great peril!"
Look, let me go back in there and face the peril
"No, it's too perilous!" Lancelot tells you as he drags you out of the castle.
Look, it is my duty as King to sample as much peril as I can
"No, we've got to find the Holy Grail. Come on!"
Oh, let me have just a little bit of peril?
"No, it's unhealthy!"
I bet you're gay!
"... No I'm not."
""")
    input("press enter to continue")
    intro2()

intro()

intro2()
