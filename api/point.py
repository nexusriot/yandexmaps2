# -*- coding: utf-8 -*-

class Point(object):
    '''
    Simple point on map
    '''
    def __init__(self, latitude, longitude):
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value

    def __str__(self):
        return '%s,%s' % (self.latitude, self.longitude)

    def __unicode__(self):
        return '%s,%s'.encode('utf8') % (self.latitude, self.longitude)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.__latitude == other.latitude and self.__longitude == other.longitude

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is not NotImplemented:
            return not result
        return result

class MarkedPoint(Point):
    '''
    Point with stamp field
    '''

    def __init__(self, latitude, longitude, stamp = None):
        super(Point, self).__init__(latitude, longitude)



