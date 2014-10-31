from vector_space import captchacker
from BeautifulSoup import BeautifulSoup
import urllib2,urllib,httplib,cookielib,json
import re

url = "https://pizzaonline.dominos.co.in/slot-machine/captcha-action.php"
'''request = urllib2.Request(url)
with requests.session() as s:
	captcha = captchacker("https://pizzaonline.dominos.co.in/slot-machine/captcha.php?0.524428098462522")
	post_args = urllib.urlencode(captcha)'''
count = 0
while(count<100):
	count=count+1
	captcha,session_id = captchacker("https://pizzaonline.dominos.co.in/slot-machine/captcha.php?0.524428098462522")
	param=''.join(captcha)
	params = {'cap':param}
	request = urllib2.Request(url, urllib.urlencode(params))

	request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0')
	request.add_header('Referer', 'https://pizzaonline.dominos.co.in/slot-machine/')
	request.add_header('Accept', '*/*')
	request.add_header('Accept-Encoding', 'gzip, deflate,sdch')
	request.add_header('Accept-Language', 'en-US,en;q=0.8')
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Connection', 'keep-alive')
	request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	request.add_header('Cookie', 'session_id='+session_id+';')# _ga=GA1.3.2019570266.1414734490; _msuuid_1832kja11681=4D525FB8-6CBC-46BE-ACA6-7EDF19C1765D; __utma=146358305.2019570266.1414734490.1414734495.1414734495.2; __utmb=146358305.3.10.1414734495; __utmz=146358305.1414734495.2.2.utmgclid=CjwKEAjww8eiBRCE7qvK9Z7W_DgSJABfOjf2mtZztu4wOrxyS5JtFZVLo93Pn6sjzWrPR_nIQR76TRoCxAvw_wcB|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); __utmc=146358305; _gat=1; __utmt=1')
	request.add_header('Host', 'pizzaonline.dominos.co.in')
	request.add_header('Pragma', 'no-cache')
	request.add_header('X-Requested-With', 'XMLHttpRequest')
	request.add_header('Content-Length', '10')

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r = opener.open(request)
	#r = urllib2.urlopen(request)









	url2 = "https://pizzaonline.dominos.co.in/slot-machine/process-slot.php"
	params2 = {'session_id':session_id}
	request2 = urllib2.Request(url2, urllib.urlencode(params2))
	
	request2.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0')
	request2.add_header('Referer', 'https://pizzaonline.dominos.co.in/slot-machine/')
	request2.add_header('Accept', '*/*')
	request2.add_header('Origin','https://pizzaonline.dominos.co.in')
	request2.add_header('Accept-Encoding', 'gzip, deflate,sdch')
	request2.add_header('Accept-Language', 'en-US,en;q=0.8')
	request2.add_header('Cache-Control', 'no-cache')
	request2.add_header('Connection', 'keep-alive')
	request2.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	request2.add_header('Cookie', 'session_id='+session_id+';')
	#request.add_header('Cookie', ' _ga=GA1.3.2019570266.1414734490; _msuuid_1832kja11681=4D525FB8-6CBC-46BE-ACA6-7EDF19C1765D; __utma=146358305.2019570266.1414734490.1414734495.1414734495.2; __utmb=146358305.3.10.1414734495; __utmz=146358305.1414734495.2.2.utmgclid=CjwKEAjww8eiBRCE7qvK9Z7W_DgSJABfOjf2mtZztu4wOrxyS5JtFZVLo93Pn6sjzWrPR_nIQR76TRoCxAvw_wcB|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); __utmc=146358305; _gat=1; __utmt=1')
	request2.add_header('Host', 'pizzaonline.dominos.co.in')
	request2.add_header('Pragma', 'no-cache')
	request2.add_header('X-Requested-With', 'XMLHttpRequest')
	request2.add_header('Content-Length', '43')

	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	x = opener.open(request2)
	y = x.read()
	pos = y.find("slot_result")
	if(pos>=0):
		result = y[pos+14:pos+15]
		if(int(result)==2 or int(result)==1):
			pos = y.find("unique_coupon")
			print result
			print 
			print y
			print
			print session_id
			print
			print y[pos+16:pos+26]
			print
