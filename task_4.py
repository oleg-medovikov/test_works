# это у меня было реализовано
import os
from glob import iglob
from datetime import datetime, timedelta

N_days = 5
directory = "tmp/*"


def main():

    cutoff_date = datetime.now() - timedelta(days=N_days)
    print(f"начинаю удалять старые фалйы в {directory}")
    for file_path in iglob(directory):
        if os.path.isfile(file_path):
            # Получение даты последнего изменения файла
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Если файл старше N_days дней, удалить его
            if file_modified_time < cutoff_date:
                try:
                    os.remove(file_path)
                except Exseption as e:
                    # тут файл может быть занят(ошибка доступа), или что-то еще
                    print(f"Файл {file_path} не удалось удалить\n{e}")
                    continue
                else:
                    print(f"Файл {file_path} был удален.")
    print("Готово!")


if __name__ == "__main__":
    main()
