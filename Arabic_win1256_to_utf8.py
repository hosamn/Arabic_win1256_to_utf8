import os

# Change the working directory to the py file dir:
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get a list of current dir subtitle files:
for root, dirs, files in os.walk("."):
    # print(len(files), files)
    # sub_ext = ('.srt','.sub','.ass','.ssa')
    sub_fls = [f for f in files if f.endswith('.srt')]
    print(sub_fls)
    break  # break after reporting current dir files and don't go deeper


# Try to Read file as win 1256 > if ok save as utf8 > if not leave it as is:
for sub_file in sub_fls:
    print('===========================================')
    print('Checking file :  " ', sub_file, '"')
    try:
        with open(sub_file, 'r', encoding='Windows-1256') as fl:
            text = fl.read()
            if 'ا' in text:
                print('file  "', sub_file, '"  red as win1256 successfully!')
                open(sub_file, 'w', encoding='UTF-8').write(text)
                print('file  "', sub_file, '"  saved as utf8 successfully!')
            else:
                print('I think  "', sub_file, '"  is NOT win1256')
    except Exception as e:
        print(e)
        # print('could not open file as win1256')

input('Press Enter to continue!')
