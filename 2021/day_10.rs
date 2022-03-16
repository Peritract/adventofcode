use std::fs;
use std::collections::HashMap;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn first_star(data:&String) -> i32 {

  let mut pairs:HashMap<char, char> = HashMap::new();
  pairs.insert('}', '{');
  pairs.insert('>', '<');
  pairs.insert(')', '(');
  pairs.insert(']', '[');

  let mut scores:HashMap<char, i32> = HashMap::new();
  scores.insert(')', 3);
  scores.insert(']', 57);
  scores.insert('}', 1197);
  scores.insert('>', 25137);

  let mut score:i32 = 0;

  for line in data.split('\n') {

    let mut stack:Vec<char> = Vec::new();
    for c in line.chars() {
      if "{[<(".contains(c) {
        stack.push(c);
      } else {
        if pairs.get(&c).unwrap() != &stack.pop().unwrap() {
          score += scores.get(&c).unwrap();
        }
      }
    }
  }
  return score;
}

fn second_star(data:&String) -> i64 {
  let mut pairs:HashMap<char, char> = HashMap::new();
  pairs.insert('}', '{');
  pairs.insert('>', '<');
  pairs.insert(')', '(');
  pairs.insert(']', '[');
  pairs.insert('{', '}');
  pairs.insert('<', '>');
  pairs.insert('(', ')');
  pairs.insert('[', ']');

  let mut scores:HashMap<char, i32> = HashMap::new();
  scores.insert(')', 1);
  scores.insert(']', 2);
  scores.insert('}', 3);
  scores.insert('>', 4);

  let mut final_scores = Vec::new();

  for line in data.split('\n') {
    let mut valid = true;
    let mut stack:Vec<char> = Vec::new();
    for c in line.chars() {
      if "{[<(".contains(c) {
        stack.push(c);
      } else {
        if pairs.get(&c).unwrap() != &stack.pop().unwrap() {
          valid = false;
        }
      }
    }
    if valid && stack.len() > 0 {
      let mut end:Vec<char> = Vec::new();
      for c in stack {
        let resp = pairs.get(&c).unwrap();
        end.insert(0, *resp);
      }
      let mut score:i64 = 0;
      for c in &end {
        println!("{:?}, {}, {}", end.clone(), c, score);
        score = score * 5;
        score += scores.get(&c).unwrap().clone() as i64;
      }
      final_scores.push(score);
    }
  }
  final_scores.sort();
  let mid:usize = (final_scores.len()) / 2;
  return final_scores[mid];

}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
