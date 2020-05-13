import os
import json

extensions = {
    'Raster Graphics File': ['.bmp', '.img', '.jpg', '.jpeg', '.png'],
    'Vector Graphics File': ['.ai', '.svg'],
    'Text File': ['.txt', '.doc'],
    'Data File': ['.xml'],
}


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = 'directory'
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        filename, file_extension = os.path.splitext(path)
        d['type'] = 'file'
        d['extension'] = file_extension
        for category, exts in extensions.items():
            if file_extension in exts:
                d['category'] = category

    return d


def main():
    structure = path_to_dict('.')
    with open('file_structure.json', 'w') as outfile:
        json.dump(structure, outfile, indent=4)


if __name__ == '__main__':
    main()
