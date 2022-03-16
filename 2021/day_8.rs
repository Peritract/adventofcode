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
  
  let mut total:i32 = 0;

  for line in data.split('\n') {
    let output:Vec<i32> = line.split(" | ").collect::<Vec<&str>>()[1].split(' ').map(|x| x.len() as i32).collect();

    for val in output {
      if [2, 3, 4, 7].contains(&val) {
        total += 1;
      }
  }
  }

  return total;
}

fn parse_digits(patterns:&Vec<&str>, output:&Vec<&str>) -> i32 {

  // Make hashmaps to hold the values
  let mut digits:HashMap<String, char> = HashMap::new();
  let mut values:HashMap<char, String> = HashMap::new();

  // While some digits are unknown
  while digits.keys().len() != 10 {

    // For each pattern
    for u_x in patterns {

      // Sort it
      let mut m = u_x.split("").collect::<Vec<&str>>();
      m.sort();
      let x = m.join("");

      // Start with no digit
      let mut dig = '-';

      // Mark off the four easy ones
      if x.len() == 2 {
        dig = '1';
      } else if x.len() == 4 {
        dig = '4';
      } else if x.len() == 3 {
        dig = '7';
      } else if x.len() == 7 {
        dig = '8';

      // Check for sixes
      } else if x.len() == 6 && values.contains_key(&'1')  && values.contains_key(&'4') {
        let one = values.get(&'1').unwrap();

        // If a six doesn't contain both 1 characters, it's a 6
        if !(x.contains(one.chars().nth(0).unwrap()) && x.contains(one.chars().nth(1).unwrap())) {
          dig = '6';
        } else {

            // If a six contains all 4 characters, it's a 9.
            let four = values.get(&'4').unwrap();
            let mut valid = true;
            for c in four.chars() {
              if !x.contains(c) {
                valid = false
              }
            }
            if valid {
              dig = '9';

            // Otherwise, it's a zero
            } else {
              dig = '0';
            }
        }

      // Check the fives
      } else if x.len() == 5 && values.contains_key(&'1') && values.contains_key(&'9') {
        let one = values.get(&'1').unwrap();

        // If a five contains both 1 characters, it's a 3
        if x.contains(one.chars().nth(0).unwrap()) && x.contains(one.chars().nth(1).unwrap()) {
          dig = '3';
        } else {
          // If a five contains almost all 9 characters, it's a 5
          let nine = values.get(&'9').unwrap();
          let mut valid = 0;
          for c in nine.chars() {
            if x.contains(c) {
              valid += 1;
            }
          }
          if valid == 5 {
            dig = '5';

          // Otherwise it's a 2
          } else {
            dig = '2';
          }
        }
      }

      // If a value was found
      if dig != '-' {
        values.insert(dig, x.clone());
        digits.insert(x.clone(), dig);
      }
    }
  }

  // Create a string to hold the result
  let mut fin:String = String::new();
  // For each output number
  for v in output {

    // Sort it
    let mut m = v.split("").collect::<Vec<&str>>();
    m.sort();
    let x = m.join("");
    // Add the digit to the final number
    fin.push(*digits.get(&x).unwrap());
  }

  // Return the parsed number
  return fin.parse::<i32>().unwrap();
}

fn second_star(data:&String) -> i32 {

  let mut total = 0;

  // For each line
  for line in data.split('\n') {

    // Split the output from the patterns
    let parts:Vec<Vec<&str>> = line.split(" | ").map(|s| s.split(' ').collect()).collect();

    // Pass it through the parser and increment the score
    total += parse_digits(&parts[0], &parts[1]);
  }
  return total;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
