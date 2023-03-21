# Work-in-Progress Matplotlib Stubs

These stubs are intended to replace the existing ones. They are still a work in progress but are being made available 
for people who might be interested in trying them out and providing feedback.

If you want to use these with Visual Studio Code and Pylance, you will need to remove the bundled stubs from 
the Pylance extension. When pylance is started, in python language service output window, it will show something like:

    Server root directory: c:\Users\fred\.vscode-insiders\extensions\ms-python.vscode-pylance-2022.7.43\dist

if you go to that folder, it should have bundled folder:

    C:\Users\fred\.vscode-insiders\extensions\ms-python.vscode-pylance-2022.7.43\dist\bundled\stubs\matplotlib\

Delete that matplotlib folder, or replace it with this folder. If you delete it, you will need to put this folder in a
folder called `typings` in the root of your workspace.

Note that you will need to repeat the replacement steps whenever the Pylance extension updates.




