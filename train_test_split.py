# split into train & test set with the ratio of 60:40
import os

benign_path = "/home/haohao/Downloads/Malware Modus Operandi/Benign"
malware_path = "/home/haohao/Downloads/Malware Modus Operandi/Malware"
save_path = "/home/haohao/Downloads/Malware Modus Operandi/"

def split_file(fname, first_fname, second_fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    with open(first_fname, 'w') as first_f:
        for line in lines[:4000]:
            first_f.write(line)
    with open(second_fname, 'w') as second_f:
        for line in lines[4000:]:
            second_f.write(line)

if __name__ == "__main__":
    split_file(benign_path, save_path + "Benign_test", save_path + "Benign_train")
    split_file(malware_path, save_path + "Malware_test", save_path + "Malware_train")
    print("Done")