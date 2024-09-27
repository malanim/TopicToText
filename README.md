# TopicToText-Light

Generating reports using the g4f library

# Документация и руководство пользователя

## Содержание

1. Введение
2. Установка
3. Основные функции
4. Интерфейс пользователя
5. Использование программы
6. Часто задаваемые вопросы (FAQ)
7. Поддержка и обратная связь
8. Заключение

## 1. Введение

Данное руководство предназначено для пользователей программы, разработанной для автоматизации процесса создания курсовых работ. Программа помогает в сборе информации, структурировании текста и проверке на плагиат.

## 2. Установка

### 2.1 Системные требования

Операционная система: Windows 10 и выше
Google Chrome версии 130.0 и выше
Подключение к интернету (для некоторых функций)

### 2.2 Шаги установки

Скачайте архив с официального сайта.
Разархивируйте архив в любое место.
В директории TopicToText откройте файл TopicToText.exe

## 3. Основные функции

Генерация текста: Автоматическое создание текста на основе введенных ключевых слов.
Структурирование: Помощь в создании структуры курсовой работы, включая введение, основные разделы и заключение.
Проверка на плагиат: Анализ текста на уникальность и предоставление отчетов.
Сохранение и экспорт: Возможность сохранения работы в формате DOCX.

## 4. Интерфейс пользователя

### 4.1 Главный экран

Поле для ввода ключевых слов.
Кнопка для генерации текста, проверки на плагиат и сохранения работы.

### 4.2 Консоль отладки

Отображение результатов и ошибок программы.

## 5. Использование программы

### 5.1 Генерация текста

Введите ключевые слова в соответствующие поля.
Нажмите на кнопку "Готово".
Ожидайте отображения надписи “continue!” в строке состояния.

### 5.2 Использование шаблонов

Добавлена возможность использовать шаблон титульного листа. Достаточно оставить файл с титульным листом под названием `template.docx` в директории с программой. Пример такого шаблона представлен в репозитории под таким же названием.

#### 5.2.1 Чтобы программа поняла, куда вставлять данные, в шаблоне могут быть использованы выражения:
- {{theme}} - Тема
- {{name}} - ФИО
- {{group}} - Группа
- {{college}} - Учебное заведение

## 6. Часто задаваемые вопросы (ЧаВо)

Вопрос: Как восстановить удалённый проект?
Ответ: Восстановление невозможно. Рекомендуется регулярно сохранять вашу работу.

Вопрос: Как обновить программу?
Ответ: Скачайте последнюю версию с официального сайта и выполните установку заново.

## 7. Поддержка и обратная связь

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по электронной почте: max1129@mail.ru.

## 8. Заключение

Спасибо за использование этой программы по назначению. Мы надеемся, что она поможет вам в учебе и сэкономит ваше время.

## 9. Использованные библиотеки

dependencies (libraries used):
eel,
g4f,
python-docx.
