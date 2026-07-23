
 🗓️ Leap Year Checker

A simple Python command-line program that checks whether a given year is a leap year.

## 📖 Description

This program takes a year as input from the user and determines whether it is a leap year, based on the standard leap year rules:

- A year is a leap year if it is divisible by **4**
- **Exception:** Century years (divisible by 100) are leap years only if they are also divisible by **400**

## ✨ Features

- Simple, interactive command-line interface
  
- Input validation — handles non-numeric and negative year inputs gracefully
  
- Clean, well-documented function logic
----------------------------------------------------------------------------------
**- Most Important Commands to Memorize:**
  
**Command	Purpose:**

1.git init: 	Initialize a repository

2.git status: 	Check repository status

3.git add .	: Stage all changes

4.git commit -m "message": 	Save changes

5.git branch: 	List local branches

6.git checkout branch-name: 	Switch branches

7.git checkout -b branch-name	: Create and switch to a new branch

8.git diff	: Show unstaged changes

9.git log --oneline: 	View commit history

10.git remote -v: 	View remote repositories

11.git push -u origin branch-name: 	Push a branch to GitHub

12.git pull origin branch-name: 	Fetch and merge changes from GitHub

13.git branch -d branch-name: 	Delete a local branch

---------------------------------------------------------------------------------------
**Here are some of the main challenges developers face when using Git:**

1.Merge conflicts – Occur when two branches modify the same part of a file.

2.Working on the wrong branch – Accidentally making changes or committing to main or dev instead of a feature branch.

3.Push rejections – Unable to push because the remote branch contains newer commits.

4.Accidental overwrites – Losing changes by resetting, checking out, or merging incorrectly.

5.Poor commit messages – Making project history difficult to understand and maintain.

6.Large, unrelated commits – Combining multiple features or fixes into a single commit.

------------------------------------------------------------------------------------------------------
  ** Enter a year when prompted — the program will tell you whether it's a leap year.**
  
## 💡 Example

```
Enter a year: 2024
2024 is a leap year!
```

```
Enter a year: 2023
2023 is not a leap year
