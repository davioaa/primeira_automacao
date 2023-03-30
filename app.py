# automacao que joga um arquivo no google drive
# aplicacao para aprendizado

import pyautogui
import time

print('Sua maquina será controlada por uma linha de codigo')
entrada = input('Caso concorde em que sua máquina senha controlada, digite [s]im: ')

if entrada != 's':
    quit()

pyautogui.alert('O codigo será executado, não mexa em nada') # exibe uma caixa de alerta
# abrir o chrome
pyautogui.press('win', interval=0.5) # pressiona uma tecla
pyautogui.write('Google Chrome') # digita o que está entre aspas
pyautogui.press('\n')
time.sleep(0.5)
# abrir o google drive
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('\n')
# entrar no diretorio onde esta o arquivo
pyautogui.hotkey('win', 'd') # pressiona as teclas juntas
pyautogui.moveTo(1305, 278, duration=1) # move o mouse para a posição informada | arquivo
# clicar no arquivo e arrastar 
pyautogui.mouseDown() # segura o botao do mouse, por padrao, o esquerdo
pyautogui.moveTo(1093, 657) # moverá segurando o botão
# entrar no google drive enquanto arrasta arquivo
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()
# largar arquivo no google drive
time.sleep(5)
pyautogui.alert('O código foi finalizado')