import time,random
import queue,threading

q = queue.Queue() # 队列对象

def Producer(name):
  count = 0
  while count <10:
    print("开始做包子")
    time.sleep(5)              # 生产包子的时间    random(randrange(3))
    q.put(count)               # 扔到队列里去 发信号
    print('生产者 %s 正在做第 %s 包子..' %(name, count))
    count +=1                  # 继续循环 知道满足条件
    #q.task_done()             # put 已经发送完了
    q.join()                   # 等待 所有完成以后 再继续打印最后的 ok
    print("ok......")

def Consumer(name):
  count = 0
  while count <10:
        time.sleep(random.randrange(4))      # 随机取1-3之间任意数字
    # if not q.empty():                      # 判断队列里还有没有包子
    #     print("waiting.....")              # 等待做包子
        #q.join()                            # 一直等着生产者做完包子
        data = q.get()                       # 如果队列里面不为空 就取出一个值
        print("吃包子")                      # 吃包子
        time.sleep(4)                        # 吃包子的过程

        q.task_done()                        # 接收信号 队列里已经有包子了 可以继续吃
        print('\033[32;1m消费者 %s 正在吃第 %s 包子\033[0m' %(name, data))
    # else:                                 # 如果包子吃的快 就打印 没有包子了
    #     print("-----没有包子了----")
        count +=1

p1 = threading.Thread(target=Producer, args=('A君',))   # 生产者 是 A
c1 = threading.Thread(target=Consumer, args=('B君',))   # 消费者 是 B/C/D
c2 = threading.Thread(target=Consumer, args=('C君',))
c3 = threading.Thread(target=Consumer, args=('D君',))

p1.start()
c1.start()
c2.start()
c3.start()

# 线程世界里 生产者就是生产数据的线程，消费者就是消费数据的线程，在多线程开发当中，如果生产者处理速度很快，
# 而消费者查理速度很慢 那么生产者就必须等待消费者处理完，才能继续生产数据。
