# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# file = open('phones_info.csv','w',encoding='UTF-8_sig')
# file.write('old_price,new_price,name,about/n')
#
# url_params = {'categoryID':'6487','did':1,'offset':0}
# url = 'https://www.be.ge/'
# while url_params['offset']<300:
#     r = requests.get(url,params=url_params)
#     content = r.text
#     soup = BeautifulSoup(content, 'html.parser')
#     phones_block = soup.find('div',{'class':'row products-grid'})
#     all_phones= phones_block.find_all('div',{'class':'col-md-4 col-xs-12'})
#     for each in all_phones:
#         a = each.find('div',{'class':'brief-desc'})
#         ab=a.br.text
#         about = ab.replace(',','!')
#         price = each.find('div',{'class':'pull-left prices s-sm'})
#         new_p = price.find('span',{'class':'c-blue price s-xxl'})
#         new_price = new_p.text
#         old_p = price.find('span',{'class':'old-price'})
#         old_price = old_p.text
#         name = each.a.text
#         # print(old_price,new_price,name, about)
#         file.write(old_price + ',' + new_price + ',' + name + ',' + about + '/n')
#     url_params['offset']+=21
#     sleep(15)
#
