def add_workout(workouts: list, title: str, duration: int, calories: int) -> None:
    """Добавляет тренировку в список."""
    workouts.append(
        {
            "title": title,
            "duration": duration,
            "calories": calories,
            "done": False,
        }
    )


def list_workouts(workouts: list) -> str:
    """Возвращает отформатированный список тренировок."""
    if not workouts:
        return "Список тренировок пуст."

    result = []
    for i, workout in enumerate(workouts):
        status = "(x)" if workout["done"] else "( )"
        result.append(
            f"{i}. {status} {workout['title']} "
            f"({workout['duration']} мин, {workout['calories']} ккал)"
        )
    return "\n".join(result)


def mark_done(workouts: list, index: int) -> None:
    """Отмечает тренировку выполненной."""
    workouts[index]["done"] = True
