blacklisted_tokens = set()

def blacklist_token(token:str):
    blacklisted_tokens.add(token)

def is_blacklisted_token(token:str) -> bool:
    return token in blacklisted_tokens