# -*- coding: utf-8 -*-
import subprocess
import os
import glob
from align_wrapper import align


def run_bash(cmd):
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

data_dir = '/Users/yongwanlim/Desktop/dataset_2drt_video_only/' # parent data directory: You can change this directory to ownCloud
out_dir = '/Users/yongwanlim/Desktop/dataset_2drt_video_only/out_alignment_75sub/'  # output directory

dir_list = next(os.walk(data_dir))[1]  # List of subjects

print(sorted(dir_list))

for each_subj in sorted(dir_list):

    # make sure that we only look at subject's directory
    if "sub" not in each_subj:
        continue

    # The template of transcript file will be used for now...
    in_trans_dir = os.path.join(data_dir, 'trans')  # transcript dir
    # in_trans_dir = os.path.join(data_dir, each_subj, 'trans')  # transcript dir

    in_wav_dir = os.path.join(data_dir, each_subj, '2drt', 'audio')  # wav dir

    # check out if renamed wave dir exists
    if os.path.isdir(in_wav_dir) is False:
        print(in_wav_dir + ' does not exist')
        continue

    # make timestamp directory
    # out_timestamp_dir = os.path.join(out_dir, each_subj, 'tstamp')
    out_timestamp_dir = os.path.join(out_dir, 'forcealign_test')
    if not os.path.exists(out_timestamp_dir):
        os.makedirs(out_timestamp_dir)

    istask = False
    # look at each of wav files
    for each_wav_file in glob.glob(os.path.join(in_wav_dir + "/*.wav")):
        head, tail = os.path.split(each_wav_file)
        task_name = tail.strip().replace(each_subj + '_2drt_', '')[3:].replace('_audio.wav', '')[:-3] # only takes "bvt", "grandfather1", or something like that

        # See only 'bVt' task
        if 'bvt' in task_name:
        # if 'shibboleth' in task_name:

            istask = True

            # get the trans file name corresponding to each wav file
            each_trans_file = glob.glob(os.path.join(in_trans_dir + "/" + task_name + ".txt"))

            # skip if the corresponding transcript file doesn't exist
            if each_trans_file:
                # print(each_trans_file[0])

                head, tail = os.path.split(each_wav_file)
                each_json_out_name = os.path.join(out_timestamp_dir, tail.replace("_audio.wav", "_forcealign.json"))

                # Do Gentle alignment to get and save the time stamp as json file
                print(each_trans_file[0], each_wav_file, each_json_out_name)

                # do align only if alignment result doesnt exist
                if not glob.glob(each_json_out_name):
                    align(txtfile=each_trans_file[0], audiofile=each_wav_file, output=each_json_out_name)

            else:
                print(each_trans_file + ' does not exist')
                continue

    if istask is False:
        print('bvt does not exist in' + each_subj)


