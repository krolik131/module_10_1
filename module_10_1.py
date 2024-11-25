import threading
import time
def write_words(word_count, file_name):
    started_at = time.time()
    for i in range(1,word_count+1):
        with open(file_name, 'a',encoding='utf-8') as f:
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    endeded_at = time.time()
    print(f'Запись завершена за {endeded_at - started_at} секунд')
    print(f'Завершилась запись в файл {file_name}')



result = write_words(10, 'example1.txt')
result = write_words(30, 'example2.txt')
result = write_words(200, 'example3.txt')
result = write_words(100, 'example4.txt')

thread = threading.Thread(target=write_words, args=(10,'example5.txt'))
thread.start()
thread = threading.Thread(target=write_words, args=(30,'example6.txt'))
thread.start()
thread = threading.Thread(target=write_words , args=(200,'example7.txt'))
thread.start()
thread = threading.Thread(target=write_words , args=(100,'example8.txt'))
thread.start()