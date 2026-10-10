import msvcrt
import logging
logger = logging.getLogger("Calrov27")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
logger.addHandler(handler)

def Tusalma():
    karakter = msvcrt.getch()
    try:
        return karakter.decode("utf-8")
    except UnicodeDecodeError:
        return karakter

print("Hoşgeldiniz, belirli komutları çalıştırmak için aşağıdaki rehbere bakınız.\nW = İleri Gitmek\nA = Sola Gitmek\nS = Aşağı Gitmek\nD = Sağa Gitmek\nZ = Armed Moduna Geçmek\nX = Disarmed Moduna Geçmek\nC = Stabilize Moduna Geçmek\nH = Depth Hold Moduna Geçmek\nV = Mevcut Durumu Görüntülemek\nQ = Çıkış")

MitArmoderNicht = "Disarmed"
Xkoordinat = 0
Ykoordinat = 0
Depthhold = False
Stabilize = False

while(1):
    girdi = Tusalma()
    match girdi:
        case "W" | "w":
            logger.info("İleri gidildi.")
            Ykoordinat += 1
        case "A" | "a":
            logger.info("Sola gidildi.")
            Xkoordinat -=1
        case "S" | "s":
            logger.info("Geri gidildi.")
            Xkoordinat -=1
        case "D" | "d":
            logger.info("Sağa gidildi")
            Xkoordinat +=1
        case "Z" | "z":
                if MitArmoderNicht == "Disarmed":
                    logger.info("Armed moduna geçildi.")
                    MitArmoderNicht = "Armed"
                else: 
                    logger.info("Araç zaten Armed modunda.")
        case "X" | "x":
                if MitArmoderNicht == "Disarmed":
                    logger.info("Araç zaten Disarmed modunda.")
                else: 
                    logger.info("Disarmed moduna geçildi") 
                    MitArmoderNicht = "Armed" 
        case "C" | "c":
                if Stabilize == False:
                    logger.info("Stabilize moduna geçildi.")
                    Stabilize = True
                else: 
                    logger.info("Stabilize modu devre dışı bırakıldı.") 
                    Stabilize = False       
        case "H" | "h":
                if Depthhold == False:
                    logger.info("Depth Hold moduna geçildi.")
                    Depthhold = True
                else: 
                    logger.info("Depth Hold modu devre dışı bırakıldı.") 
                    Depthhold = False                    
        case "V" | "v":
              logger.info("=" * 35 + f"\nKoordinat = {Xkoordinat},{Ykoordinat}\n{MitArmoderNicht}\nStabilize Modu = {Stabilize}\nDepth Hold Modu = {Depthhold}\n" + "=" * 35)
        case "Q" | "q":
              logger.info("Program başarılı bir şekilde sonlandırılıyor")
              break
        
              
            