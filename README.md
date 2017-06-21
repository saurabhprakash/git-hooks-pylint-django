# git-hooks-pylint-django
git hooks for pylint specific to django projects

For using this project, please follow these steps:

1. install using setup.py

2. add following to your settings file
  * ERROR_COUNT=[integer] 
  * CONVENTION_COUNT=[integer]
  * WARNINGS=[integer]
  * CODEBASE=<string - codebase relative path>
  * THRESHOLD_LINT_SCORE=[float between 0 to 10]
  
3. whenever you do commit, pylint will run
