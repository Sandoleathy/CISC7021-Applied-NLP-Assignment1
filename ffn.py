import torch
import torch.nn as nn
import torch.optim as optim

class FeedForwardNeuralNetwork(nn.Module):
    def __init__(self, d_model=512, hidden_layer=2048):
        super(FeedForwardNeuralNetwork, self).__init__()
        # 输入层到第一个隐藏层
        self.fc1 = nn.Linear(d_model, hidden_layer)
        # 第二个隐藏层到输出层
        self.fc2 = nn.Linear(hidden_layer, d_model)
    def forward(self, x):
        out = self.fc1(x)
        out = torch.relu(out)
        out = self.fc2(out)
        return out        