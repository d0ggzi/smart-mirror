# ПО для умного зеркала компании ReflectMe

## Основная информация

Данное программное обеспечение предназначено для работы на физическом прототипе умного зеркала. Весь код написан на python, основные используемые библиотеки:  

* PyQt5  
* OpenCV  
* mediapipe  

Экраны интерфейса:  

* Главный  
* Каталог  
* Галерея  
* Корзина  

![Главный экран](https://github.com/d0ggzi/smart-mirror/assets/43131496/198b3b27-5efc-4bbc-8d36-63a7d3d80006)        ![Каталог](https://github.com/d0ggzi/smart-mirror/assets/43131496/fe86da3b-68aa-43d1-9ca6-b74b85672570)  

![Галерея](https://github.com/d0ggzi/smart-mirror/assets/43131496/709f2f48-9f47-4f8f-8406-d140b18f07bd)        ![Корзина](https://github.com/d0ggzi/smart-mirror/assets/43131496/d847b626-302e-4432-a55e-7281eea51769)  



## Структура

```
smart-mirror
├── img  
│   ├── catalog - каталог одежды, разделённый на подкатегории  
│   │   ├── кофты  
│   │   ├── платья  
│   │   ├── футболки  
│   │   ├── ...  
│   ├── gallery - галерея фотографий, сделанных пользователем при нажатии на камеру  
│   ├── UI-images - картинки, используемые в интерфейсе  
├── mp_hand_gesture - дополнительные файлы mediapipe для распознавания жестов
├── ui - хранит ui файлы интерфейса библиотеки PyQt5  
├── size_recognizer - модуль распознавания размера одежды  
│   main.py - основной файл для запуска проекта  
│   ...Window.py - файлы для управления экранами  
│   gestures.py - отвечает за определение позиции руки, управление мышью компьютера, а также распознавание жестов (временно отключено)  
```

## Использование

> [!NOTE]  
> ПО предназначено для вертикальных экранов по подобию зеркала, если Ваш экран не вмещает главный экран полностью, попробуйте увеличить разрешение монитора в настройках системы  

Выбор одежды происходит нажатиями ▲ и ▼, выбранная одежда слева отображается больше, чем обычные  
При нажатии кнопки фотографирования встаньте на расстояние около 1.8 метра от камеры  
Начнется обратный отсчёт 5 секунд - позируйте!   
Подождите, пока фотография обработается...  
Выбранная одежда наложится на Вас, а также определится Ваш размер по параметрам высоты и ширины тела  
Понравилась одежда? Добавьте ее в корзину, нажав на кнопку "В корзину"  




## Установка на *linux*

1. Скачать репозиторий   
    > git clone https://github.com/d0ggzi/smart-mirror  
    > cd smart-mirror  

2. Создание и активация виртуального окружения  
    > python -m venv venv  
    > source venv/bin/activate  

3. Установка библиотек  
    > pip install -r requirements.txt  

    *Это займет время...*  

4. Дать дополнительные права запуска  
    > xhost +SI:localuser:root  

5. Запустить  
    > sudo python main.py  

6. Готово! Вы прекрасны!