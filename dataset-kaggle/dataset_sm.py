import os
import shutil
from tqdm import tqdm


frames_dir = "kaggle-dataset-6classes-preprocessed/frames/"

# files_count_dict = dict()

# for sub_dir in os.listdir(train_dir):
#     files_count = len(os.listdir(train_dir+"/"+sub_dir))
#     files_count_dict[int(sub_dir)] = files_count

# for k, v in sorted(files_count_dict.items(), key=lambda t: t[1]):
#     print(f"dir_name: {k}  -->  files_count: {v}")


dst_dir = "dataset-sm/"
n_chunks = 5
os.makedirs(dst_dir, exist_ok=True)
for sub_dir in ["trainval", "test"]:
    os.makedirs(dst_dir+"/"+sub_dir, exist_ok=True)
    for step in os.listdir(frames_dir+"/"+sub_dir):
        src_step_dir = os.path.join(frames_dir, sub_dir, step)
        dst_step_dir = os.path.join(dst_dir, sub_dir, step)
        os.makedirs(dst_step_dir, exist_ok=True)
        print(f"Copying to {dst_step_dir}")
        files_count = len(os.listdir(src_step_dir))
        for file_name in tqdm(os.listdir(src_step_dir)[:files_count//n_chunks]):
            src_pth = src_step_dir+"/"+file_name
            dst_pth = os.path.join(dst_dir, sub_dir, step, file_name)
            shutil.copy(src_pth, dst_pth)