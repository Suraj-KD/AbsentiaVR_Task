from facebook_imp import *


# Create Adset in created Campaign
def createAdset(campaign_id):
    fields = []
    params = {
        'status': 'PAUSED',
        'targeting': {'geo_locations':{'countries':['US']}},
        'daily_budget': '10000',
        'billing_event': 'IMPRESSIONS',
        'bid_amount': '20',
        'campaign_id': campaign_id,
        'optimization_goal': 'PAGE_LIKES',
        'promoted_object': {'page_id': page_id},
        'name': 'My AdSet',
    }
    ad_set = AdAccount(ad_account_id).create_ad_set(
        fields=fields,
        params=params,
    )
    print ('ad_set', ad_set)

    return ad_set.get_id()


# Get the list of Adset
def readAdsets():
    print(AdAccount(ad_account_id).get_ad_sets())


# Delete the created Adset
def deleteAdset(adSetID):
    adset = AdSet(adSetID)
    adset.remote_delete()
    print('Adset with ID: ', adSetID, 'deleted!')


# Pause  the Adset if it is in active state
def pauseAdset(adSetID):
    adset = AdSet(fbid=adSetID, parent_id=ad_account_id)
    adset.update({
    AdSet.Field.status: AdSet.Status.paused,
    })
    adset.remote_update()
    print('Adset with ID: ', adSetID,' paused!')


# Start the Adset if it is paused
def startAdset(adSetID):
    adset = AdSet(fbid=adSetID, parent_id=ad_account_id)
    adset.update({
    AdSet.Field.status: AdSet.Status.active,
    })
    adset.remote_update()
    print('Adset with ID: ', adSetID,' activated!')
