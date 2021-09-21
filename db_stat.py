import MySQLdb as mysql
from rich.console import Console

console = Console()

db = mysql.connect(
  host='localhost',
  user='root',
  password='root',
  db='INFORMATION_SCHEMA'
)

cur = db.cursor()

def get_info_of_db():
    cur.execute('SHOW STATUS')
    res = cur.fetchall()
    r = dict(res)
    console.print(f"\tUptime, {r['Uptime']}\n\tThreads_created, {r['Threads_created']}\n\tThreads_connected, {r['Threads_connected']}\n\tThreads_running, {r['Threads_running']}\n\tQueries, {r['Queries']}\n\tMax_used_connections, {r['Max_used_connections']}", style='bold blue')
	
def get_process_list():
	cur.execute("select ID,DB from PROCESSLIST") 
	res = cur.fetchall()
	console.print(f"\t{res}")


	
def menu():
	console.print("1. Information Of Database\n2. Show Process List\n3. Exit",style="bold cyan")
	
	

while True:
    menu()
    ch = int(input("Enter the Choice: "))
    if ch == 1:
        get_info_of_db()
    elif ch == 2:
        get_process_list()
    else:
        cur.close()
        break