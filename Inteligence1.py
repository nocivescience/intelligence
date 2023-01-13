import matplotlib.pyplot as plt
import numpy as np
import torch as th
from manim import *

# Defining the model
class Net(th.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = th.nn.Linear(2, 4)
        self.fc2 = th.nn.Linear(4, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = th.sigmoid(x)
        x = self.fc2(x)
        return x

# Creating an instance of the model
model = Net()

# Plotting the model
fig, ax = plt.subplots()
# ax.axis('off')
# Creating the nodes
nodes = []
for i, (name, param) in enumerate(model.named_parameters()):
    layer_name, node_name = name.split('.')
    x, y = np.random.rand(2)
    nodes.append((x, y, node_name))
    ax.text(x, y, node_name)

# Connecting the nodes
for i, (x1, y1, name1) in enumerate(nodes):
    for x2, y2, name2 in nodes[i+1:]:
        if name1 in name2:
            ax.plot([x1, x2], [y1, y2], '-', c='r')

plt.show()
class IntelligenceScene(Scene):
    def construct(self):
        self.play(Create(ax),Create(fig))
        self.wait()