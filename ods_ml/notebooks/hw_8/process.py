
POSSIBLE_TAGS = ['javascript', 'java', 'python', 'ruby',\
                 'php', 'c++', 'c#', 'go', 'scala', 'swift']

LABELS = {val: str(key + 1) for key, val in enumerate(POSSIBLE_TAGS)}

def prepare_text(text):
    text = text.strip()
    text = text.replace('|', '')
    text = text.replace(':', '')
    return text

def process_line(line):
    line = line.strip()
    parts = line.split('\t')
    if len(parts) != 2 or not line[0] or not line[1]:
        return None, None
    text = prepare_text(parts[0])
    tags = parts[1].split()
    if not text or not tags:
        return None, None
    tags_found = 0
    res_tag = None
    for tag in POSSIBLE_TAGS:
        if tag in tags:
            tags_found += 1
            if tags_found > 1:
                res_tag = None
                break
            res_tag = tag
    return text, res_tag


def process_file(filename, target_filename):
    print('Start processing file')
    line_counter = 0
    with open(filename, 'r') as f_from:
        with open(target_filename, 'w+') as f_to:
            for line in f_from:
                text, tag = process_line(line)
                if text and tag:
                    tag = LABELS[tag]
                    f_to.write('{} |{}\n'.format(tag, text))
                    line_counter += 1
    print('Done, lines: {}'.format(line_counter))


def split_train_test(filename):
    print('Start split')
    train_size = 1463018
    ind = 0
    train_file = open('stackoverflow_train.vw', 'w+')
    test_file = open('stackoverflow_test.vw', 'w+')
    valid_file = open('stackoverflow_valid.vw', 'w+')
    train_labels = open('stackoverflow_train.txt', 'w+')
    test_labels = open('stackoverflow_test.txt', 'w+')
    valid_labels = open('stackoverflow_valid.txt', 'w+')

    with open(filename, 'r') as file_from:
        for line in file_from:
            tag = line.split('|')[0].strip()
            if ind < train_size:
                train_file.write(line)
                train_labels.write('{}\n'.format(tag))
            elif ind < 2 * train_size:
                valid_file.write(line)
                valid_labels.write('{}\n'.format(tag))
            else:
                test_file.write(line)
                test_labels.write('{}\n'.format(tag))
            ind += 1
            if ind == train_size:
                print('== train done, writing valid')
            if ind == 2 * train_size:
                print('== valid done, writing test')

    train_file.close()
    test_file.close()
    valid_file.close()
    train_labels.close()
    test_labels.close()
    print('Done')


if __name__ == '__main__':
    from_file = 'F:\stack_overflow_data\stackoverflow.10kk.tsv'
    to_file = 'input.vw'
    process_file(from_file, to_file)
    split_train_test(to_file)
