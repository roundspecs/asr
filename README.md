# asr
A time tracking and journaling tool

## Usage
### Add task
  ```bash
  $ asr task add complete-chapter-one
  ```
### Add subtask
  Add task like [emmet](https://emmet.io/) except # and . does not represent id and class\
  ```bash
  $ asr task add complete-chapter-one>read-intro
  ```
  ```bash
  $ asr task add task1>(task1.1>(task1.1.1+task1.1.2))+task1.2
  ```
### Remove tasks or subtasks
  ```bash
  $ asr task remove complete-chapter-one>read-intro
  ```
  Don't remember the task name? We got you.
  ```bash
  $ asr task remove
  List of subtasks
    complete-chapter-one
    task1
  $ asr task remove task1>
  List of subtasks
    task1.1
    task1.2
  $ asr task remove task1>task1.1.1+
  List of subtasks
    task1.1.2
  ```
### Start working on a subtask
  ```bash
  $ asr start complete-chapter-one>read-intro
  ```
  Note: Only tasks with no children can be started
### Stop working
  ```bash
  $ asr stop
  ```
### See what you are working on
  ```bash
  $ asr status
  ```