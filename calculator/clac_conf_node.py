from examples.calculator.calc_conf import *
from examples.calculator.calc_node_base import *


@register_node(OP_NODE_SQR)
class CalcNode_Add(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_SQR, "Square", "Statements", inputs=[1, 1, 1, 1, 1, 0, 0, 0, 0], outputs=[2, 2, 2, 2, 2])


@register_node(OP_NODE_REC)
class CalcNode_Rec(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_REC, "Rectangle", "For", inputs=[1, 1, 1, 1, 1, 0, 0, 0, 0], outputs=[2, 2, 2, 2, 2])


@register_node(OP_NODE_RMB)
class CalcNode_Rmb(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_RMB, "Rhombus", "Conditional IF", inputs=[1, 1, 1, 1, 1, 0, 0, 0, 0], outputs=[2, 2, 2, 2, 2])


@register_node(OP_NODE_STR)
class CalcNode_Str(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_STR, "Start Node", inputs=[], outputs=[4, 4, 4, 4, 4])


@register_node(OP_NODE_END)
class CalcNode_End(CalcNode):
    def __init__(self, scene):
        super().__init__(scene, OP_NODE_END, "End Node", inputs=[3, 3, 3, 3, 3], outputs=[])
