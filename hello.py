import itchat

Wchat = itchat.auto_login(hotReload=True)
friends = itchat.get_friends()[1:]
print(friends)

friend_Uid = ""
n = input("请输入好友的备注名称:")
for i in friends:
    if i["RemarkName"] == n:
        print("已经找到了好友的UID哦...")
        friend_Uid = i["UserName"]
        break
tex = input("send message:")
itchat.send_msg(tex, friend_Uid)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply_text = msg['Text']
    return reply_text 
t = text_reply()
print(t)
itchat.run()