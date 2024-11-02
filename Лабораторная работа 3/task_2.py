def find_common_participants(first_group, second_group, separator = ","):

    general_participants = []  # Создаём список для внесения туда общих участников

    for general in first_group.split(separator):  # Берём каждого участника из первой группы
        if general in second_group.split(separator):  # Проверяем, есть ли этот участник во второй
            general_participants.append(general)  # Если такой есть, то добавляем его в список общих участников

    return sorted(general_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator = "|"))
