# Song Describer Dataset Data Card
## Dataset Overview
| Subset | Tracks | Captions | Annotators | Cap len (avg) | Vocab size  | Audio len | 
|:----:|:----:|:-----:|:-----:|:----:|:-----:|:-----:|
| full | 706 | 1106 | 142 |  21.7 ± 12.4 |  2859 |  ~ 2 min | 
| valid| 546 | 746  | 114 |  18.2 ± 7.6 | 1942 |  ~ 2 min | 

## Dataset Structure

The dataset is structured as follows:
-  **`audio`**: contains the audio files organised in subfolders
    - `00`
        - `audio_id_xx.2min.mp3`
        - ...
    - ...
- **`song_describer.csv`**: main csv file containing the data annotations and metadata
- **`audio_licenses.txt`**: text file with the audio licenses for each track in the dataset
- **`song_describer.mtg-jamendo.tsv`**: [MTG-Jamendo](https://mtg.github.io/mtg-jamendo-dataset/) metadata for each track in the dataset

Each instance in the metadata contained in `song_describer.csv` contains the following fields:
```json
"caption_id": , # unique id assigned to the caption
"track_id": ,
"caption": "",
"is_valid_subset": True,
"familiarity": 
"artist_id": , # unique id for the track's artist (from MTG-Jamendo)
"album_id": , # unique id for the track's album (from MTG-Jamendo)
"path": , # relative path to the audio file
"duration": , # duration of the original track (from MTG-Jamendo)
"genre": [], #  (from MTG-Jamendo)
"instrument": [], # (from MTG-Jamendo)
"mood/theme": [], # (from MTG-Jamendo)
```

We provide a single split for the dataset, as it is solely intended for evaluation.

All the audio files are in 320kbps MP3 format.

## Dataset Creation
The Song Describer Dataset was developed as a benchmark dataset for evaluating models on music-and-language (M&L) tasks.

### Data Collection
The audio in the Song Describer Dataset comes from the `split-0` test split of the [MTG-Jamendo dataset](). The annotations (captions) were crowdsourced via the [Song Describer platform](https://github.com/ilaria-manco/song-describer).

### Data Validation
[todo]
