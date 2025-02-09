# MIT License
#
# Copyright (c) 2021 Soohwan Kim and Sangchun Ha and Soyoung Cho
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import torch
from omegaconf import DictConfig
from torch import Tensor

from ... import register_audio_feature_transform
from ...audio.spectrogram.configuration import SpectrogramConfigs


@register_audio_feature_transform("spectrogram", dataclass=SpectrogramConfigs)
class SpectrogramFeatureTransform(object):
    r"""
    Create a spectrogram from a audio signal.

    Configurations:
        name (str): name of feature transform. (default: spectrogram)
        sample_rate (int): sampling rate of audio (default: 16000)
        frame_length (float): frame length for spectrogram (default: 20.0)
        frame_shift (float): length of hop between STFT (default: 10.0)
        del_silence (bool): flag indication whether to apply delete silence or not (default: False)
        num_mels (int): the number of mfc coefficients to retain. (default: 161)

    Args:
        configs (DictConfig): configuraion set

    Returns:
        Tensor: A spectrogram feature. The shape is ``(seq_length, num_mels)``
    """
    def __init__(self, configs: DictConfig) -> None:
        super(SpectrogramFeatureTransform, self).__init__()
        self.n_fft = int(round(configs.audio.sample_rate * 0.001 * configs.audio.frame_length))
        self.hop_length = int(round(configs.audio.sample_rate * 0.001 * configs.audio.frame_shift))
        self.function = torch.stft

    def _get_feature(self, signal: np.ndarray) -> np.ndarray:
        """
        Provides feature extraction

        Inputs:
            signal (np.ndarray): audio signal

        Returns:
            feature (np.ndarray): feature extract by sub-class
        """
        spectrogram = self.function(
            Tensor(signal), self.n_fft, hop_length=self.hop_length,
            win_length=self.n_fft, window=torch.hamming_window(self.n_fft),
            center=False, normalized=False, onesided=True
        )
        spectrogram = (spectrogram[:, :, 0].pow(2) + spectrogram[:, :, 1].pow(2)).pow(0.5)
        spectrogram = np.log1p(spectrogram.numpy())
        return spectrogram
