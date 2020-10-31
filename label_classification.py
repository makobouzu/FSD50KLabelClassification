# -*- coding:utf-8 -*-

import sys
import os
import shutil
import csv

def create_folder(csv, label):
    folder = csv.split('/')[1].split('.')[0]
    new_dir = folder + "/" + label
    if not os.path.isdir(folder):
        os.mkdir(folder)
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
        print("make directory " + new_dir)

def label_classification(names, labels, csv, label):
    folder = csv.split('/')[1].split('.')[0]
    new_dir = folder + "/" + label
    for num,row in enumerate(labels):
        for i in row:
            if label == i:
                name = names[num]
                shutil.copy("FSD50K." + folder + "_audio" + "/" + name + ".wav", new_dir + "/" + name + ".wav")
                print("copy wav " + name + ".wav")
            else:
                break

if __name__ == "__main__":
    args = sys.argv

    csv_file = open(args[1], "r")
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    names = []
    labels = []
    for row in f:
        labels.append(row[1].split(','))
        names.append(row[0])

    create_folder(args[1], args[2])
    label_classification(names, labels, args[1], args[2])
