# Gentle alignment for speech MRI audio

## Getting Started

1. Please download audio data. [LINK](https://drive.google.com/file/d/1opqYQsVCIDG7y1Kd7Kziq39qvW1XVlPC/view?usp=sharing) 

2. Please download the source code and run ```./install.sh```. 

3. Run ```python3 main_gentle_aligner_75sub.py``` to run alignment. 
```bash
git clone git@github.com:yongwanlim/gentle.git
cd gentle
./install.sh
python3 main_gentle_aligner_75sub.py
```

Please note that you have to change the [`data_dir`](https://github.com/yongwanlim/gentle/blob/a1d8ff6b995958660b366078d4cfe49116948568/main_gentle_aligner_75sub.py#L11) and [`out_dir`](https://github.com/yongwanlim/gentle/blob/a1d8ff6b995958660b366078d4cfe49116948568/main_gentle_aligner_75sub.py#L12) in ```main_gentle_aligner_75sub.py``` to your path to data. 

The ```main_gentle_aligner_75sub.py``` will run the alignment for "bvt" task. If you want to run for all other tasks, please comment [this line](https://github.com/yongwanlim/gentle/blob/a1d8ff6b995958660b366078d4cfe49116948568/main_gentle_aligner_75sub.py#L48) in ```main_gentle_aligner_75sub.py``` and run ```python3 main_gentle_aligner_75sub.py```.

For other tasks to run, you need to have the corresponding transcript file located in ```in_trans_dir```. I placed some example transcript files under that directory. 





