from time import time
import ctypes
import re
import os
import subprocess
import multiprocessing

RETURN_OK               =   0
RETURN_ERROR            =   1
RETURN_INTERRUPT        =   2
RETURN_ITERNAL_ERROR    =   3
RETURN_TIMEOUT          =   4


def f(test, return_code):
    proc = subprocess.Popen(["pytest", f"{test}"], stdout = subprocess.DEVNULL)
    proc.wait()
    return_code.value = proc.returncode
    return


def find_source(files, text):
    output = []
    for i in range(len(files)):
        if re.search(text, files[i]):
            output.append(files[i])

    return output


def print_from_col(file, text, data, col, size):
    file.write(text)
    for i in range(1, size + 1):
        file.write(f"{data[i][col]}\n")
    file.write("\n")
    return


def update_data(path, data):
    data_file = open(path, "w")
    data_file.write('TEST_NUMBER:\n')
    data_file.write(f"{data[0]}\n\n")

    n = data[0]
    print_from_col(data_file, 'MAX_TIME:\n',         data, 0, n)
    print_from_col(data_file, 'POINTS_PER_GROUP:\n', data, 1, n)
    print_from_col(data_file, 'TEST_RESULT:\n',      data, 2, n)

    data_file.write('SCORE:\n')
    data_file.write(f"{data[n + 1]}\n")

    data_file.close()


def run_unit_test(data_source, test_source):
    data_file = open(data_source, "r+")
    data = []
    for line in data_file:
        if (line == 'TEST_NUMBER:\n' or
            line == 'MAX_TIME:\n' or
            line == 'POINTS_PER_GROUP:\n' or
            line == 'TEST_RESULT:\n' or
            line == 'SCORE:\n' or
                line == '\n'):
            pass
        else:
            data.append(line[:-1])

    n = int(data[0])

    temp_data = [n]
    for i in range(1, n + 1):
        temp_data.append([float(data[i]), int(data[i + n]), data[i + (2 * n)]])
    data = temp_data

    counter = 1
    for test in test_source:
        ret_value = multiprocessing.Value("d", 0, lock = False)
        result = multiprocessing.Process(target = f, args = (test, ret_value))
        result.start()
        start_time = time()

        while time() - start_time < data[counter][0] and result.is_alive(): continue

        ret_value = ctypes.c_float(ret_value.value).value
        
        if result.exitcode == None:
            ret_value = RETURN_TIMEOUT
            data[counter][2] = "Time Exceeded"
        elif ret_value == RETURN_ERROR:
            data[counter][2] = "Wrong Output"
        elif ret_value == RETURN_INTERRUPT:
            data[counter][2] = "Program stopped by user"
        elif ret_value == RETURN_ITERNAL_ERROR:
            data[counter][2] = "Program died by iternal error"
        elif ret_value == RETURN_OK:
            data[counter][2] = "OK"

        if ret_value != RETURN_OK:
            for i in range(counter + 1, n + 1):
                data[i][2] = "Complete previous tests"
            break


        result.terminate()
        result.join()

        counter += 1


    score = 0
    for i in range(1, len(data)):
        if data[i][2] == "OK":
            score += data[i][1]
        else:
            break

    data.append(score)
    data_file.close()
    update_data(data_source, data)


def run_all_tests():
    for path, directories, files in os.walk(".\\WDI"):

        if len(files) and files[0] == "DATA.txt":
            prog = find_source(files, "^prog.*")
            data = find_source(files, "DATA.txt")
            test = find_source(files, "^test.*")

            if prog != []:
                prog_source = "{}{}{}".format(path, os.sep, prog[0])
                data_source = "{}{}{}".format(path, os.sep, data[0])
                test_source = ["{}{}{}".format(path, os.sep, i) for i in test]

                if True: #os.path.getmtime(prog_source) > os.path.getmtime(data_source):
                    output = prog_source.rsplit("\\")[2:4]
                    print(f"Checking {output[1]} from {output[0]}")
                    run_unit_test(data_source, test_source)


def menu():
    action = 1

    match action:
        case 1:
            run_all_tests()
        case _:
            return False

    return False


if __name__ == '__main__':
    while menu(): pass
