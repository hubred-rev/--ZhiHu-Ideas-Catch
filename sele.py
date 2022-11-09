from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time,os
import requests as r
br=wd.Firefox()
n=0
ni=0
br.get('https://www.zhihu.com/people/gong-ge-cheng-52/pins?page=1')
nm=int(br.page_source.split('<button type="button" class="Button PaginationButton PaginationButton-next Button--plain">下一页</button>')[0].split('<button type="button" class="Button PaginationButton Button--plain">')[-1:][0].split('<')[0])
print('總頁數：',nm)
while True:
    np=0
    if(nm-n)==0:break
    br.get('https://www.zhihu.com/people/gong-ge-cheng-52/pins?page=%d'%(nm-n))
    cl=br.find_element(By.XPATH,'//*[@class="Button Modal-closeButton Button--plain"]')
    if cl:cl.click()
    while True:
        br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ps1=br.page_source
        time.sleep(0.5)
        ps2=br.page_source
        if ps1==ps2:break
    it=br.find_elements(By.XPATH,'//*[@class="Zi Zi--ArrowDown ContentItem-arrowIcon"]')
    print('第%d頁縮放想法數目：'%(nm-n),len(it))
    for a in it:
        a.click()
    tl=br.page_source.split('<div class="List-item" tabindex="0">')[1:]
    tl[len(tl)-1]=tl[len(tl)-1].split('<div class="Pagination">')[0]
    tl2=[]
    for a in range(len(tl)):
        tl2.append(tl[len(tl)-a-1])
    tl=tl2
    print('第%d頁想法數目：'%(nm-n),len(tl))
    for a in tl:
        ni+=1
        os.makedirs(pa:=str(ni).rjust(6).replace(' ','0'))
        f=open('%s/text.htm'%pa,'w+');f.write(a);f.close()
        pl=[b.split('"')[0]for b in a.split('data-original="')[1:]]
        if'<em class="Thumbnail-Surplus-Sign">'in a:
            npx=br.find_elements(By.XPATH,'//*[@class="Thumbnail-Surplus-Sign"]')
            try:npx[len(npx)-1-np].click()
            except:br.execute_script("window.scrollBy(0, -128);");npx[len(npx)-1-np].click()
            while True:
                if'class="ImageGallery-arrow-right ImageGallery-arrow-disabled"'in br.page_source:break
                br.find_element(By.XPATH,'//*[@class="Zi Zi--ArrowRight"]').click()
                try:plz=br.page_source.split('class="ImageGallery-Img ImageGallery-fixed ImageGallery-CursorZoomIn"')[1].split('data-original="')[1].split('"')[0]
                except:
                    time.sleep(2)
                    plz=br.page_source.split('<div class="ImageGallery-Inner">')[1]
                    plz=plz.split('data-original="')[1].split('"')[0]
                pl.append(plz)
            br.find_element(By.XPATH,'//*[@class="Zi Zi--Close"]').click()
            np+=1
        pl2=[]
        for b in pl:
            if b not in pl2:pl2.append(b)
        pl=pl2
        pn=0
        for b in pl:
            pn+=1
            d=r.get(b,stream=True,timeout=5)
            f=open('%s/%s.jpg'%(pa,str(pn).rjust(6).replace(' ','0')),'wb+');f.write(d.content);f.close()
    n+=1
br.quit()
