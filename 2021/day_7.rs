use std::fs;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn median(nums: &mut Vec<i32>) -> i32 {
  nums.sort();
  let med = nums.len() / 2;
  return nums[med];
}

fn first_star(data:&String) -> i32 {
  let mut crabs:Vec<i32> = data.split(',').map(|c| c.parse::<i32>().unwrap()).collect();

  let med = median(&mut crabs);

  return crabs.iter().map(|c| (med - c).abs()).sum();
}

fn second_star(data:&String) -> i32 {
  let crabs:Vec<i32> = data.split(',').map(|c| c.parse::<i32>().unwrap()).collect();

  let min = *crabs.iter().min().unwrap();
  let max = *crabs.iter().max().unwrap();
  let mut tot:i32 = crabs.iter().map(|c| {let x = (max - c).abs(); return (x*(x+1))/2}).sum();
  let mut sum:i32;

  for step in min..max {
    sum = crabs.iter().map(|c| {let x = (step - c).abs(); return (x*(x+1))/2}).sum();
    if sum < tot {
      tot = sum;
    }
  }

  return tot;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
