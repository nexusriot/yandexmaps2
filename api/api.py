# -*- coding: utf-8 -*-


import xml.dom.minidom
try:
    import urllib.parse as urllib
except ImportError:
    import urllib

try:
    from httprequest import httprequest
    from point import Point
except:
    from api.httprequest import httprequest
    from api.point import Point


STATIC_URL = 'http://static-maps.yandex.ru/1.x/?'
GEOCODE_URL  = 'http://geocode-maps.yandex.ru/1.x/?'
DYNAMIC_URL = 'http://api-maps.yandex.ru/2.0.9/?'

class Utils(object):
    '''
    Utility Class
    '''
    @staticmethod
    def formatfloat(lon, lat):
        return '%0.7f, %0.7f' % (float(lon), float(lat))

    @staticmethod
    def getUrl(api_key, location, **kwargs):
        try:
            getfrom = kwargs['getfrom']
        except KeyError:
            raise AttributeError('Key-based argument "getfrom" required')
        if kwargs['getfrom']:
            if getfrom == 'point':
                cpoint = '%s, %s' % (location.latitude, location.longitude)
                parameters = urllib.urlencode({'geocode':cpoint, 'key': api_key})
            elif getfrom == 'address':
                address = location.encode('utf8')
                parameters = urllib.urlencode({'geocode':address, 'key': api_key})
        return '%s%s' % (GEOCODE_URL, parameters)

    @staticmethod
    def getDocument(api_key, location, timeout = 3, **kwargs):
        try:
            mode = kwargs['mode']
        except KeyError:
            raise AttributeError('Key-based argument "mode" required')
        if mode == 'reverse':
            url = Utils.getUrl(api_key, location, getfrom='point')
        elif mode == 'geocode':
            url = Utils.getUrl(api_key, location, getfrom='address')
        (status, reason, response) = httprequest('GET', url, timeout=timeout)
        return response

class Yandexapi(object):
    '''
    Yandex API maintance class
    '''
    def __init__(self, api_key):
        self.__api_key = api_key

    def geocode(self, address):
        '''
        returns a a Point Object from an address string
        '''
        try:
            response = Utils.getDocument(self.__api_key, address, mode='geocode')
            dom = xml.dom.minidom.parseString(response)
            posElement = dom.getElementsByTagName('pos')[0]
            posData = posElement.childNodes[0].data
            (lat, lon) = tuple(posData.split())
            return Point(lat, lon)
        except IOError:
            return Point(None, None)

    def reverse(self, point):
        '''
        reverse geocoding, returns an address string from a Point Object
        '''
        try:
            response = Utils.getDocument(self.__api_key, point, mode='reverse')
            dom = xml.dom.minidom.parseString(response)
            posElement = dom.getElementsByTagName('AddressLine')[0]
            posData = posElement.childNodes[0].data
            return posData
        except IndexError:
            return None
        except:
            raise

    @staticmethod
    def getStaticMapUrlWithLabels (points, **kwargs):
        '''
        generates a static url with number labels from a list of Point Object
        '''
        if 'startpoint' in kwargs:
            startpoint = kwargs['startpoint']
        resp = '%s%s' % (STATIC_URL, 'l=map&pt=')
        for (i, point) in enumerate(points):
            resp+= '%0.7f,%0.7f,%d~' % (point.latitude, point.longitude, i + 1)
        resp = resp[:-1]
        return resp