import re

log_counts = {

}

with open("app.log", "r") as file:
    log_file = file.read()

to_find = ['INFO', 'WARNING', 'ERROR']

for word in to_find:
    info = re.findall(word, log_file)
    log_counts[word] = len(info)

print(log_counts)