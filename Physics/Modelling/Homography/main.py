from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk


# Ниже можно увидеть две функции, основная из них get_gomography, а вторая get_rotation_of_image
# get_gomography - функция для получения гомографии
# get_rotation_of_image - функция для получения поворота изображения
# Работа функций осуществляется с помощью библиотеки cv2 (OpenCV) и библиотеки numpy
# Все функции работают с изображениями, которые находятся в папке Photos
# К сожалению, пути к изображению приходится вводить вручную, поскольку это сильно усложняет работу с функциями

def get_rotation_of_image(path):
    new_window = Toplevel()

    # Чтение изображения
    image = PhotoImage(file="C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png")
    img = cv2.imread("C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png", 0)
    height, width = img.shape[:2]
    label = Label(new_window, image=image)
    label.pack()
    label.place(x=0, y=0)

    # Поворот изображения
    new_window.geometry(str(width * 2) + "x" + str(height))
    im_src = cv2.imread("C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png")
    pts_src = np.array([[100, 200], [400, 200], [100, 50], [400, 50]])
    im_dst = cv2.imread("C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png")
    pts_dst = np.array([[150, 150], [430, 170], [130, 20], [440, 10]])

    # Получение матрицы гомографии
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Применение матрицы гомографии
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    # Вывод изображения
    image_output = np.array(im_out)
    
    # Перевод изображения в формат, который может быть прочитан библиотекой PIL
    final_output = ImageTk.PhotoImage(image=Image.fromarray(image_output))
    canvas = Label(new_window, image=final_output)
    canvas.pack()
    canvas.place(x=width, y=0)
    new_window.mainloop()


# Функция для получения гомографии
def get_gomography(first_path, second_path):
    # Чтение изображений
    image1 = cv2.imread("C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png")
    image2 = cv2.imread("C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube2.png")

    # Дальше идет подготовка изображений для поиска ключевых точек (Мы использвуем несколько методов библиотеки OpenCV)
    # Инициализация SIFT детектора
    detected_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    detected_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(50)

    # Поиск ключевых точек и их дескрипторов
    kp1, des1 = orb.detectAndCompute(detected_image1, None)
    kp2, des2 = orb.detectAndCompute(detected_image2, None)

    # Создание BFMatcher объекта
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

    # Использование knnMatch() для получения двух лучших совпадений
    matches = matcher.match(des1, des2, None)
    matches = sorted(matches, key=lambda x: x.distance)

    # Отрисовка совпадений
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    # Получение координат точек
    for i, match in enumerate(matches):
        points1[i, :] = kp1[match.queryIdx].pt
        points2[i, :] = kp2[match.trainIdx].pt
    h = cv2.findHomography(points1, points2, cv2.RANSAC)[0]
    height, width, channels = image2.shape

    # Получение гомографии
    im1Reg = cv2.warpPerspective(image1, h, (width, height))
    img3 = cv2.drawMatches(detected_image1, kp1, detected_image2, kp2, matches[:10], None)
    print(h)

    # Вывод изображений
    cv2.imshow('Keypoint matches', img3)
    cv2.imshow('Registered image', im1Reg)
    cv2.waitKey(0)


if __name__ == '__main__':
    # Здесь создается среда для работы с графическим интерфейсом
    window = Tk()
    window.geometry("680x500")
    window.title("Homography")

    # Загрузка иконки для окна
    icon = PhotoImage(file="C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\icon.png")
    window.iconphoto(True, icon)
    background_image = PhotoImage(file="C:\\Users\\DNK\\PycharmProjects\\pythonProject2\\Photos\\cube1.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Работа с графическим интерфейсом (кнопки, поля ввода и т.д.)
    entry_first = Entry(window)
    entry_first.pack()

    # При работе с приложением не нужно вводить путь к файлу, так как он уже указан в коде
    entry_first.insert(0, "Path to first image")
    entry_first.place(x=22, y=115)
    entry_second = Entry(window)
    entry_second.pack()
    entry_second.insert(0, "Path to second image")
    entry_second.place(x=22, y=135)
    entry = Entry(window, width=14)
    entry.pack()
    entry.insert(0, "Path")
    entry.place(x=22, y=75)

    # Кнопка для получения изображения с поворотом по точкам (заданы в функции get_rotation_of_image)
    button_first = Button(window, text="Rotate Image",
                          command=lambda: get_rotation_of_image(entry.get()),
                          font=("Arial", 10), fg="#00FF00", bg="black")
    button_first.pack()
    button_first.place(x=22, y=50)

    # Кнопка для получения изображения с перспективным преобразованием (заданы в функции get_gomography)
    button_second = Button(window, text="Get Homography",
                           command=lambda: get_gomography(entry_first.get(), entry_second.get()),
                           font=("Arial", 10), fg="#00FF00", bg="black")
    button_second.pack()
    button_second.place(x=22, y=155)
    window.mainloop()
