// Got this one independently, but only with a brute force solution that took forever. Once being told the trick though, wrote the code to do it much more speedily.

use std::fs;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn first_star(data:&String) -> usize {
  let mut fishes:Vec<i32> = [0].to_vec();
  let fish_list:Vec<i32> = data.split(",").map(|f| f.parse::<i32>().unwrap()).collect();
  let mut ideal:Vec<usize> = [1].to_vec();
  let length = 80;
  for _i in 1..length + 1 {
    let mut count = 0;
    fishes = fishes.into_iter().map(|f| {
      if f == 0 {
        count += 1;
        return 6;
      } else {  
        return f - 1;
      }
      }).collect();
    for _x in 0..count {
      fishes.push(8);
    }
    ideal.push(fishes.len())
  }
  let mut total = 0;
  for f in fish_list {
    total += ideal[(length - f) as usize];
  }
  
  return total;
}

fn _brute_force_second_star(data:&String) -> usize {
  let mut fishes:Vec<i32> = [0].to_vec();
  let fish_list:Vec<i32> = data.split(",").map(|f| f.parse::<i32>().unwrap()).collect();
  let mut ideal:Vec<usize> = [1].to_vec();
  let length = 256;
  for _i in 1..length + 1 {
    let mut count = 0;
    fishes = fishes.into_iter().map(|f| {
      if f == 0 {
        count += 1;
        return 6;
      } else {  
        return f - 1;
      }
      }).collect();
    for _x in 0..count {
      fishes.push(8);
    }
    ideal.push(fishes.len())
  }
  let mut total = 0;
  for f in fish_list {
    total += ideal[(length - f) as usize];
  }
  
  return total;
}

fn second_star(data:&String) -> usize {
  let mut fishes:Vec<usize> = vec![0; 9];
  for f in data.split(",").map(|f| f.parse::<usize>().unwrap()) {
    fishes[f] += 1;
  }

  for _day in 1..257 {
    let spawn = fishes[0].clone();
    fishes = fishes[1..fishes.len()].to_vec();
    fishes.push(spawn);
    fishes[6] += spawn;
  }
  return fishes.iter().sum::<usize>();
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
