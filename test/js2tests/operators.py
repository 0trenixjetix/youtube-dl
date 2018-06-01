from youtube_dl.jsinterp2.jsgrammar import Token
from youtube_dl.jsinterp2.tstream import _OPERATORS

tests = [
    {
        'code': 'return 1 << 5;',
        'asserts': [{'value': 32}],
        'ast': [
            (Token.RETURN,
             (Token.EXPR, [
                 (Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.INT, 1), None, None),
                     (Token.MEMBER, (Token.INT, 5), None, None),
                     (Token.OP, _OPERATORS['<<'][1])
                 ]), None)
             ]))]
    }, {
        'code': 'return 19 & 21;',
        'asserts': [{'value': 17}],
        'ast': [
            (Token.RETURN,
             (Token.EXPR, [
                 (Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.INT, 19), None, None),
                     (Token.MEMBER, (Token.INT, 21), None, None),
                     (Token.OP, _OPERATORS['&'][1])
                 ]), None)
             ]))
        ]
    }, {
        'code': 'return 11 >> 2;',
        'asserts': [{'value': 2}],
        'ast': [
            (Token.RETURN,
             (Token.EXPR, [
                 (Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.INT, 11), None, None),
                     (Token.MEMBER, (Token.INT, 2), None, None),
                     (Token.OP, _OPERATORS['>>'][1])
                 ]), None)
             ]))]
    }
]
