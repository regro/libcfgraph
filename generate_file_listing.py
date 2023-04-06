import json
import glob
import hashlib

N_FILES = 10


def _fname_to_index(fname):
    return (
        abs(int(hashlib.sha1(fname.encode("utf-8")).hexdigest(), 16))
        % N_FILES
    )


all_fnames = glob.glob('artifacts/**/*.json', recursive=True)
all_finds = [_fname_to_index(fname) for fname in all_fnames]

for i in range(N_FILES):
    with open(".file_listing_%d.json" % i, "w") as fp:
        json.dump(
            sorted([fname for fname, find in zip(all_fnames, all_finds) if find == i]),
            fp,
            indent=2,
        )

with open(".file_listing_meta.json", "w") as fp:
    json.dump({"n_files": N_FILES}, fp, indent=2)
