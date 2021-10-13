from notion.client import NotionClient

token_v2 = "0217a4cccaec69b8f49e42411ca5fe2e0644c125859a5081847c9d6c46d4fd1923dd77d996399206f6a5fb6a463b9b90a59cbf1d528bd1ea876d6cccae11194d5ca711da377c44fcd8491e819b8f "

# url = "https://www.notion.so/d441a23e9264477eaa45a967b548d52a"

url = "https://www.notion.so/js-5cf1291b4f3d42ca949d2d00df2a50bd"
client = NotionClient(token_v2=token_v2)
page = client.get_block(url)
print(page)


# test_url = "https://www.notion.so/ts-ts-js-ts-0f3b4a4675eb4389afea01af8f31b60e"
# c_page = client.get_block(test_url)
# print(c_page)



# for children_id in page.get("content"):
#     try:
#         print(children_id)
#
#         children = client.get_block(children_id)
#         print(children)
#     except:
#         print(1)


