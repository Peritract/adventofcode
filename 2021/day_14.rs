// Made a brute-force solution that one day would have worked, but had to get the fundamental insight for part 2 from the subreddit. Code all mine though.

use std::fs;
use std::collections::HashMap;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn parse_input(data:&str) -> (String, HashMap<String, String>) {
  let (start, raw_rules) = data.split_at(data.find("\n\n").unwrap());

  let raw_rules:Vec<Vec<&str>> = raw_rules.trim().split('\n').map(|s| s.split(" -> ").collect()).collect();

  let mut rules:HashMap<String, String> = HashMap::new();

  for r in raw_rules {
    rules.insert(String::from(r[0]), String::from(r[1]));
  }
  
  return (String::from(start), rules);
}

fn first_star(data:&String) -> i32 {
  let (start, rules) = parse_input(data);

  let mut curr = start.clone();
  for _step in 1..11 {
    let mut chunks:Vec<String> = Vec::new();
    for i in 0..curr.len()-1 {
      if rules.contains_key(&curr[i..i+2]) {
        chunks.push(String::from(&curr[i..i+1]));
        chunks.push(String::from(rules.get(&curr[i..i+2]).unwrap()))
      }
    }
    chunks.push(String::from(&curr[curr.len()-1..]));
    curr = chunks.join("");
  }

  let mut counts:HashMap<char, i32> = HashMap::new();
  for c in curr.chars() {
    let ce = counts.entry(c).or_insert(0);
    *ce += 1;
  }

  let mut max:i32 = 0;
  let mut min:i32 = 100000;
  for (_k, v) in &counts {
    if *v > max {
      max = v.clone();
    }
    if *v < min || min == -1 {
      min = v.clone();
    }
  }
  return max - min;
}

fn second_star(data:&String) -> i64 {
  let (start, rules) = parse_input(data);
  let mut counts:HashMap<String, i64> = HashMap::new();

  // Set up the initial counts
  for i in 0..start.len()-1 {
    let ce = counts.entry(String::from(&start[i..i+2])).or_insert(0);
    *ce += 1;
  }

  for _i in 1..41 {
    let mut new_counts:HashMap<String, i64> = HashMap::new();
    for (k, v) in &counts {
      let extra = rules.get(k).unwrap();
      let p1 = String::from(k.chars().next().unwrap().to_string() + extra);
      let mut p2 = extra.to_string();
      p2.push(k.chars().nth(1).unwrap());
      let mut pair = new_counts.entry(p1).or_insert(0);
      *pair += v;
      pair = new_counts.entry(p2).or_insert(0);
      *pair += v;
    }
    counts = new_counts;
  }

  let mut char_counts:HashMap<char, i64> = HashMap::new();
  for (k,v) in &counts {
    for c in k.chars() {
      let val = char_counts.entry(c).or_insert(0);
      *val += v;
    }
  }

  println!("{:?}", char_counts);

  
  // Add 1 to the count of start and end to account for unpaired letters
  let start_char = char_counts.entry(start.chars().next().unwrap()).or_insert(0);
  *start_char += 1;
  let end = char_counts.entry(start.chars().nth(start.len()-1).unwrap()).or_insert(0);
  *end += 1;
  
  // Max - min
  let mut max:i64 = 0;
  let mut min:i64 = -1;
  for (_k, v) in &char_counts {
    if *v > max {
      max = v.clone();
    }
    if *v < min || min == -1 {
      min = v.clone();
    }
  }

  // Maths stuff that I intuited - each char appears as either end of a pair, so counting keys doubles the count. However, position 0 and -1 are both only one side of a pair each, so adding 1 to each before counting up and then dividing gets the right result
  return max / 2 - min / 2;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
