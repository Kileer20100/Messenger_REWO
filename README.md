

markdown
# Мессенджер WORE на Python з використанням Kivy та ZeroMQ

Цей проект реалізує додаток на **Python**, використовуючи бібліотеки **Kivy** для створення графічного інтерфейсу та **ZeroMQ** для організації швидкого і ефективного обміну повідомленнями між компонентами програми.

## Технології

1. **Python** — мова програмування для розробки додатків.
2. **Kivy** — потужна бібліотека для створення кросплатформових графічних інтерфейсів користувача (GUI).
3. **ZeroMQ** — бібліотека для реалізації мережевої взаємодії з низьким рівнем затримки та високою пропускною здатністю.

## Вимоги

- Python 3.6 або новіше
- pip (менеджер пакетів для Python)

## Інструкції по встановленню

### Для macOS

1. Встановіть Python 3 через [Homebrew](https://brew.sh/) або скачайте з офіційного сайту Python.
2. Встановіть необхідні бібліотеки:
   
   ```bash
   pip install kivy pyzmq
   ```
4. Завантажте проект:
   ```bash
   git clone https://github.com/Kileer20100/Messenger_REWO.git
   cd yourproject
   ```
5. Запустіть додаток:
   ```bash
   python main.py
   ```

### Для Linux (Ubuntu)

1. Встановіть Python 3 та необхідні бібліотеки:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev build-essential
   pip3 install kivy pyzmq
   ```
2. Завантажте проект:
   ```bash
   git clone https://github.com/Kileer20100/Messenger_REWO.git
   cd yourproject
   ```
3. Запустіть додаток:
   ```bash
   python3 main.py
   ```

### Для Linux (Fedora)

```markdown
### Для Linux (Fedora)

1. Встановіть Python 3 та необхідні бібліотеки:
   ```bash
   sudo dnf install python3-pip python3-devel gcc-c++ make
   pip3 install kivy pyzmq
   ```
2. Завантажте проект:
   ```bash
   git clone https://github.com/Kileer20100/Messenger_REWO.git
   cd yourproject
   ```
3. Запустіть додаток:
   ```bash
   python3 main.py
   ```
```

### Для Windows

1. Завантажте Python 3 з [офіційного сайту](https://www.python.org/downloads/).
2. Після встановлення Python, відкрийте командний рядок та встановіть необхідні бібліотеки:
   ```bash
   pip install kivy pyzmq
   ```
3. Завантажте проект:
   ```bash
   git clone https://github.com/Kileer20100/Messenger_REWO.git
   cd yourproject
   ```
4. Запустіть додаток:
   ```bash
   python main.py
   ```

## Використання

Цей додаток забезпечує швидкий обмін повідомленнями між різними частинами вашої програми за допомогою **ZeroMQ**, а також надає зручний **графічний інтерфейс** за допомогою **Kivy**. Після запуску програми ви зможете взаємодіяти з основними компонентами через GUI, а всі повідомлення будуть передаватися через ZeroMQ.

## Зв'язок з розробниками

Нема.

## Ліцензія


