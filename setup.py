def setup():
    import sys

    sys.path.append('/usr/local/google_appengine/')
    sys.path.append('/usr/local/google_appengine/lib/yaml/lib/')
    sys.path.append('/usr/local/google_appengine/lib/webapp2-2.5.2')
    sys.path.append('/usr/local/google_appengine/lib/fancy_urllib/')
    sys.path.append('/usr/local/google_appengine/lib/webob-1.1.1/')
    sys.path.append('/usr/local/google_appengine/lib/django-1.4')
    sys.path.append('../haggle_server/src')
    sys.path.append('../../haggle_server/src')
    sys.path.append('../src/')

    import getpass

    def auth_func():
        return (raw_input('Username:'), getpass.getpass('Password:'))

    from google.appengine.ext.remote_api import remote_api_stub
    remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_func,'haggle-test1.appspot.com')

