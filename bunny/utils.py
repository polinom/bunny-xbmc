from xbmc import executebuiltin
from simplejson import loads, dumps
from datetime import datetime
# from etvnet.auth import Auth
import urllib2
try:
    import simplejson as json
except:
    import json
from etvnet.define import *


# in order to use this cache_responce decorator 
# 'self' suppose to have 'Cache' object in '_cache' attribute
def cache_responce(request_method):
    def cahed_request_method(self, path, use_cache=True, *args, **kwargs):
        if use_cache:
            resp = self._cache.get(path)
            if not resp:
                resp = request_method(self, path, *args, **kwargs)
                self._cache.set(path,resp)
            return resp
        else:
            return request_method(self, path, *args, **kwargs)
    return cahed_request_method


# in order to use this hendles_http_server_errors decorator 
# self suppose to have 'access_token' attribute
def hendles_http_server_errors(request):
    def changed_request(self, *args, **kwargs):

        # if HTTP error with status 401  end responce error is invalid token,
        # then we need refresh the access token
        try:
            resp = request(self, *args, **kwargs)
        except urllib2.HTTPError, e:
            print e
            if e.code == 401 and json.loads(e.read())['error'] == 'invalid_token':
                auth = Auth()
                success, resp = auth.get_token(refresh=True)
                if success == auth.SUCCESS:
                    self.access_token = auth.access_token
                    return request(self, *args, **kwargs)
                else:
                     CloseWindow()
                     ShowDialogNotification(str(e))
                     return 
            elif e.code not in [201,204,206,404]:
                # temporary print error for user SERVER_ERROR_MESSAGE
                ShowDialogNotification(str(e))
                return e.code
            return e.code
        return resp
    return changed_request