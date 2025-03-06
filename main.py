from asyncore import loop
from pydoc import importfile

def loop(a) :
    total = 0 
    if str(a) == "SFJ" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會思考各種滿足及迎合他人的方法，最終令自己筋疲力盡\n你下決定之前要先詢問他人，否則會失去方向及十分焦慮\n你由於質疑自己嘅能力，十分需要他人的認可\n你會設想各種最壞的可能性，令自己更加不安\n")
        print("Option 2 \n你會變得十分焦慮，為自己與他人設立過高的標準，過度糾結細節\n你失去平常的親和力，容易與人產生爭執\n你會減少同人與世界的聯繫，不斸分析過去的負面記憶中不能自拔，並用冷酷尖酸的態度責備自己/他人\n另一呈現方式為過度著重細節與過度分析，給人吹毛求疵的感覺\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "NTP" : 
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會失去平常的冷靜與思考能力，會詢問他人來確定自己正在做對的事\n你比起平常更在意旁人的感受，由於會設想各種可能性，或會過度解讀人心木人情感\n你由於質疑自己嘅能力，十分需要他人的認可\n你會設想各種最壞的可能性，令自己更加不安\n")
        print("Option 2 \n你會失去平常的創意與探索精神\n你容易劃地為牢，表現得誠惶誠恐、患得患失\n因為過去的失敗，你覺得自己未來也不會成功\n你會減少同人與世界的聯繫，不斸分析過去的負面記憶中不能自拔，並用冷酷尖酸的態度責備自己/他人\n另一呈現方式為過度著重細節與過度分析，給人吹毛求疵的感覺\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "NFJ" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會十分注重自己的外在形象，需要從他人那裡得到認可來排除不安感\n沒有得到別人稱讚或認同的話會非常焦慮、情緒低落或發脾氣，可能會因此認為對方討厭自己\n你會瘋狂購物/吃東西/飲酒，無視這樣做可能帶來的後果\n")
        print("Option 2 \n你會容易停留在理想中而忽略現實，你傾向認為「完美」的事物是存在的，因此會強迫自己達到不切實際的高標準\n你會失去平常的親和力，給人冰泠的感覺\n你無法達成心目中的完美的話會對自己十分失望，容易過度操勞而不自知\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "STP" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會十分注重自己的外在形象，需要從他人那裡得到認可來排除不安感\n你會努力去討好別人、花費過多時間和心力在人際關係上、盲從同伴而失去主見\n你嘗試透過贈送禮物來修補關係，卻忽視了問題的深層成因\n")
        print("Option 2 \n你會容易停留在理想中而忽略現實，你傾向認為「完美」的事物是存在的，因此會強迫自己達到不切實際的高標準\n你會變得十分抽離、多疑、焦慮\n你會因為希望找出完美的處事手法而失去平常的執行力\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "STJ" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會思考各種可能性，儘管你未必有十足證據支持這些想法\n你會過早下判斷，失去平常實事求是的一面\n你不懂從過去學習\n你有新點子便改變舊有做法，過多的變化令自己與他人無所適從\n")
        print("Option 2 \n你會被果在過去的負面記憶中不能自拔，依舊感受到當時的心碎與失望\n基於過往失敗經驗，你不敢再踏出舒適圈，感到迷失 \n你失去平常的冷靜與執行力，變得優柔寡斷\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "NFP" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會思考各種可能性，儘管你未必有十足證據支持這些想法\n你會失去平常善解人意的一面，可能變得冷酷無情\n你會變成工作狂，無視自己的情緒 \n 你會過分執著輸贏/成功與否\n")
        print("Option 2 \n你會被果在過去的負面記憶中不能自拔，依舊感受到當時的心碎與失望\n你會失去平常的創意與探索精神\n你認為自己是個十惡不赦、品格低劣的廢物\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "NTJ" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會過於著重當下而忽略了未來，你未必會細想自己行動的後果，容易說出不顧他人感受的話\n你會用強硬、進取、甚至不道德的手段來完成當下的工作\n你行事魯莽，給人橫衝直撞的感覺，失去平時的遠見\n你為了完成而工作，卻沒有思考工作的目標與意義，令你欲速則不達\n")
        print("Option 2 \n你容易錯將腦海中的理想/自己未來的模樣當成是現實，因而忽略現實中的問題，變得自欺欺人\n你會變得多疑，容易把他人對你的意見當作人身攻擊\n你感覺到焦慮與不安，但認為自己十分理性，容易與他人造成衝突\n你因為多疑而容易對他人產生敵意\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total =  0
        elif loop == 2 :
            total =  1
        else :
            total =  10 
    if str(a) == "SFP" :
        print("\n")
        print("你喺有少少壓力，感覺陷入咗一個死循環嗰陣，邊個Option似你多啲？\n")
        print("Option 1 \n你會過於著重當下而忽略了未來，你未必會細想自己行動的後果，容易說出不顧他人感受的話\n你會用強硬、進取、甚至不道德的手段來完成當下的工作\n你失去平常活潑的一面，變得過於進取，甚至咄咄逼人\n你無法三思而行，容易下一些魯莽的決定、常與人產生衝突\n")
        print("Option 2 \n你容易錯將腦海中的理想/自己未來的模樣當成是現實，因而忽略現實中的問題，變得自欺欺人\n你會變得多疑，容易把他人對你的意見當作人身攻擊\n你活在幻想中，傾向無視客觀事實與他人的意見， eg即使另一半虧待自己，你也會選擇無視他的缺點\n你變得多疑和焦慮，失去安全感\n")
        print("Option 3 \n兩個都唔似\n")
        loop = int(input("答案："))
        if loop == 1 :
            total = total + 0
        elif loop == 2 :
            total = total + 1
        else :
            total = total + 10 
    return total

def grip(b) :
    total = 0
    if str(b) == "SFJ" :
        print("\n")
        print(" 當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時具同理心，擅長照顧他人和社交\n當你有很大壓力時，你會變得十分冷酷，不願顧他人感受，常冷嘲熱諷，甚至變得passive aggressive\n你會批判自己與他人、自我封閉、矯枉過正等\n")
        print("Option 2 \n你平時是可靠、勤勞、記憶力佳、循規蹈矩、做事有條理的人\n當你有很大壓力時，你會變得混亂、有種神不守舍的感覺、容易被新的想法擾亂，失去了平常井井有條的模樣\n你可能會想到一些很壞的可能性後開始杞人憂天，不過那些可能性未必有根據、或是發生機會根本不大\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "NTP" : 
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時具創造力、想像力、喜歡探索新事物、天馬行空\n當你有很大壓力時，你會停留在過去自己犯錯或是不愉快的經驗當中，因為害怕犯錯而失去活力與創意、變得畏首畏尾\n")
        print("Option 2 \n你平時以冷靜與擅長思考見稱\n當你有很大壓力時，你會大發雷霆、脾氣非常暴躁、甚至拿別人來出氣，失去了一貫的冷靜\n或者你會突然變得非常外向，在社交時容易失言，失去了平常三思而行的特徵\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "NFJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時具同理心，擅長照顧他人和社交\n當你有很大壓力時，你會變得十分冷酷，不願顧他人感受，常冷嘲熱諷，甚至變得passive aggressive\n你會批判自己與他人、自我封閉、矯枉過正等\n")
        print("Option 2 \n你平時具遠見、擅長設定目標與花很多時間思考抽象事物\n當你有很大壓力時，你會過度沉溺於感官世界（吃喝玩樂、性etc)、物質享受、對自己與他人的外表過於苛刻（有機會演變成飲食失調、整容上癮等\n你可能會變得漫無目的，不願去想未來與後果，變得衝動\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "STP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時是活在當下的享樂主義者，懂得如何烹受生活、重視物質、喜歡尋找感官刺激 \n但當你很大壓力時，你對未來及其不確定性感到極大恐懼，得很多疑而怪異\n你會過度沉溺在精神世界中，變得脫離現實、悲觀、失去熱情、甚至自欺欺人\n")
        print("Option 2 \n你平時以冷靜與擅長思考見稱\n當你有很大壓力時，你會大發雷霆、脾氣非常暴躁、甚至拿別人來出氣，失去了一貫的冷靜\n或者你會突然變得非常外向，在社交時容易失言，失去了平常三思而行的特徵\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "STJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時一貫的形象為效率高、果斷而冷靜、擅長帶領人群\n當你有很大壓力時，你會變得猶豫不決、質疑自己的決定是否正確、失去方向和目標、覺得自己所做的是沒有意義\n你會變得悲觀、屈服於內心一直積壓下來的不穴、憂鬱而沮喪\n")
        print("Option 2 \n你平時是可靠、勤勞、記憶力佳、循規蹈矩、做事有條理的人\n當你有很大壓力時，你會變得混亂、有種神不守舍的感覺、容易被新的想法擾亂，失去了平常井井有條的模樣\n你可能會想到一些很壞的可能性後開始杞人憂天，不過那些可能性未必有根據、或是發生機會根本不大\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "NFP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時具創造力、想像力、喜歡探索新事物、天馬行空\n當你有很大壓力時，你會停留在過去自己犯錯或是不愉快的經驗當中，因為害怕犯錯而失去活力與創意、變得畏首畏尾\n")
        print("Option 2 \n你平時是敏感、有強烈價值觀、重視自己感受、有同情心\n當你有很大壓力時，你會變得冷酷無情、過度重視結果與利益，繼而可能忽視個人道德與信念、㧗評旁人與事物為「沒有用」等等\n你會變成控制狂，與他人合作時逼別人服從自己、變成工作狂、變得衝動\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "NTJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時一貫的形象為效率高、果斷而冷靜、擅長帶領人群\n當你有很大壓力時，你會變得猶豫不決、質疑自己的決定是否正確、失去方向和目標、覺得自己所做的是沒有意義\n你會變得悲觀、屈服於內心一直積壓下來的不穴、憂鬱而沮喪\n")
        print("Option 2 \n你平時具遠見、擅長設定目標與花很多時間思考抽象事物\n當你有很大壓力時，你會過度沉溺於感官世界（吃喝玩樂、性etc)、物質享受、對自己與他人的外表過於苛刻（有機會演變成飲食失調、整容上癮等\n你可能會變得漫無目的，不願去想未來與後果，變得衝動\n")
        print("Option 3 \n兩個都唔似\n")
        lgrip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    if str(b) == "SFP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n你平時是活在當下的享樂主義者，懂得如何烹受生活、重視物質、喜歡尋找感官刺激 \n但當你很大壓力時，你對未來及其不確定性感到極大恐懼，得很多疑而怪異\n你會過度沉溺在精神世界中，變得脫離現實、悲觀、失去熱情、甚至自欺欺人\n")
        print("Option 2 \n你平時是敏感、有強烈價值觀、重視自己感受、有同情心\n當你有很大壓力時，你會變得冷酷無情、過度重視結果與利益，繼而可能忽視個人道德與信念、㧗評旁人與事物為「沒有用」等等\n你會變成控制狂，與他人合作時逼別人服從自己、變成工作狂、變得衝動\n")
        print("Option 3 \n兩個都唔似\n")
        grip = int(input("答案："))
        if grip == 1 :
            total =  0
        elif grip == 2 :
            total = 1
        else :
            total = 10 
    return total
def blind(c) :
    if str(c) == "SFJ" :
        print("\n")
        print(" 當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "NTP" : 
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "NFJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "STP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "STJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "NFP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "NTJ" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input(" 答案：")
    if str(c) == "SFP" :
        print("\n")
        print("當你有好大壓力，表現同平時幾乎完全相反嘅時候eg理性嘅會變得情緒化、鐘意享樂嘅會變得疑神疑鬼，你嘅表現似邊個option?\n")
        print("Option 1 \n\n\n\n")
        print("Option 2 \n\n\n\n")
        print("Option 3 \n兩個都唔似\n")
        loop = input("答案：")


def  cognitive_functions(cf) :
    if str(cf) == "Se" :
        print("- 對當下發生的事情很敏銳，能快速作出反應或描述自己的觀察\n- 熱愛身體上的自由，容易感到被管束\n- 會為了尋求刺激而做出冒險的行為，通常是與身體有關eg「如果我這樣做，會有什麼樣的感覺？」\n- 越即時的問題越能處理好，但對未來的事情支吾以對\n- 給人樂天的感覺，說話生動有節奏感\n- 姿態自然，眼神分為型格和精靈兩種，但都是很有焦點的\n- 動時生龍活虎，靜時沒精打彩 (活動不一定要有社交成分)")
        print("- 對紙上談兵沒有興趣，喜歡動手動腳做事\n- 多靠髮型、衣服、小飾物、紋身等來標記自己，或是用肢體語言來表達自己的想法\n")
    if str(cf) == "Si" :
        print("- 當有人找你傾訴時，會不斷引用自己的類似經歷，然後指出那些經歷和你的經歷有什麼異同，從而建立關係或給予建議\n- 一說到自己的經歷時容易變成滔滔不絕，因為會勾起很多當時的細節和感受，就像重新經歷一次一樣\n- 看到與自己認知有出入的事物時會比較大反應，例如說：「哇！這個好奇怪！」然後大笑（但如果是影響到你的話就會崩潰 哈哈）\n- 容易過度預測風險，連發生機率很低的意外都會害怕\n- 事情出錯後會說「都說應該xxx，有做到就不會這樣。」\n- 坐肢端正，眼神聚焦，說話時會猛瞪大眼\n-偶爾會說想試試新的事物，但目的是為了建立更好的習慣")
        print("- 越熟悉的事物越叫人安心，因為可預料性較高。反之，越不熟悉的事物，因為變數太多的關係就可免則免\n- 比起虛無飄渺的大方向，較喜歡清晰、仔細、有例可循的指示\n- 比較實事求是，重視事實根據，不容易接受沒有實證的理論\n- 因為常常跟從習慣行事的關係，一旦面對新挑戰或突發事件時會容易反應不過來，缺乏了應變能力方面的訓練\n")
    if str(cf) == "Ne" :
        print("- 說話時容易離題，會由一個話題聯想起另一個話題，再聯想起另一個話題，要很有意識地把自己拉回正題\- 興趣很廣泛，什麼也會一點點，但學習是出於好奇多過有實際用途\n- 不喜歡「萌塞」的想法，或容易覺得別人萌塞而自己比較開明（事實上不一定）\n- 會為了滿足好奇心而做出即興的行為，例如做實驗或冒小風險 (「如果我這樣做，會發生什麼事情？」)\n- 下判斷時會表現出不肯定、開放性、懷疑。常常回答「可能是也可能不是」、「不知道」、「到時就會知道」\n- 姿態如水，眼神發散沒焦點，有童真感 (例如：Mr. Bean)\n-偶爾會很留意事物細節，但目的是為了論證自己的新理論")
        print("- 當接觸事物時，會聯想出多個可能性和潛質。例如某件事除了按表面解讀之外，還有沒有其他忽視了的考慮因素？原本無關的事物能否加成在一起，產生新的火花？/n- 不喜歡把思維局限在常態當中，他們希望能打破常規，擁抱變幻無常的人生/n- 給人多疑、不相信自己、愛辯駁的印象，而且他們的結論大多為開放式，認為自己學得越多，懂得越少/n- 越新奇的事物越叫人興奮，因為能探索不同的可能性/n- 容易出現「三分鐘熱度」的情況，每被一個新idea吸引，就很容易對舊的idea失去興趣，結果很難完整地做好一件事情，也無法預料自己何時會突然放棄\n- 情還未發生之前都存在無數的可能性，即便你很早就計劃好，最後也是要根據實際狀況而作出調整，那倒不如隨遇而安\n- 習慣靈活應變，就算是事先計劃，也會有隨時不按計劃而行的心理準備，而這個結果也不會令他們很煩躁\n- 相比起不可預料性，他們更害怕局限了自己的選擇")
    if str(cf) == "Ni" :
        print("- 語句精闢獨到，也有貼題的意識\n- 傾向用概念詞歸納重點多於交代細節，甚至會用諷刺來表達一些只能意會，不能言傳的信息\n- 每次都會根據處境找出適當的做法，而不是參考之前的做法\n- 事情不是根據預期般發展時會感到焦躁，無法隨遇而安\- 經常說自己猜中了某些事情的發生，但又不是建基於一些具體的過往經歷，叫你解釋時又難以說出那個感知是從何而來\n- 有想善用肢體的傾向但略為不自然，眼神具穿透力，氣質神秘及有與世隔絕的感覺，彷彿第三身觀察者\n- 受壓時會想享受一下感官刺激 (吃喝玩樂) 但事後會感到心虛和自責，而且會顧著分析那個活動/物品的含義多於那個感受本身")
        print("- 記的並不是事件的細節，而是背後的含義\n- 很多事情表面上看似無關 (藍色的窗簾布是他媽的藍色)，但在你的世界裡，這些事情的含義、象徵意義都能連結起來 (藍色的窗簾布是解抑鬱，因為文章中有其他部分與「抑鬱」這個主題有關)\n- 旨在收窄範圍 (重深不重廣)，根據處境找出最準確的詮釋是什麼\n- 看待時間是流動性的，像一個趨勢圖，每一個部分都只是在揭示一個大整體，而這個河流都在向著某個方向流去，產生對未來的洞見 \n- 身處一個混亂的環境，不能線性地走到目標時，他們很容易感到焦慮不安\n ")
    if str(cf) == "Te" :
        print("- 喜歡問「這有什麼用」，事物的用途和對達到目的有沒有幫助很重要\n- 喜歡問「你怎樣看？」在日常中收集不同人在處事上的看法，從而了解外界的系統\n- 會很熱心地幫自己關心的人解決問題，甚至彷彿比當事人更上心，對方無力解決自己的問題時會感到嘆息\n- 對於一般閒雜人等會採取一副「你好自為之」的態度，認為人是要對自己負責的，別人幫不了你那麼多，失敗了就要承擔後果\n- 容易把自己的失敗歸咎於外在條件而不是自身\n- 想要維持效率，效率不夠高時容易煩躁\n- 熟絡後會留意到你有很澎湃、灼熱的感抑壓在內，但要你分享自己的情感時卻有一定困難，因為會自然地把焦點轉回客觀的考量點上\n- 對事不對人，所以未必能妥善解決情感方面的問題，可能會在社交場合說一些不不解溫柔的話\n- 給人老成持重的感覺，通常擔當規矩執行者或解決師的角色")
        print("- 對社會的遊戲規則越敏銳，但對自我的精神世界和價值觀越輕視，甚至視內心為一個人的弱點/n- 努力做好事情、達到目標，從外界獲取力量，只要有能者掌權或自己成為能者，世界就會變得更好/n- 避開依賴自己的主觀感受來做決定，因為這樣做就不公正、不客觀/n- 對自己的能力要求比較高，「到底我有沒有足夠的影響力？」成就與自尊有很大的關係\n- 重視知識的用途多於純為滿足好奇心\n")
    if str(cf) == "Ti" :
        print("- 被餵食資訊而無法獨自思考時會感到很困惑，要用自己的方式從頭學習一次才能真正學懂。常見問題是「為什麼？」\n- 沒有難度地表達自己看到的事實和真相，給人感覺直率。可能會不小心激怒別人，但會為了和諧而退讓\n- 一般情況都很隨和，但遇到不合理的事情時會突然變戰鬥格，尖銳地挑出對方邏輯上的問題\n- 不熱衷於管別人的事，也不喜歡被別人管\n- 說話時喜歡以「我認為」、「我同意/不同意」為起首\n- 會模仿常見的社交技巧和表情，但表情幅度較細，親切背後帶著陣陣的寒意和抽離感\n- 對付別人的方式是利用他們的邏輯來反攻他們，或假裝順應他們的邏輯來抽身\n- 會用嘲諷的態度面對不合理的事情，例如惡搞議題、自嘲等，以半認真的方式把真相揭露於人前")
        print("- 渴望抽離地進行獨立思考，推翻人類慣常的認知甚至突破傳統科學\n- 不喜歡施以控制和下達命令，最好就是各自有各自的做法\n- 會因為無法合理解釋自己的情感而感到困惑\n- 比起沈悶的日常閒聊更熱衷於探討有趣的知識\n")
    if str(cf) == "Fe" :
        print("- 對人觀察入微，能留意到人與人之間的關係，即便是秘密的關係可能也逃不過法眼，個別人士的隱藏情感他們可能也會察覺得到\n- 喜歡了解人的共同特性，包括人與人之間的相處之道和不同人格碰撞而產生的火花\n- 見到有拖後腿的人會盡量嘗試理解和看看有什麼可以幫忙，真的太沒得救時才會放棄治療，期間可能會犧牲了點效率和白費心機\n- 喜歡照顧別人的需要，但容易過分相信自己的猜測而忽略了對方真正的需要，強行幫忙可能會好心做壞事或侵害了對方的個人意願\n- 情感外顯，笑容大方\n- 給人和暖的感覺，但比較一視同仁，彷彿中央空調\n- 在群體中尋找角色，例如看看當下的社交環境有什麼未被填補的位置，再給補上，可能像「社交變色龍」\n- 容易對人不對事，會根據別人性子做判斷 -- 因為注視點始終是人，所以會圍繞他們對人的了解來思考和說話")
        print("- 以大整體的價值為基礎衡量做法是否合乎規範/群體文化、能滿足大部分人的需要、達到社交和諧等\n- 過分忠於自己而破壞團體陣形這些行為應免則免；每個人都是大整體的一分子，應為大整體服務\n")
    if str(cf) == "Fi" :
        print("- 無法表達自己時會感到很壓抑，但又會因為害怕衝突和受傷而不喜歡把隱藏的情感直接說出來，所以會透過間接渠道抒發。一般需要在建立足夠的信任後才能安心的把自己最脆弱或最奇特的一面展現出來\n- 沒有難度地表達自己對事情的感受，熟絡後給人感覺很真性情\n- 一般情況都很隨和，但當被人挑戰到自己很核心的價值時會突然變戰鬥格，禁不住發表自己的批判\n- 不熱衷於管別人的事，也不喜歡被別人管\n- 說話時喜歡以「我認為」、「我喜歡/不喜歡」、「我同意/不同意」為起首\- 年輕時給人柔軟、純真的感覺，可能會激發起別人的保護慾或欺負慾\n- 外貌通常比實際年齡年輕，有些年紀較大的為了讓自己看下去成熟點，會刻意留胡子或鍛鍊身形，否則容易被小看 ")
        print("- 以自己的一套語言衡量事情是否重要、該做、道德等，即便參考外界的價值觀，也是經過了長時間的內化和嚴格的篩選，確保自己的人格是能對得起自己的\n- 自我意識通常比較強，但不代表自私，而是渴望更了解自己和尋找對自己真正重要的價值\n- 雖然很重視活出真我，但同時也重視人的感受，所以年輕的你們最常見的煩惱就是難以找到配合外界和忠於自己的適當平衡，例如會因為直率不懂世故而開罪別人\n- 產生同理心，透過推己及人、回想個人經驗的方式來了解其他人的感受\n- 講求人的獨特性，所以對社會弱細社群和邊緣人士的關注一般會比較大\n- 對重視的事情熱情如火，對不重視的事情冷若冰霜，這方面非常兩極\n- 追求的是情感的強度，這能體現在對煽情作品的興趣\n")
    

         



print("Option 1 \n你會透過製造一些可以被聽到看到觸摸到的具體事物來表達自己的獨特價值或獨特想法 \n對你來說，作品就是你的身份證明\n")
print("Option 2 \n你顯得十分穩定，就像個修補城牆的人一樣每天努力的保護城裏的住民 \n你重視安全感，重視傳統、權威，也重視承諾、誠信、責任\n")
print("Option 3 \n你熱衷於探索精神領域，於你而言，直覺更多是精神追求\n你重視理想、價值、人文思想，希望透過探索抽象領域提升自己或群體的精神修養\n")
print("Option 4 \n你渴望自己成為智者，你對直覺的理解更接近智慧\n你渴望知道真相，以知識與頭腦解決未知的謎題，有時候會給人只想不做的感覺\n")
temperament = int(input("邊個option最似你?\n"))
if temperament == 1 :
    print("\n")
    print("你覺得以下嘅描述整體而言似唔似你？似嘅話打'yes'，唔似嘅話打'no' \n")
    cognitive_functions("Se")
    ansse = input("答案：\n")
    if str(ansse).lower() == "yes" :
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲？\n")
        print("Option 1:\n")
        cognitive_functions("Ti") 
        print("Option 2:\n")
        cognitive_functions("Fi")
        print("Option 3: 兩個都唔似\n")
        anstf = input("答案：\n")
        if int(anstf) == 1 :
            res = loop("STP") + grip("STP")
            if res == 2 :
                print("Your MBTI is ISTP")
            elif res == 0 :
                print("Your MBTI is ESTP")
            else:
                print("Sorry I don't know your MBTI") 
        elif int(anstf) == 2 :
            res = loop("SFP") + grip("SFP")
            if res == 2 :
                print("Your MBTI is ISFP")
            elif res == 0 :
                print("Your MBTI is ESFP")
            else:
                print("Sorry I don't know your MBTI") 
    else :
        print("ERROR")
elif temperament == 2 :
    print("\n")
    print("你覺得以下嘅描述整體而言似唔似你？似嘅話打'yes'，唔似嘅話打'no' \n")
    cognitive_functions("Si")
    anssi = input("答案：\n")
    if str(anssi).lower() == "yes" :
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲?\n")
        print("Option 1:\n")
        cognitive_functions("Te") 
        print("Option 2:\n")
        cognitive_functions("Fe")
        print("Option 3: 兩個都唔似\n")
        anstf = input("答案：\n")
        if int(anstf) == 1 :
            res = loop("STJ") + grip("STJ")
            if res == 2 :
                print("Your MBTI is ISTJ")
            elif res == 0 :
                print("Your MBTI is ESTJ")
            else:
                print("Sorry I don't know your MBTI") 
        elif int(anstf) == 2 :
            res = loop("SFJ") + grip("SFJ")
            if res == 2 :
                print("Your MBTI is ISFJ")
            elif res == 0 :
                print("Your MBTI is ESFJ")
            else:
                print("Sorry I don't know your MBTI") 
    else :
        print("ERROR")
elif temperament == 3 : #NF
    print("\n")
    print("你覺得以下邊個option嘅描述似你多啲？\n")
    print("Option 1:\n")
    cognitive_functions("Ne") 
    print("Option 2:\n")
    cognitive_functions("Ni")
    print("Option 3: 兩個都唔似\n")
    ansneni = int(input("答案：\n"))
    if ansneni == 1 : #Ne
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲?\n")
        print("Option 1:\n")
        cognitive_functions("Fe") #error
        print("Option 2:\n")
        cognitive_functions("Fi") #xnfp
        print("Option 3: 兩個都唔似\n")
        ansfefi = input("答案：\n")
        if int(ansfefi) == 1 : # NE+FE
            print("Your case is a bit complicated, please chat with me in-person")
        elif int(ansfefi) == 2 : # Ne+Fi
            res = loop("NFP") + grip("NFP")
            if res == 2 :
                print("Your MBTI is INFP")
            elif res == 0 :
                print("Your MBTI is ENFP")
            else:
                print("Sorry I don't know your MBTI")
    elif ansneni == 2 : #Ni
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲?\n")
        print("Option 1:\n")
        cognitive_functions("Fe") #xnfj
        print("Option 2:\n")
        cognitive_functions("Fi") #error
        print("Option 3: 兩個都唔似\n")
        ansfefi = input("答案：\n")
        if int(ansfefi) == 1 : # Ni+FE
            res = loop("NFJ") + grip("NFJ")
            if res == 2 :
                print("Your MBTI is INFJ")
            elif res == 0 :
                print("Your MBTI is ENFJ")
            else:
                print("Sorry I don't know your MBTI")
        elif int(ansfefi) == 2 : #Ni+Fi
            print("Your case is a bit complicated, please chat with me in-person")
    else :
        print("please start the test again as you may chose the wrong answer at the beginning")
elif temperament == 4 : #NT
    print("\n")
    print("你覺得以下邊個option嘅描述似你多啲？\n")
    print("Option 1:\n")
    cognitive_functions("Ne") 
    print("Option 2:\n")
    cognitive_functions("Ni")
    print("Option 3: 兩個都唔似\n")
    ansneni = int(input("答案：\n"))
    if ansneni == 1 : #Ne
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲?\n")
        print("Option 1:\n")
        cognitive_functions("Te") #error
        print("Option 2:\n")
        cognitive_functions("Ti") #xntp
        print("Option 3: 兩個都唔似\n")
        ansfefi = input("答案：\n")
        if int(ansfefi) == 1 : # NE+TE
            print("Your case is a bit complicated, please chat with me in-person")
        elif int(ansfefi) == 2 : # Ne+Ti
            res = loop("NTP") + grip("NTP")
            if res == 2 :
                print("Your MBTI is INTP")
            elif res == 0 :
                print("Your MBTI is ENTP")
            else:
                print("Sorry I don't know your MBTI")
    elif ansneni == 2 : #Ni
        print("\n")
        print("你覺得以下邊個option嘅描述似你多啲?\n")
        print("Option 1:\n")
        cognitive_functions("Te") #xntj
        print("Option 2:\n")
        cognitive_functions("Ti") #error
        print("Option 3: 兩個都唔似\n")
        ansteti = input("答案：\n")
        if int(ansteti) == 1 : # Ni+TE
            res = loop("NTJ") + grip("NFJ")
            if res == 2 :
                print("Your MBTI is INTJ")
            elif res == 0 :
                print("Your MBTI is ENTJ")
            else:
                print("Sorry I don't know your MBTI")
        elif int(ansteti) == 2 : #Ni+Ti
            print("Your case is a bit complicated, please chat with me in-person")
    else :
        print("please start the test again as you may chose the wrong answer at the beginning")
else:
    print ("其實打個number係咪真係咁難呢？")
    

        

            



    
            
        
   
    
