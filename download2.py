
# downloading the files using gdown 
# https://github.com/wkentaro/gdown

import os
import gdown
import shutil

# file ids
links = {
    "1xANPbBH2jejXNChGbXgkW_Hoh3gTohNH": ["endeffector.onnx", "onnx/"],
    "1zglw_b6FzHgykQmUuXvqZVjY1ZQHLUv8": ["person.onnx", "onnx/"],
    "1wGZt2f7xwvNzeEoiSLWRqKXCHVY5awUr": ["probe.onnx", "onnx/"],
    "1FcuxS3pg4WTfLAZE4aANdwwb0aHqZYdd": ["problance.onnx", "onnx/"],
    "10kViLknZKXHP-mmzviWCTkwkyqTo2mww": ["yolo_converted.onnx", "onnx/"],
    "1w1omnNN14j7UAg0aNET63EDcjdnaVsjH": ["yoloconverted2.onnx", "onnx/"]
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
