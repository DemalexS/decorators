from datetime import datetime, date, time
import hashlib

# def decor(old_func, path):
#     def logger():
#         output_file = open(path, 'a', encoding='utf-8')
#         md5 = old_func(path)
#         output_file.write(str(datetime.now()) + '_' + str(old_func.__name__) + '_' + str(md5) + '_' + str(path) + '\n')
#         output_file.close()
#         return md5
#     return logger


def parametrized_decor(parameter):
    def decor(old_func):
        def logger():
             output_file = open(parameter, 'a', encoding='utf-8')
             md5 = old_func(parameter)
             output_file.write(str(datetime.now()) + '_' + str(old_func.__name__) + '_' + str(md5) + '_' + str(parameter) + '\n')
             output_file.close()
             return md5
        return logger
    return decor


@parametrized_decor('log.txt')
def gen_md5(file_name):
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()

foo = gen_md5()

print(foo)

