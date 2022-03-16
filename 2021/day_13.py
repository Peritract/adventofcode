use std::fs;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

#[derive(Debug, PartialEq, Eq, Copy, Clone)]
struct Point{x:i32, y:i32}

impl Point {
  fn new(s:&str) -> Self {

    let c:Vec<i32> = s.split(',').map(|x| x.parse::<i32>().unwrap()).collect();

    return Self{x:c[0], y:c[1]};
  }

  fn flip_y(&mut self, dist:i32) {
    let offset = self.y - dist;
    self.y = dist - offset;
  }

  fn flip_x(&mut self, dist:i32) {
    let offset = dist - self.x;
    self.x = dist + offset;
  }
}

fn split_rule(inp:&str) -> (String, i32) {
  let s = String::from(inp);
  let parts:Vec<&str> = s[11..].split('=').collect();

  let parts = (String::from(parts[0]), parts[1].parse::<i32>().unwrap());

  return parts;
}

fn parse_input(data:&str) -> (Vec<Point>, Vec<(String, i32)>) {

  let (raw_dots, raw_rules) = data.split_at(data.find("\n\n").unwrap());
  
  let dots:Vec<Point> = raw_dots.split('\n').map(|s| Point::new(s)).collect();

  let rules:Vec<(String, i32)> = raw_rules.trim().split('\n').map(|s| split_rule(s)).collect();

  return (dots, rules);
} 

fn first_star(data:&String) -> i32 {
  let (dots, rules) = parse_input(data);

  let r = &rules[0];
  let mut visible = Vec::new();

  for mut p in dots {
    if r.0 == "y" && r.1 < p.y {
      p.flip_y(r.1);
    } else if r.0 == "x" && r.1 < p.x {
      p.flip_x(r.1);
    }
    if !visible.contains(&p) {
        visible.push(p);
    }
  }
  return visible.len() as i32;
}

fn display_grid(dots:&Vec<Point>) {
  let mut max_x = 0;
  let mut max_y = 0;
  let mut min_x = 10000;
  let mut min_y = 10000;

  for d in dots {
    if d.x > max_x {
      max_x = d.x;
    }
    if d.y > max_y {
      max_y = d.y;
    }
    if d.x < min_x {
      min_x = d.x;
    }
    if d.y < min_y {
      min_y = d.y;
    }
  }

  let mut grid:Vec<Vec<char>> = vec![vec![' '; (max_x + 1) as usize]; (max_y + 1) as usize];

  for d in dots {
    grid[d.y as usize][d.x as usize] = '#';
  }

  for row in grid {
    println!("{}", row[(min_x as usize)..].iter().collect::<String>());
  }
}

fn second_star(data:&String) -> &str {
  let (mut dots, rules) = parse_input(data);

  for r in rules {
    let mut altered_dots = dots.clone();
    for p in altered_dots.iter_mut() {
      if r.0 == "y" && r.1 < p.y {
        p.flip_y(r.1);
      } else if r.0 == "x" && r.1 < p.x {
        p.flip_x(r.1);
      }
    }
    dots = altered_dots.clone();
  }

  display_grid(&dots);

  return "See above.";
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
