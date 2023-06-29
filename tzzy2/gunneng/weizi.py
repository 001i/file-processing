import os


class weizi:

    #前
    def qian(shuzu,text):
        wjname=[]
        for i in shuzu:
            wenjianming = os.path.splitext(i)[0]
            houzui = os.path.splitext(i)[1]
            wjname.append(text+wenjianming + houzui)
        return wjname

    #中
    def zhong(shuzu,text,shu):
        wjname = []
        for i in shuzu:
            wenjianming = os.path.splitext(i)[0]
            houzui = os.path.splitext(i)[1]
            qian=wenjianming[:shu]
            hou=wenjianming[shu:]
            wjname.append(qian+text+hou+houzui)
        return wjname

    #后
    def hou(shuzu,text):
        wjname = []
        for i in shuzu:
            wenjianming = os.path.splitext(i)[0]
            houzui = os.path.splitext(i)[1]
            wjname.append(wenjianming + houzui+text)
        return wjname

    #合
    def he(shuzu,text,shu):
        wjname = []
        if 1==shu:
            for i in shuzu:
                wenjianming = os.path.splitext(i)[0]
                houzui = os.path.splitext(i)[1]
                wjname.append(text + wenjianming + houzui)
            return wjname
        if 2==shu:
            for i in shuzu:
                wenjianming = os.path.splitext(i)[0]
                houzui = os.path.splitext(i)[1]
                qian = wenjianming[:shu]
                hou = wenjianming[shu:]
                wjname.append(qian + text + hou + houzui)
            return wjname
        if 3==shu:
            for i in shuzu:
                wenjianming = os.path.splitext(i)[0]
                houzui = os.path.splitext(i)[1]
                wjname.append(wenjianming + houzui + text)
            return wjname