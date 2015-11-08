#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import base64

class Header(object):

    @staticmethod
    def prepare_base64_auth(username, password):
        auth_string = '%s:%s' % (username, password)

        if sys.version_info[0] == 3:
            auth_string = bytes(auth_string, 'ascii')

        encoded = base64.b64encode(auth_string)

        if sys.version_info[0] == 3:
            encoded = encoded.decode('ascii')
        return encoded

