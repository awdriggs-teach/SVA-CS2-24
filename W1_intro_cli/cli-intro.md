# New Skill Unlocked!
*using the command line*

## Basic commmands
### Moving Around
- `cd directory_name` →  change into directory_name
- `cd ..` →  move up to parent directory
- `ls` →  list files and folders in current directory
- `ls -l` → list each file on it's own line
- `ls -la` → list the hidden files too!
- `pwd` →  print the path to the working directory
- `../` → (parent directory), used as part of path to navigate/save one directory up.   
- `open .` → (open working directory), view in Finder.

### Creating and Editing Files
- `mkdir directory_name` →  create new directory directory_name
- `touch filename.ext` →  create file
- `mv directory_name_1 directory_name_2` →  move folder into another folder
- `mv filename_1 filename_2` →  rename file

### DANGER! 
**Be careful with these commands** the `rm` command deletes files in a way that can't be undone. They don't go to the trash can! 
- `rm`/`rmdir` (remove / remove directory), permanently removes files!  
- `rm file_name` →  delete file
- `rm -rf directory_name' →  delete all children files and directories in directory_name

- `sudo` (root access), sometimes commands need root access to run. Be careful when using this command! 

### Previewing
- `cat` → displays the contents of a file to the terminal
- `head -10` → lists the first ten lines of a file
- `tail -10` → lists the last ten lines of a file

### Shortcuts
- `TAB` (autocomplete), completes command or directory/filename.
- `UP ARROW` (history), toggle through recent commands. 
- `CTRL + C` (cancel), stop any task mid process. 

## Mac Setup

### Terminal
Use the terminal app to access command line tools.

Mac OS uses the ZSH as the default shell. [Oh my ZSH!](https://ohmyz.sh/) is a nice package that gives you some great add-ons. 

### Package Manager
A package manager is software that helps you manage applications installed using the command line. It helps keep tools up to date and allows you to have multiple versions of software installed.

Mac doesn't ship with a package manager but [homebrew](https://brew.sh/) is by far the most popular and is really useful. You suggest install it!

## Windows Setup
The default windows shell, Powershell, is a piece of trash that nobody uses.

You can run a Linux OS on your Windows System using [Windows Subsystem for Linux, WSL](https://learn.microsoft.com/en-us/windows/wsl/about). This creates a virtual linux system on your machine.

## More Resources
- [MDN Command line crash course](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line) is a good place to learn more!
- [Ubuntu Terminal, Linked Learning](https://www.linkedin.com/learning/learning-linux-command-line-14447912/learning-linux-command-line?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=56746073), you have free access as an SVA student!
 
  
