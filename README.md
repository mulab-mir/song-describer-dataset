<div  align="center">

# The Song Describer Dataset: a Corpus of Audio Captions for Music-and-Language Evaluation
[Ilaria Manco](https://ilariamanco.com/)\*<sup>1,2</sup>,
[Benno Weck]()\*<sup>3</sup>, 
[Seungheon Doh]()<sup>4</sup>, 
[Minz Won]()<sup>5</sup>,
[Yixiao Zhang]()<sup>1</sup>,
[Dmitry Bogdanov]()<sup>3</sup>, 
[Yusong Wu]()<sup>6</sup>, 
[Ke Chen]()<sup>7</sup>, 
[Philip Tovstogan]()<sup>3</sup>, 
[Emmanouil Benetos](http://www.eecs.qmul.ac.uk/~emmanouilb/)<sup>1</sup>,
[Elio Quinton](https://scholar.google.com/citations?user=IaciybgAAAAJ)<sup>2</sup>,
[George Fazekas](http://www.eecs.qmul.ac.uk/~gyorgyf/about.html)<sup>1</sup>,
[Juhan Nam]()<sup>4</sup><br>

<sup>1</sup>  QMUL, <sup>2</sup>  UMG, <sup>3</sup> UPF, <sup>4</sup> KAIST, <sup>5</sup> ByteDance, <sup>6</sup> MILA, <sup>7</sup> UCSD 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-000-<COLOR>.svg)](https://arxiv.org/abs/000)
![Zenodo doi badge](https://img.shields.io/badge/DOI-000%2Fzenodo.000-blue.svg)

<p align="center">
<img src="sdd.png" width="500">
</p align="center">
</div>
* equal contribution

This repository contains starter code for the Song Describer Dataset (SDD).
* [Paper](https://arxiv.org/abs/???) (accepted to the [ML for Audio workshop](https://mlforaudioworkshop.com/) @ NeurIPS 2023) 
* [Zenodo]()
* [Datasheet](datasheet.md)
* [Huggingface]()

## Dataset overview

SDD contains ~1.1k captions for 706 music recordings and can be used to evaluate models that address music-and-language tasks such as music captioning, text-to-music generation and music-language retrieval. More information about the data, collection method and validation is provided in the [data card](datacard.md).

| Subset | Tracks | Captions | Annotators | Cap len (avg) | Vocab size  | Audio len | 
|:----:|:----:|:-----:|:-----:|:----:|:-----:|:-----:|
| full | 706 | 1106 | 142 |  21.7 ± 12.4 |  2859 |  ~ 2 min | 
| valid| 546 | 746  | 114 |  18.2 ± 7.6 | 1942 |  ~ 2 min | 

## Downloading the dataset

The dataset is available to download from Zenodo. Download script [here](download.sh).

```bash
[todo]
```

## Code setup
Create a virtual environment:

```bash
python -m venv venv 
source venv/bin/activate
```

Then, clone the repository and install the dependencies:

```bash
git clone [todo]
```

## Using the dataset

## Reproducing the analysis in the paper
The overview statistics presented in the paper can be reproduced via the code in the [`dataset_stats.ipynb`](dataset_stats.ipynb) notebook.

## Cite
If you use the dataset or the code in this repo, please consider citing our work:

```bib
[todo]
```

## License
This repository is released under the MIT License. Please see the [LICENSE](LICENSE) file for more details. The dataset is released under the [CC BY-SA 4.0 license]().

## Contact
If you have any questions, please get in touch: [i.manco@qmul.ac.uk](i.manco@qmul.ac.uk).
