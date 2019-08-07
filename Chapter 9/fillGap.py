import os, re, shutil

src_fdr = input('Enter source folder to search from:\n')
des_fdr = input('Enter destination folder to rename to:\n')
prefix_pos, prefix_len =input('Prefix starts at (Beginning/End) of file name?: '), str(len(input('Prefix starts with: ')))

prefix_start_regex = re.compile(r'\b\d{' + prefix_len + r'}(\D+\.\w+)')  # Search prefix at beginning of file name.
prefix_end_regex = re.compile(r'(\w+\D)\d{' + prefix_len + r'}(\.\w+)')  # Search prefix at end of file name.
prefix_count = 1
list_files = []

for file in os.listdir(src_fdr):
    if prefix_pos == 'Beginning':  # Find files with prefix starting & append to a list var.
        fileObj = prefix_start_regex.search(file)
        if fileObj != None:
            list_files.append(file)
    elif prefix_pos == 'End':  # Find files with prefix ending & append to a list var.
        fileObj = prefix_end_regex.search(file)
        if fileObj != None:
            list_files.append(file)

for each in sorted(list_files):  # Sort the list in ascending order.
    if prefix_pos == 'Beginning':  # Rename prefix at the beginning of file name.
        fileObj = prefix_start_regex.search(each)
        if fileObj != None:
            new_prefix = str(prefix_count).zfill(int(prefix_len))
            new_filename = new_prefix + fileObj.group(1)
            prefix_count += 1
            shutil.move(os.path.join(src_fdr, each), os.path.join(des_fdr, new_filename))
    elif prefix_pos == 'End':  # Rename prefix at the end of file name.
        fileObj = prefix_end_regex.search(each)
        if fileObj != None:
            new_prefix = str(prefix_count).zfill(int(prefix_len))
            new_filename = fileObj.group(1) + new_prefix + fileObj.group(2)
            prefix_count += 1
            shutil.move(os.path.join(src_fdr, each), os.path.join(des_fdr, new_filename))

print('Prefixes for files are renamed in running order.')
