from facebook_imp import *


# Create an Ad  within created Adset
def adcreate(ad_set_id):
    #Image Hash
    image = AdImage(parent_id=ad_account_id)
    # Provide the absolute path of the image
    image[AdImage.Field.filename] = '/home/mafia/Downloads/pubg.jpg'
    image.remote_create()

    print(image[AdImage.Field.hash])


    #AdCreative
    fields = []
    params = {
        'body': 'Like My Page',
        'name': 'My Creative',
        'title': 'My Page Like Ad',
        'object_story_spec': {'page_id':'1961041583957344','link_data':{'image_hash':image[AdImage.Field.hash],'link':'https://facebook.com/1961041583957344','message':'try it out'}},
    }
    creative = AdAccount(ad_account_id).create_ad_creative(
        fields=fields,
        params=params,
    )
    print ('creative', creative)

    creative_id = creative.get_id()
    print ('creative_id:', creative_id, '\n')


    #Ad
    fields = []
    params = {
        'status': 'PAUSED',
        'adset_id': ad_set_id,
        'name': 'My Ad',
        'creative': {'creative_id':creative_id},
    }
    ad = AdAccount(ad_account_id).create_ad(
        fields=fields,
        params=params,
    )
    print ('ad', ad)

    return ad.get_id()



def adPreview(ad_id):
    #Ad Preview
    fields = []
    params = {
        'ad_format': 'DESKTOP_FEED_STANDARD',
        }
    print (Ad(ad_id).get_previews(
        fields=fields,
        params=params,
    ))


# get the list of Ads created
def readADS():
    print(AdAccount(ad_account_id).get_ads())


# Delete the Ads created
def deleteAd(adIDD):
    ad = Ad(adIDD)
    ad.remote_delete()
    print('Ad with ID: ', adIDD, 'deleted!')


# Pause the Ad if  it is in active state
def pauseAD(adID):
    ad = Ad(fbid=adID, parent_id=ad_account_id)
    ad.update({
    Ad.Field.status: Ad.Status.paused,
    })
    ad.remote_update()
    print('Ad with ID: ', adID,'paused!')


# Start the Ad if it is paused
def startAd(adID):
    ad = Ad(fbid=adID, parent_id=ad_account_id)
    ad.update({
    Ad.Field.status: Ad.Status.active,
    })
    ad.remote_update()
    print('Ad with ID: ', adID,'activated!')
