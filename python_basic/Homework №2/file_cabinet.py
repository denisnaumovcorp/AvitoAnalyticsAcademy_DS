#!/usr/bin/env python3
import csv
from typing import Dict, List, Set
from collections import defaultdict
import os


def read_employee_data(filename: str) -> List[Dict[str, str]]:
    employees = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {filename} не найден")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")

    return employees


def get_department_hierarchy(
    employees: List[Dict[str, str]],
) -> Dict[str, Set[str]]:
    hierarchy = defaultdict(set)

    for employee in employees:
        department = employee.get("Департамент", "").strip()
        team = employee.get("Отдел", "").strip()

        if department and team:
            hierarchy[department].add(team)

    return dict(hierarchy)


def print_department_hierarchy(hierarchy: Dict[str, Set[str]]) -> None:
    print("\nИерархия команд:")
    print("=" * 50)

    for department in sorted(hierarchy.keys()):
        print(f"\n{department}:")
        teams = sorted(hierarchy[department])
        for team in teams:
            print(f"  └── {team}")

    print()


def calculate_department_statistics(
    employees: List[Dict[str, str]],
) -> Dict[str, Dict]:
    department_stats = defaultdict(lambda: {"count": 0, "salaries": []})

    for employee in employees:
        department = employee.get("Департамент", "").strip()
        salary_str = employee.get("Оклад", "").strip()

        if department and salary_str:
            try:
                salary = int(salary_str)
                department_stats[department]["count"] += 1
                department_stats[department]["salaries"].append(salary)
            except ValueError:
                continue

    result = {}
    for department, data in department_stats.items():
        if data["salaries"]:
            salaries = data["salaries"]
            result[department] = {
                "count": data["count"],
                "min_salary": min(salaries),
                "max_salary": max(salaries),
                "avg_salary": round(sum(salaries) / len(salaries), 2),
            }

    return result


def print_department_statistics(stats: Dict[str, Dict]) -> None:
    print("\nСводный отчет по департаментам:")
    print("=" * 80)
    print(
        f"{'Департамент':<20} {'Численность':<12} "
        f"{'Мин-Макс':<15} {'Средняя зарплата':<18}"
    )
    print("-" * 80)

    for department in sorted(stats.keys()):
        data = stats[department]
        salary_range = f"{data['min_salary']}-{data['max_salary']}"
        print(
            f"{department:<20} {data['count']:<12} "
            f"{salary_range:<15} {data['avg_salary']:<18}"
        )

    print()


def save_statistics_to_csv(stats: Dict[str, Dict], filename: str) -> None:
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [
                    "Департамент",
                    "Численность",
                    "Минимальная зарплата",
                    "Максимальная зарплата",
                    "Средняя зарплата",
                ]
            )
            for department in sorted(stats.keys()):
                data = stats[department]
                writer.writerow(
                    [
                        department,
                        data["count"],
                        data["min_salary"],
                        data["max_salary"],
                        data["avg_salary"],
                    ]
                )

        print(f"Сводный отчет сохранен в файл: {filename}")

    except Exception as e:
        raise IOError(f"Ошибка при сохранении файла: {e}")


def display_menu() -> None:
    print("\n" + "=" * 50)
    print("МЕНЮ АНАЛИЗА ДАННЫХ О СОТРУДНИКАХ")
    print("=" * 50)
    print("1. Вывести иерархию команд")
    print("2. Вывести сводный отчет по департаментам")
    print("3. Сохранить сводный отчет в CSV файл")
    print("0. Выход")
    print("=" * 50)


def get_user_choice() -> int:
    try:
        choice = int(input("Выберите пункт меню (0-3): "))
        if choice not in [0, 1, 2, 3]:
            raise ValueError("Выбор должен быть от 0 до 3")
        return choice
    except ValueError as e:
        raise ValueError(f"Некорректный ввод: {e}")


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "Corp_Summary.csv")

    try:
        employees = read_employee_data(filename)
        print(f"Загружено {len(employees)} записей о сотрудниках")

        department_stats = calculate_department_statistics(employees)

        while True:
            display_menu()

            try:
                choice = get_user_choice()

                if choice == 0:
                    print("До свидания!")
                    break

                elif choice == 1:
                    hierarchy = get_department_hierarchy(employees)
                    print_department_hierarchy(hierarchy)

                elif choice == 2:
                    print_department_statistics(department_stats)

                elif choice == 3:
                    output_filename = input(
                        "Введите имя файла для сохранения "
                        "(по умолчанию: department_report.csv): "
                    ).strip()
                    if not output_filename:
                        output_filename = "department_report.csv"

                    if not output_filename.endswith(".csv"):
                        output_filename += ".csv"

                    save_statistics_to_csv(department_stats, output_filename)

            except ValueError as e:
                print(f"Ошибка: {e}")
                print("Попробуйте еще раз.\n")
                continue

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        print(
            "Убедитесь, что файл Corp_Summary.csv находится "
            "в той же папке, что и программа."
        )
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
