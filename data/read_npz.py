import numpy as np

data = np.load('/home/msc_lab/zxh/MBNSF/data/av1_traj/1d676737-4110-3f7e-bec0-0c90f74c248f.npz', allow_pickle=True)
print(list(data.keys()))
print(data['pcs'][0].shape)