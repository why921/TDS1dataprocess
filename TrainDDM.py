import os
import math
import argparse
from torch import nn
import torch
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

import numpy as np
from DDMdataset import data_transforms
from DDMdataset import DDMDataSet
from ViTGNSSR import vit_base_patch128

#vit_base_patch16_224
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
def main():

    if os.path.exists("./weights") is False:
        os.makedirs("./weights")

    tb_writer = SummaryWriter()
    idtxt = open('test.txt', 'w')

    ddm_ds_t = DDMDataSet(labeltxt='E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\pa.txt', transform=data_transforms)
    ddm_ds_t.__init__(labeltxt='E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\pa.txt', transform=data_transforms)

    #   spectrogram_ds=spectrogramDataset(labeltxt='',transform=data_transforms)
    #  spectrogram_ds.__init__(labeltxt='', transform=data_transforms)

    # "E:\ALOSPALSAR\ValidationData\ALPSRP205991510test\pauli24.txt"


    train_loader = torch.utils.data.DataLoader(dataset=ddm_ds_t,
                                               batch_size=1,
                                               shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=ddm_ds_t,
                                               batch_size=1,
                                               shuffle=True)
    device = torch.device('cuda')

    x, label = iter(train_loader).next()
    print('x:', x.shape, 'label:', label.shape)
    device = torch.device('cuda')
    model = vit_base_patch128().to(device)

    # loss_func = nn.MSELoss()
    # criteon = nn.CrossEntropyLoss().to(device)
    loss_func = nn.CrossEntropyLoss().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    print(model)
    for epoch in range(10):
        model.train()
        for batchidx, (x, label) in enumerate(train_loader):
            x, label = x.to(device), label.to(device)
            # print(x.shape)
            logits = model(x)
            loss = loss_func(logits, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    # print(epoch, 'loss:', loss.item())
    model.eval()
    with torch.no_grad(),open('test.txt','a') as f:
        for x, label in test_loader:
          x, label = x.to(device), label.to(device)
          logits = model(x)
          pred = logits.argmax(dim=1)
          pprreedd = np.array(pred.cpu())
          np.savetxt(f, pprreedd, fmt='%d',delimiter=' ')
    idtxt.close()

if __name__ == '__main__':
    main()
