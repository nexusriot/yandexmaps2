# -*- coding: utf-8 -*-

from __future__ import with_statement
import contextlib
import httplib2

def httprequest(method, url, body = None, headers = {}, timeout = None):
    host = url.split('/')[2]

    try:
        conn = httplib2.HTTPConnectionWithTimeout(host, timeout=timeout)
    except:
        raise

    with contextlib.closing(conn):
        conn.request(method, url, body, headers)
        resp = conn.getresponse()

        return (resp.status, resp.reason, resp.read())