# get last modified code-workspace file:
# vscode_project_file=$(ls --sort=t *.code-workspace | head -1)

# get main project code-workspace file:
cwd=${PWD##*/}
vscode_project_file=$(ls ${cwd}.code-workspace | head -1)
code ${vscode_project_file}
# code-insiders ${vscode_project_file}