import json
from pathlib import Path
from shutil import copy


def get_metadata(path):
    if not path.exists():
        return None
    filename = path.name.replace('.tar.gz', '')
    splitname = filename.split('-')
    cp_loc = Path('serve/system/releases/{}/{}/'.format(splitname[0][0], splitname[0]))
    cp_loc.mkdir(parents=True, exist_ok=True)
    copy(str(path), str(cp_loc))
    return {
        'author': splitname[0],
        'name': splitname[1],
        'version': splitname[2],
        "tag_list": []
    }


def prepare_repo():
    modules = Path('modules')
    all_meta = []
    for module in modules.iterdir():
        meta = get_metadata(module)
        if meta:
            all_meta.append(meta)

    metadata_file = Path('serve/modules.json')
    if metadata_file.exists():
        metadata_file.unlink()
    with metadata_file.open('w') as outfile:
        json.dump(all_meta, outfile)


if __name__ == '__main__':
    prepare_repo()
