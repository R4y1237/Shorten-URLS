# Ray Wang
# 2023/10/09
# This program will take in a link and shorten it as much as possible or replace it with a preffered link name
# Uses https://cutt.ly/ as api

import requests

def shortenLink(long_link, name):
    Key = "db7590fd0f2ef5b152b1113470004765d98f7"
    link = "https://cutt.ly/api/api.php"

    pull = requests.get(link, params={"key": Key, "short": long_link, "name": name}).json()

    # pull produces a json string with 'url' as its name
    # 'url' value is a dictionary that must contain keyname of 'status'
    # if value of 'status' is 7, it means the request worked and the dictionary will contain all other information of the link including:
    # date, shortLink, title
    # otherwise, 'status' will contain a number corresponding to an error message

    try:
        short = pull["url"]["shortLink"]
        print(f"Shortened Link: {short}\n")

    except:
        status = pull["url"]["status"]
        if status == 1:
            print(
                "The shortened link comes from the domain that shortens the link, i.e. the link has already been shortened"
            )
        elif status == 2:
            print("The entered link is not a link")
        elif status == 3:
            print("The preferred link name is already taken")
            # give user link without preffered name
            shortenLink(long_link, "")
        elif status == 4:
            print("Invalid API key")
        elif status == 5:
            print("The link has not passed the validation. Includes invalid characters")
        elif status == 6:
            print("The link provided is from a blocked domain")
        elif status == 8:
            print(
                "You have reached your monthly link limit. You can upgrade your subscription plan to add more links."
            )
        else:
            print(f"Error Status: {status}")

#user input
link = input("Enter your link: ")
title = input(
    "Enter preffered link name (If you don't want a customised link name, leave blank): "
)

print("\n")
shortenLink(link, title)
