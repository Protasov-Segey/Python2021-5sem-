#!/bin/bash
cd /home
touch info.txt
date > info.txt
whoami >> info.txt
uname >> info.txt
ls -la | grep ^d | wc  -l >> info.txt
ls -laR | grep "^-" | wc -l >> info.txt

