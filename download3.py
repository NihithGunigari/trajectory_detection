
# downloading the files using gdown 
# https://github.com/wkentaro/gdown

import os
import gdown
import shutil

# file ids
links = {
    "1wCF-oaXLT04cpB9WCXiNIuFivwEYctCR": ["class_person_train.txt", "data/"],
    "1nDgi87f-SE6aRQCy_O-vomT27yrAcPJs": ["class_end_effector.txt", "data/"],
    "1QpAqhU46WJON8pedp6jB2pDsidsnBxvL": ["class_problance_train.txt", "data/"],
    "12X-DdLJkgcknkWdQOtoB8cmKiglPcKtX": ["class_probe_train.txt", "data/"]
}

# download the files and save to respective folder
cwd = os.getcwd()
for id in links:
  filename = links[id][0]
  filepath = links[id][1]
  destination = os.path.join(cwd, filepath)

  if not os.path.isdir(destination):
    os.mkdir(destination)

  url = f"https://drive.google.com/uc?id={id}"
  gdown.download(url, filename, quiet=False)
  shutil.move(os.path.join(cwd, filename), destination)
