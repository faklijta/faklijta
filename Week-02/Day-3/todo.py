# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"
todoText = "My todo \n" + todoText[0:-1] + '\n'
todoText = todoText[ : ] + " - Download games \n"
todoText = todoText[ : ] + "      -Diablo"

print(todoText)