memory_in_mb = 1.44  # Память дискеты в Мб
memory_in_kb = 1024 * memory_in_mb  # Память дискеты в Кб
memory_in_byte = 1024 * memory_in_kb  # Память дискеты в Байтах
page_count = 100  # Количество страниц
line_count = 50  # Количество строк на странице
character_count = 25  # Количество символов в строке
total_character_count = character_count * line_count * page_count  # Общее количество символов в книге
total_character_size = total_character_count * 4  # Память, которую занимают символы в одной книге
books_in_memory = memory_in_byte // total_character_size  # Количество книг, которые могут храниться в дискете
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(books_in_memory))
