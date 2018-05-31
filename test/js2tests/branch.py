from youtube_dl.jsinterp2.jsgrammar import Token
from youtube_dl.jsinterp2.tstream import _RELATIONS

skip = {'interpret': 'Interpreting if statement not yet implemented'}

tests = [
    {
        'code': '''
            function a(x) {
                if (x > 0)
                    return true;
                else
                    return false;
            }
            ''',
        'asserts': [{'value': True, 'call': ('a', 1)}, {'value': False, 'call': ('a', 0)}],
        'ast': [
            (Token.FUNC, 'a', ['x'], [
                (Token.IF,
                 (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.ID, 'x'), None, None),
                     (Token.MEMBER, (Token.INT, 0), None, None),
                     (Token.REL, _RELATIONS['>'][1])
                 ]), None)]),
                 (Token.RETURN, (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.BOOL, True), None, None)]), None)])),
                 (Token.RETURN, (Token.EXPR, [(Token.ASSIGN, None, (Token.OPEXPR, [
                     (Token.MEMBER, (Token.BOOL, False), None, None)]), None)])))
            ])
        ]
    }
]
