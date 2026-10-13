import re

log_counts = {
    "INFO" : 0,
    "WARNING" : 0,
    "ERROR" : 0
}
error_logs = []

to_find = ['INFO', 'WARNING', 'ERROR']

pattern = r"ERROR\s*(.*)"


with open("app.log", "r") as file:
    
    for line in file:
        match = re.search(r"\b(INFO|WARNING|ERROR)\b", line)
        error_match = re.search(pattern, line)

        if error_match:
            print(error_match.group(1))
            error_logs.append(error_match.group(1))

        if match:
            print(match.group())
            old_count =  log_counts[match.group()]
            log_counts[match.group()] = old_count + 1

        

    log_file = file.read()


print(log_counts)
print(error_logs)