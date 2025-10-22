import heapq
import sys

"""
    Сортирует N отсортированных списков из файла и сохраняет результат в <input_filename>_out.txt
    
    Args:
        input_filename (str): Путь к входному файлу
        
    Returns:
        result_list: отсортированный список
    """

def merge_sorted_lists(input_filename):
    
    with open(input_filename, 'r') as f:
        # Читаем количество списков
        N = int(f.readline().strip())
        
        # Читаем отсортированные списки
        lists = []
        for _ in range(N):
            line = f.readline().strip()
            if line:  # если строка не пустая
                numbers = list(map(int, line.split()))
                lists.append(numbers)
            else:
                lists.append([])  # добавляем пустой список
    
    # Создаем кучу с первыми элементами каждого списка
    heap = []
    for i, lst in enumerate(lists):
        if lst:  # если список не пустой
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Процесс слияния
    result = []
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        # Если в текущем списке есть следующий элемент, добавляем его в кучу
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
    
    # Формируем имя выходного файла
    if input_filename.endswith('.txt'):
        output_filename = input_filename.replace('.txt', '_out.txt')
    else:
        output_filename = input_filename + '_out.txt'
    
    # Записываем результат
    with open(output_filename, 'w') as f:
        f.write(' '.join(map(str, result)))
    
    return result

def test_case(test_name, actual, expected):
        
        print(f"Test : {test_name}")
        if actual == expected:
            print(f"  ✅ УСПЕХ: получен ожидаемый результат")
            print(f"     Результат:{actual}")
            return True
        else:
            print(f"  ❌ ОШИБКА: результат не совпадает с ожидаемым!")
            print(f"     Ожидалось: {expected}")
            print(f"     Получено:  {actual}")
            return False

if __name__ == "__main__":

    passed = 0
    failed = 0

    result1 = merge_sorted_lists("tests/test1.txt")
    if test_case("test1", result1, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        passed = passed + 1
    else:
        failed = failed + 1

    result2 = merge_sorted_lists("tests/test2.txt")
    if test_case("test2", result2, [10, 20, 30, 40, 50]):
        passed = passed + 1
    else:
        failed = failed + 1

    result3 = merge_sorted_lists("tests/test3.txt")
    if test_case("test3", result3, [5, 5, 5, 5, 5, 5, 5, 5, 5]):
        passed = passed + 1
    else:
        failed = failed + 1

    result4 = merge_sorted_lists("tests/test4.txt")
    if test_case("test4", result4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]):
        passed = passed + 1
    else:
        failed = failed + 1

    if(failed == 0):
        print(f"  ✅ Все {passed} тестов прошли!")
    else:
        print(f"  ❌ Тестирование не пройдено:")
        print(f"  {passed} - passed")
        print(f"  {failed} - failed")
        sys.exit(-1) 