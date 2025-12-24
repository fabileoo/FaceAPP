# FaceAPP

Простое Python-приложение для распознавания лиц.  
Программа отличает меня от моей девушки по фотографии.

## Возможности
- Определяет лицо на изображении
- Сравнивает с сохранёнными образцами
- Возвращает результат: "Я", "Девушка" или "Неизвестный человек"

## Технологии
- Python 3.10
- face-recognition
- OpenCV
- NumPy

## Установка и запуск
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py