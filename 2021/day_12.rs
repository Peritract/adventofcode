use std::fs;
use std::collections::HashMap;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn parse_caves(data:&String) -> HashMap<String, Vec<String>> {
  let mut caves:HashMap<String, Vec<String>> = HashMap::new();

  for route in data.split('\n') {
    let parts:Vec<String> = route.split('-').map(|s| String::from(s)).collect();
    if parts[1] != String::from("start") {
          let c = caves.entry(parts[0].clone()).or_insert(Vec::new());
      c.push(parts[1].clone());
    }
    if parts[0] != String::from("start") {
      let d = caves.entry(parts[1].clone()).or_insert(Vec::new());
      d.push(parts[0].clone())
    }
  }

  caves.remove("end");

  return caves;
}

fn find_routes(caves:&HashMap<String, Vec<String>>, start:String, end:String, small_seen:Vec<String>) -> Vec<Vec<String>> {
// Find all valid routes from the start to the end;
// Probably some recursive/memoised nonsense.

if start == end {
  let mut end_vec = Vec::new();
  end_vec.push(vec!["end".to_string()]);
  return end_vec;
} else {
  let options:Vec<String> = caves.get(&start).unwrap().iter().map(|s| String::from(s)).collect();
  let mut routes:Vec<Vec<String>> = Vec::new();

  for opt in options {
    let mut valid = true;

    if opt == "start" || small_seen.contains(&opt) {
      valid = false;
    }

    if valid {
      let mut new_ss = small_seen.clone();
      if opt.to_lowercase() == opt {
        new_ss.push(opt.clone());
      }
      let new_routes = find_routes(&caves, opt, end.clone(), new_ss);

      for mut x in new_routes {
        x.insert(0, start.clone());
        routes.push(x);
      }
    }
  }

  return routes;
}
}

fn first_star(data:&String) -> i32 {

  let caves = parse_caves(data);

  let routes = find_routes(&caves, String::from("start"), String::from("end"), Vec::new());

  return routes.len() as i32;
}

fn find_double_routes(caves:&HashMap<String, Vec<String>>, start:String, end:String, small_seen:HashMap<String, i32>) -> Vec<Vec<String>> {
// Find all valid routes from the start to the end;
// Probably some recursive/memoised nonsense.

if start == end {
  let mut end_vec = Vec::new();
  end_vec.push(vec!["end".to_string()]);
  return end_vec;
} else {
  let options:Vec<String> = caves.get(&start).unwrap().iter().map(|s| String::from(s)).collect();
  let mut routes:Vec<Vec<String>> = Vec::new();

  for opt in options {
    let mut valid = true;

    if opt == "start" {
      valid = false;
    }

    if small_seen.contains_key(&opt) {
      for (k, v) in &small_seen {
        if v > &1 {
          valid = false;
        }
      }
    }

    if valid {
      let mut new_ss = small_seen.clone();
      if opt.to_lowercase() == opt {
        let o = new_ss.entry(opt.clone()).or_insert(0);
        *o += 1;
      }
      let new_routes = find_double_routes(&caves, opt, end.clone(), new_ss);

      for mut x in new_routes {
        x.insert(0, start.clone());
        routes.push(x);
      }
    }
  }

  return routes;
}
}

fn second_star(data:&String) -> i32 {
  let caves = parse_caves(data);

  let routes = find_double_routes(&caves, String::from("start"), String::from("end"), HashMap::new());

  return routes.len() as i32;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
