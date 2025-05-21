from concurrent.futures import ThreadPoolExecutor
for id in ID_lists:
    future = pool.submit(kk,id)


pool = ThreadPoolExecutor(2)



