import os
import json

extensions = {
    'Raster Graphics File': ['.bmp', '.img', '.jpg', '.jpeg', '.png', '.gif', '.tiff'],
    'Vector Graphics File': ['.ai', '.svg', '.eps', '.ai'],
    'Video File': ['.mp4', '.avi', '.mpeg', '.mkv', '.flv', '.mov', '.vob', '.wmv', '.rmvb'],
    'Audio File': ['.mp3', '.aac', '.flac', '.3gp', '.m4a', '.mpc', '.wav', '.wma'],
    'Text File': ['.txt', '.doc', '.docx', '.odt', '.rtf', '.tex'],
    'Data File': ['.xml', '.json'],
    'PDF File': ['.pdf'],
    'Spreadsheet File': ['.xls'],
    'Web File': ['.html', '.css'],
    'Programming Language File': ['.py', '.js', '.c', '.cpp', '.h', '.hpp', '.pyc'],
    'Executable File': ['.exe', '.bat', '.bash'],
    'Binary File': ['.bin'],
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
