import csv
import pandas as pd


def read_df(path):
    df = pd.read_pickle(path)
    return df


def create_csv(data_dump_path):
    annotations_df = read_df(f"{data_dump_path}/annotations.pickle")
    validation_df = get_validated_captions(data_dump_path)
    annotations_df = annotations_df.join(
        validation_df.set_index("id"), lsuffix="_left", rsuffix="_right"
    )
    annotations_df["caption_id"] = annotations_df.index
    final_columns = ["caption_id", "track_id_left", "text", "valid", "familiarity"]
    annotations_df = annotations_df[final_columns].rename(
        columns={
            "track_id_left": "track_id",
            "text": "caption",
            "valid": "is_valid_subset",
        }
    )
    annotations_df.sort_values(by="track_id", inplace=True)
    annotations_df = add_jamendo_info(annotations_df, f"{data_dump_path}/jamendo.tsv")
    annotations_df.to_csv(f"{data_dump_path}/song_describer.csv", index=False)
    return annotations_df


def group_by_track(annotations_df, out_dir, save=False):
    annotations_df = annotations_df[["track_id", "text"]]
    annotations_per_track = annotations_df.groupby("track_id", as_index=False).agg(
        lambda x: list(x)
    )
    if save:
        annotations_per_track.to_csv(
            f"{out_dir}/annotations_per_track.csv", index=False
        )
    return annotations_per_track


def get_id(value):
    return int(value.split('_')[1])


def add_jamendo_info(metadata_df, tsv_file):
    tracks = {}
    with open(tsv_file) as fp:
        reader = csv.reader(fp, delimiter='\t')
        for row in reader:
            track_id = get_id(row[0])
            tracks[track_id] = {
                'artist_id': get_id(row[1]),
                'album_id': get_id(row[2]),
                'path': row[3],
                'duration': float(row[4]),
                'tags': row[5:],  
            }
    for col in ['artist_id', 'album_id', 'path', 'duration']:
        metadata_df[col] = metadata_df['track_id'].map(lambda x: tracks[int(x)][col])
    return metadata_df


def get_validated_captions(data_dump_path):
    validation_path = f"{data_dump_path}/validation"
    col_names = ["id", "track_id", "user_id", "valid"]
    evaluated_dfs = [
        pd.read_csv(f"{validation_path}/evaluated_{i}.csv", header=None)
        for i in ["0", "1", "2_3", "4", "5", "6", "7", "8_9"]
    ]
    evaluated = pd.concat(evaluated_dfs, ignore_index=True)
    evaluated.columns = col_names
    map_valid = {-1: False, 0: None, 1: True}
    evaluated["valid"] = evaluated["valid"].map(map_valid)
    return evaluated


if __name__ == "__main__":
    data_dump_path = "data/data_dump_14_04_23"
    create_csv(data_dump_path)
