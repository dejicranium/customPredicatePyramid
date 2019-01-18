class UserAgentPredicate: 
    def __init__(self, val, config):
        self.val = val
    
    def text(self):
        return "device should be {}".format(self.val)
    
    phash = text
    
    def __call__(self, context, request):
        import re
        return re.search('mobi', request.user_agent, re.IGNORECASE) == True and self.val == "mobile"