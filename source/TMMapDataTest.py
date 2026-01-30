import tokens

tokens.get_new_tokens()

liveToken = getLiveTokenFromFile()
coreToken = getCoreTokenFromFile()

test_mapData(coreToken[0], liveToken[0])

#print(get_all_saved_wrs())