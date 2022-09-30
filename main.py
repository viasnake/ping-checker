from ping3 import ping
import time, csv

def ping_test():
  result = []
  result.append(time.strftime('%Y/%m/%d %H:%M:%S'))
  result.append(ping('8.8.8.8'))
  result.append(ping('1.1.1.1'))
  return result

def write_csv(result):
  with open('ping.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(result)

def main():
  while True:
    result = ping_test()
    print(result)
    try:
      with open('ping.csv', 'r') as f:
        write_csv(result)
    except FileNotFoundError:
      with open('ping.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Google Public DNS', 'Cloudflare Public DNS'])
    time.sleep(1)

if __name__ == '__main__':
  main()
