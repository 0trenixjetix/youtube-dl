from __future__ import unicode_literals

from youtube_dl.jsinterp2.jsgrammar import Token
from youtube_dl.jsinterp2.tstream import _ASSIGN_OPERATORS, _UNARY_OPERATORS, _RELATIONS

skip = {
    'jsinterp': 'For loop is not supported',
    'interpret': 'Interpreting for loop not yet implemented'
}

tests = [
    {
        'code': '''
            function f(x){
                for (var h = 0; h <= x; ++h) {
                    a = h;
                }
                return a;
            }
            ''',
        'asserts': [{'value': 5, 'call': ('f', 5)}],
        'ast': [
            (Token.FUNC, 'f', ['x'], [
                (Token.FOR,
                 (Token.VAR, zip(['h'], [
                     (Token.ASSIGN, None, (Token.OPEXPR, [(Token.MEMBER, (Token.INT, 0), None, None)]), None)
                 ])),
                 (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.ID, 'h'), None, None),
                     (Token.MEMBER, (Token.ID, 'x'), None, None),
                     (Token.REL, _RELATIONS['<='][1])
                 ]), None)]),
                 (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.ID, 'h'), None, None),
                     (Token.PREFIX, _UNARY_OPERATORS['++'][1])
                 ]), None)]),
                 (Token.BLOCK, [
                     (Token.EXPR, [
                         (Token.ASSIGN, _ASSIGN_OPERATORS['='][1],
                          (Token.OPEXPR, [(Token.MEMBER, (Token.ID, 'a'), None, None)]),
                          (Token.ASSIGN, None, (Token.OPEXPR, [(Token.MEMBER, (Token.ID, 'h'), None, None)]), None))
                     ])
                 ])),
                (Token.RETURN, (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                    (Token.MEMBER, (Token.ID, 'a'), None, None)]), None)]))
            ])
        ]
    }
]
