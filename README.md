# git-hooks-pylint-django
git hooks for pylint specific to django projects

For using this project, please follow these steps:

### How it works
* Use ./install.sh to install the pre-commit hook (All settings are present in install.sh)
* ERROR_COUNT, CONVENTION_COUNT, WARNINGS, CODEBASE, THRESHOLD_LINT_SCORE : These counts/score needs to be modified based on requirement(these are default scores on which linter would evaluate).
* A pre-commit hook is installed in the CODEBASE's .git dir and runs pylint only for the *.py files being checked-in as a part of that commit.

### TODO:
* Copy and append requirements.txt to the project's
* Allow override from settings.py of django (in a way that it dynamically works with all projects, without hardcoding "webapp.settings")
* Hook to capture data to a central reporting location
* Check if pre-commit hook already exists and ask for permission before overwriting
* Install.sh throws error but doesn't check for it and displays "patched" message at the end. Error handling should be added
* Advanced: Parse pylint report and check only for the actual lines being checked-in and not just the files to make it a more accurate tool
