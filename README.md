<div align="center">
  
![image](https://user-images.githubusercontent.com/38921656/120930774-af166880-c729-11eb-91c5-4229fe70eab3.png)

  
</div>

  
<p align="center">
  <a href="https://github.com/sooftware/openspeech/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-informational">
  <a href="https://github.com/sooftware/openspeech/releases"><img src="https://img.shields.io/badge/release-v0.1-informational">
  <a href="https://pypi.org/project/openspeech-core/"><img src="https://img.shields.io/badge/pypi-v0.1-informational">
  <img src="https://img.shields.io/badge/build-passing-33CF57?&logo=GitHub">
  <a href="https://sooftware.github.io/openspeech/"><img src="https://img.shields.io/badge/docs-passing-33CF57?&logo=GitHub">
  <a href="https://www.codefactor.io/repository/github/sooftware/openspeech"><img src="https://www.codefactor.io/repository/github/sooftware/openspeech/badge?s=1cc697a8b26b61fb987f892dc715255c1f2bae13"></a>
</p>

</div>
  
---
  
<img src="https://user-images.githubusercontent.com/42150335/120691940-14781880-c4e2-11eb-8b1d-34390631cd55.png" height=20> Openspeech provides reference implementations of various ASR modeling papers and three languages recipe to perform tasks on automatic speech recognition. We aim to make ASR technology easier to use for everyone.    
   

<img src="https://user-images.githubusercontent.com/42150335/120691940-14781880-c4e2-11eb-8b1d-34390631cd55.png" height=20>  Openspeech is backed by the two powerful libraries — [PyTorch-Lightning](https://github.com/PyTorchLightning/pytorch-lightning) and [Hydra](https://github.com/facebookresearch/hydra). 
Various features are available in the above two libraries, including Multi-GPU and TPU training, Mixed-precision, and hierarchical configuration management.
  
  
<img src="https://user-images.githubusercontent.com/42150335/120691940-14781880-c4e2-11eb-8b1d-34390631cd55.png" height=20>  We appreciate any kind of feedback or contribution. Feel free to proceed with small issues like bug fixes, documentation improvement. For major contributions and new features, please discuss with the collaborators in corresponding issues.  
  
## Why should I use openspeech?  
  
1. Easy-to-experiment with the famous ASR models.  
    - Supports 10+ models and is continuously updated.  
    - Low barrier to entry for educators and practitioners.  
    - Save time for researchers who want to conduct various experiments.
2. Provides recipes for the most widely used languages, English, Chinese, and + Korean.
    - LibriSpeech - 1,000 hours of English dataset most widely used in ASR tasks.
    - AISHELL-1 - 170 hours of Chinese Mandarin speech corpus.
    - KsponSpeech - 1,000 hours of Korean open-domain dialogue speech.  
3. Easily customize a model or a new dataset to your needs:
    - The default hparams of the supported models are provided but can be easily adjusted.
    - Easily create a custom model by combining modules that are already provided.  
    - If you want to use the new dataset, you only need to define a `pl.LightingDataModule` and `Vocabulary` classes.
4. Audio processing
    - Representative audio features such as Spectrogram, Mel-Spectrogram, Filter-Bank, and MFCC can be used easily.
    - Provides a variety of augmentation, including SpecAugment, Noise Injection, and Audio Joining.
  
## Why shouldn't I use openspeech?
  
- This library provides code for learning ASR models, but does not provide APIs by pre-trained models.  
- We do not provide pre-training mechanisms such as Wav2vec 2.0 since pre-training costs a lot of computation. Though computation optimization is very important, this library does not provide that optimization.    
  
## Model architectures  
  
We support all the models below. Note that, the important concepts of the model have been implemented to match, but the details of the implementation may vary.  
  
1. [**DeepSpeech2**]() (from Baidu Research) released with paper [Deep Speech 2: End-to-End Speech Recognition in
English and Mandarin](https://arxiv.org/abs/1512.02595.pdf), by Dario Amodei, Rishita Anubhai, Eric Battenberg, Carl Case, Jared Casper, Bryan Catanzaro, Jingdong Chen, Mike Chrzanowski, Adam Coates, Greg Diamos, Erich Elsen, Jesse Engel, Linxi Fan, Christopher Fougner, Tony Han, Awni Hannun, Billy Jun, Patrick LeGresley, Libby Lin, Sharan Narang, Andrew Ng, Sherjil Ozair, Ryan Prenger, Jonathan Raiman, Sanjeev Satheesh, David Seetapun, Shubho Sengupta, Yi Wang, Zhiqian Wang, Chong Wang, Bo Xiao, Dani Yogatama, Jun Zhan, Zhenyao Zhu. 
2. [**RNN-Transducer**]() (from University of Toronto) released with paper [Sequence Transduction with Recurrent Neural Networks](https://arxiv.org/abs/1211.3711.pdf), by Alex Graves.
3. [**Listen Attend Spell**](https://sooftware.github.io/openspeech/Listen%20Attend%20Spell.html) (from Carnegie Mellon University and Google Brain) released with paper [Listen, Attend and Spell](https://arxiv.org/abs/1508.01211), by William Chan, Navdeep Jaitly, Quoc V. Le, Oriol Vinyals.  
4. [**Location-aware attention based Listen Attend Spell**]() (from University of Wrocław and Jacobs University and Universite de Montreal ) released with paper [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503), by Jan Chorowski, Dzmitry Bahdanau, Dmitriy Serdyuk, Kyunghyun Cho, Yoshua Bengio.  
5. [**Joint CTC-Attention based Listen Attend Spell**]() (from Mitsubishi Electric Research Laboratories and Carnegie Mellon University) released with paper [Joint CTC-Attention based End-to-End Speech Recognition using Multi-task Learning](https://arxiv.org/abs/1609.06773), by Suyoun Kim, Takaaki Hori, Shinji Watanabe.  
6. [**Deep CNN Encoder with Joint CTC-Attention Listen Attend Spell**]() (from Mitsubishi Electric Research Laboratories and Massachusetts Institute of Technology and Carnegie Mellon University) released with paper [Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM](https://arxiv.org/abs/1706.02737), by Takaaki Hori, Shinji Watanabe, Yu Zhang, William Chan.
7. [**Multi-head attention based Listen Attend Spell**]() (from Google) released with paper [State-of-the-art Speech Recognition With Sequence-to-Sequence Models](https://arxiv.org/abs/1712.01769), by Chung-Cheng Chiu, Tara N. Sainath, Yonghui Wu, Rohit Prabhavalkar, Patrick Nguyen, Zhifeng Chen, Anjuli Kannan, Ron J. Weiss, Kanishka Rao, Ekaterina Gonina, Navdeep Jaitly, Bo Li, Jan Chorowski, Michiel Bacchiani.  
8. [**Speech-Transformer**]() (from University of Chinese Academy of Sciences and Institute of Automation and Chinese Academy of Sciences) released with paper [Speech-Transformer: A No-Recurrence Sequence-to-Sequence Model for Speech Recognition](https://ieeexplore.ieee.org/document/8462506), by Linhao Dong; Shuang Xu; Bo Xu.
9. [**VGG-Transformer**]() (from Facebook AI Research) released with paper [Transformers with convolutional context for ASR](https://arxiv.org/abs/1904.11660), by Abdelrahman Mohamed, Dmytro Okhonko, Luke Zettlemoyer.  
10. [**Transformer with CTC**](https://github.com/sooftware/openspeech-dev/issues/151) (from NTT Communication Science Laboratories, Waseda University, Center for Language and Speech Processing, Johns Hopkins University) released with paper [Improving Transformer-based End-to-End Speech Recognition with Connectionist Temporal Classification and Language Model Integration](https://www.isca-speech.org/archive/Interspeech_2019/pdfs/1938.pdf), by Shigeki Karita, Nelson Enrique Yalta Soplin, Shinji Watanabe, Marc Delcroix, Atsunori Ogawa, Tomohiro Nakatani.
11. [**Joint CTC-Attention based Transformer**](https://github.com/sooftware/openspeech-dev/issues/151)(from NTT Corporation) released with paper [Self-Distillation for Improving CTC-Transformer-based ASR Systems](https://www.isca-speech.org/archive/Interspeech_2020/pdfs/1223.pdf), by Takafumi Moriya, Tsubasa Ochiai, Shigeki Karita, Hiroshi Sato, Tomohiro Tanaka, Takanori Ashihara, Ryo Masumura, Yusuke Shinohara, Marc Delcroix.
12. [**Jasper**]() (from NVIDIA and New York University) released with paper [Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/pdf/1904.03288.pdf), by Jason Li, Vitaly Lavrukhin, Boris Ginsburg, Ryan Leary, Oleksii Kuchaiev, Jonathan M. Cohen, Huyen Nguyen, Ravi Teja Gadde.   
13. [**QuartzNet**]() (from NVIDIA and Univ. of Illinois and Univ. of Saint Petersburg) released with paper [QuartzNet: Deep Automatic Speech Recognition with 1D Time-Channel Separable Convolutions](https://arxiv.org/abs/1910.10261.pdf), by Samuel Kriman, Stanislav Beliaev, Boris Ginsburg, Jocelyn Huang, Oleksii Kuchaiev, Vitaly Lavrukhin, Ryan Leary, Jason Li, Yang Zhang.  
14. [**Transformer Transducer**]() (from Facebook AI) released with paper [Transformer-Transducer:
End-to-End Speech Recognition with Self-Attention](https://arxiv.org/abs/1910.12977.pdf), by Ching-Feng Yeh, Jay Mahadeokar, Kaustubh Kalgaonkar, Yongqiang Wang, Duc Le, Mahaveer Jain, Kjell Schubert, Christian Fuegen, Michael L. Seltzer.  
15. [**Conformer**]() (from Google) released with paper [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100), by Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar, Yu Zhang, Jiahui Yu, Wei Han, Shibo Wang, Zhengdong Zhang, Yonghui Wu, Ruoming Pang.  
16. [**Conformer with CTC**]() (from Northwestern Polytechnical University and University of Bordeaux and Johns Hopkins University and Human Dataware Lab and Kyoto University and NTT Corporation and Shanghai Jiao Tong University and  Chinese Academy of Sciences) released with paper [Recent Developments on ESPNET Toolkit Boosted by Conformer](https://arxiv.org/abs/2010.13956.pdf), by Pengcheng Guo, Florian Boyer, Xuankai Chang, Tomoki Hayashi, Yosuke Higuchi, Hirofumi Inaguma, Naoyuki Kamo, Chenda Li, Daniel Garcia-Romero, Jiatong Shi, Jing Shi, Shinji Watanabe, Kun Wei, Wangyou Zhang, Yuekai Zhang.
17. [**Conformer with LSTM Decoder**]() (from IBM Research AI) released with paper [On the limit of English conversational speech recognition](https://arxiv.org/abs/2105.00982.pdf), by Zoltán Tüske, George Saon, Brian Kingsbury.
  
## Get Started
  
We use [Hydra](https://github.com/facebookresearch/hydra) to control all the training configurations. 
If you are not familiar with Hydra we recommend visiting the [Hydra website](https://hydra.cc/). 
Generally, Hydra is an open-source framework that simplifies the development of research applications by providing the ability to create a hierarchical configuration dynamically. 
If you want to know how we used Hydra, we recommend you to read [here](https://sooftware.github.io/openspeech/notes/hydra_configs.html).
  
### Supported Datasets
 
We support [LibriSpeech](https://www.openslr.org/12), [KsponSpeech](https://aihub.or.kr/aidata/105), and [AISHELL-1](https://www.openslr.org/33/).   
  
LibriSpeech is a corpus of approximately 1,000 hours of 16kHz read English speech, prepared by Vassil Panayotov with the assistance of Daniel Povey. The data was derived from reading audiobooks from the LibriVox project and has been carefully segmented and aligned.   
   
Aishell is an open-source Chinese Mandarin speech corpus published by Beijing Shell Shell Technology Co.,Ltd. 400 people from different accent areas in China were invited to participate in the recording, which was conducted in a quiet indoor environment using high fidelity microphone and downsampled to 16kHz.
  
KsponSpeech is a large-scale spontaneous speech corpus of Korean. This corpus contains 969 hours of general open-domain dialog utterances, spoken by about 2,000 native Korean speakers in a clean environment. All data were constructed by recording the dialogue of two people freely conversing on a variety of topics and manually transcribing the utterances. To start training, the KsponSpeech dataset must be prepared in advance. To download KsponSpeech, you need permission from [AI Hub](https://aihub.or.kr/).
  
### Pre-processed Manifest Files
  
   
|Dataset    |Unit                   |Manifest   |Vocab|SP-Model|   
|-----------|--------------|:---------:|:----:|:--------:|   
|LibriSpeech|character|[[Link]](https://drive.google.com/file/d/1ZTjkTN8hCwVqiygq8LSIyv_V3D1P3njH/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1qsSgb3z_qCXYglB7JlPjG3JjLqOWCCIv/view?usp=sharing)|-|      
|LibriSpeech|subword|[[Link]](https://drive.google.com/file/d/1IY4Qm1uxbKOcdagNyji5zoXDaSV2KevR/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/16551boLSMTUAeidyDQ8bOSbJoQslDaRj/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1nqfGJ2uBQJEvjnY-GJ7GgZNZxH_AonoY/view?usp=sharing)|   
|AISHELL-1|character|[[Link]](https://drive.google.com/file/d/1qUEu-txKjB8QVSauWEA8tOPysYT990B7/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1pnZ8cpWm7HLkemeRLXIznlqzKL4Uyf03/view?usp=sharing)|-|  
|KsponSpeech|character|[[Link]](https://drive.google.com/file/d/1JkimBCPi68wko-8wiKW0MQv1yE8rrNAP/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1hDvFTo4czh29sdSKTuqTlHAe37tOyofy/view?usp=sharing)|-|  
|KsponSpeech|subword|[[Link]](https://drive.google.com/file/d/1S9umHLLGlKF-bk1OU_WNGMftl93ZhiQW/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1YmhxXjT8n65Ag8kLkWf3luwsenvx_xm6/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/1YI_2TdAajiRVasOUcsUuNwQ1CJ9LPkkc/view?usp=sharing)|  
|KsponSpeech|grapheme|[[Link]](https://drive.google.com/file/d/1cVHBnubAQEVyNdy1oJN6gPk65R0Wr7Wp/view?usp=sharing)|[[Link]](https://drive.google.com/file/d/11cGb0lKDVtjtZzyHHDKU6YKaY3LrnIhS/view?usp=sharing)|-|   
  
KsponSpeech needs permission from [AI Hub](https://aihub.or.kr/).   
Please send e-mail including the approved screenshot to sh951011@gmail.com.
  
### Manifest File
  
- Manifest file format:
  
```
LibriSpeech/test-other/8188/269288/8188-269288-0052.flac        ▁ANNIE ' S ▁MANNER ▁WAS ▁VERY ▁MYSTERIOUS       4039 20 5 531 17 84 2352
LibriSpeech/test-other/8188/269288/8188-269288-0053.flac        ▁ANNIE ▁DID ▁NOT ▁MEAN ▁TO ▁CONFIDE ▁IN ▁ANYONE ▁THAT ▁NIGHT ▁AND ▁THE ▁KIND EST ▁THING ▁WAS ▁TO ▁LEAVE ▁HER ▁A LONE    4039 99 35 251 9 4758 11 2454 16 199 6 4 323 200 255 17 9 370 30 10 492
LibriSpeech/test-other/8188/269288/8188-269288-0054.flac        ▁TIRED ▁OUT ▁LESLIE ▁HER SELF ▁DROPP ED ▁A SLEEP        1493 70 4708 30 115 1231 7 10 1706
LibriSpeech/test-other/8188/269288/8188-269288-0055.flac        ▁ANNIE ▁IS ▁THAT ▁YOU ▁SHE ▁CALL ED ▁OUT        4039 34 16 25 37 208 7 70
LibriSpeech/test-other/8188/269288/8188-269288-0056.flac        ▁THERE ▁WAS ▁NO ▁REPLY ▁BUT ▁THE ▁SOUND ▁OF ▁HURRY ING ▁STEPS ▁CAME ▁QUICK ER ▁AND ▁QUICK ER ▁NOW ▁AND ▁THEN ▁THEY ▁WERE ▁INTERRUPTED ▁BY ▁A ▁GROAN     57 17 56 1368 33 4 489 8 1783 14 1381 133 571 49 6 571 49 82 6 76 45 54 2351 44 10 3154
LibriSpeech/test-other/8188/269288/8188-269288-0057.flac        ▁OH ▁THIS ▁WILL ▁KILL ▁ME ▁MY ▁HEART ▁WILL ▁BREAK ▁THIS ▁WILL ▁KILL ▁ME 299 46 71 669 50 41 235 71 977 46 71 669 50
...
...
```
  
### Training examples
 
You can simply train with LibriSpeech dataset like below:  
  
- Example1: Train the `conformer-lstm` model with `filter-bank` features on GPU.
  
```
$ python ./openspeech_cli/hydra_train.py \
    dataset=librispeech \
    dataset.dataset_download=True \
    dataset.dataset_path=$DATASET_PATH \
    dataset.manifest_file_path=$MANIFEST_FILE_PATH \  
    vocab=libri_subword \
    model=conformer_lstm \
    audio=fbank \
    lr_scheduler=warmup_reduce_lr_on_plateau \
    trainer=gpu \
    criterion=joint_ctc_cross_entropy
```
  
You can simply train with KsponSpeech dataset like below:
  
- Example2: Train the `listen-attend-spell` model with `mel-spectrogram` features On TPU:
  
```
$ python ./openspeech_cli/hydra_train.py \
    dataset=ksponspeech \
    dataset.dataset_path=$DATASET_PATH \
    dataset.manifest_file_path=$MANIFEST_FILE_PATH \  
    dataset.test_dataset_path=$TEST_DATASET_PATH \
    dataset.test_manifest_dir=$TEST_MANIFEST_DIR \
    vocab=kspon_character \
    model=listen_attend_spell \
    audio=melspectrogram \
    lr_scheduler=warmup_reduce_lr_on_plateau \
    trainer=tpu \
    criterion=joint_ctc_cross_entropy
```
   
You can simply train with AISHELL-1 dataset like below:
  
- Example2: Train the `quartznet` model with `mfcc` features On GPU with FP16:
  
```
$ python ./openspeech_cli/hydra_train.py \
    dataset=aishell \
    dataset.dataset_path=$DATASET_PATH \
    dataset.dataset_download=True \
    dataset.manifest_file_path=$MANIFEST_FILE_PATH \  
    vocab=aishell_character \
    model=quartznet15x5 \
    audio=mfcc \
    lr_scheduler=warmup_reduce_lr_on_plateau \
    trainer=gpu-fp16 \
    criterion=ctc
```
  
## Installation
  
This project recommends Python 3.7 or higher.  
We recommend creating a new virtual environment for this project (using virtual env or conda).
  

### Prerequisites
  
* numpy: `pip install numpy` (Refer [here](https://github.com/numpy/numpy) for problem installing Numpy).
* pytorch: Refer to [PyTorch website](http://pytorch.org/) to install the version w.r.t. your environment.   
* librosa: `conda install -c conda-forge librosa` (Refer [here](https://github.com/librosa/librosa) for problem installing librosa)
* torchaudio: `pip install torchaudio==0.6.0` (Refer [here](https://github.com/pytorch/pytorch) for problem installing torchaudio)
* sentencepiece: `pip install sentencepiece` (Refer [here](https://github.com/google/sentencepiece) for problem installing sentencepiece)
* pytorch-lightning: `pip install pytorch-lightning` (Refer [here](https://github.com/PyTorchLightning/pytorch-lightning) for problem installing pytorch-lightning)
* hydra: `pip install hydra-core --upgrade` (Refer [here](https://github.com/facebookresearch/hydra) for problem installing hydra)
* warp-rnnt: Refer to [warp-rnnt page](https://github.com/1ytic/warp-rnnt) to install the library.
* ctcdecode: Refer to [ctcdecode page](https://github.com/parlance/ctcdecode) to install the library.
  
### Install from pypi
  
You can install openspeech with pypi.
```
pip install openspeech-core
```
  
### Install from source
Currently, we only support installation from source code using setuptools. Checkout the source code and run the   
following commands:  
```
$ ./install.sh
```
  
### Install Apex (for 16-bit training) 
  
For faster training install NVIDIA's apex library:
  
```
$ git clone https://github.com/NVIDIA/apex
$ cd apex

# ------------------------
# OPTIONAL: on your cluster you might need to load CUDA 10 or 9
# depending on how you installed PyTorch

# see available modules
module avail

# load correct CUDA before install
module load cuda-10.0
# ------------------------

# make sure you've loaded a cuda version > 4.0 and < 7.0
module load gcc-6.1.0

$ pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```  

## Troubleshoots and Contributing
If you have any questions, bug reports, and feature requests, please [open an issue](https://github.com/sooftware/openspeech/issues) on Github.   
  
We appreciate any kind of feedback or contribution.  Feel free to proceed with small issues like bug fixes, documentation improvement.  For major contributions and new features, please discuss with the collaborators in corresponding issues.
  
### Code Style
We follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) for code style. Especially the style of docstrings is important to generate documentation. 
  
### License
This project is licensed under the MIT LICENSE - see the [LICENSE.md](https://github.com/sooftware/openspeech/blob/master/LICENSE) file for details
  
## Citation
  
If you use the system for academic work, please cite:
  
```
@GITHUB{2021-openspeech,
  author       = {Kim, Soohwan and Ha, Sangchun and Cho, Soyoung},
  author email = {sh951011@gmail.com, seomk9896@naver.com, soyoung.cho@kaist.ac.kr}
  title        = {Openspeech: Open-Source Toolkit for End-to-End Speech Recognition},
  howpublished = {\url{https://github.com/sooftware/openspeech}},
  docs         = {\url{https://sooftware.github.io/openspeech}},
  year         = {2021}
}
```
