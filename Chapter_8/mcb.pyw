#! python3
# mcb.pyw - Созраняет и загружает фрагменты текста в буфер обмена.
# Использование: py.exe mcb.pyw save <ключевое слово> - Сохраняет буфер обмена в ключевое слово.
#                py.exe mcb.pyw <ключевое слово> - Загружает ключевое слово в буфер обмена.
#                py.exe mcb.pyw list - Загружает все ключевые слова в буфер обмена.

import shelve
import pyperclip
import sys

mbcShelf = shelve.open('mcb')
# Сохранить содержимое буфера обмена.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
        # Сформировать список ключевых слов и загрузить содержимое.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mbcShelf.close()
