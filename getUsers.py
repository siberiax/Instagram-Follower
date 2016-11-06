import mechanize
import re
from random import shuffle

def getUsers():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 'Chrome')]

    url = "https://www.instagram.com/accounts/login/?force_classic_login=&next=/oauth/authorize/%3Fclient_id%3D9d836570317f4c18bca0db6d2ac38e29%26redirect_uri%3Dhttp%3A//websta.me/callback%26response_type%3Dcode%26scope%3Drelationships%2Blikes%2Bcomments%2Bbasic%2Bfollower_list%2Bpublic_content"
    url2 = "https://websta.me/tag/"

    user = '____________'
    passwd = '____________'

    response = br.open(url)

    br.select_form(nr=0)
    br.form["username"] = user
    br.form["password"] = passwd
    success = br.submit()

    tags = ['love', 'instagood', 'photooftheday', 'tbt', 'cute', 'beautiful', 'happy', 'me', 'followme', 'follow', 'fashion', 'selfie', 'picoftheday', 'like4like', 'summer', 'friends', 'instadaily', 'girl', 'fun', 'tagsforlikes', 'smile', 'repost', 'igers', 'instalike', 'food', 'art', 'family', 'instamood', 'likeforlike', 'style', 'nature', 'nofilter', 'follow4follow', 'amazing', 'life', 'bestoftheday', 'fitness', 'vscocam', 'sun', 'beauty', 'swag', 'followforfollow', 'beach', 'music', 'sky', 'f4f', 'pretty', 'l4l', 'travel', 'dog', 'hair', 'tflers', 'vsco', 'sunset', 'photo', 'lol', 'party', 'foodporn', 'cool', 'girls', 'cat', 'makeup', 'baby', 'ootd', 'night', 'funny', 'iphoneonly', 'instapic', 'instagram', 'hot', 'instacool', 'webstagram', 'yummy', 'instasize', 'healthy', 'pink', 'tweegram', 'followback', 'iphonesia', 'black', 'my', 'blue', 'instafollow', 'model', 'gym', 'work', 'motivation', 'christmas', 'instalove', 'igdaily', 'sweet', 'red', 'birthday', 'flowers', 'awesome', 'wcw', 'instafood', 'throwback', 'nyc', 'design']

    shuffle(tags)

    usersAndPics = {}

    for i in range(50):
        tag = tags[i]
        res = br.open(url2 + tag)

        string = res.read()
        user = re.findall(":&quot;(\d+_\d+)&quot;,&quot;user&quot;:{&quot;username&quot;:&quot;(.*?)&quot;", string)
        for u in user:
            usersAndPics[u[1]] = u[0]

    return usersAndPics
