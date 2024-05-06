# EVENT FUNCTION - THE COPY OF FILES FROM DIRECTIRY (from 'root_path' to 'path_to_save')
def copy_image(e):

    total_path = []


    # print(f'{check_1.value}, {check_2.value},{check_3.value}')

    begining_path = root_path.value.replace('\\','/')

    destination_path = path_to_save.value.replace('\\', '/')


    if check_1.value == True:

        paths = sorted(Path(begining_path).glob(f'**/*.{check_1.label}'))
        new = list(map(str, paths))
        total_path.extend(new)
        page.update()

    if check_2.value == True:

        paths = sorted(Path(begining_path).glob(f'**/*.{check_2.label}'))
        new = list(map(str, paths))
        total_path.extend(new)
        page.update()

    if check_3.value == True:

        paths = sorted(Path(begining_path).glob(f'**/*.{check_3.label}'))
        new = list(map(str, paths))
        total_path.extend(new)
        page.update()

    if check_4.value == True:

        paths = sorted(Path(begining_path).glob(f'**/*.{check_4.label}'))
        new = list(map(str, paths))
        total_path.extend(new)
        page.update()


    if check_5.value == True:

        paths = sorted(Path(begining_path).glob(f'**/*.{check_5.label}'))
        new_5 = list(map(str, paths))
        total_path.extend(new_5)
        page.update()

    for image in total_path:
        shutil.copy(image, f'{destination_path}')


    print(total_path)
    page.update()
