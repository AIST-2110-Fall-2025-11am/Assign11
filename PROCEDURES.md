## ASSIGNMENT COMPLETION PROCEDURES

Repeat the following steps for each of the exercises in this assignment.

1. **Follow the instructions to complete the exercise**

    - Click on the exercise folder using the explorer view on the left.
    - Open the exercise-specific README to access the instructions and start
      working on the exercise. 
    - Write your code in the supplied  Python script file.

2. **Run the script to test it yourself**

    Choose one of the following options to run your scripts. _**This is
    primarily how you should test your script**_. The automated tests provide
    little to no feedback, so you will not be able to "debug" your scripts using
    automated tests alone.

    **Option 1**

    From the _terminal_, navigate to the appropriate assignment part subfolder
    using the `cd` command. For example:
    ```bash
    cd 01-hello/
    ```

    Then you can execute your script using directly. For example:
    ```bash
    python hello.py
    ```

    **Option 2**

    Alternatively you can simply execute your scripts using full relative paths.
    For example:
    ```bash
    python 01-hello/hello.py
    ```

3. **Test the script**

    To ensure that you got the exercise correctly, you can run local tests before
    you submit your code. If the code passes the test, you are good to submit. If
    not, you can check the test(s) that failed and fix your code.

    Follow these steps to test your code:

    - Click on the beaker icon on the left tab.
    - Locate the test you want to run.
    - Click on the play arrow to run the test.
    - If it is green, the test passed and you should be good to submit this
      exercise.
    - If it is red, you possibly made a mistake. Check the error in the test "Test
      Results" tab on the view at the bottom of the screen (same location as the
      Terminal view)
    - Repeat the above for each exercise in this assignment.

## General Tips

- Make sure to frequently save and push your changes to your GitHub repository.
- Run your code after each significant modification.
  + Also run the automated test for each exercise in this assignment after each
    change when you are "done" but still tweaking.
- Commit and sync your code before you stop working for the day to ensure that
  your repository and codspace stay in sync and you don't risk losing your work.

## How to Submit

Most of you will now choose to use the VSCode Source Control extension to submit
your assginments. However, you can always use the terminal.

- Use the VS code Source Control Tab to submit your assignment:
    - Click click the + next to the list of "Changes" to stage all changes that
      you have made.
    - Write a commit message, e.g., "Finished with part 1" or "Finished with
      assignment"
      > _**YOU MUST SUPPLY A COMMIT MESSAGE OR YOU WILL GET ERRORS THAT YOU MAY
      > OR MAY NOT EVEN NOTICE**_
    - Click "Commit"
    - Click "Sync"
      > _**IF YOU DO NOT "Stage" ALL CHANGES, THEN YOU MUST `push` INSTEAD OF
      > `sync`.**_ To do this, either:
      > 
      > - click the ellipsis (...) to the right of the**v SOURCE CONTROL**
      >   header (this is the lower of the two things that say "SOURCE
      >   CONTROL"...yes this is confusing) and select Push
      > 
      > or:
      >
      > - instead of clicking "Commit" in the previous step, click the down
      >   arrow and select Commit & Push.

- Alternatively, you can use git to add, commit, and push your changes. Make
  sure you are in your `assn-3-yourusername` folder. `cd` your way there if not.
  Then type:
  
  ```bash
  git add .
  git commit -m "YOUR MEANINGFUL MESSAGE"
  git push
  ```

## Validate the Submission in GitHub and Submit to D2L

The last step is to submit your assignment to D2L. But in order to do that, you
**MUST** first validate that you correctly submitted the assignment to the
GitHub repository.

- Visit the GitHub repository for this assignment

- On the repository page, make sure you are looking at the `<> Code` tab.

- Look at each file in your submission.
  + Click on the file to ensure that your changes are showing.
  + Look at the commit message to ensure that you commit message is as expected.

- Now again back on the `<> Code` tab, look near the top right for something
  that looks like this:

  ![GitHub Commit ID](.res/commit_id.png)
  
  Copy that 7-digit number (it's hexadecimal, so there may be letters, too).

- Return to D2L and paste that ID into the submission comment for this
  assignment.

- Submit the assignment in D2L.
