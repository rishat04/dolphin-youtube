import asyncio
import random
import pyanty as dolphin
import requests

from playwright.sync_api import sync_playwright, expect

# api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDc3MGQ4MTQxMjIxOWU3ZmUxOGU1MjFhNDVmMjY5MTYzYjcxZTZlMGNjNmE0ODQzN2UwYzMyN2RmZWIxMDNkZDExZjVjYmM1MzAzMjYzODYiLCJpYXQiOjE3MzI2MTc5MzAuMjY4NjMyLCJuYmYiOjE3MzI2MTc5MzAuMjY4NjM0LCJleHAiOjE3MzUyMDk5MzAuMjYwMTExLCJzdWIiOiIzNjk2Mzc2Iiwic2NvcGVzIjpbXX0.MBYAt04KZE0d084tfSibCwznmbE0-2LYU6jSJ_t2hSVSPEupMi6_WqltTBHREdR5SLZXG5_fwZilxYWcIf0iDCgb8fRRu1y-w3fzT0cuK_jzWOkxIJ2Kl1ivLojefkQCns7thu1YiEVMKZ5hOkirJavVt8RovxvRIOmNK-hzeFPYmhiDcYqHm7DGnfpcfrAyX3sRCU-fkeEF4ipGRQWsbkmgwOEJrHZnwQdE2baH0piY5UqJC0kEq_4tklvPHCKWrGjfeHcz116GtXZ8mGUGM-36d-4bx11b5poytW8T_ndAVvBvgOH_hxWetx71q6bzV15kE79VgjsOyezULQ5JzjLP3vJlwQs6xu0JazxsdB9amvjNHlce2JcSMtAdyiEgk_fjP5Q8kn53an8BzKxVABTianlYG_CPiIq_BSJ89VEnHs3PYEoCuVhTCKSKc6MS2_BQBqvo68de8IwS5k5Ycy3vCjBDdSAwmv6qPhZm6zCjA4JuVoyiZrr_X50N3rF8yDFiSxZRWjSehEIG35aRM0NNOQpvFVCwSj-SwPwRVsWDevJgZLqpZ9wqPdUaKQIL5fZmW5oz8dxCSgLbju6qy9q8-fQ7_0vcDc9ZniORh_mFEsyPeRQ11_9DOrnBWYsKlnaGu1MWkEnfi-kSRlrGkKPPUt5b1FbJTslUcrPbFNQ'
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg4Y2Y5ZGNlMDBmODc3MjI2NDQ1Mzg3NGE3ZTJkNjc2NDEyOGRjNmFjNzc0NWVjN2RjYjI4NzUyNDQyMTAyYWUxY2EwNmI2MWJjOTUxOTciLCJpYXQiOjE3MzI2NDk5MTMuMDc4MzU5LCJuYmYiOjE3MzI2NDk5MTMuMDc4MzYxLCJleHAiOjE3MzUyNDE5MTMuMDcxMTY4LCJzdWIiOiIxODA0NiIsInNjb3BlcyI6W119.RXr4PUq23H31Khu5OLQnp0xagDxzEETGP06eyfaR3SJFzOnDZB-YW6P6s4gCnnc3Weal_29N3CKfKkezdZwxW1eH5SHv1gk96JOxZclqkTildsfdpl6NpKvSdO4Z-mLRwqeJEoC0niciuWfOh0PpHsuS5r-qg7ruO1xUGXUDrkXm-PBfjdHLCztvATnGG2Vie8AxAmZ-6LV3vWgYF3r_TONzTyJ1NoAy239S7vxnewle2Afqu8aAK22R1oOMzOJOrEdab6FMiNkWs073ADrkKkVyD0Ine8Gw0MzVD_-dwONe4YU5UrUTxClCo27zNjrPoRDVWrkDLj-OliMtUVk_PmyMxaeNOxBP7WCWGGudkjyAIfDO64wFZIOjaJ-QAAKOQaPUsAsvkBiyP_S9AvMJjVsuxY1mAA_xmhxhIwsigSz2r59m7hYpAwdcUZHyy6WqPBdalM7GI6-z5WEZJuQUqWTsUSaQlbkbS_6PNmdhMypc7DUWBRLmuZGWlASZkkPf0-yqarJEsDV1JpuZhgCwyji2GXPV9Do4IkNLNe2tpjtvaIVdpRPUqH9-wBI7KuXnAZg4c1HJF89-VnXU9c3vgMtuQWGPfjPyO3uXCxVb3DVoCHp9u8rzQuIID4Jp5ScBsNV3ZZdvJo_D141ERLANZtn9jam87J9Gi8Y7fX-WrmM'

# headers = {"Authorization": f"Bearer {api_key}"}

# response = requests.get('https://dolphin-anty-api.com/browser_profiles', headers=headers)
# profile_ids = []

# if response.json()['data']:
#     for profile in response.json()['data']:
#         profile_ids.append(profile['id'])

profile_id = 479431620

def main():
    response = dolphin.run_profile(profile_id)
    print(response)
    port = response['automation']['port']
    ws_endpoint = response['automation']['wsEndpoint']

    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_endpoint}')

        # browser = await dolphin.get_browser(ws_endpoint, port, core='playwright')
        page = browser.contexts[0].pages[0]
        
        page.goto('https://www.youtube.com/watch?v=i_fPatDvfGY', timeout=0)
        page.wait_for_load_state('networkidle')

        page.click("//button[contains(@class, 'ytp-large-play-button ytp-button')]")
        # await asyncio.sleep(5)
        scroll_count = 5
        while scroll_count:
            page.locator("//ytd-comments[contains(@id, 'comments')]").scroll_into_view_if_needed()
            page.wait_for_timeout(2000)
            scroll_count -= 1

        try:
            page.wait_for_selector("//ytd-comment-simplebox-renderer//div[@contenteditable='true']", timeout=30000)
            print("Comment box is available")

            # JavaScript code to insert comment and click submit
            page.evaluate(f"""
                var commentBox = document.querySelector('ytd-comment-simplebox-renderer div[contenteditable="true"]');
                var submitButton = document.querySelector('ytd-comment-simplebox-renderer #submit-button');

                if (commentBox) {{
                    commentBox.innerHTML = 'asdasdasd';
                    commentBox.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    submitButton.click();
                }}
            """)
            print("Comment posted")
        except Exception as e:
            print(f"Error: {str(e)}")
            #creation-box
        # await browser.disconnect()
        dolphin.close_profile(profile_id)

# asyncio.run(main())
if __name__ == '__main__':
    main()