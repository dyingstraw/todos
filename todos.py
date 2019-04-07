# encoding = utf-8
import re
import os
import win32api
import win32gui
import win32con
from PIL import Image, ImageDraw,ImageFont
def drawTxtInPic(picPath="C:\\Users\\10836\\Desktop\\todos\\1.bmp",txtlist=[u"无待办事项"],lines=0):
    im01 = Image.open(picPath)
    im01=im01.convert("RGBA")
    w,h=im01.size
    im2 = Image.new("RGBA", im01.size,(0,0,0))
    draw2 = ImageDraw.Draw(im2)
    draw2.rectangle((int(w/2-350), int(h/2-100), int(w/2+350), int(h/2+100)), fill=(51, 51, 51, 128))
    fontSize =25
    font = ImageFont.truetype("c:/windows/fonts/msyh.ttc", fontSize)
    for index,txt in enumerate(txtlist) :
        draw2.text((int(w/2-350), int(h/2-100)+(fontSize+5)*(lines+index)),str(index)+":"+txt, fill=(255,255,255),font=font)

    blend = Image.blend(im01, im2, 0.5)
    # blend.show()
    blend.save("dist.bmp")
def switchWallPic(path = "C:\\Users\\10836\Desktop\\todos\\dist.bmp"):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
        "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") 
    #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
def todos(str1="- [ ] 腾讯性格测试 st:2017/04/07&end:2019/04/08&at:2017/04/07"):
    p=re.compile("^-\s\[[\s]?\][\s]?(\w*)")
    pdone=re.compile("^-\s\[[x,X]\][\s]?(\w*)")
    pat=re.compile("at:(20\d{2}/[0-1]?[\d]/[0-3]?[\d])")
    pst=re.compile("st:(20\d{2}/[0-1]?[\d]/[0-3]?[\d])")
    pend=re.compile("end:(20\d{2}/[0-1]?[\d]/[0-3]?[\d])")
    # print(str1)
    s=p.findall(str1)
    # 在几点完成
    s1=pat.findall(str1)
    # 开始时间
    s2=pst.findall(str1)
    # 结束时间
    s3=pend.findall(str1)
    if(s.__len__()>0):
        return s[0]+": DeadLine:"+s1[0]
    else:
        return ""

if __name__ == "__main__":
    with open("todo.md",encoding='utf-8') as f:
        txt=f.read()
    f.close()
    print(txt)
    todoss = txt.split("\n")
    print(todoss)
    txtlist=[]
    for todo in todoss:
        if todo!="":
            txt = todos(todo)
            if(txt!=""):
                txtlist.append(txt)
    drawTxtInPic(picPath="image/1.jpg",txtlist=txtlist,lines=0)
    # 这个要是绝对路径，相对路径好像壁纸更改不成功
    switchWallPic("C:\\Users\\10836\Desktop\\todos\\dist.bmp")