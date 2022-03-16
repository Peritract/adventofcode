use std::fs;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn first_star(data:&String) -> i32 {
  let nums = data.split("\n").collect::<Vec<&str>>();

  let mut gamma = String::with_capacity(nums[0].len());
  let mut epsilon = String::with_capacity(nums[0].len());

  for pos in 0..nums[0].len() {
      gamma.push(find_common(&nums, pos, true));
      epsilon.push(find_common(&nums, pos, false));
  }

  let pc = i32::from_str_radix(&gamma, 2).unwrap() * i32::from_str_radix(&epsilon, 2).unwrap();

  return pc;
}

fn find_common(data:&Vec<&str>, pos:usize, most:bool) -> char {
    let mut one:i32 = 0;
    let mut zero:i32 = 0;

    for line in data {
      if line.chars().nth(pos) == Some('1') {
        one += 1;
      } else {
        zero += 1;
      }
    }

    if one > zero {
      if most {
        return '1';
      } else {
        return '0';
      }
    } else if one == zero {
      if most {
        return '1';
      } else {
        return '0';
      }
    } else {
      if most {
        return '0';
      } else {
        return '1';
      }
    }
}

fn second_star(data:&String) -> i32 {

  let mut oxy = data.split("\n").collect::<Vec<&str>>();
  let mut co = data.split("\n").collect::<Vec<&str>>();

  let mut pos:usize = 0;
  let mut c:char;
  while oxy.len() > 1 {
    c = find_common(&oxy, pos, true);
    oxy = oxy.into_iter().filter(|val| val.chars().nth(pos) == Some(c)).collect();
    pos += 1;
  }
  pos = 0;
  while co.len() > 1 {
    c = find_common(&co, pos, false);
    co = co.into_iter().filter(|val| val.chars().nth(pos) == Some(c)).collect();
    pos += 1;
  }

  let ls = i32::from_str_radix(&oxy[0], 2).unwrap() * i32::from_str_radix(&co[0], 2).unwrap();

  return ls;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
