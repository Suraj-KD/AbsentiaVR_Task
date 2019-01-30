from facebook_imp import *

print('In camps.py')

# Create campaign with setting provided in params argument
def createCamp():
    fields = []
    params = {
        'objective': 'PAGE_LIKES',
        'status': 'PAUSED',
        'buying_type': 'AUCTION',
        'name': 'My Campaign',
    }
    campaign = AdAccount(ad_account_id).create_campaign(
        fields=fields,
        params=params,
    )
    print ('campaign', campaign)

    campaign_id = campaign.get_id()
    return campaign_id

# get  the list of campaign created in app
def readCampaigns():
    print((AdAccount(ad_account_id)).get_campaigns())


# Delete Campaign by providing id of created Campaign
def deleteCampaigns(campIDD):
    campaign = Campaign(campIDD)
    campaign.remote_delete()
    print('Campaign with ID: ', campIDD, 'deleted!')


# Pause the Campaign if it in active state
def pauseCamp(campIDD):
    camp = Campaign(fbid=campIDD, parent_id=ad_account_id)
    camp.update({
    Campaign.Field.status: Campaign.Status.paused,
    })
    camp.remote_update()
    print('Campaign with ID: ', campIDD,'paused!')


# Start the Campaign if it is paused
def startCamp(campIDD):
    camp = Campaign(fbid=campIDD, parent_id=ad_account_id)
    camp.update({
    Campaign.Field.status: Campaign.Status.active,
    })
    camp.remote_update()
    print('Campaign with ID: ', campIDD,'activated!')
