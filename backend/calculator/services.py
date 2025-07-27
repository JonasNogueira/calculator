
from .models import Operation

from ast import Add,Sub, Mult, Div, USub, Constant, BinOp, UnaryOp, parse

from operator import add, sub, mul, truediv, neg
from .models import Operation

ALLOWED_OPERATORS = {
    Add: add,
    Sub: sub,
    Mult: mul,
    Div: truediv,
    USub: neg,
}


def eval_expr(expr: str) -> float:

    def _eval(node):
        if isinstance(node, Constant):
            return node.n
        elif isinstance(node, BinOp):
            return ALLOWED_OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, UnaryOp):
            return ALLOWED_OPERATORS[type(node.op)](_eval(node.operand))
        else:
            raise ValueError("Operação inválida")

    try:
        tree = parse(expr, mode="eval")
        return _eval(tree.body)
    except Exception:
        raise ValueError("Expressão inválida")


def save_operation(user, expression: str, result: float) -> Operation:
    return Operation.objects.create(
        user=user, parameters=expression, result=str(result)
    )
