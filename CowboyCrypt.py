def encrypt():
    sentence = input("Type an sentence to encrypt: ")
    charDec = []
    charBin = []
    newSentence = ""
    for c in sentence:
        if(c=='a'):
            charDec.append(0)
        elif(c=='b'):
            charDec.append(1)
        elif(c=='c'):
            charDec.append(2)
        elif(c=='d'):
            charDec.append(3)
        elif(c=='e'):
            charDec.append(4)
        elif(c=='f'):
            charDec.append(5)
        elif(c=='g'):
            charDec.append(6)
        elif(c=='h'):
            charDec.append(7)
        elif(c=='i'):
            charDec.append(8)
        elif(c=='j'):
            charDec.append(9)
        elif(c=='k'):
            charDec.append(10)
        elif(c=='l'):
            charDec.append(11)
        elif(c=='m'):
            charDec.append(12)
        elif(c=='n'):
            charDec.append(13)
        elif(c=='o'):
            charDec.append(14)
        elif(c=='p'):
            charDec.append(15)
        elif(c=='q'):
            charDec.append(16)
        elif(c=='r'):
            charDec.append(17)
        elif(c=='s'):
            charDec.append(18)
        elif(c=='t'):
            charDec.append(19)
        elif(c=='u'):
            charDec.append(20)
        elif(c=='v'):
            charDec.append(21)
        elif(c=='w'):
            charDec.append(22)
        elif(c=='x'):
            charDec.append(23)
        elif(c=='y'):
            charDec.append(24)
        elif(c=='z'):
            charDec.append(25)
        elif(c=='A'):
            charDec.append(26)
        elif(c=='B'):
            charDec.append(27)
        elif(c=='C'):
            charDec.append(28)
        elif(c=='D'):
            charDec.append(29)
        elif(c=='E'):
            charDec.append(30)
        elif(c=='F'):
            charDec.append(31)
        elif(c=='G'):
            charDec.append(32)
        elif(c=='H'):
            charDec.append(33)
        elif(c=='I'):
            charDec.append(34)
        elif(c=='J'):
            charDec.append(35)
        elif(c=='K'):
            charDec.append(36)
        elif(c=='L'):
            charDec.append(37)
        elif(c=='M'):
            charDec.append(38)
        elif(c=='N'):
            charDec.append(39)
        elif(c=='O'):
            charDec.append(40)
        elif(c=='P'):
            charDec.append(41)
        elif(c=='Q'):
            charDec.append(42)
        elif(c=='R'):
            charDec.append(43)
        elif(c=='S'):
            charDec.append(44)
        elif(c=='T'):
            charDec.append(45)
        elif(c=='U'):
            charDec.append(46)
        elif(c=='V'):
            charDec.append(47)
        elif(c=='W'):
            charDec.append(48)
        elif(c=='X'):
            charDec.append(49)
        elif(c=='Y'):
            charDec.append(50)
        elif(c=='Z'):
            charDec.append(51)
        elif(c==' '):
            charDec.append(52)
        elif(c=='.'):
            charDec.append(53)
        elif(c=='0'):
            charDec.append(54)
        elif(c=='1'):
            charDec.append(55)
        elif(c=='2'):
            charDec.append(56)
        elif(c=='3'):
            charDec.append(57)
        elif(c=='4'):
            charDec.append(58)
        elif(c=='5'):
            charDec.append(59)
        elif(c=='6'):
            charDec.append(60)
        elif(c=='7'):
            charDec.append(61)
        elif(c=='9'):
            charDec.append(62)
        elif(c=='9'):
            charDec.append(63)
    for num in charDec:
        charBin.append("{0:6b}".format(num))
    for num in charBin:
        i = 0
        word = ""
        for c in str(num):
            if(i==0 and c=='1'):
                word += "Y"
            elif(i==0 and (c=='0' or c==' ')):
                word += "y"
            elif(i==1 and c=='1'):
                word += "E"
            elif(i==1 and (c=='0' or c==' ')):
                word += "e"
            elif(i==2 and c=='1'):
                word += "E"
            elif(i==2 and (c=='0' or c==' ')):
                word += "e"
            elif(i==3 and c=='1'):
                word += "H"
            elif(i==3 and (c=='0' or c==' ')):
                word += "h"
            elif(i==4 and c=='1'):
                word += "A"
            elif(i==4 and (c=='0' or c==' ')):
                word += "a"
            elif(i==5 and c=='1'):
                word += "W"
            elif(i==5 and (c=='0' or c==' ')):
                word += "w"
            i += 1
        newSentence += word + " "
    print(newSentence)
def decrypt():
    sentence = input("Type a sentence to decrypt: ")
    newSentence = ""
    i = 0
    for s in sentence:
        if(s==' '):
            numBin = ""
            n = 0
            for c in (sentence[i-6 : i]):
                if(n == 0 and c == 'Y'):
                    numBin += "1"
                elif(n == 0 and c == 'y'):
                    numBin += "0"
                if(n == 1 and c == 'E'):
                    numBin += "1"
                elif(n == 1 and c == 'e'):
                    numBin += "0"
                if(n == 2 and c == 'E'):
                    numBin += "1"
                elif(n == 2 and c == 'e'):
                    numBin += "0"
                if(n == 3 and c == 'H'):
                    numBin += "1"
                elif(n == 3 and c == 'h'):
                    numBin += "0"
                if(n == 4 and c == 'A'):
                    numBin += "1"
                elif(n == 4 and c == 'a'):
                    numBin += "0"
                if(n == 5 and c == 'W'):
                    numBin += "1"
                elif(n == 5 and c == 'w'):
                    numBin += "0"
                n += 1
            numDec = int(numBin, 2)
            if(numDec==0):
                newSentence += "a"
            elif(numDec==1):
                newSentence += "b"
            elif(numDec==2):
                newSentence += "c"
            elif(numDec==3):
                newSentence += "d"
            elif(numDec==4):
                newSentence += "e"
            elif(numDec==5):
                newSentence += "f"
            elif(numDec==6):
                newSentence += "g"
            elif(numDec==7):
                newSentence += "h"
            elif(numDec==8):
                newSentence += "i"
            elif(numDec==9):
                newSentence += "j"
            elif(numDec==10):
                newSentence += "k"
            elif(numDec==11):
                newSentence += "l"
            elif(numDec==12):
                newSentence += "m"
            elif(numDec==13):
                newSentence += "n"
            elif(numDec==14):
                newSentence += "o"
            elif(numDec==15):
                newSentence += "p"
            elif(numDec==16):
                newSentence += "q"
            elif(numDec==17):
                newSentence += "r"
            elif(numDec==18):
                newSentence += "s"
            elif(numDec==19):
                newSentence += "t"
            elif(numDec==20):
                newSentence += "u"
            elif(numDec==21):
                newSentence += "v"
            elif(numDec==22):
                newSentence += "w"
            elif(numDec==23):
                newSentence += "x"
            elif(numDec==24):
                newSentence += "y"
            elif(numDec==25):
                newSentence += "z"
            elif(numDec==26):
                newSentence += "A"
            elif(numDec==27):
                newSentence += "B"
            elif(numDec==28):
                newSentence += "C"
            elif(numDec==29):
                newSentence += "D"
            elif(numDec==30):
                newSentence += "E"
            elif(numDec==31):
                newSentence += "F"
            elif(numDec==32):
                newSentence += "G"
            elif(numDec==33):
                newSentence += "H"
            elif(numDec==34):
                newSentence += "I"
            elif(numDec==35):
                newSentence += "J"
            elif(numDec==36):
                newSentence += "K"
            elif(numDec==37):
                newSentence += "L"
            elif(numDec==38):
                newSentence += "M"
            elif(numDec==39):
                newSentence += "N"
            elif(numDec==40):
                newSentence += "O"
            elif(numDec==41):
                newSentence += "P"
            elif(numDec==42):
                newSentence += "Q"
            elif(numDec==43):
                newSentence += "R"
            elif(numDec==44):
                newSentence += "S"
            elif(numDec==45):
                newSentence += "T"
            elif(numDec==46):
                newSentence += "U"
            elif(numDec==47):
                newSentence += "V"
            elif(numDec==48):
                newSentence += "W"
            elif(numDec==49):
                newSentence += "X"
            elif(numDec==50):
                newSentence += "Y"
            elif(numDec==51):
                newSentence += "Z"
            elif(numDec==52):
                newSentence += " "
            elif(numDec==53):
                newSentence += "."
            elif(numDec==54):
                newSentence += "0"
            elif(numDec==55):
                newSentence += "1"
            elif(numDec==56):
                newSentence += "2"
            elif(numDec==57):
                newSentence += "3"
            elif(numDec==58):
                newSentence += "4"
            elif(numDec==59):
                newSentence += "5"
            elif(numDec==60):
                newSentence += "6"
            elif(numDec==61):
                newSentence += "7"
            elif(numDec==62):
                newSentence += "8"
            elif(numDec==63):
                newSentence += "9"
        i += 1
    print(newSentence)
eord = ""
while(eord!="E" and eord!= "D"):
    eord = input("Would you like to encrypt or decrypt? (E or D)? ").upper()
if(eord=="E"):
    encrypt()
else:
    decrypt()
    