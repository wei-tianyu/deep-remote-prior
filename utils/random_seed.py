import torch

random_seed = 545
torch.manual_seed(random_seed)

net_input = torch.zeros((3,3))
net_input.normal_()
print(net_input)