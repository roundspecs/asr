# asr
A time tracking and journaling tool

## Usage
### Add task
  `$ asr task add complete-chapter-one`
### Add subtask
  `$ asr task add complete-chapter-one/read-intro`\
  `$ asr task add make-popcorn/(buy-instant-popcorn-packet/(go-to-shop+ask-for-popcorn+pay-bill+come-home))+turn-on-oven+put-the-packet-inside-oven+wait-for-2-min+take-it-out`\
  The above will create:
  - [ ] make-popcorn
    - [ ] buy-instant-popcorn-packet
      - [ ] go-to-shop
      - [ ] ask-for-popcorn
      - [ ] pay-bill
      - [ ] come-home
    - [ ] turn-on-oven
    - [ ] put-the-packet-inside-oven
    - [ ] wait-for-2-min+take-it-out
### Remove tasks or subtasks
  `$ asr task remove complete-chapter-one/read-intro`\
  Note: Remove multiple tasks by separating them with sapce
### Start working on a subtask
  `$ asr start complete-chapter-one/read-intro`\
  Note: Only tasks with no children can be started
### Stop working
  `$ asr stop`
### See what you are working on
  `$ asr status`