class Timer:
    def __enter__(self):
        import time
        self.start=time.time()
        print("start timer")
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        import time
        end=time.time()
        print(f"Timer Stopped - took {end-self.start:.2f}s")
        return False
    
with Timer() as t:
    total=sum(range(10000))
    print(f"Sum={total}")