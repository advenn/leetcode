# import time
# from threading import Thread
#
#
# def func_4_thread(thread_name: str, sleep_secs: int = 10) -> None:
#     msg_prefix = f"{thread_name} thread, sleeping for {sleep_secs} seconds: "
#     print(msg_prefix, "init")
#     time.sleep(sleep_secs)
#     print(msg_prefix, "done")
#
#
# normal_thread = Thread(target=func_4_thread, args=("normal", 10))
# normal_thread.start()
#
# daemon_thread = Thread(target=func_4_thread, args=("daemon", 20), daemon=True)
# daemon_thread.start()
import time
from threading import Thread
from queue import Queue

func_result_queue: Queue = Queue(maxsize=0)


def func_4_thread() -> None:
    print("thread doing work...")
    time.sleep(5)
    func_result = "func result"
    # put result in queue
    func_result_queue.put(func_result)


thread = Thread(target=func_4_thread)
thread.start()

func_result = func_result_queue.get()
print(func_result, "from queue")
