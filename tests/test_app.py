from todo.api import get_tasks, create_task, finish_task, delete_task


def test_list_tasks(test_app):
    # make sure there are no existing tasks
    assert get_tasks() == []
    create_task('buy milk')
    create_task('buy cookies')
    assert len(get_tasks()) == 2


def test_create_task(test_app):
    create_task('Get milk')
    existing_tasks = get_tasks()
    assert len(existing_tasks) == 1
    first_task = existing_tasks[0]
    assert first_task.body == 'Get milk'
    assert first_task.done is False


def test_finish_task(test_app):
    create_task('Get milk')
    assert len(get_tasks()) == 1

    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    finish_task(get_milk_id)

    get_milk = get_tasks().pop()
    assert get_milk.done is True


def test_delete_task(test_app):
    create_task('Get milk')
    assert len(get_tasks()) == 1

    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    delete_task(get_milk_id)

    assert len(get_tasks()) == 0
