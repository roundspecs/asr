# asr
A time tracking and journaling tool

## Usage
### Add tasks
```
$ asr task add complete-chapter-one
Added task:
  complete-chapter-one
```
```
$ asr task add complete-chapter-one/read-intro
Added task:
  ☐ complete-chapter-one
  └──☐ read-intro
```
Add task like [emmet](https://emmet.io/) except {} instead of (), / instead of >
```
$ asr task add task1/{task1.1/{task1.1.1+task1.1.2}}+task1.2
Added task:
  ☐ task1
  ├──☐ task1.1
  │  ├──☐ task1.1.1
  │  └──☐ task1.1.2
  └──☐ task1.2
```
### Remove tasks
```
$ asr task remove complete-chapter-one/read-intro
Removed task:
  ☐ complete-chapter-one
  └──🗹 read-intro
```
Don't remember the task name? We got you.
```
$ asr task remove
List of subtasks
  ☐ complete-chapter-one
  ☐ task1
$ asr task remove task1/
List of subtasks
  🗹 task1.1
  ☐ task1.2
$ asr task remove task1/task1.1.1+
List of subtasks
  ☐ task1.1.2
```
### Start working on a subtask
```
$ asr task start complete-chapter-one/read-intro
Started task at 08:11 PM:
  ☐ complete-chapter-one
  └──☐ read-intro
```
Note: Only tasks with no children can be started
### Stop working
```
$ asr task stop
Stopped task, started 2h 25min ago
  ☐ complete-chapter-one
  └──☐ read-intro
```
### See what you are working on
```
$ asr task status
Working on complete-chapter-one/read-intro for 2 hours
```
### Mark complete
```
$ asr task done
Marked done. Stopped Task.
  ☐ complete-chapter-one
  └──🗹 read-intro
$ asr task done task1/task1.1
Marked done. Stopped Task.
  ☐ task1
  └──🗹 task1.1
```