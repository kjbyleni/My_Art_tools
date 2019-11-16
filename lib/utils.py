import os


def print_items(items):
    for item in items:
        print(f'\t\t{item}')


def print_result(items, context):
    print(
        '\n\t',
        f'---------   Creating your {context}  ---------'
    )
    print_items(items)
    print(f'\t -----------   {context} Created!   -----------\n')


def validate_is_number(how_many=None, attempt=0):
    if how_many is None:
        how_many = input('How Many? ')
    try:
        return int(how_many)
    except ValueError:
        print("input must be a number")
        if attempt > 1:
            print("too many attempts!")
        else:
            validate_is_number(how_many=None, attempt=attempt + 1)


# edit_file requires a generator object
def edit_file(generator):
    tmp_path = './tmp_path.json'
    # print keys
    print_items(generator.get_keys())
    key = input("\nWhich list to modify? ")
    f = open(tmp_path, 'w')
    if key in generator.lst:
        for item in sorted(generator.lst[key]):
            # print existing list
            f.write(f'{item}\n')
        f.close()

        # open notepad.exe allow user to edit.  Wait until done editing
        os.system(f'notepad.exe {tmp_path}')
        generator.lst[key] = generator.convert_file_to_array(tmp_path)
        generator.export_lst()
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
            print("SUCCESS!")
