import ply.lex as lex

query = """
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = (
    'COMMENT',
    'SELECT',
    'VAR',
    'WHERE',
    'LIMIT',
    'STRING',
    'DOT',
    'AC',
    'FC',
    'NUMBER',
    'PREFIX_NAME',
    'A'
)

t_COMMENT = r"\#.*"
t_SELECT = r"select"
t_WHERE = r"where"
t_LIMIT = r"LIMIT"
t_VAR = r"\?[a-zA-Z0-9_]+"
t_STRING = r'"[^"]*"(?:@[a-zA-Z]+)?'
t_DOT = r"\."
t_AC = r"\{"
t_FC = r"\}"
t_PREFIX_NAME = r"[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*"
t_A = r'a'

def t_NUMBER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r"\r?\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Símbolo inválido na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(query)

while (token := lexer.token()):
    print(token)
