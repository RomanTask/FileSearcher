import time
import flet as ft
import shutil
from pathlib import Path
import easygui


def main(page: ft.Page):
    # PAGE SETTINGS
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.title = 'Search and copy by file resolution'
    page.window_width = 600
    page.window_height = 900
    page.window_center()

    # EVENT FUNCTION - THE COPY OF FILES FROM DIRECTORY (from 'root_path' to 'path_to_save')
    def copy_image(e):

        total_path = []

        # print(f'{check_1.value}, {check_2.value},{check_3.value}')

        begining_path = root_path.value.replace('\\', '/')

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

        text_coping.value = 'Coping'

        progress_bar.visible = True
        page.update()
        total_count = len(total_path)



        for image in total_path:
            shutil.copy(image, f'{destination_path}')


        time.sleep(3)


        progress_bar.value =1

        total_result.value = f'Копирование объектов в количестве {total_count} завершено'
        page.update()

    def beginPath(e):
        root_path.value = easygui.diropenbox()
        begining_path = root_path.value.replace('\\', '/')
        root_path.value = begining_path
        page.update()

    def destinationPath(e):
        path_to_save.value = easygui.diropenbox()
        destination_path = path_to_save.value.replace('\\', '/')
        path_to_save.value = destination_path
        page.update()

    # ACTION CHECKBOX ELEMENTS
    check_1 = ft.Checkbox(label='jpg')
    check_2 = ft.Checkbox(label='png')
    check_3 = ft.Checkbox(label='heic')
    check_4 = ft.Checkbox(label='mp4')
    check_5 = ft.Checkbox(label='avi')

    # ACTION BUTTON
    button_action = ft.ElevatedButton(text='START COPYING', bgcolor='#79A0C1', color='black', width=350,
                                      on_click=copy_image)

    # TEXTFIELD WHERE SAVE
    path_to_save = ft.TextField(helper_text='ENTER DIRECTORY WHERE TO SAVE', width=300)

    # TEXTFIELD WHERE ARE FINDING FILES
    root_path = ft.TextField(helper_text='ENTER DIRECTORY PATH WHERE SEARCH', width=300)

    # PROGRESSIVE BAR
    progress_bar = ft.ProgressBar(width=350, visible=False)

    # TEXT IN DURING COPING
    text_coping = ft.Text()

    # TOTAL RESULT TEXT
    total_result = ft.Text(weight=ft.FontWeight.BOLD)

    # WIDGET STRUCTURE
    main_container = ft.Container(
        padding=5,
        width=450,
        height=700,
        border_radius=25,
        bgcolor='black',
        content=ft.Container(
            padding=ft.padding.all(50),
            bgcolor='black',
            border_radius=25,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=['lightblue600', 'yellow']),
            content=(ft.Column(controls=[
                ft.Row([
                    ft.Text('FILE MANAGER', font_family="Consolas", weight=ft.FontWeight.BOLD, size=18)
                ]),
                ft.Column([ft.Row([
                    root_path,
                    ft.IconButton(ft.icons.FOLDER_OPEN, on_click=beginPath)

                ])]),
                ft.Divider(visible=True),
                ft.Column([
                    ft.Row([
                        path_to_save,
                        ft.IconButton(ft.icons.FOLDER_OPEN, on_click=destinationPath)
                    ])]),
                ft.Divider(visible=True),
                ft.Row([
                    button_action
                ]),
                ft.Divider(visible=True),
                ft.Container(content=ft.Text('File resolution for copying:', weight=ft.FontWeight.BOLD)),
                ft.Column([ft.Column([ft.Row([
                    check_1,
                    check_2,
                    check_3,
                    check_4,
                    check_5
                ])])]),
                ft.Column([text_coping,progress_bar,total_result])

            ], horizontal_alignment=ft.MainAxisAlignment.CENTER, alignment=ft.CrossAxisAlignment.CENTER)
            )
        ))

    page.add(
        main_container
    )


ft.app(target=main, assets_dir='assets')
