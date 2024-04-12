# from bigO import BigO
# from bigO import algorithm
#
# lib = BigO()


# def summ3(x: list):
#     if not x:
#         return 0
#     return x[0] + summ3(x[1:])
# print(summ3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def countdown(i):
    print(i)
    if i <= 0:  # Base     case
        return
    else:  # Recursive    case
        countdown(i - 1)


# countdown(10)


def summ(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(summ([1, 2, 3, 4]))


def summ2(x: list):
    if not x:
        return 0
    return x[0] + summ2(x[1:])


print(summ2([1, 2, 3, 4]))

# print(lib.test_all(summ))  # , array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(lib.test_all(summ2))  # , array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(lib.runtime(function=summ2, array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

import requests

headers = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8,uz;q=0.7
cache-control: max-age=0
cookie: usn_visitor_id=57645e6806220000da322c63a4020000d4b30100; akacd_www=2177452799~rv=73~id=589a8aa615ea4e393a7442752e198760; ak_bmsc=437498633B19D5D8F6A9F850886FD2BB~000000000000000000000000000000~YAAQV2ReaAOwpECDAQAANKamZBFMHYenF/qg7qC6/2M7ocSrzf1vFc6KHRIQjwSbSl4oeAbUtfcZxYqYAvKrL5grnwlGxDhf05bFePx4nt+IdG0c9iaNpkC0759q/r2vnSrnlJa5TbCE3n0QUPReSAvw/BvCoJJ6VCxDh793KqT93m/pkzRfyGBZyL0Wt3/LcgrepFE4+iiBCtoJblF8LTUlbEpxXVKngYuolA18VPE927hYBVUS4FQHS1BVdchE0SJEKiugs6b9LcDI7F+wLSpwyJ7rcwO5t0cK8RPNM3RQLlVRDJSKPEBcnmOBfhtCtYvRTXB1nK/lAu7DQvVbzb6zjSBKEv0pd+iM8+a7/t9t/UC8lQpPWcKkw3NgTsTNMwY/ypMrrc/jqQ==; bm_sz=EECC4547092912E08AAD63394A3FD9E6~YAAQV2ReaAWwpECDAQAANKamZBFrW64QKRBN0+gzyIs2ENyytGrjAGSjP/iPm+An7D8lMabcLR4Fel0BCbgaBBL5w881MEZKts7ZKzyiz/e+LMsTk/nkQibF0aeclbu9Of026WWdfX/7wxXpzREcKXE0xnGH5x0zuHbLtCwa3m0RRWY2zSzQvIjPAC0eAcgpAENxsSTpVXF/3K3ieF4eJkDaHJsTnvLs0eOhVs3PJXVU6GEE/1l8F68T0OSq6sZCDHA6xxVe9dblefQ0WMPFBkXsx86h9XBoD/J4s/eNrBezcjg=~3621426~3159856; usn_session_id=6384098816486404; cogv=education; usprivacy=1YNY; edu-page-views=1; gradSaveReminderShouldAppear=false; _abck=C06854C76BE3D31F36E0DCFB7670ECBF~0~YAAQV2ReaCOwpECDAQAAo66mZAhzp5acgsAe5Quk6tih1v1Fe/4aUlH2YoyfwSJCKP6BwB2gBI6lny4f61OVn+GEbS2YKhhB8+rCXaca8MzI7ea1bgS2hsQlSWamVqpSxyoZMevsFgibrfpt7CjAM7m9HycZeedBmTTE8tJKBlSGXkTGcHYD8iIVeSMthbHA/c+bRyb6G7wLapTSGCNZfQgOExoki+wtYvvmkFs7Mf5Wdhn4ky/3fIdi/PjKCS6oOch3KDXpPThlmxEYgtC7kIWTs2zJoIT96MYrd77a3Cqwv1PcX2AuukHCqTmoY0Yfsykw4BwgnF0BRcwbclhhPyPlyDVHWDIHv7ar3aSYpzH/m/60RBP1vZgB2P2BvkH1XuauqGEhAh8nE7IDbifQmX9BE/TH~-1~||-1||~-1; _pbjs_userid_consent_data=3524755945110770; g_state={"i_p":1663848193780,"i_l":1}; education-compare-slideout-state=collapsed; bm_sv=E457D647E36A11A5C1ABD9284CE6D728~YAAQV2ReaMK1pECDAQAAje6nZBEKgv+91zKd/nwmA6yUT9EF0KHRPAm1T4gSyAJ6JF2zpexnUQgLZ5ZcnjkUsDL6W566+acrl4GW7LvFuekxWtSY5lyveGppY2R5ZyEUrJaFItqavEscLuSB2vfZn2EupcSex1dURlGamc3i9CFPFIyhM64WHeaV+kb7qh4KSaRTplho5uTdC0J1FYNt/hB7D69Oh0IcedCd6al5ks6gLE1Z9KOoncanQ8bcscGi~1
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"""

# parse headers into dict of headers with double list comprehension
# headers = {k: v for k, v in [line.split(': ') for line in headers.splitlines()]}
hedaers = {k: v for k, v in list(line.split(": ") for line in headers.splitlines())}
url = "https://www.usnews.com/best-graduate-schools/api/search?format=json&program=top-business-schools&specialty=mba&_page={p}"
data = []
for p in range(1, 11):
    r = requests.get(url.format(p=p), headers=headers)
    for i in r.json()["data"]["items"]:
        data.append(i)

print(len(data))
