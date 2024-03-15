import subprocess
import torch

subprocess.run("conda info --envs")
print(torch.cuda.is_available())
