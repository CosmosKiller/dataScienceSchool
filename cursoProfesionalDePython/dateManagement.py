from datetime import datetime

my_time = datetime.now()
global_time = datetime.utcnow()

my_time = my_time.strftime('%d/%m/%Y')
global_time = global_time.strftime('%m/%d/%Y')

print(my_time)
print(global_time)