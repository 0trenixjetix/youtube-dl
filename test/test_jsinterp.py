#!/usr/bin/env python

# """
# see: `js2tests`
# """

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import logging

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.jsinterp2 import JSInterpreter
from .js2tests import gettestcases

defs = gettestcases()
# set level to logging.DEBUG to see messages about missing assertions
logging.basicConfig(stream=sys.stderr, level=logging.WARNING)


class TestJSInterpreter(unittest.TestCase):
    def setUp(self):
        self.defs = defs


def generator(test_case, name):
    def test_template(self):
        for test in test_case['subtests']:
            if 'code' not in test:
                log_reason = 'No code in subtest, skipping'
            elif 'asserts' not in test:
                log_reason = 'No assertion in subtest, skipping'
            else:
                log_reason = None

            if log_reason is None:
                jsi = JSInterpreter(test['code'], variables=test.get('globals'))
                for a in test['asserts']:
                    if 'value' in a:
                        if 'call' in a:
                            self.assertEqual(jsi.call_function(*a['call']), a['value'])
                        else:
                            self.assertEqual(jsi.run(), a['value'])
                    else:
                        log.debug('No value in assertion, skipping')
            else:
                log.debug(log_reason)

    log = logging.getLogger('TestJSInterpreter.%s' % name)
    return test_template


# And add them to TestJSInterpreter
for n, tc in enumerate(defs):
    reason = tc['skip'].get('interpret', False)
    tname = 'test_' + str(tc['name'])
    i = 1
    while hasattr(TestJSInterpreter, tname):
        tname = 'test_%s_%d' % (tc['name'], i)
        i += 1

    if reason is not True:
        log_reason = 'Entirely'
    elif not any('asserts' in test for test in tc['subtests']):
        log_reason = '''There isn't any assertion'''
    else:
        log_reason = None

    if log_reason is not None:
        test_method = generator(tc, tname)
        test_method.__name__ = str(tname)
        if reason is not False:
            test_method.__unittest_skip__ = True
            test_method.__unittest_skip_why__ = reason
        setattr(TestJSInterpreter, test_method.__name__, test_method)
        del test_method
    else:
        log = logging.getLogger('TestJSInterpreter')
        log.debug('Skipping %s:%s' % (tname, log_reason))

if __name__ == '__main__':
    unittest.main()
