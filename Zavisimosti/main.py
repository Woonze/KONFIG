import csv
import sys
import requests
import re
from graphviz import Digraph

def read_config(file_path):
    """Чтение конфигурации из CSV."""
    config = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                key, value = row
                config[key.strip()] = value.strip()
    return config

def get_dependencies(package, max_depth):
    """Получение зависимостей пакета с сайта PyPI рекурсивно."""
    dependencies = {}

    def resolve(package, depth):
        if depth > max_depth or package in dependencies:
            return
        try:
            response = requests.get(f'https://pypi.org/pypi/{package}/json')
            response.raise_for_status()
            data = response.json()

            dep_list = data.get('info', {}).get('requires_dist', []) or []
            dependencies[package] = []

            for dep in dep_list:
                dep_name_match = re.match(r'^[^<>=,;!\s]+', dep.strip())
                if dep_name_match:
                    dep_name = dep_name_match.group(0)
                    dependencies[package].append(dep_name)
                    resolve(dep_name, depth + 1)

        except requests.RequestException as e:
            print(f"ВНИМАНИЕ: Не удалось получить данные для пакета {package}: {e}")

    resolve(package, 0)
    return dependencies

def create_graph(dependencies, output_path):
    """Создание и сохранение графа зависимостей."""
    graph = Digraph(format='png')

    # Множество для отслеживания всех узлов и рёбер, чтобы не добавлять их несколько раз
    visited_nodes = set()
    visited_edges = set()

    def add_edges(pkg, deps):
        """Добавление рёбер для текущего пакета и его зависимостей в граф."""
        if pkg not in visited_nodes:
            visited_nodes.add(pkg)  # Добавляем пакет в посещённые узлы
            for dep in deps:
                edge = (pkg, dep)
                if edge not in visited_edges:  # Проверяем, что ребро ещё не добавлено
                    graph.edge(pkg, dep)  # Добавляем ребро
                    visited_edges.add(edge)  # Отмечаем ребро как добавленное
                if dep in dependencies:  # Рекурсивно обрабатываем зависимости
                    add_edges(dep, dependencies[dep])

    # Запуск добавления рёбер для всех пакетов
    for pkg, deps in dependencies.items():
        add_edges(pkg, deps)

    # Сохраняем граф
    graph.render(output_path, cleanup=True)


def visualize_dependencies(config_path):
    """Основной процесс визуализации зависимостей."""
    config = read_config(config_path)
    package_name = config.get('Package Name')
    output_path = config.get('Output Path')
    max_depth = int(config.get('Max Depth', 1))

    if not all([package_name, output_path]):
        raise ValueError("Конфигурационный файл содержит недостаточно данных.")

    dependencies = get_dependencies(package_name, max_depth)
    create_graph(dependencies, output_path)
    print("Визуализация графа зависимостей успешно выполнена.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Использование: python main.py <путь к конфигурации>")
        sys.exit(1)

    config_path = sys.argv[1]
    visualize_dependencies(config_path)
