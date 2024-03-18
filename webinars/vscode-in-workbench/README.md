# VS Code Webinar (2024-03-19)

Using VS Code in Posit Workbench.

## Additional Resources

- VS Code Docs: https://code.visualstudio.com/Docs
- Python for VS Code Docs: https://code.visualstudio.com/Docs
- Command Palette: https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette
- Multiple Cursors: https://code.visualstudio.com/docs/editor/codebasics
- Keyboard Shortcuts: https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference

## Tasks

**Navigating the File System**

- [ ] Open a folder with the `File` menu.
- [ ] Open a folder with the Command Pallet `>File: Open Folder`.

**Command Pallet**

- [ ] Open the command pallet with `Cmd` + `Shift` + `p`.
- [ ] Open your home directory, then open this project again.
- [ ] Open the settings with `>Preferences: Open User Settings`.
- [ ] Open the terminal with `>Terminal: Create New Terminal`.

**Understanding workspaces in VS Code vs. Projects in RStudio**

- VS Code does not have a notion of projects.
- You can think of the directory that you choose to open VS Code as the project. VS Code refers to this as the "Workspace"
- Workspace specific settings are stored in the `./vscode/` directory.
- [ ] Change a setting for this Workspace only with `Preferences: Open Workspace Settings`

**Extensions**

- VS Code is a simple text editor. The power comes from extensions!
- Many of the best Python extensions are developed by Microsoft, but anyone can develop and share an extensions.
- Workbench will automatically include the basic Python extensions.
- See `./vscode/extensions.json` for my recommended extensions.

**The terminal**

- [ ] See all of the terminal commands with `>Terminal:`
- [ ] Toggle the bottom pane using `Cmd` + `j`.
- [ ] Toggle the terminal using ^ + `\``




- Open a .py file:
    - IntelliSense (https://code.visualstudio.com/docs/editor/intellisense)
        - Triggger IntelliSense with `^Space`
        - Use arrow keys to select
        - Press `Tab` or `Enter` to insert
    - RStudio style interactive coding with Python
    - `#%%` For running chunks of a script, and showing off the interactive window
    - Linting and Formatting
    - Debugging
    - Refactoring
    - Formatting
    - Multiple cursors
    - Quick fix with `command+.`
    - VS Code Workbench Jobs
- Open a .ipynb file
    - Selecting the kernel - it auto prompts me to install `ipykernel`
    - Notebooks in VS Code
- Understanding VS Code settings
- Other tips
    - Open VS Code in the same folder as the python .venv, otherwise it can be finnicky with auto-complete
    - How to get back to Workbench home page.

- [ ]
