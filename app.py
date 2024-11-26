import asyncio
import random
import pyanty as dolphin
from pyanty import DolphinAPI, STABLE_CHROME_VERSION
import requests

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDc3MGQ4MTQxMjIxOWU3ZmUxOGU1MjFhNDVmMjY5MTYzYjcxZTZlMGNjNmE0ODQzN2UwYzMyN2RmZWIxMDNkZDExZjVjYmM1MzAzMjYzODYiLCJpYXQiOjE3MzI2MTc5MzAuMjY4NjMyLCJuYmYiOjE3MzI2MTc5MzAuMjY4NjM0LCJleHAiOjE3MzUyMDk5MzAuMjYwMTExLCJzdWIiOiIzNjk2Mzc2Iiwic2NvcGVzIjpbXX0.MBYAt04KZE0d084tfSibCwznmbE0-2LYU6jSJ_t2hSVSPEupMi6_WqltTBHREdR5SLZXG5_fwZilxYWcIf0iDCgb8fRRu1y-w3fzT0cuK_jzWOkxIJ2Kl1ivLojefkQCns7thu1YiEVMKZ5hOkirJavVt8RovxvRIOmNK-hzeFPYmhiDcYqHm7DGnfpcfrAyX3sRCU-fkeEF4ipGRQWsbkmgwOEJrHZnwQdE2baH0piY5UqJC0kEq_4tklvPHCKWrGjfeHcz116GtXZ8mGUGM-36d-4bx11b5poytW8T_ndAVvBvgOH_hxWetx71q6bzV15kE79VgjsOyezULQ5JzjLP3vJlwQs6xu0JazxsdB9amvjNHlce2JcSMtAdyiEgk_fjP5Q8kn53an8BzKxVABTianlYG_CPiIq_BSJ89VEnHs3PYEoCuVhTCKSKc6MS2_BQBqvo68de8IwS5k5Ycy3vCjBDdSAwmv6qPhZm6zCjA4JuVoyiZrr_X50N3rF8yDFiSxZRWjSehEIG35aRM0NNOQpvFVCwSj-SwPwRVsWDevJgZLqpZ9wqPdUaKQIL5fZmW5oz8dxCSgLbju6qy9q8-fQ7_0vcDc9ZniORh_mFEsyPeRQ11_9DOrnBWYsKlnaGu1MWkEnfi-kSRlrGkKPPUt5b1FbJTslUcrPbFNQ'

headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get('https://dolphin-anty-api.com/browser_profiles', headers=headers)

profile_ids = []

for profile in response.json()['data']:
    profile_ids.append(profile['id'])

response = dolphin.run_profile(profile_ids[1])
print(response)
port = response['automation']['port']
ws_endpoint = response['automation']['wsEndpoint']

async def main():
    browser = await dolphin.get_browser(ws_endpoint, port, core='playwright')
    pages = await browser.pages()
    page = pages[0]
    await page.goto('https://www.youtube.com/watch?v=i_fPatDvfGY')
    await asyncio.sleep(60)
    await browser.disconnect()

asyncio.run(main())
dolphin.close_profile(profile_ids[1])