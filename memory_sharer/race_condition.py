from threading import Thread
from time import sleep

acumulador = 0
repeticoes = 100_000

def incrementador(repeticoes: int):
  global acumulador
  for _ in range(repeticoes):
    acumulador +=10
    sleep(0.01)
    
  
def decrementador(repeticoes: int):
  global acumulador
  for _ in range(repeticoes):
    acumulador -=10
    sleep(0.01)
    

if __name__ == "__main__":
  thread1 = Thread(target=incrementador, args=(repeticoes,))
  thread2 = Thread(target=decrementador, args=(repeticoes,))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print(f'Resultado Final:{acumulador}')
