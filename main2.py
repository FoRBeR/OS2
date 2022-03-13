from string import ascii_lowercase
import multiprocessing as mp
import hashlib
from datetime import datetime


def division(parts):
    a = ascii_lowercase
    if parts == 2:
        result = [a[0:13], a[13:]]
    elif parts == 3:
        result = [a[0:9], a[9:18], a[18:]]
    elif parts == 5:
        result = [a[0:5], a[5:10], a[10:15], a[15:20], a[20:]]
    elif parts == 7:
        result = [a[0:4], a[4:8], a[8:12], a[12:16], a[16:20], a[20:23], a[23:]]
    else:
        result = []
    return result


def enumeration(code, start_time, letters1, letters2=ascii_lowercase, letters3=ascii_lowercase,
                letters4=ascii_lowercase,
                letters5=ascii_lowercase):
    for a in letters1:
        for b in letters2:
            for c in letters3:
                for d in letters4:
                    for e in letters5:
                        word = a + b + c + d + e
                        if code == hashlib.sha256(word.encode()).hexdigest():
                            print(f'Совпадение найдено!\nИскомое слово: {word}\nВремя: {datetime.now() - start_time}')
    print(f'Выполнение функции завершено с временем {datetime.now() - start_time}')


if __name__ == '__main__':
    code = input('Введите хэш > ')
    while True:
        count = input('Количество потоков от 1 до 8 > ')
        if count != '1' and count != '2' and count != '3' and count != '4' and count != '5' and count != '6' and count != '7' and count != '8':
            print('Incorrect input')
        else:
            break

    start_time = datetime.now()
    if count == '1':
        p1 = mp.Process(target=enumeration, args=(code, start_time, ascii_lowercase,))
        p1.start()
        p1.join()
    elif count == '2':
        array = division(2)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[1],))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif count == '3':
        array = division(3)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[1],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array[2],))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
    elif count == '4':
        array = division(2)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[0],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[1],))
        p4 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[1],))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
    elif count == '5':
        array = division(5)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[1],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array[2],))
        p4 = mp.Process(target=enumeration, args=(code, start_time, array[3],))
        p5 = mp.Process(target=enumeration, args=(code, start_time, array[4],))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
    elif count == '6':
        array1 = division(2)
        array2 = division(3)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array1[0], array2[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array1[1], array2[1],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array1[0], array2[2],))
        p4 = mp.Process(target=enumeration, args=(code, start_time, array1[1], array2[0],))
        p5 = mp.Process(target=enumeration, args=(code, start_time, array1[0], array2[1],))
        p6 = mp.Process(target=enumeration, args=(code, start_time, array1[1], array2[2],))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
    elif count == '7':
        array = division(7)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[1],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array[2],))
        p4 = mp.Process(target=enumeration, args=(code, start_time, array[3],))
        p5 = mp.Process(target=enumeration, args=(code, start_time, array[4],))
        p6 = mp.Process(target=enumeration, args=(code, start_time, array[5],))
        p7 = mp.Process(target=enumeration, args=(code, start_time, array[6],))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
    elif count == '8':
        array = division(2)
        p1 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[0], array[0],))
        p2 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[0], array[1],))
        p3 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[1], array[0],))
        p4 = mp.Process(target=enumeration, args=(code, start_time, array[0], array[1], array[1],))
        p5 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[0], array[0],))
        p6 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[0], array[1],))
        p7 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[1], array[0],))
        p8 = mp.Process(target=enumeration, args=(code, start_time, array[1], array[1], array[1],))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()