from datetime import datetime
import pytz

def main():
	now = datetime.now().timestamp()
	now = datetime.fromtimestamp(now, pytz.timezone('America/Santiago'))
	date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
	print(f"Fecha y hora actual:\n\t{date_time_str}")

if __name__ == "__main__":
	main()