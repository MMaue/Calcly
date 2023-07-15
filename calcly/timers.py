import time
import datetime


def timer(acc=1, wait_time=0.1):
	starttime = time.time()
	try:
		NOT_INTERUPTED = True
		while NOT_INTERUPTED:
			teatime = round((time.time() - starttime), acc)
			print(f">>>\t{teatime}s", end="\r")
			time.sleep(wait_time)
	except KeyboardInterrupt:
		print(f"\t{teatime}s")

		#teatime = int(teatime)
		hours = teatime // 3600
		teatime-=hours*3600
		minutes = (teatime % 3600) // 60
		teatime-=minutes*60
		seconds = teatime % 60
		output = ""
		if hours != 0:
			output += f"{hours:.0f}h\t"
		if minutes != 0:
			output += f"{minutes:.0f}m\t"
		if seconds != 0:
			output += f"{round(teatime, acc)}s"
		print(output.strip())

def countdown(h=0, m=0, s=0, acc=1, wait_time=0.1):
	total_time = h * 3600 + m * 60 + s
	starttime = time.time()
	endtime = datetime.datetime.now() + datetime.timedelta(seconds=total_time)
	print(endtime)
	teatime = 0
	while teatime < total_time:
		teatime = round((time.time() - starttime), acc)
		#print(f">>>\t{total_time-teatime}s", end="\r")
		timer = datetime.timedelta(seconds=total_time-teatime)
		print(f">>>\t{timer}", end="\r")
		time.sleep(wait_time)
	print()
