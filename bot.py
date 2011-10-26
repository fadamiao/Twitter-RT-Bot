#! /usr/bin/python
import twitter, time

# Author = Fernando A. Damiao
# Last Mod = dom 25 set 2011
# Hosted on Git Hub : https://github.com/fa-damiao/Twitter-RT-Bot
# Build and Tested on Mac OS X 10.6 (a.k.a Snow Leopard)

# Next Feature = Use regex(?) for make a list with a variations of a hashtag
# Next Feature = Make a error log
# Next Feature = Auto #FF, make a list in XML with the users

#Insert here the Tokens from Twitter Developers
myconsumer_key = ''
myconsumer_secret = '' 
oauth_token = ''
oauth_token_secret = ''

api=twitter.Api(consumer_key = myconsumer_key,consumer_secret = myconsumer_secret, access_token_key = oauth_token,access_token_secret = oauth_token_secret)

mentions = api.GetMentions()

print '======== Last Mentions ========'
for m in mentions:
    print m.id, m.user.screen_name, m.text

lastmention = mentions[0].id

print '=================================='

#Dont delete anything above this line
while True:
    time.sleep(20)
    mentions = api.GetMentions(since_id = lastmention)
    print '=================================='
    for m in mentions:
        text1 = m.text.replace('@perfil_da_aplicacao', '')
	if m.user.screen_name == 'INSERTYOURUSERHERE':
		print 'Oops try self RT'
        elif (m.user.screen_name != 'INSERTYOURUSERHERE') and (text1.find('#INSERTTHEHASHTAG') >= 0):
                status = api.PostUpdate('RT @' + m.user.screen_name + ': ' + m.text)
        else:
		print 'Error'

    if m.id > lastmention:
         lastmention = m.id