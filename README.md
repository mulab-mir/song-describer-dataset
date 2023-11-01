<div  align="center">

# The Song Describer Dataset: a Corpus of Audio Captions for Music-and-Language Evaluation
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-000-<COLOR>.svg)](https://arxiv.org/abs/000)
![Zenodo doi badge](https://img.shields.io/badge/DOI-000%2Fzenodo.000-blue.svg)
[![Huggingface](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-yellow)](https://huggingface.co/datasets/mulab-mir/song-describer)

[Ilaria Manco](https://ilariamanco.com/)\*<sup>1,2</sup>,
[Benno Weck]()\*<sup>3</sup>, 
[Seungheon Doh](https://seungheondoh.github.io/)<sup>4</sup>, 
[Minz Won](https://minzwon.github.io/)<sup>5</sup>,
[Yixiao Zhang](http://www.eecs.qmul.ac.uk/~yz007/)<sup>1</sup>,
[Dmitry Bogdanov](https://dbogdanov.com/)<sup>3</sup>, 
[Yusong Wu](https://lukewys.github.io/)<sup>6</sup>, 
[Ke Chen](https://www.knutchen.com/)<sup>7</sup>, 
[Philip Tovstogan](https://philtgun.me/)<sup>3</sup>, 
[Emmanouil Benetos](http://www.eecs.qmul.ac.uk/~emmanouilb/)<sup>1</sup>,
[Elio Quinton](https://scholar.google.com/citations?user=IaciybgAAAAJ)<sup>2</sup>,
[George Fazekas](http://www.eecs.qmul.ac.uk/~gyorgyf/about.html)<sup>1</sup>,
[Juhan Nam](https://mac.kaist.ac.kr/~juhan/)<sup>4</sup><br>

<sup>1</sup>  QMUL, <sup>2</sup>  UMG, <sup>3</sup> UPF, <sup>4</sup> KAIST, <sup>5</sup> ByteDance, <sup>6</sup> MILA, <sup>7</sup> UCSD 

</div>
* equal contribution

This repository contains starter code for the Song Describer Dataset (SDD).
* [Paper](https://arxiv.org/abs/???) (accepted to the [ML for Audio workshop](https://mlforaudioworkshop.com/) @ NeurIPS 2023) 
* [Zenodo]()
* [Datasheet](datasheet.md)
* [Huggingface]()

## Dataset overview
<div align="center">
  
https://github.com/ilaria-manco/song-describer-dataset/assets/32579635/31ea7adc-149f-4f16-96af-48fce7a9941a
  
*"A retro-futurist drum machine groove drenched in bubbly synthetic sound effects and a hint of an acid bassline."*
  
</div>

SDD contains ~1.1k captions for 706 permissively licensed music recordings. It is designed for use in evaluation of models that address music-and-language (M&L) tasks such as music captioning, text-to-music generation and music-language retrieval. More information about the data, collection method and validation is provided in the [data card](datacard.md), together with more in-depth documentation in the [datasheet](datasheet.md).

| Subset | Tracks | Captions | Annotators | Cap len (avg) | Vocab size  | Audio len | 
|:----:|:----:|:-----:|:-----:|:----:|:-----:|:-----:|
| full | 706 | 1106 | 142 |  21.7 ± 12.4 |  2859 |  ~ 2 min | 
| valid| 546 | 746  | 114 |  18.2 ± 7.6 | 1942 |  ~ 2 min | 

## Downloading the dataset

The dataset is available to download from [Zenodo]():

```bash
wget [todo]
unzip [todo]
cd [todo]
```
A download script is also available [here](download.sh).

## Code setup
To use this code, we recommend creating a new python3 virtual environment:

```bash
python -m venv venv 
source venv/bin/activate
```

Then, clone the repository and install the dependencies:

```bash
git clone https://github.com/mulab-mir/song-describer-dataset.git
cd song-describer-dataset
pip install -r requirements.txt
```

## Reproducing the analysis in the paper
The overview statistics presented in the paper can be reproduced via the code in the [`dataset_stats.ipynb`](dataset_stats.ipynb) notebook.

## Using the dataset
### PyTorch
[Coming soon]

### HuggingFace

```python
!pip install datasets
from datasets import load_dataset

ds = load_dataset("mulab-mir/song-describer")
```

### Benchmarking M&L models with SDD

[coming soon]

## Cite
If you use the dataset or the code in this repo, please consider citing our work:

```bib
@inproceedings{manco2023thesong,
  title={The Song Describer Dataset: a Corpus of Audio Captions for Music-and-Language Evaluation}, 
  author={Manco, Ilaria and Weck, Benno and Doh, Seungheon and Won, Minz and Zhang, Yixiao and Bogdanov, Dmitry and Wu, Yusong and Chen, Ke and Tovstogan, Philip and Benetos, Emmanouil and Quinton, Elio and Fazekas, György and Nam, Juhan},
  booktitle={Machine Learning for Audio Workshop at NeurIPS 2023}, 
  year={2023},
}
```

## License
This repository is released under the MIT License. Please see the [LICENSE](LICENSE) file for more details. The dataset is released under the [CC BY-SA 4.0 license]().

## Contact
If you have any questions, please get in touch: [i.manco@qmul.ac.uk](i.manco@qmul.ac.uk).
