# - * - coding:utf-8 - * -
import requests
from bs4 import BeautifulSoup
import os

all_url = 'http://www.mzitu.com'


#http����ͷ
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}
#������ͷ�ƽ����

start_html = requests.get(all_url,headers = Hostreferer)

#�����ַ
path = '/home/lyt/mzitu/'

#��Ѱ���ҳ��
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text


same_url = 'http://www.mzitu.com/page/'
for n in range(1,int(max_page)+1):
    ul = same_url+str(n)
    start_html = requests.get(ul, headers = Hostreferer)
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text() #��ȡ�ı�
        if(title != ''):
            print("׼����ȡ��"+title)

            #win���ܴ���������Ŀ¼
            if(os.path.exists(path+title.strip().replace('?',''))):
                    #print('Ŀ¼�Ѵ���')
                    flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))
            href = a['href']
            html = requests.get(href,headers = Hostreferer)
            mess = BeautifulSoup(html.text,"html.parser")
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text #���ҳ��
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('�Ѿ�������ϣ�����')
                continue
            for num in range(1,int(pic_max)+1):
                pic = href+'/'+str(num)
                html = requests.get(pic,headers = Hostreferer)
                mess = BeautifulSoup(html.text,"html.parser")
                pic_url = mess.find('img',alt = title)
                print(pic_url['src'])
                #exit(0)
                html = requests.get(pic_url['src'],headers = Picreferer)
                file_name = pic_url['src'].split(r'/')[-1]
                f = open(file_name,'wb')
                f.write(html.content)
                f.close()
            print('���')
    print('��',n,'ҳ���')