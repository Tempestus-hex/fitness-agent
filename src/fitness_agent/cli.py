"""Модуль командной строки для взаимодействия с пользователем."""

from rich.console import Console

from .operations import add_workout, list_workouts, mark_done

console = Console()


def start_cli() -> None:
    """Запускает основной цикл программы."""
    workouts = []
    console.print("[bold green]Добро пожаловать в Fitness Assistant![/bold green]")
    console.print("Введите 'help' для списка команд.")

    while True:
        try:
            command = console.input("[bold yellow]> [/bold yellow]").strip().lower()

            if command == "add":
                title = console.input("Название тренировки: ").strip()
                if not title:
                    console.print("[red]Ошибка: название не может быть пустым.[/red]")
                    continue
                duration_str = console.input("Длительность (мин): ")
                duration = int(duration_str)
                if duration <= 0:
                    console.print(
                        "[red]Ошибка: длительность должна быть больше нуля.[/red]"
                    )
                    continue
                calories_str = console.input("Сожжено калорий: ")
                calories = int(calories_str)
                if calories <= 0:
                    console.print("[red]Ошибка: калории должны быть больше нуля.[/red]")
                    continue
                add_workout(workouts, title, duration, calories)
                console.print("[green]Тренировка добавлена![/green]")
            elif command == "list":
                console.print(list_workouts(workouts))

            elif command == "done":
                if not workouts:
                    console.print("[red]Список пуст. Нечего отмечать.[/red]")
                    continue

                console.print(list_workouts(workouts))
                index = int(console.input("Введите номер выполненной тренировки: "))

                if index < 0 or index >= len(workouts):
                    console.print("[red]Ошибка: тренировки с таким номером нет![/red]")
                    continue

                mark_done(workouts, index)
                console.print("[green]Статус обновлен![/green]")

            elif command == "help":
                help_text = (
                    "[bold]Доступные команды:[/bold]\n"
                    "  add  - добавить тренировку (название, время, калории)\n"
                    "  list - показать список тренировок\n"
                    "  done - отметить тренировку выполненной\n"
                    "  help - справка\n"
                    "  exit - выход"
                )
                console.print(help_text)

            elif command == "exit":
                console.print("[bold blue]До встречи![/bold blue]")
                break

            else:
                console.print("[red]Неизвестная команда. Введите 'help'.[/red]")

        except ValueError:
            console.print(
                "[bold red]Ошибка ввода: там, где нужно число, "
                "введен текст![/bold red]"
            )
