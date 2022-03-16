use std::fs;

fn load_data(filepath:&str) -> String {
  return fs::read_to_string(filepath).expect("Error!");
}

fn first_star() -> i32{
  let mut count:i32 = 0;
  let contents = load_data("input.txt");
  let vals = contents.split("\n").map(|a| {return a.parse::<i32>().unwrap();});
  let mut prev = 0;
  for num in vals {
    if num > prev {
      count = count + 1;
    }
    prev = num;
  };
  return count - 1;
}

fn second_star() -> i32{
  let data = load_data("input.txt");
  let contents = data.split("\n").map(|a| {return a.parse::<i32>().unwrap();}).collect::<Vec<_>>();
  let length = contents.len();
  let mut prev = 0;
  let mut count = 0;
  for i in 0..length-2 {
    let tot = contents[i] + contents[i+1] + contents[i+2];
    if tot > prev {
      count = count + 1;
    }
    prev = tot;
  }
  return count - 1;
}

fn main() {
  println!("First star: {}", first_star());
  println!("Second star: {}", second_star());
}
