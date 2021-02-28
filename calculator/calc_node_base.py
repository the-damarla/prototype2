from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from nodeeditor.node_node import Node
from nodeeditor.node_content_widget import QDMNodeContentWidget, QDMTextEdit
from nodeeditor.node_graphics_node import QDMGraphicsNode
from examples.calculator.calc_drag_listbox import *


class CalcGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        """Set up internal attributes like `width`, `height`, etc."""
        super().initSizes()
        self.width = 160
        self.height = 240
        self.edge_roundness = 10.0
        self.edge_padding = 10.0
        self.title_horizontal_padding = 4.0
        self.title_vertical_padding = 4.0


class CalcContent(QDMNodeContentWidget):
    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        wdg_label = QLabel(self.node.content_text, self)
        self.layout.addWidget(wdg_label)
        self.layout.addWidget(QDMTextEdit(""))
        self.layout.setObjectName(self.node.content_text_objname)



class CalcNode(Node):
    def __init__(self, scene, op_code, op_title, content_text="", content_text_objname="calc_node_bg", inputs=[2, 2], outputs=[1]):
        self.op_code = op_code
        self.op_title = op_title
        self.content_text = content_text
        self.content_text_objname = content_text_objname

        super().__init__(scene, self.op_title, inputs, outputs)


    def initInnerClasses(self):
        self.content = CalcContent(self)
        self.grNode = CalcGraphicsNode(self)


