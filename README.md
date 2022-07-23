# asr
A time tracking and journaling tool

## Usage
### Add tasks
```shell
$ asr task add complete-chapter-one
```
```shell
$ asr task add complete-chapter-one/read-intro
```
Add task like [emmet](https://emmet.io/) except {} instead of (), / instead of >
```shell
$ asr task add task1/{task1.1/{task1.1.1+task1.1.2}}+task1.2
```
### Remove tasks
```shell
$ asr task remove complete-chapter-one/read-intro
```
Don't remember the task name? We got you.
```shell
$ asr task remove
List of subtasks
  complete-chapter-one
  task1
$ asr task remove task1/
List of subtasks
  task1.1
  task1.2
$ asr task remove task1/task1.1.1+
List of subtasks
  task1.1.2
```
### Start working on a subtask
```shell
$ asr start complete-chapter-one/read-intro
```
Note: Only tasks with no children can be started
### Stop working
```shell
$ asr stop
```
### See what you are working on
```shell
$ asr status
Working on complete-chapter-one/read-intro for 2 hours
```