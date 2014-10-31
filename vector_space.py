import math
import os
from PIL import Image
import hashlib
import time
import urllib,urllib2
from shutil import copyfileobj


class VectorCompare:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def buildvector(im):
  d1 = {}
  count = 0
  for i in im.getdata():
    d1[count] = i
    count += 1
  return d1
v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']

imageset = []

for letter in iconset:
  for img in os.listdir('Captcha_cleaned/%s/'%(letter)):
    temp = []
    if img != "Thumbs.db":
      temp.append(buildvector(Image.open("Captcha_cleaned/%s/%s"%(letter,img))))
    imageset.append({letter:temp})




def captchacker(captcha_name):
	
	set_cookie = urllib.urlopen("https://pizzaonline.dominos.co.in/slot-machine/").headers.getheader("Set-Cookie")
	sess_id = set_cookie[set_cookie.index("=")+1:set_cookie.index(";")]
	headers = {"Cookie": "session_id="+sess_id}
	in_stream = urllib2.urlopen(urllib2.Request(captcha_name,headers=headers))
	with open("captcha.png", 'wb') as out_file:
   	 copyfileobj(in_stream, out_file)

	in_stream.close()
	#image = urllib.urlretrieve(captcha_name, "captcha.png")
	im = Image.open("captcha.png")
	im = im.convert("P")
	im2 = Image.new("P",im.size,255)
	im = im.convert("P")

	temp = {}

	for x in range(im.size[1]):
	  for y in range(im.size[0]):
	    pix = im.getpixel((y,x))
	    temp[pix] = pix
	    if pix == 0: # these are the numbers to get
	      im2.putpixel((y,x),0)
	# new code starts here

	inletter = False
	foundletter=False
	start = 0
	end = 0
	letters = []

	for y in range(im2.size[0]): # slice across
	  for x in range(im2.size[1]): # slice down
	    pix = im2.getpixel((y,x))
	    if pix != 255:
	      inletter = True
	  if foundletter == False and inletter == True:
	    foundletter = True
	    start = y

	  if foundletter == True and inletter == False:
	    foundletter = False
	    end = y
	    letters.append((start,end))

	  inletter=False
	answer = []
	count = 0
	for letter in letters:
 	 m = hashlib.md5()
 	 im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
 	 #m.update("%s%s"%(time.time(),count))
 	 #im3.save("Captcha_cleaned/%s.gif"%(m.hexdigest()))
 	 count += 1

 	 guess = []

 	 for image in imageset:
  	  for x,y in image.iteritems():
  	    if len(y) != 0:
  	      guess.append( ( v.relation(y[0],buildvector(im3)),x) )

 	 guess.sort(reverse=True)
 	 #print "",guess[0][1]
 	 value = guess[0][1]
 	 answer.append(value)
 	return answer,sess_id
 	

