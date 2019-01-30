from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adimage import AdImage
from facebook_business.api import FacebookAdsApi

# User Access Token obtained from Facebook Developer portal
access_token = 'EAAEAmvRsZCaMBAOGpnY6LaF1D1nKWedYvmZCGrFySjZBOtdXJBHsFdIAXmp6x6Co4ZCCVr7VpoKVaj86ZCXE3zrZB9OLN19bYDh6BLirOGylUpOvw5HZBmxHGwttLwsbq0GjFiyxRCUX5oDp12eWRbNEgdunruQ5J5KeIDD0b2jigZDZD'

# AdAcount id
ad_account_id = 'act_2040033849620997'
# app secret obtained after creating app
app_secret = '05bf4eb4dbabf197696687484bfac836'
# Page id of the page created by you in facebook
page_id = '827663007299658'
# app id of the created app
app_id = '282140502457763'

# initialize Facebook api objects with user access toekn
FacebookAdsApi.init(access_token=access_token)
