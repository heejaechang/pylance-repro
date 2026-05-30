from pegen.grammar import GrammarVisitor


class MyParser(GrammarVisitor):
    def visit(self, node):
        return super().visit(node)
