import pytest
import os
from zipfile import ZipFile


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RESOURSES_DIR = os.path.join(CURRENT_DIR, 'resourses')

@pytest.fixture(scope='session', autouse=True)
def test_create_files_zip():
    if not os.path.exists('resourses/'):
        os.mkdir('resourses')
    source_dir = os.path.abspath('tmp')  # адрес директории
    final_dir = os.path.abspath('resourses')  # адрес директории куда будет перемещен архив
    os.chdir(TMP_DIR)  # переход в директорию
    list_files = [os.path.join(source_dir,'test.csv'),
                  os.path.join(source_dir, 'test.xlsx'),
                  os.path.join(source_dir, 'test.pdf')]  # список файлов которые будут добавлены в архив
    zip_name = os.path.join(final_dir, 'files.zip')  # имя архива
    if os.path.exists(zip_name):
        os.remove(zip_name)
    with ZipFile(zip_name, 'w') as zipbox:  # создание архива
        for file in list_files:  # добавление файлов в архив
            zipbox.write(file, arcname=os.path.basename(file))
    assert os.path.exists(zip_name) is True