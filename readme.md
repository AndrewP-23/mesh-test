**Разметка облаков точек и mesh для оценки геометрических характеристик объектов**

_Тестовое задание_

Для запуска использовать _main.py_.

Первой командой принимается файл со входными данными (множество точек).
Далее могут передаваться следующие команды:

_count_ - вывести количество точек в облаке;

_print_ - вывести координаты точек;

_rm_ `lower_bound` `upper_bound` - удалить точки с координатой z, лежайщей в заданном диапазоне;

_hist_ - вывести гистограмму высот;

_exit_ - закончить исполнение программы.

В файле _input.txt_ приведен пример подаваемых команд.

В _mesh.txt_ - 1000 точек с координатами в диапазоне от -30 до 30, сгенерированных случайно с равномерным распределением на данном отрезке.

Можно использовать _generate_mesh.py_ для генерации подобных входных файлов, меняя в нем параметры.

Команда для запуска docker-контейнера: docker run --rm -it andrewp23/mesh:1.0
