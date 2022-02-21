from string import ascii_lowercase
import threading
import hashlib
from datetime import datetime


class myThread(threading.Thread):
    def __init__(self, name, counter, max_count):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.max_count = max_count

    def run(self):
        thread_separation(self.name, self.counter, self.max_count)


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
    elif parts == 11:
        result = [a[0:2], a[2:4], a[4:6], a[6:8], a[8:10], a[10:12], a[12:14], a[14:17], a[17:20], a[20:23], a[23:]]
    elif parts == 13:
        result = [a[0:2], a[2:4], a[4:6], a[6:8], a[8:10], a[10:12], a[12:14], a[14:16], a[16:18], a[18:20], a[20:22],
                  a[22:24], a[24:]]
    elif parts == 17:
        result = [a[0:2], a[2:4], a[4:6], a[6:8], a[8:10], a[10:12], a[12:14], a[14:16], a[16:18]] + list(a[18:])
    elif parts == 19:
        result = [a[0:2], a[2:4], a[4:6], a[6:8], a[8:10], a[10:12], a[12:14]] + list(a[14:])
    elif parts == 23:
        result = [a[0:2], a[2:4], a[4:6]] + list(a[6:])
    else:
        result = []
    return result


def enumeration(letters1, letters2=ascii_lowercase, letters3=ascii_lowercase, letters4=ascii_lowercase,
                letters5=ascii_lowercase):
    global code
    global start_time
    for a in letters1:
        for b in letters2:
            for c in letters3:
                for d in letters4:
                    for e in letters5:
                        word = a + b + c + d + e
                        if code == hashlib.sha256(word.encode()).hexdigest():
                            print(f'Совпадение найдено!\nИскомое слово: {word}\nВремя: {datetime.now() - start_time}')


def thread_separation(threadName, counter, max_count):
    if max_count == 1:
        enumeration(ascii_lowercase)
    elif max_count == 2:
        l1 = division(max_count)
        if counter == 1:
            enumeration(l1[0])
        else:
            enumeration(l1[1])
    elif max_count == 3:
        l1 = division(max_count)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        else:
            enumeration(l1[2])
    elif max_count == 4:
        l = division(2)
        if counter == 1:
            enumeration(l[0], l[0])
        elif counter == 2:
            enumeration(l[1], l[0])
        elif counter == 3:
            enumeration(l[1], l[1])
        else:
            enumeration(l[0], l[1])
    elif max_count == 5:
        l1 = division(max_count)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        else:
            enumeration(l1[4])
    elif max_count == 6:
        l1 = division(2)
        l2 = division(3)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[1], l2[0])
        elif counter == 5:
            enumeration(l1[1], l2[1])
        else:
            enumeration(l1[1], l2[2])
    elif max_count == 7:
        l1 = division(7)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        else:
            enumeration(l1[6])
    elif max_count == 8:
        l = division(2)
        if counter == 1:
            enumeration(l[0], l[0], l[0])
        elif counter == 2:
            enumeration(l[0], l[0], l[1])
        elif counter == 3:
            enumeration(l[0], l[1], l[0])
        elif counter == 4:
            enumeration(l[0], l[1], l[1])
        elif counter == 5:
            enumeration(l[1], l[0], l[0])
        elif counter == 6:
            enumeration(l[1], l[0], l[1])
        elif counter == 7:
            enumeration(l[1], l[1], l[0])
        else:
            enumeration(l[1], l[1], l[1])
    elif max_count == 9:
        l = division(3)
        if counter == 1:
            enumeration(l[0], l[0])
        elif counter == 2:
            enumeration(l[0], l[1])
        elif counter == 3:
            enumeration(l[0], l[2])
        elif counter == 4:
            enumeration(l[1], l[0])
        elif counter == 5:
            enumeration(l[1], l[1])
        elif counter == 6:
            enumeration(l[1], l[2])
        elif counter == 7:
            enumeration(l[2], l[0])
        elif counter == 8:
            enumeration(l[2], l[1])
        else:
            enumeration(l[2], l[2])
    elif max_count == 10:
        l1 = division(2)
        l2 = division(5)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[0], l2[3])
        elif counter == 5:
            enumeration(l1[0], l2[4])
        elif counter == 6:
            enumeration(l1[1], l2[0])
        elif counter == 7:
            enumeration(l1[1], l2[1])
        elif counter == 8:
            enumeration(l1[1], l2[2])
        elif counter == 9:
            enumeration(l1[1], l2[3])
        else:
            enumeration(l1[1], l2[4])
    elif max_count == 11:
        l1 = division(11)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        else:
            enumeration(l1[10])
    elif max_count == 12:
        l12 = division(2)
        l3 = division(3)
        if counter == 1:
            enumeration(l12[0], l12[0], l3[0])
        elif counter == 2:
            enumeration(l12[0], l12[0], l3[1])
        elif counter == 3:
            enumeration(l12[0], l12[0], l3[2])
        elif counter == 4:
            enumeration(l12[0], l12[1], l3[0])
        elif counter == 5:
            enumeration(l12[0], l12[1], l3[1])
        elif counter == 6:
            enumeration(l12[0], l12[1], l3[2])
        elif counter == 7:
            enumeration(l12[1], l12[0], l3[0])
        elif counter == 8:
            enumeration(l12[1], l12[0], l3[1])
        elif counter == 9:
            enumeration(l12[1], l12[0], l3[2])
        elif counter == 10:
            enumeration(l12[1], l12[1], l3[0])
        elif counter == 11:
            enumeration(l12[1], l12[1], l3[1])
        else:
            enumeration(l12[1], l12[1], l3[2])
    elif max_count == 13:
        l1 = division(13)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        elif counter == 11:
            enumeration(l1[10])
        elif counter == 12:
            enumeration(l1[11])
        else:
            enumeration(l1[12])
    elif max_count == 14:
        l1 = division(2)
        l2 = division(7)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[0], l2[3])
        elif counter == 5:
            enumeration(l1[0], l2[4])
        elif counter == 6:
            enumeration(l1[0], l2[5])
        elif counter == 7:
            enumeration(l1[0], l2[6])
        elif counter == 8:
            enumeration(l1[1], l2[0])
        elif counter == 9:
            enumeration(l1[1], l2[1])
        elif counter == 10:
            enumeration(l1[1], l2[2])
        elif counter == 11:
            enumeration(l1[1], l2[3])
        elif counter == 12:
            enumeration(l1[1], l2[4])
        elif counter == 13:
            enumeration(l1[1], l2[5])
        else:
            enumeration(l1[1], l2[6])
    elif max_count == 15:
        l1 = division(3)
        l2 = division(5)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[0], l2[3])
        elif counter == 5:
            enumeration(l1[0], l2[4])
        elif counter == 6:
            enumeration(l1[1], l2[0])
        elif counter == 7:
            enumeration(l1[1], l2[1])
        elif counter == 8:
            enumeration(l1[1], l2[2])
        elif counter == 9:
            enumeration(l1[1], l2[3])
        elif counter == 10:
            enumeration(l1[1], l2[4])
        elif counter == 11:
            enumeration(l1[2], l2[0])
        elif counter == 12:
            enumeration(l1[2], l2[1])
        elif counter == 13:
            enumeration(l1[2], l2[2])
        elif counter == 14:
            enumeration(l1[2], l2[3])
        else:
            enumeration(l1[2], l2[4])
    elif max_count == 16:
        l = division(2)
        if counter == 1:
            enumeration(l[0], l[0], l[0], l[0])
        elif counter == 2:
            enumeration(l[0], l[0], l[0], l[1])
        elif counter == 3:
            enumeration(l[0], l[0], l[1], l[0])
        elif counter == 4:
            enumeration(l[0], l[0], l[1], l[1])
        elif counter == 5:
            enumeration(l[0], l[1], l[0], l[0])
        elif counter == 6:
            enumeration(l[0], l[1], l[0], l[1])
        elif counter == 7:
            enumeration(l[0], l[1], l[1], l[0])
        elif counter == 8:
            enumeration(l[0], l[1], l[1], l[1])
        elif counter == 9:
            enumeration(l[1], l[0], l[0], l[0])
        elif counter == 10:
            enumeration(l[1], l[0], l[0], l[1])
        elif counter == 11:
            enumeration(l[1], l[0], l[1], l[0])
        elif counter == 12:
            enumeration(l[1], l[0], l[1], l[1])
        elif counter == 13:
            enumeration(l[1], l[1], l[0], l[0])
        elif counter == 14:
            enumeration(l[1], l[1], l[0], l[1])
        elif counter == 15:
            enumeration(l[1], l[1], l[1], l[0])
        else:
            enumeration(l[1], l[1], l[1], l[1])
    elif max_count == 17:
        l1 = division(17)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        elif counter == 11:
            enumeration(l1[10])
        elif counter == 12:
            enumeration(l1[11])
        elif counter == 13:
            enumeration(l1[12])
        elif counter == 14:
            enumeration(l1[13])
        elif counter == 15:
            enumeration(l1[14])
        elif counter == 16:
            enumeration(l1[15])
        else:
            enumeration(l1[16])
    elif max_count == 18:
        l12 = division(3)
        l3 = division(2)
        if counter == 1:
            enumeration(l12[0], l12[0], l3[0])
        elif counter == 2:
            enumeration(l12[0], l12[0], l3[1])
        elif counter == 3:
            enumeration(l12[0], l12[1], l3[0])
        elif counter == 4:
            enumeration(l12[0], l12[1], l3[1])
        elif counter == 5:
            enumeration(l12[0], l12[2], l3[0])
        elif counter == 6:
            enumeration(l12[0], l12[2], l3[1])
        elif counter == 7:
            enumeration(l12[1], l12[0], l3[0])
        elif counter == 8:
            enumeration(l12[1], l12[0], l3[1])
        elif counter == 9:
            enumeration(l12[1], l12[1], l3[0])
        elif counter == 10:
            enumeration(l12[1], l12[1], l3[1])
        elif counter == 11:
            enumeration(l12[1], l12[2], l3[0])
        elif counter == 12:
            enumeration(l12[1], l12[2], l3[1])
        elif counter == 13:
            enumeration(l12[2], l12[0], l3[0])
        elif counter == 14:
            enumeration(l12[2], l12[0], l3[1])
        elif counter == 15:
            enumeration(l12[2], l12[1], l3[0])
        elif counter == 16:
            enumeration(l12[2], l12[1], l3[1])
        elif counter == 17:
            enumeration(l12[2], l12[2], l3[0])
        else:
            enumeration(l12[2], l12[2], l3[1])
    elif max_count == 19:
        l1 = division(19)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        elif counter == 11:
            enumeration(l1[10])
        elif counter == 12:
            enumeration(l1[11])
        elif counter == 13:
            enumeration(l1[12])
        elif counter == 14:
            enumeration(l1[13])
        elif counter == 15:
            enumeration(l1[14])
        elif counter == 16:
            enumeration(l1[15])
        elif counter == 17:
            enumeration(l1[16])
        elif counter == 18:
            enumeration(l1[17])
        else:
            enumeration(l1[18])
    elif max_count == 20:
        l12 = division(2)
        l3 = division(5)
        if counter == 1:
            enumeration(l12[0], l12[0], l3[0])
        elif counter == 2:
            enumeration(l12[0], l12[0], l3[1])
        elif counter == 3:
            enumeration(l12[0], l12[0], l3[2])
        elif counter == 4:
            enumeration(l12[0], l12[0], l3[3])
        elif counter == 5:
            enumeration(l12[0], l12[0], l3[4])
        elif counter == 6:
            enumeration(l12[0], l12[1], l3[0])
        elif counter == 7:
            enumeration(l12[0], l12[1], l3[1])
        elif counter == 8:
            enumeration(l12[0], l12[1], l3[2])
        elif counter == 9:
            enumeration(l12[0], l12[1], l3[3])
        elif counter == 10:
            enumeration(l12[0], l12[1], l3[4])
        elif counter == 11:
            enumeration(l12[1], l12[0], l3[0])
        elif counter == 12:
            enumeration(l12[1], l12[0], l3[1])
        elif counter == 13:
            enumeration(l12[1], l12[0], l3[2])
        elif counter == 14:
            enumeration(l12[1], l12[0], l3[3])
        elif counter == 15:
            enumeration(l12[1], l12[0], l3[4])
        elif counter == 16:
            enumeration(l12[1], l12[1], l3[0])
        elif counter == 17:
            enumeration(l12[1], l12[1], l3[1])
        elif counter == 18:
            enumeration(l12[1], l12[1], l3[2])
        elif counter == 19:
            enumeration(l12[1], l12[1], l3[3])
        else:
            enumeration(l12[1], l12[1], l3[4])
    elif max_count == 21:
        l1 = division(3)
        l2 = division(7)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[0], l2[3])
        elif counter == 5:
            enumeration(l1[0], l2[4])
        elif counter == 6:
            enumeration(l1[0], l2[5])
        elif counter == 7:
            enumeration(l1[0], l2[6])
        elif counter == 8:
            enumeration(l1[1], l2[0])
        elif counter == 9:
            enumeration(l1[1], l2[1])
        elif counter == 10:
            enumeration(l1[1], l2[2])
        elif counter == 11:
            enumeration(l1[1], l2[3])
        elif counter == 12:
            enumeration(l1[1], l2[4])
        elif counter == 13:
            enumeration(l1[1], l2[5])
        elif counter == 14:
            enumeration(l1[1], l2[6])
        elif counter == 15:
            enumeration(l1[2], l2[0])
        elif counter == 16:
            enumeration(l1[2], l2[1])
        elif counter == 17:
            enumeration(l1[2], l2[2])
        elif counter == 18:
            enumeration(l1[2], l2[3])
        elif counter == 19:
            enumeration(l1[2], l2[4])
        elif counter == 20:
            enumeration(l1[2], l2[5])
        else:
            enumeration(l1[2], l2[6])
    elif max_count == 22:
        l1 = division(2)
        l2 = division(11)
        if counter == 1:
            enumeration(l1[0], l2[0])
        elif counter == 2:
            enumeration(l1[0], l2[1])
        elif counter == 3:
            enumeration(l1[0], l2[2])
        elif counter == 4:
            enumeration(l1[0], l2[3])
        elif counter == 5:
            enumeration(l1[0], l2[4])
        elif counter == 6:
            enumeration(l1[0], l2[5])
        elif counter == 7:
            enumeration(l1[0], l2[6])
        elif counter == 8:
            enumeration(l1[0], l2[7])
        elif counter == 9:
            enumeration(l1[0], l2[8])
        elif counter == 10:
            enumeration(l1[0], l2[9])
        elif counter == 11:
            enumeration(l1[0], l2[10])
        elif counter == 12:
            enumeration(l1[1], l2[0])
        elif counter == 13:
            enumeration(l1[1], l2[1])
        elif counter == 14:
            enumeration(l1[1], l2[2])
        elif counter == 15:
            enumeration(l1[1], l2[3])
        elif counter == 16:
            enumeration(l1[1], l2[4])
        elif counter == 17:
            enumeration(l1[1], l2[5])
        elif counter == 18:
            enumeration(l1[1], l2[6])
        elif counter == 19:
            enumeration(l1[1], l2[7])
        elif counter == 20:
            enumeration(l1[1], l2[8])
        elif counter == 21:
            enumeration(l1[1], l2[9])
        else:
            enumeration(l1[1], l2[10])
    elif max_count == 23:
        l1 = division(23)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        elif counter == 11:
            enumeration(l1[10])
        elif counter == 12:
            enumeration(l1[11])
        elif counter == 13:
            enumeration(l1[12])
        elif counter == 14:
            enumeration(l1[13])
        elif counter == 15:
            enumeration(l1[14])
        elif counter == 16:
            enumeration(l1[15])
        elif counter == 17:
            enumeration(l1[16])
        elif counter == 18:
            enumeration(l1[17])
        elif counter == 19:
            enumeration(l1[18])
        elif counter == 20:
            enumeration(l1[19])
        elif counter == 21:
            enumeration(l1[20])
        elif counter == 22:
            enumeration(l1[21])
        else:
            enumeration(l1[22])
    elif max_count == 24:
        l123 = division(2)
        l4 = division(3)
        if counter == 1:
            enumeration(l123[0], l123[0], l123[0], l4[0])
        elif counter == 2:
            enumeration(l123[0], l123[0], l123[0], l4[1])
        elif counter == 3:
            enumeration(l123[0], l123[0], l123[0], l4[2])
        elif counter == 4:
            enumeration(l123[0], l123[0], l123[1], l4[0])
        elif counter == 5:
            enumeration(l123[0], l123[0], l123[1], l4[1])
        elif counter == 6:
            enumeration(l123[0], l123[0], l123[1], l4[2])
        elif counter == 7:
            enumeration(l123[0], l123[1], l123[0], l4[0])
        elif counter == 8:
            enumeration(l123[0], l123[1], l123[0], l4[1])
        elif counter == 9:
            enumeration(l123[0], l123[1], l123[0], l4[2])
        elif counter == 10:
            enumeration(l123[0], l123[1], l123[1], l4[0])
        elif counter == 11:
            enumeration(l123[0], l123[1], l123[1], l4[1])
        elif counter == 12:
            enumeration(l123[0], l123[1], l123[1], l4[2])
        elif counter == 13:
            enumeration(l123[1], l123[0], l123[0], l4[0])
        elif counter == 14:
            enumeration(l123[1], l123[0], l123[0], l4[1])
        elif counter == 15:
            enumeration(l123[1], l123[0], l123[0], l4[2])
        elif counter == 16:
            enumeration(l123[1], l123[0], l123[1], l4[0])
        elif counter == 17:
            enumeration(l123[1], l123[0], l123[1], l4[1])
        elif counter == 18:
            enumeration(l123[1], l123[0], l123[1], l4[2])
        elif counter == 19:
            enumeration(l123[1], l123[1], l123[0], l4[0])
        elif counter == 20:
            enumeration(l123[1], l123[1], l123[0], l4[1])
        elif counter == 21:
            enumeration(l123[1], l123[1], l123[0], l4[2])
        elif counter == 22:
            enumeration(l123[1], l123[1], l123[1], l4[0])
        elif counter == 23:
            enumeration(l123[1], l123[1], l123[1], l4[1])
        else:
            enumeration(l123[1], l123[1], l123[1], l4[2])
    elif max_count == 25:
        l = division(5)
        if counter == 1:
            enumeration(l[0], l[0])
        elif counter == 2:
            enumeration(l[0], l[1])
        elif counter == 3:
            enumeration(l[0], l[2])
        elif counter == 4:
            enumeration(l[0], l[3])
        elif counter == 5:
            enumeration(l[0], l[4])
        elif counter == 6:
            enumeration(l[1], l[0])
        elif counter == 7:
            enumeration(l[1], l[1])
        elif counter == 8:
            enumeration(l[1], l[2])
        elif counter == 9:
            enumeration(l[1], l[3])
        elif counter == 10:
            enumeration(l[1], l[4])
        elif counter == 11:
            enumeration(l[2], l[0])
        elif counter == 12:
            enumeration(l[2], l[1])
        elif counter == 13:
            enumeration(l[2], l[2])
        elif counter == 14:
            enumeration(l[2], l[3])
        elif counter == 15:
            enumeration(l[2], l[4])
        elif counter == 16:
            enumeration(l[3], l[0])
        elif counter == 17:
            enumeration(l[3], l[1])
        elif counter == 18:
            enumeration(l[3], l[2])
        elif counter == 19:
            enumeration(l[3], l[3])
        elif counter == 20:
            enumeration(l[3], l[4])
        elif counter == 21:
            enumeration(l[4], l[0])
        elif counter == 22:
            enumeration(l[4], l[1])
        elif counter == 23:
            enumeration(l[4], l[2])
        elif counter == 24:
            enumeration(l[4], l[3])
        else:
            enumeration(l[4], l[4])
    elif max_count == 26:
        l1 = list(ascii_lowercase)
        if counter == 1:
            enumeration(l1[0])
        elif counter == 2:
            enumeration(l1[1])
        elif counter == 3:
            enumeration(l1[2])
        elif counter == 4:
            enumeration(l1[3])
        elif counter == 5:
            enumeration(l1[4])
        elif counter == 6:
            enumeration(l1[5])
        elif counter == 7:
            enumeration(l1[6])
        elif counter == 8:
            enumeration(l1[7])
        elif counter == 9:
            enumeration(l1[8])
        elif counter == 10:
            enumeration(l1[9])
        elif counter == 11:
            enumeration(l1[10])
        elif counter == 12:
            enumeration(l1[11])
        elif counter == 13:
            enumeration(l1[12])
        elif counter == 14:
            enumeration(l1[13])
        elif counter == 15:
            enumeration(l1[14])
        elif counter == 16:
            enumeration(l1[15])
        elif counter == 17:
            enumeration(l1[16])
        elif counter == 18:
            enumeration(l1[17])
        elif counter == 19:
            enumeration(l1[18])
        elif counter == 20:
            enumeration(l1[19])
        elif counter == 21:
            enumeration(l1[20])
        elif counter == 22:
            enumeration(l1[21])
        elif counter == 23:
            enumeration(l1[22])
        elif counter == 24:
            enumeration(l1[23])
        elif counter == 25:
            enumeration(l1[24])
        else:
            enumeration(l1[25])


code = input("Введите хэш, который надо расшифровать > ")
count = int(input("Количество потоков : "))
print("Начало вычислений...")
start_time = datetime.now()
threads = []
for i in range(count):
    threads.append(myThread("Thread", i + 1, count))
for i in range(count):
    threads[i].start()
for i in range(count):
    threads[i].join()
print(f"Exiting the Program\nTime: {datetime.now() - start_time}\tThreads: {count}")
