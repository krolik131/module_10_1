import time
import threading

def write_words(word_count, file_name):

    for i in range(1,word_count+1):
        with open(file_name, 'a',encoding='utf-8') as f:
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)


    print(f'Завершилась запись в файл {file_name}')


started_at = time.time()
result = write_words(10, 'example1.txt')
result = write_words(30, 'example2.txt')
result = write_words(200, 'example3.txt')
result = write_words(100, 'example4.txt')
endeded_at = time.time()
print(f'Запись при последовательных вызовов завершена за {endeded_at - started_at} секунд')

started_potok_at = time.time()

thread1 = threading.Thread(target=write_words, args=(10,'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30,'example6.txt'))
thread3 = threading.Thread(target=write_words , args=(200,'example7.txt'))
thread4 = threading.Thread(target=write_words , args=(100,'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

endeded_potok_at = time.time()

print(f'Запись при многопоточности завершена за {endeded_potok_at - started_potok_at} секунд')
print(f'При многопоточности запись производится в {(endeded_at - started_at) / (endeded_potok_at - started_potok_at):.2f} раза быстрее')
