# git-hooks-pylint-django
git hooks for pylint specific to django projects

For using this project, please follow these steps:
a. install using setup.py
b. add following to your settings file
  ERROR_COUNT=<integer> 
  CONVENTION_COUNT=<integer>
  WARNINGS=<integer>
  CODEBASE=<string - codebase relative path>
  THRESHOLD_LINT_SCORE=<integer>
c. whenever you do commit, pylint will run
