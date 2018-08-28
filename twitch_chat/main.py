from twitchstream import chat as twchat

main = twchat.TwitchChatStream('sladoy', 'oauth:nk5j3khe6zrwerotr4fxzqir8na3ua')
main.connect()
main.join_channel('oceanmud')
main.send_chat_message('oceanm1Bing')