# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open('romeo_and_juliet.txt', 'r') as file:
    content = file.read()




# Count how many times the word "Juliet" appears
juliet_count = content.count('Juliet')

print(f"The word 'Juliet' appears {juliet_count} times.")