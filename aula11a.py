# Código ANSI - scape sequence - utilizar para o terminal
# começa com \+código
# codigos = style - text - background
# style 0 - none/ 1 - negrito/ 4 - sublinhado/ 7 - invert configurations
# text 30 -37
# background 40 -47
print('\033[1;31;40mOlá Mundo!\033[m')
print('\033[7;31;40mOlá Mundo!\033[m')
print('\033[4;31;40mOlá Mundo!\033[m')
