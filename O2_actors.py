import ray

# https://docs.ray.io/en/latest/ray-core/actors.html

ray.init()


@ray.remote
class Counter(object):
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def get_counter(self):
        return self.value


# Create an actor from this class.
counter = Counter.remote()

# %%

obj_ref = counter.increment.remote()
assert ray.get(obj_ref) == 1

# %%
# Methods called on different actors can execute in parallel,
# and methods called on the same actor are executed serially in the order that they are called.
# Methods on the same actor will share state with one another, as shown below.

# Create ten Counter actors.
counters = [Counter.remote() for _ in range(10)]

# Increment each Counter once and get the results. These tasks all happen in
# parallel.
results = ray.get([c.increment.remote() for c in counters])
print(results)  # prints [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Increment the first Counter five times. These tasks are executed serially
# and share state.
results = ray.get([counters[0].increment.remote() for _ in range(5)])
print(results)  # prints [2, 3, 4, 5, 6]
