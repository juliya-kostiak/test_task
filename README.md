# test_task
Процедура запуска проекта

1.	Скачиваем папку с проектом с репозитория на Githab

2.	Открываем проект в IDE (PyCharm)

3.	Устанавливаем виртуальное окружение <br/>
    Для это открываем на панели меню File/Settings <br/>
    В открывшемся окне выбираем Project/Python Interpreter <br/>
    В верхнем правом углу, щелкнув по иконке настроек, выбираем Add/Virtualenv Environment 
    
4.	Открываем терминал

5.	Переходим в папку cd keymanage_app (если мы находимся не в ней)

6.	Устанавливаем зависимости из requirements.txt
    pip install -r requirements.txt
  
7.	Далее запускаем проект 
    python manage.py runserver
