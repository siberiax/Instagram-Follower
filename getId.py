import mechanize
import re

def getUserId(username):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 'Chrome')]

    url = "https://smashballoon.com/instagram-feed/find-instagram-user-id/?username="
    url += username
    response = br.open(url)

    user_id = re.findall("<b>User ID: (.*?)</b>", response.read())

    return (user_id[0])
