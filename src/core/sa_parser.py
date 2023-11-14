from .sly import Parser
from .sa_lexer import Lexer


class Parser(Parser):
    tokens = Lexer.tokens
    precedence = (("left", PLUS, MINUS), ("left", TIMES, DIVIDE), ("right", UMINUS))

    def __init__(self):
        ...

    @_("")
    def block(self, p):
        return ("block",)

    @_("statement block")
    def block(self, p):
        return ("block", p.statement, *p.block[1:])

    @_("")
    def in_block(self, p):
        return ("in_block",)

    @_("in_statement in_block")
    def in_block(self, p):
        return ("in_block", p.in_statement, *p.in_block[1:])

    # ----------------------------------
    @_("")
    def block_struct(self, p):
        return ("block_struct",)

    @_("struct_declare block_struct")
    def block_struct(self, p):
        return ("block_struct", p.struct_declare, *p.block_struct[1:])

    @_("var_declare")
    def struct_declare(self, p):
        return p.var_declare

    @_("CUSE STRING")
    def struct_declare(self, p):
        return ("cuse", p.STRING, p.lineno)

    # -----------------------------------
    # use <name>
    @_("USE name")
    def statement(self, p):
        return ("use", p.name[0], p.lineno)

    # use <name>,<name>,...
    @_("USE names2")
    def statement(self, p):
        return ("uses", p.names2, p.lineno)

    # -----------------------------------

    # cuse "c code"
    @_("CUSE STRING")
    def statement(self, p):
        return ("cuse", p.STRING, p.lineno)

    # cuse """multi line c code"""
    @_("CUSE MULTILINE_STRING")
    def statement(self, p):
        return ("cuse", p.MULTILINE_STRING, p.lineno)

    # cuse <name>
    @_("CUSE name")
    def statement(self, p):
        return ("cinclude", p.name[0], p.lineno)

    # cuse "c code"
    @_("CUSE STRING")
    def in_statement(self, p):
        return ("cuse", p.STRING, p.lineno)

    # cuse """multi line c code"""
    @_("CUSE MULTILINE_STRING")
    def in_statement(self, p):
        return ("cuse", p.MULTILINE_STRING, p.lineno)

    # -----------------------------------
    @_("enum_stmt")
    def statement(self, p):
        return p.enum_stmt

    @_("enum_stmt")
    def in_statement(self, p):
        return p.enum_stmt

    # enum <name> {
    #     <names>
    # }
    @_("ENUM NAME LBC names RBC")
    def enum_stmt(self, p):
        return ("enum", p.NAME, p.names, p.lineno)

    # ----------------------------------
    # Variable and const decalration
    # var <name> = <expr>
    @_("VAR NAME ASSIGN expr")
    def var_declare(self, p):
        return ("var_auto_type", p.NAME, p.expr, p.lineno)

    # var <name> : <return_type>
    @_("VAR NAME COLON return_type")
    def var_declare(self, p):
        return ("var_without_assignment", p.return_type, p.NAME, p.lineno)

    # var <name> : <return_type> = <expr>
    @_("VAR NAME COLON return_type ASSIGN expr")
    def var_declare(self, p):
        return ("var_with_assignment", p.return_type, p.NAME, p.expr, p.lineno)

    # const <name> = <expr>
    @_("CONST NAME ASSIGN expr")
    def var_declare(self, p):
        return ("const_auto_type", p.NAME, p.expr, p.lineno)

    # const <name> : <return_type>
    @_("CONST NAME COLON return_type")
    def var_declare(self, p):
        return ("declare", "const_no_expr", p.NAME, p.return_type, p.lineno)

    # const <name> : <return_type> = <expr>
    @_("CONST NAME COLON return_type ASSIGN expr")
    def var_declare(self, p):
        return ("declare", "const", p.return_type, p.NAME, p.expr, p.lineno)

    @_("var_declare")
    def statement(self, p):
        return p.var_declare
    @_("var_declare")
    def in_statement(self, p):
        return p.var_declare
    # -----------------------------------
    # <name> = <expr>
    @_("name ASSIGN expr")
    def in_statement(self, p):
        return ("assign", ("var", p.name[0], p.name[1]), p.expr, p.lineno)

    # <name>[<expr>] = <expr>
    @_("name LBRCK expr RBRCK ASSIGN expr")
    def in_statement(self, p):
        return (
            "assign_var_index",
            ("var", p.name[0], p.name[1]),
            p.expr0,
            p.expr1,
            p.lineno,
        )

    # <name>[<expr>].<name> = <expr>
    @_("name LBRCK expr RBRCK DOT name ASSIGN expr")
    def in_statement(self, p):
        return (
            "assign_var_index_struct",
            ("var", p.name0[0], p.name0[1]),
            p.expr0,
            p.name1[0],
            p.expr1,
            p.lineno,
        )

    # ^<name> = <expr>
    @_("POW name ASSIGN expr")
    def in_statement(self, p):
        return ("assign_ptr", ("var", p.name[0], p.name[1]), p.expr, p.lineno)

    # -----------------------------------
    @_("if_stmt")
    def in_statement(self, p):
        return p.if_stmt

    # if <expr> {
    #      <block>
    # }
    @_("IF expr LBC in_block RBC")
    def if_stmt(self, p):
        return ("if", p.expr, p.in_block, p.lineno)

    # if <expr> {
    #      <in_block>
    # } else {
    #      <in_block>
    # }
    @_("IF expr LBC in_block RBC ELSE LBC in_block RBC")
    def if_stmt(self, p):
        return ("if_else", p.expr, p.in_block0, p.in_block1, p.lineno)

    # if <expr> {
    #      <in_block>
    # } else <expr> {
    #      <in_block>
    # }
    @_("IF expr LBC in_block RBC ELSE if_stmt")
    def if_stmt(self, p):
        return ("if_else2", p.expr, p.in_block, p.if_stmt, p.lineno)

    # -----------------------------------
    # return <expr>
    @_("RETURN expr")
    def in_statement(self, p):
        return ("return", p.expr, p.lineno)

    # -----------------------------------
    @_("for_stmt")
    def in_statement(self, p):
        return p.for_stmt

    # for <name> in <name> {
    #      <in_block>
    # }
    @_("FOR NAME IN name LBC in_block RBC")
    def for_stmt(self, p):
        return ("for", p.NAME, p.name[0], p.in_block, p.lineno)

    # for <name> in <expr>{
    #   <in_block>
    # }
    @_("FOR NAME IN expr LBC in_block RBC")
    def for_stmt(self, p):
        return ("for_expr", p.NAME, p.expr, p.in_block, p.lineno)
    # -----------------------------------
    @_("while_stmt")
    def in_statement(self, p):
        return p.while_stmt

    # while <expr> {
    #      <in_block>
    # }
    @_("WHILE expr LBC in_block RBC")
    def while_stmt(self, p):
        return ("while", p.expr, p.in_block, p.lineno)

    # -----------------------------------
    @_("struct_stmt")
    def statement(self, p):
        return p.struct_stmt

    # struct <name> {
    #     <block_struct>
    # }
    @_("STRUCT NAME LBC block_struct RBC")
    def struct_stmt(self, p):
        return ("struct", p.NAME, p.block_struct, p.lineno)

    # struct <name> : <name> {
    #     <block_struct>
    # }
    @_("STRUCT NAME COLON NAME LBC block_struct RBC")
    def struct_stmt(self, p):
        return ("struct_inheritance", p.NAME0, p.NAME1, p.block_struct, p.lineno)

    # -----------------------------------
    # break
    @_("BREAK")
    def in_statement(self, p):
        return ("break", p.lineno)

    # continue
    @_("CONTINUE")
    def in_statement(self, p):
        return ("continue", p.lineno)

    # -----------------------------------
    # function <name>(<optional_params>) : <optional_return_type> {
    #      <in_block>
    # }
    @_("decorator FUNCTION NAME LPAREN optional_params RPAREN optional_return_type LBC in_block RBC")
    def statement(self, p):
        return (
            "function",
            p.optional_return_type,
            p.NAME,
            p.optional_params,
            p.in_block,
            p.lineno,
            p.decorator,
        )

    
    # function <name>(<optional_params>) : <optional_return_type>
    @_("decorator FUNCTION NAME LPAREN optional_params RPAREN optional_return_type")
    def statement(self, p):
        return (
            "inline_function",
            p.optional_return_type,
            p.NAME,
            p.optional_params,
            p.lineno,
            p.decorator,
        )
    # ------------------------------------
    # delete <name>
    @_("DELETE NAME")
    def delete(self, p):
        return ("delete", p.NAME, p.lineno)

    @_("delete")
    def statement(self, p):
        return p.delete

    @_("delete")
    def in_statement(self, p):
        return p.delete

    # ------------------------------------
    @_("call")
    def in_statement(self, p):
        return ("call_stmt", p.call)

    @_("expr")
    def exprs(self, p):
        return p.expr

    # <expr>, <expr>
    @_("exprs COMMA expr")
    def exprs(self, p):
        return ("exprs", p.exprs, p.expr, p.lineno)

    # [<expr>, <expr>]
    @_("LBRCK exprs RBRCK")
    def expr(self, p):
        return ("list", p.exprs, p.lineno)
    
    # [<expr>, <expr>]
    @_("LBRCK RBRCK")
    def expr(self, p):
        return ("empty_list", p.lineno)

    # <expr> + <expr>
    @_("expr PLUS expr")
    def expr(self, p):
        return ("add", p.expr0, p.expr1, p.lineno)

    # <expr> * <expr>
    @_("expr TIMES expr")
    def expr(self, p):
        return ("mul", p.expr0, p.expr1, p.lineno)

    # <expr> - <expr>
    @_("expr MINUS expr")
    def expr(self, p):
        return ("sub", p.expr0, p.expr1, p.lineno)

    # <expr> / <expr>
    @_("expr DIVIDE expr")
    def expr(self, p):
        return ("div", p.expr0, p.expr1, p.lineno)

    # -<expr>
    @_("MINUS expr %prec UMINUS")
    def expr(self, p):
        return ("sub", ("int", 0), p.expr, p.lineno)

    # (<expr>)
    @_("LPAREN expr RPAREN")
    def expr(self, p):
        return ("paren_expr", p.expr, p.lineno)

    # <name>(<args>)
    @_("NAME LPAREN args RPAREN")
    def call(self, p):
        return ("call", p.NAME, p.args, p.lineno)

    # <name>()
    @_("NAME LPAREN RPAREN")
    def call(self, p):
        return ("call", p.NAME, (), p.lineno)

    @_("call")
    def expr(self, p):
        return p.call

    # <name>
    @_("name")
    def expr(self, p):
        return ("var", p.name[0], p.name[1])

    # not <expr>
    @_("NOT expr")
    def expr(self, p):
        return ("not", p.expr, p.lineno)

    # <name>[<expr>]
    @_("name LBRCK expr RBRCK")
    def expr(self, p):
        return ("var_index", ("var", p.name[0], p.name[1]), p.expr, p.lineno)

    # new <return_type>(<expr>)
    @_("NEW return_type LPAREN expr RPAREN")
    def expr(self, p):
        return ("new", p.return_type, p.expr, p.lineno)

    @_("NUMBER")
    def expr(self, p):
        return ("int", p.NUMBER, p.lineno)

    @_("STRING")
    def expr(self, p):
        return ("string", p.STRING, p.lineno)

    @_("MULTILINE_STRING")
    def expr(self, p):
        return ("multiline_string", p.MULTILINE_STRING, p.lineno)

    @_("CHAR")
    def expr(self, p):
        return ("char", p.CHAR, p.lineno)

    @_("boolean")
    def expr(self, p):
        return ("bool", p.boolean[0], p.boolean[1])

    @_("float")
    def expr(self, p):
        return ("float", p.float[0], p.float[1])

    @_("NUMBER DOT NUMBER")
    def float(self, p):
        return ("{0}.{1}".format(p.NUMBER0, p.NUMBER1), p.lineno)

    @_("name_t")
    def name(self, p):
        return ([p.name_t[0]], p.name_t[1])

    @_("name DOT name_t")
    def name(self, p):
        return (p.name[0] + [p.name_t[0]], p.name_t[1])

    @_("NAME")
    def name_t(self, p):
        return (p.NAME, p.lineno)

    # true
    @_("TRUE")
    def boolean(self, p):
        return ("true", p.lineno)

    # false
    @_("FALSE")
    def boolean(self, p):
        return ("false", p.lineno)

    # ------------------------------------------
    # <name>,<name>
    @_("names COMMA NAME")
    def names(self, p):
        return "{0},{1}".format(p.names, p.NAME, p.lineno)

    @_("NAME")
    def names(self, p):
        return p.NAME

    # <name>,<name>
    @_("names2 COMMA name")
    def names2(self, p):
        return "{0},{1}".format(p.names2, p.name[0], p.lineno)

    @_("name")
    def names2(self, p):
        return p.name[0]

    # ------------------------------------------
    # <expr> == <expr>
    @_("expr EQEQ expr")
    def expr(self, p):
        return ("equals", p.expr0, p.expr1, p.lineno)

    # <expr> != <expr>
    @_("expr NOTEQ expr")
    def expr(self, p):
        return ("not_equals", p.expr0, p.expr1, p.lineno)

    # <expr> >= <expr>
    @_("expr GREATEREQ expr")
    def expr(self, p):
        return ("greater_equals", p.expr0, p.expr1, p.lineno)

    # <expr> <= <expr>
    @_("expr LESSEQ expr")
    def expr(self, p):
        return ("less_equals", p.expr0, p.expr1, p.lineno)

    # <expr> > <expr>
    @_("expr GREATER expr")
    def expr(self, p):
        return ("greater", p.expr0, p.expr1, p.lineno)

    # <expr> < <expr>
    @_("expr LESS expr")
    def expr(self, p):
        return ("less", p.expr0, p.expr1, p.lineno)

    # <expr> and <expr>
    @_("expr AND expr")
    def expr(self, p):
        return ("and", p.expr0, p.expr1, p.lineno)

    # <expr> or <expr>
    @_("expr OR expr")
    def expr(self, p):
        return ("or", p.expr0, p.expr1, p.lineno)

    # -----------------------------------------
    # <param>, <param>
    @_("param_t")
    def params(self, p):
        return ("params", ("param_no",), p.param_t)
    
    @_("params COMMA param_t")
    def params(self, p):
        return ("params", p.params, p.param_t, p.lineno)

    # <name> : <return_type>
    @_("NAME COLON return_type")
    def param_t(self, p):
        return ("param", p.NAME, p.return_type, p.lineno)

    @_("")
    def optional_params(self, p):
        return ("param_no",)
    @_("params")
    def optional_params(self, p):
        return p.params
    # ------------------------------------------
    # <arg>, <arg>
    @_("arg")
    def args(self, p):
        return [p.arg]

    @_("args COMMA arg")
    def args(self, p):
        return p.args + [p.arg]

    @_("return_type")
    def arg(self, p):
        return p.return_type

    @_("expr")
    def arg(self, p):
        return p.expr

    # ------------------------------------------
    # @<name>
    @_("AT NAME")
    def decorator(self, p):
        return ("decorator", p.NAME, p.lineno)

    @_("")
    def decorator(self, p):
        return ("decorator_no",)

    # ------------------------------------------
    # int
    @_("INTVAR")
    def return_type(self, p):
        return ("standard_type", "int", p.lineno)

    # string
    @_("STRINGVAR")
    def return_type(self, p):
        return ("standard_type", "string", p.lineno)

    # char
    @_("CHARVAR")
    def return_type(self, p):
        return ("standard_type", "char", p.lineno)

    # bool
    @_("BOOLVAR")
    def return_type(self, p):
        return ("standard_type", "bool", p.lineno)

    # float
    @_("FLOATVAR")
    def return_type(self, p):
        return ("standard_type", "float", p.lineno)

    # void
    @_("VOIDVAR")
    def return_type(self, p):
        return ("standard_type", "void", p.lineno)

    # <name>
    @_("NAME")
    def return_type(self, p):
        return ("standard_type", p.NAME, p.lineno)

    # [<return_type>]
    @_("LBRCK return_type RBRCK")
    def return_type(self, p):
        return ("return_type_array", p.return_type, p.lineno)

    # <return_type>^
    @_("return_type POW")
    def return_type(self, p):
        return ("ptr_type", p.return_type, p.lineno)

    # <return_type>?
    @_("return_type QS")
    def return_type(self, p):
        return ("nullable_type", p.return_type, p.lineno)

    # Function[<type>,...]<return_type>
    @_('FUNCTION_TYPE LBRCK return_types RBRCK return_type')
    def return_type(self,p):
        return ('funtion_type',p.return_types,p.return_type,p.lineno)

    # static <return_type>
    @_('STATIC return_type')
    def return_type(self,p):
        return ('static_type',p.return_type,p.lineno)

    @_("return_type")
    def return_types(self, p):
        return [p.return_type]
    
    @_("return_types COMMA return_type")
    def return_types(self, p):
        return p.return_types + [p.return_type]

    @_("COLON return_type")
    def optional_return_type(self, p):
        return p.return_type
    @_("")
    def optional_return_type(self, p):
        return ("standard_type","void",None) # TODO : should check for p.lineno
    # ------------------------------------------
    # (<return_type>) <expr>
    @_("LPAREN return_type RPAREN expr")
    def expr(self, p):
        return ("cast", p.return_type, p.expr, p.lineno)

    # ------------------------------------------
    # &<name>
    @_("AMP name")
    def expr(self, p):
        return ("pass_by_ref", ("var", p.name[0], p.name[1]), p.lineno)

    # ^<name>
    @_("POW name")
    def expr(self, p):
        return ("pass_by_ptr", ("var", p.name[0], p.name[1]), p.lineno)

    # todo : support int^^,...
    # ------------------------------------------