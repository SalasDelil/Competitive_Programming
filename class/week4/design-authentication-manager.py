class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.token = defaultdict(int)
        self.time = timeToLive

    def generate(self, tokenId, currentTime):
        self.token[tokenId] = currentTime

    def renew(self, tokenId, currentTime):
        limit = currentTime-self.time
        if tokenId in self.token and self.token[tokenId]>limit:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime):
        limit = currentTime-self.time
        c = 0
        for i in self.token:
            if self.token[i]>limit:
                c+=1
        return c