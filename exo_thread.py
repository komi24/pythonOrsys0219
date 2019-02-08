from threading import Thread, Lock
import time
import random

lock1 = Lock()

class MonThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.liste_hellos = ["Bonjour", "Hello", "Hola", "Bom dia", "Nin hao"]

	def run(self):
		lock1.acquire()
		for word in self.liste_hellos:
			print(word)
			time.sleep(random.randint(0,5))
		lock1.release()

t1 = MonThread()
t2 = MonThread()
t3 = MonThread()

t1.start()
t2.start()
t3.start()
