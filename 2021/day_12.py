from collections import defaultdict

def load_input(filename="input.txt"):
  with open(filename) as f_obj:
    data = [x.strip() for x in f_obj.readlines()]
  return data

def parse_data(data):
  caves = defaultdict(lambda: [])
  for line in data:
    a, b = line.split("-")

    caves[a].append(b)
    caves[b].append(a)

  return caves

def find_routes(caves, start, end, small_seen=[]):
  if start == end:
    return ["end",]
  else:
    routes = []
    for opt in caves[start]:
      valid = True
      if opt == 'start' or (opt.lower() == opt and opt in small_seen):
        valid = False
      
      if valid:
        new_ss = [x for x in small_seen]
        if opt.lower() == opt:
          new_ss.append(opt)
        new_routes = find_routes(caves, opt, end, new_ss)
        for x in new_routes:
          if type(x) == str:
            routes.append([start, x])
          else:
            y = [start]
            y.extend(x)
            routes.append(y)
    return routes
  
def find_double_routes(caves, start, end, small_seen={}):
  if start == end:
    return ["end",]
  else:
    routes = []
    for opt in caves[start]:
      valid = True
      if opt == 'start' or (opt.lower() == opt and opt in small_seen and any([val > 1 for val in small_seen.values()])):
        valid = False
      
      if valid:
        new_ss = {k:v for k,v in small_seen.items()}
        if opt.lower() == opt:
          if opt in new_ss:
            new_ss[opt] += 1
          else:
            new_ss[opt] = 1
        new_routes = find_double_routes(caves, opt, end, new_ss)
        for x in new_routes:
          if type(x) == str:
            routes.append([start, x])
          else:
            y = [start]
            y.extend(x)
            routes.append(y)
    return routes

def first_star(data):
  caves = parse_data(data)
  routes = find_routes(caves, "start", "end", small_seen=[])
  return len(routes)

def second_star(data):
  caves = parse_data(data)
  routes = find_double_routes(caves, "start", "end", small_seen=dict())
  return len(routes)

if __name__ == "__main__":
  data = load_input()
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

