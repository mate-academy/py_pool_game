# py_pool_game

This is a classic simulation task. There is a pool in which fish live. They are born, swim, eat and die. In this case, we are dealing with the so-called legacy code. It works, but does not meet development standards. To improve the situation, automatic code quality checks were added to the repository.

The task that needs to be solved is simple: you need to add a new species of predator - the pike. It has the following options:
{
  "_life_counter": 10,
  "_born_rate": 3,
  "_born_num": 2
}
Also, the size of the pool should be increased to 20x20.
The main difficulty of this task is to satisfy all quality checks.

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest --cov=pool`

`flake8 .`

`pylint fishes pool config test_pool main`

`mypy .`