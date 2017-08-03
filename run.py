from curiosity import Curiosity


def  painters():
    # ЦИКЛ ПРОХОДА ИЗОБРАЖЕНИЙ ДЛЯ ХУДОЖНИКА
    count = 0
    max_index = len(Curiosity.topic_img_0_scr) - 1
    while count <= max_index:
        Curiosity.painter(count)
        count = count + 1
    return print(f"ХУДОЖНИК УСПЕШНО ОТРИСОВА {max_index} ИЗОБРАЖЕНИЙ")


def test():
    Curiosity.topicsparser()

try:
    test()
except:
    print("ОШИБКА В ХОДЕ ТЕСТА")
    pass
finally:
    test()

if __name__ == "__main__":
    print("ТЕСТ ЛЮБОПЫТСТВА ВЫПОЛНЕН")